#!/usr/bin/env python3
"""Out-of-bounds analysis for the JiMS button-field window.

Question: of the chord tones in a jazz corpus that fall outside the
button-field's 17-column fifths-chain window Se(-6)..Li(+10), how many
fall off the flat (negative) edge vs. the sharp (positive) edge —
and which window placement minimizes out-of-bounds events?

Corpus: DCMLab Jazz Harmony Treebank (iRealPro-derived, 1,170 jazz
standards with declared keys and full chord sequences).
https://github.com/DCMLab/JazzHarmonyTreebank

Method:
  * Every chord symbol is expanded to its chord tones as fifths-chain
    offsets from the root (correct spelling by construction: e.g. the
    dominant seventh is -2, the dim7's diminished seventh is -9).
  * Each tone's chain position is taken relative to Do. Major keys:
    Do = tonic. Minor keys: Do = relative major's tonic (La-based minor).
  * Two analyses:
      RAW        - roots as spelled in the charts (iRealPro orthography).
      FUNCTIONAL - each root respelled to its minimal spelling within
                   +-6 fifths of Do (JiMS-honest spelling). This removes
                   iRealPro's typographical sharp-spelling artifacts
                   (e.g. "B7" written for a functional Cb7 in Db major).

Results (2026-08-03): see OOB_RESULTS.md alongside this script.
"""

import collections
import json
import os
import re
import sys
import urllib.request

TREEBANK_URL = ("https://raw.githubusercontent.com/DCMLab/"
                "JazzHarmonyTreebank/master/treebank.json")
TREEBANK_FILE = os.path.join(os.path.dirname(__file__), "treebank.json")

BASE = {'F': -1, 'C': 0, 'G': 1, 'D': 2, 'A': 3, 'E': 4, 'B': 5}

# Chord-tone templates as fifths-chain offsets from the root (root = 0).
# M3 = +4, m3 = -3, P5 = +1, d5 = -6, A5 = +8, M6 = +3, m7 = -2,
# M7 = +5, d7 = -9, P4 = -1.
QUAL = {
    '^':   [0, 4, 1],          # major triad
    '':    [0, 4, 1],
    'm':   [0, -3, 1],
    '7':   [0, 4, 1, -2],
    'm7':  [0, -3, 1, -2],
    '^7':  [0, 4, 1, 5],
    '6':   [0, 4, 1, 3],
    'm6':  [0, -3, 1, 3],
    'm^7': [0, -3, 1, 5],
    '%7':  [0, -3, -6, -2],    # half-diminished
    'o7':  [0, -3, -6, -9],    # diminished seventh (strict bb7 spelling)
    'o':   [0, -3, -6],
    'sus': [0, -1, 1],
    '+':   [0, 4, 8],
}

WINDOWS = [(-6, 10, 'current, Re-centred'),
           (-7, 9, '1-step flat, So-centred'),
           (-8, 8, '2-step flat, Do-centred'),
           (-9, 7, '3-step flat, Fa-centred')]


def chain(note):
    """Fifths-chain position of a spelled note. '#' = +7, 'b'/'-' = -7."""
    m = re.match(r'^([A-Ga-g])([b#-]*)$', note)
    letter, acc = m.group(1).upper(), m.group(2)
    return (BASE[letter] + 7 * acc.count('#')
            - 7 * (acc.count('b') + acc.count('-')))


def do_of(key):
    """Chain position of Do. Lowercase key = minor; La-based minor puts
    Do at the relative major's tonic, 3 fifths flat of the minor tonic."""
    return chain(key) - (3 if key[0].islower() else 0)


def respell_min(root_pos, do):
    """Force a root to its minimal enharmonic spelling within +-6 fifths
    of Do (12 fifths = enharmonic step at the 12-TET readout)."""
    rel = root_pos - do
    while rel > 6:
        rel -= 12
    while rel < -6:
        rel += 12
    return rel


def analyse(treebank, functional):
    hist = collections.Counter()
    for tune in treebank:
        do = do_of(tune['key'])
        for symbol in tune['chords']:
            m = re.match(r'^([A-G][b#]*)(.*)$', symbol)
            root, qual = chain(m.group(1)), m.group(2)
            rel_root = respell_min(root, do) if functional else root - do
            for off in QUAL[qual]:
                hist[rel_root + off] += 1
    return hist


def report(label, hist):
    total = sum(hist.values())
    flat = sum(v for k, v in hist.items() if k < -6)
    sharp = sum(v for k, v in hist.items() if k > 10)
    print(f"\n=== {label} ===")
    print(f"chord-tone events: {total}")
    print(f"OoB flat (< -6): {flat} ({flat / total:.3%})   "
          f"OoB sharp (> +10): {sharp} ({sharp / total:.3%})")
    for lo, hi, name in WINDOWS:
        oob = sum(v for k, v in hist.items() if k < lo or k > hi)
        print(f"  window [{lo:+d},{hi:+d}] ({name}): "
              f"OoB {oob} ({oob / total:.3%})")
    print("  histogram (chain position rel. Do):")
    for p in sorted(hist):
        mark = '  <-- OoB' if p < -6 or p > 10 else ''
        print(f"    {p:+3d}: {hist[p]:6d}{mark}")


def main():
    if not os.path.exists(TREEBANK_FILE):
        print(f"downloading {TREEBANK_URL} ...", file=sys.stderr)
        urllib.request.urlretrieve(TREEBANK_URL, TREEBANK_FILE)
    treebank = json.load(open(TREEBANK_FILE))
    print(f"tunes: {len(treebank)}")
    report("RAW chart spellings (iRealPro orthography)",
           analyse(treebank, functional=False))
    report("FUNCTIONAL respelling (roots within +-6 fifths of Do)",
           analyse(treebank, functional=True))


if __name__ == '__main__':
    main()
