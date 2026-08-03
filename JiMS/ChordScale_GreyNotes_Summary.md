# Berklee's Chord-Scale System, the Grey Notes, and JiMS Chord-Naming

*Summary of a research thread, 2026-08-03. Companion documents: `Sources/SOURCES.md`
(annotated bibliography), `Analysis/OOB_RESULTS.md` (corpus analysis), and the
primary JiMS documents in `Sources/`.*

---

## 1. Berklee's system, as actually structured

Berklee's harmony curriculum (Nettles, *Harmony 1–4* workbooks, 1987; Nettles &
Graf, *The Chord Scale Theory & Jazz Harmony*, 1997) contains **two distinct
doctrines**, taught chapters apart and never reconciled:

**Chord-scale theory proper.** Every chord takes a parent scale built from its
own root. The diatonic ii–V–I in a major key is assigned Dorian, Mixolydian,
Ionian — three root-local names for one unmoving collection. The word "mode"
here names the *key's own notes*, read from the chord's root.

**Modal interchange.** A later handler for non-diatonic chords, invoked only
after the dominant-logic handlers (secondary dominants, substitute dominants,
diminished passing chords) fail to claim a chord. The donor is a parallel mode
on the fixed tonic; the chord is attributed to whichever parallel mode contains
it. The word "mode" here names a *foreign collection* on the home tonic. Donor
attribution is underdetermined (♭VII7 lives in Aeolian, Dorian, and Mixolydian)
and resolved by convention — proof that it is bookkeeping, not fact. Once the
chord is filed functionally ("subdominant minor" = the Le-containing group:
IVm7, ♭VImaj7, ♭VII7, IIm7♭5), the donor story does no further work.

The system is root-local by design: its customer is an improviser on a
fixed-pitch instrument reading absolute-pitch charts under time pressure. The
cost is multiplicative — every (root × quality) pair is a separate object to
internalize, ×12 through scales, voicings, and tension spellings. The
celebrated "context-free" decodability is relief from a burden the
absolute-pitch representation itself creates. (Internal critique: Hal Galper's
"there are no modes in a ii–V–I.")

## 2. The JiMS translation, component by component

| Berklee component | JiMS equivalent | Compression |
|---|---|---|
| Chord-scale equivalence (a chord implies a scale) | `XxN` and `Xx13` are truncations of one object | a doctrine becomes the numeral N |
| Diatonic chord-scale table (7 mode assignments) | `Do13`…`Ti13` — seven entries of one Circle of Thirds | 7 facts → 0 |
| Tension/avoid-note charts | avoid = a tension a m9 above a chord tone; the collection has exactly two semitones (Mi–Fa, Ti–Do) | dozens of chart entries → 2 semitone locations + 1 rule |
| Secondary-dominant scales (Mixo, Mixo ♭13, Mixo ♭9♭13…) | chord-scale = home collection + the transplant's manufactured syllables, already visible in the name (`Mi:So7` contains Si) | 5 named scales ×12 keys → 1 rule |
| Interchange scale choice ("A♭maj7 takes Lydian") | minimal manufacture: `Le:Fa13` imports 3 foreign syllables, `Le:Do13` would import 4 | convention → arithmetic |
| Exotic chord-scale catalog (modes of melodic minor etc.) | one dot-set re-declaration per family; "Lydian dominant" = `Re13` of the jazz-minor dots | ~21 catalog entries → 3–4 declarations |

Verified in detail: the avoid-note rule reproduces Berklee's entire diatonic
table (Lydian is avoid-free because its would-be clash note is the root — the
structural basis of George Russell's claim that major's true parent is Lydian).
The secondary-dominant rule reproduces all five Berklee scale assignments; note
the orthographic inversion it exposes — in "Mixolydian ♭9 ♭13" for V7/vi, the
flatted labels mark **the key's own diatonic notes** (Fa, Do), while the one
genuinely manufactured note (Si) carries no accidental at all, hidden inside
the root-local scale name.

**Revealed overall:** Berklee's system is tonic-local at every load-bearing
joint (tensions-from-the-key, minimal-foreignness scale choices) and root-local
only in its packaging. The packaging is what multiplies it by twelve.

## 3. The Grey Notes

Berklee grants that the White Notes — one diatonic collection, seven modes —
are a thing. Take the same step for the Ionian tonic's parallel minor: the
**Grey Notes**, the collection three fifths flatward — {Le Te Do Re Me Fa So},
chain −4…+2 — sharing the tonic through its La-mode. In JiMS: one dot-change.

**The modal-interchange inventory is the Grey collection's native degree-stacks,
and Berklee's per-chord scale prescriptions are Grey's native modes:**

| interchange chord | as Grey native | Grey mode | Berklee prescribes |
|---|---|---|---|
| IVm7 | `Re13` of Grey | Dorian | Dorian ✓ |
| ♭VImaj7 | `Fa13` of Grey | Lydian | Lydian ✓ |
| ♭VII7 (backdoor) | `So13` of Grey | Mixolydian | Mixolydian ✓ |
| IIm7♭5 | `Ti13` of Grey | Locrian | Locrian ✓ |
| Vm7 | `Mi13` of Grey | Phrygian | ✓ |
| ♭IIImaj7 | `Do13` of Grey | Ionian | Lydian (see below) |
| Im7 | `La13` of Grey | Aeolian | Dorian (see below) |

