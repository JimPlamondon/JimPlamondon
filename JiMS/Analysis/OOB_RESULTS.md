# Out-of-Bounds Analysis: JiMS Button-Field Window Placement for Jazz

**Question.** The JiMS button-field's 17 pitch-class columns span the fifths chain
Se(−6)…Li(+10), symmetric about Re(+2) — the Circle of Thirds' Dorian axis. For
jazz repertoire, should the window shift flatward (hiding sharps to expose flats),
on the suspicion that jazz's chromatic traffic is flat-heavy?

**Corpus.** DCMLab Jazz Harmony Treebank (iRealPro-derived): 1,170 jazz standards,
declared keys, full chord sequences. 232,503 chord-tone events after expanding
every chord symbol to correctly-spelled chord tones (fifths-chain offsets from
the root: M3 = +4, m7 = −2, d7 = −9, etc.). Positions taken relative to Do;
minor keys anchored at the relative major (La-based minor).

**Script.** `oob_chain_analysis.py` (downloads the corpus, reproduces all numbers).

## Results (2026-08-03)

### Raw chart spellings (iRealPro orthography)

| OoB flat (< −6) | OoB sharp (> +10) | ratio |
|---|---|---|
| 1,651 (0.71%) | 1,759 (0.76%) | ≈ 1 : 1 |

The sharp tail is an **orthography artifact**: its top offenders are chords like
`B7` in D♭ major at +11…+14 — functional C♭7s that iRealPro spells sharp for
typographical convenience. Chart habit, not music.

### Functional respelling (roots forced within ±6 fifths of Do — JiMS-honest)

| OoB flat | OoB sharp | ratio |
|---|---|---|
| 3,618 (1.56%) | 48 (0.02%) | **75 : 1 flatward** |

Functionally, jazz chords essentially never leave the field sharpward. Flat
overflow is structural:

- **De(−7): 1,050 events** — subV sevenths (`Ra:So7` = Ra–Fa–Le–De; D♭7-in-C's
  C♭), exactly as predicted analytically.
- −8…−15: ~2,570 events, dominated by dim7 strict-spelling diminished sevenths
  (`A♭o7`-in-F and kin).

### Window comparison (functional spelling)

| window | centre | OoB rate |
|---|---|---|
| −6…+10 (current) | Re | 1.58% |
| **−7…+9 (one step flat)** | **So** | **1.36% ← optimum** |
| −8…+8 (two steps) | Do | 1.73% |
| −9…+7 (three steps) | Fa | 2.74% |

## Conclusion

The flat-shift suspicion is **confirmed in direction, bounded in magnitude**:

1. Shift **one column** flatward: trading Li(+10, 534 events) for De(−7, 1,050
   events) is clear profit — the subV seventh comes on-field.
2. **Stop there.** The second step trades Ri(+9, 1,527 events) for Fe(−8, 653) —
   a clear loss. Ri carries real traffic (♯9 of the home dominant, V7/iii's
   third) — and keeping Ri also preserves the septimal blue-third button that
   dynamic tonality and the Hendrix/augmented-sixth analysis want.

## Caveats

- Chord charts only: no solo lines, no unnotated tensions.
- The dim7 template uses the strict ♭♭7 spelling (−9). Filing the dim7's fourth
  tone as a 6th shrinks the deep-flat tail but leaves De's subV mass — the part
  that decides the one-step shift — untouched.
- The functional-respelling rule (minimal spelling within ±6 fifths of Do) is an
  assumption; the truth lies between the two analyses. The raw analysis's sharp
  tail is demonstrably artifactual, so the functional numbers are the better
  guide for a notation that spells honestly.
- Either way, the 17-column field covers ≈98.5% of all chord-tone events:
  window placement is margin-trimming, not crisis management.