The backdoor dominant is Grey's own `So7`, cadencing onto a shared tonic. The
whole interchange chapter is one sentence: *slide the dots three columns flat;
the stacks recompute.*

**The two mismatches reveal a gradient of greys.** Berklee's tonic-minor Dorian
prefers the collection only two fifths flat; its ♭III Lydian keeps White's La.
Both are minimal-manufacture overriding Grey-nativity — exposing that there is
one grey per flatward step, each sharing the tonic through a successively
darker mode: −1 (Mixolydian shade, adds Te), −2 (Dorian, +Me), −3 (Aeolian —
*the* "parallel minor"), −4 (Phrygian, +Ra), −5 (Locrian, +Se). Corpus census
(1,170 jazz standards, Jazz Harmony Treebank; see `Analysis/`): shade usage
decays monotonically with darkness — Te 8,074, Me 6,313, Le 5,817, Ra 2,690,
Se 1,582 events. **"The parallel minor" is not a privileged donor; it is the
middle shade of grey, the one the nineteenth century happened to name.**

**Structure of the White/Grey pair.** The collections share a four-note core —
Fa, Do, So, Re (chain −1…+2) — and differ by swapped trios: La–Mi–Ti against
Te–Me–Le. The swap is the fifths-chain reflection p ↦ 1−p, the mirror through
the Do–So axis: Mi↔Me, La↔Te, Ti↔Le, Fa↔Re, Do↔So. This is Ernst Levy's
"negative harmony" mirror and, before that, Riemann's dualism made literal:
**the Grey collection is the White collection reflected through the
tonic–dominant axis**, the reflected tonic triad is the parallel-minor triad
(the neo-Riemannian P transform), and mixture is partial reflection — keep the
core, flip some or all of the trio.

## 4. JiMS chord-naming applied to Berklee's system

**Same shapes, any root.** The seven White-derived canonical stacks are the
entire shape vocabulary; the colon applies them to any root, light button or
grey: `Le:Fa7`, `Te:So7`, `Ra:So7`. On the isomorphic button-field this is
literal — same intervals, same geometry, same hand — extending fingering
invariance from *across keys* to *within the key, across collections*.

**The dual-coordinate theorem.** The shape transplanted onto a grey root is
always the chord's native degree in its own Grey: A♭maj7 = `Le:Fa7`, and A♭ is
Fa-of-Grey; B♭7 = `Te:So7` (So-of-Grey); Fm7 = `Fa:Re7` (Re-of-Grey); Dø7 =
`Re:Ti7` (Ti-of-Grey). Both collections run the same Circle of Thirds, so
"which shape" = "which circle position" — collection-independent. A transplant
name is therefore a dual-coordinate pair: **left side = the root's White
address; right side = its Grey address.** The borrowing analysis is not applied
to the name; it is already written in it.

**Shade selection by shape choice.** At N=7 several shapes coincide
(`Do7`≡`Fa7`; `Re7`≡`La7`≡`Mi7`) and diverge only as N grows — at the 9
(Phrygian's ♭9) and the 13 (Dorian's M13 vs Aeolian's ♭13). So extending the
stack forces the shade-of-grey commitment in one glyph: `Do:Re13` *is* "C
Dorian" (−2 grey), `Do:La13` *is* "C Aeolian" (−3), `Do:Mi13` is C Phrygian
(−4). Berklee's per-chord chord-scale deliberation reduces to which degree-name
the stack is extended under.

**Visit versus move.** The colon marks borrowing; a dot-change marks settling
into the Grey collection (a minore section, a modal B-section), whereupon
transplants become natives (`Le:Fa7` → `Fa7`). This is the collection-level
twin of the diamond's tonicization/modulation distinction — and it forces
explicitly the commitment that "borrowed from the parallel minor," as prose,
always let theorists dodge.

**Not translated, honestly:** Berklee's absolute-pitch bandstand interface
(chart symbols decodable by a cold sight-reader on a fixed-pitch instrument —
a virtue only relative to that hardware), and the horizontal layer
(voice-leading, avoid-note resolution, functional succession), which JiMS
deliberately leaves to the linear domain that no vertical symbol system
captures.

## 5. Hardware corollary

The greys are heavy enough to bend plastic: the out-of-bounds analysis
(`Analysis/OOB_RESULTS.md`) found chord-tone overflow past the 17-column
button-field runs 75:1 flatward under functional spelling, and the optimal
jazz window sits one column flat of the Re-centred default (So-centred,
−7…+9) — bringing the subV seventh (De) on-field while keeping the blue third
(Ri).

## 6. Verdict

"Chords borrowed from the parallel minor" names something real — a measurable,
monotonically-graded flatward annex around a fixed major tonic, formalizable as
the Grey collections and countable in corpora — but it was never a *loan*: the
donor-key metaphysics, the asymmetric accounting (minor's larger borrowings
from Ionian were naturalized as "the minor key"), and the Ionian-ruler
orthography were all coordinate-system artifacts. Berklee's chord-scale system
contains the correct ontology (chord = scale-slice; fixed tonic; minimal
manufacture) wrapped in root-local, Ionian-normed packaging; JiMS is that
ontology with the packaging removed — one circle, seven entries, a colon, a
dot-set, and an N.
