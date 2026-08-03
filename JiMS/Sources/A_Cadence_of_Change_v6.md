# A Cadence of Change

### The Rise and Fall of the Ionian-ization of Minor

---

## Part I — The finding

### 1. What was found

Between the fourteenth century and the eighteenth, the final cadence of minor-mode Western music was rebuilt in three datable changes, arriving in sequence, separated by generations, in strictly decreasing order of resemblance to Ionian's cadence. This paper names the three changes for the three changes' results: the **Dominant-ization** (the raised seventh, giving the cadential pre-tonic dominant quality; established by the fourteenth century), the **Major-ization** (the major third imposed at the cadential tonic; complete by about 1565), and the **Fortification** (the augmented sixth added at the cadential pre-pre-tonic; established by about 1740). Each change, once established, remained available thereafter, so that by the mid-eighteenth century the fully rebuilt form — augmented sixth, dominant seventh, major tonic — existed as a cadence-type containing no chord that Dorian, Aeolian, or Phrygian supplies. §7 shows what the conjunction never became: the majority ending — the Major-ization was already collapsing as the Fortification arrived.

The three changes then came apart, and the three changes came apart along three different curves. The Major-ization collapsed between roughly 1740 and 1830 — from 94 percent to 14 — and the two endpoints measured since, Chopin's 14.3 percent and modern popular song's 13.2, coincide. The Dominant-ization never collapsed: the raised seventh stands today within three points of the raised seventh's rate in 1619. The Fortification was still rising while the Major-ization's collapse ran, the two series carried by the same keyboard corpora from Scarlatti forward. And the seven-mode field that the Ionian-ization had pruned — Lydian reclassified out of existence, Locrian excluded, Dorian and Phrygian marginalized — never refilled: Ionian and Aeolian together hold nine-tenths of modern popular song.

Alongside the composed record runs a second record: the teaching literature. At every measured transition, the teaching literature moved a generation after the leading edge of composition — naming each change after composers had established the change, and in one case preserving a dead convention in classrooms for two hundred and fifty years after composers abandoned the convention.

Part I documents all of the above — rise, fall, and teaching record — in the language of observation: *appears*, *completes*, *rises*, *falls*, *is absent*. Part I contains no causal claims. Why the sequence rose, and why the sequence fell apart in exactly three ways, is a different order of claim, argued in Part II as a conjecture ranked against rival explanations. Part I also reports one result that emerged from the measurements: two of the objects modern pedagogy teaches as *scales* — harmonic minor and melodic minor — are not scales, but two descriptions of the residue left by the first change (§5).

The evidence base is roughly 30,000 encoded works across nine corpora — the trecento repertory (14th c.), the Josquin Research Project (c. 1420–1550), CRIM (c. 1500–1610, per-piece dates), the Palestrina corpus (c. 1554–94, modes declared rather than inferred), the Tasso in Music Project (1571–1649, per-work publication dates), the Sapp corpora of Bach chorales and of Scarlatti, Haydn, Mozart, and Beethoven keyboard sonatas, the Sapp corpora of Chopin preludes and mazurkas, and the Hooktheory corpus of modern popular song (26,175 entries, modes declared) — together with the theoretical and pedagogical sources of each period. Appendix I specifies the sources, corpora, operational definitions, and statistical conventions behind the paper's measurements; Appendix II lists the analysis code, with a manifest stating which published tables each script regenerates; Appendix III reports the sensitivity analyses and full result tables; and Appendix I's closing note records which analyses have validated drivers and which remain pending.

### 2. Terms

The following terms are used throughout, one term per concept.

**Final cadence** — the closing progression of a piece: the last chord and the chords immediately preceding the last chord.

**Cadential tonic** — the last chord of the final cadence.

**Cadential pre-tonic** — the chord immediately before the cadential tonic. In common-practice minor the cadential pre-tonic is the dominant seventh.

**Cadential pre-pre-tonic** — the chord immediately before the cadential pre-tonic. In common-practice minor the cadential pre-pre-tonic is where the augmented sixth appears.

These three positional terms are coined here. The literature supplies partial equivalents — *ultima* and *penultima* in Renaissance cadence theory, *dominant* and *predominant* in functional harmony — but the two vocabularies belong to different systems and neither vocabulary extends cleanly to the third position.

**Modal** — supplied by the mode in which the piece is written.

**Extra-modal** — not supplied by the mode in which the piece is written.

**Extra-diatonic** — supplied by no diatonic mode at all. An extra-diatonic feature is extra-modal in every mode; the reverse does not hold.

**Minor-destination modes** — Dorian, Aeolian and Phrygian: the three modes with a minor third and a perfect fifth above the final. Common-practice minor descends from Dorian, Aeolian and Phrygian; the descent is the subject of §4.

**Ionian-izing** — a graded property of an alteration: the degree to which the feature the alteration installs identifies Ionian. An alteration is maximally Ionian-izing when Ionian alone natively possesses the installed feature, moderately so when the feature is shared with other modes, and not Ionian-izing at all when no mode — Ionian included — possesses the feature.

**Law** — a convention observed without exceptions. A law's compliance rate sits at or near one hundred percent, which distinguishes a law from a strong preference: a preference produces seventy percent, and a law produces totals — 128 of 128, 574 of 580.

**Choice** — a convention applied where a stated condition holds and withheld where the condition fails. A choice's rate floats with the frequency of the condition, while the conditional rate — apply-given-condition — stays stable.

Two further terms are standard and used in their standard sense: **Picardy third**, the major third at the cadential tonic of a minor-destination piece; and **augmented sixth**, the chord built on the flat sixth degree with a raised fourth above the flat sixth degree.

Each of the three modifications documented below is called a **change**. The three changes' names, introduced in §1, are defined here in full:

**Dominant-ization** — the first change: the raising of the seventh degree at the cadential pre-tonic. Raising the seventh beside a flat sixth creates an augmented second, singers removed the augmented second by raising the sixth as well, and the raised sixth is therefore part of the Dominant-ization (§4, §5). The Dominant-ization's result is a cadential pre-tonic of dominant quality — in mature chordal form, dominant-seventh quality.

**Major-ization** — the second change: the imposition of a major third at the cadential tonic — the Picardy third made obligatory.

**Fortification** — the third change: the addition of the augmented sixth at the cadential pre-pre-tonic, preparing the Dominant-ized cadential pre-tonic.

**De-Ionian-ization** — the coming-apart documented in §7.

*The hyphenated-neologisms rule.* Terms coined in this paper are hyphenated — Ionian-ization, Ionian-izing, Dominant-ization, Major-ization, De-Ionian-ization, extra-modal, extra-diatonic — so that the coinage stays visible on the page. Established words, Fortification among them, are not.

### 3. The object measured

The rebuilt object is the final cadence of a minor-destination piece in the fully armed form the sequence assembled — every element established as practice by about 1740, the assembled form never the majority ending (§7): a cadential pre-pre-tonic driving onto the cadential pre-tonic by contrary semitones; a cadential pre-tonic whose internal tritone resolves onto the cadential tonic's frame, raised seventh rising a semitone to the tonic and fourth degree falling a semitone to the third; and a cadential tonic carrying a major third.

Measured against the minor-destination modes, every functional element of that final cadence is extra-modal. The raised seventh is extra-modal. The Picardy third is extra-modal. The augmented sixth is extra-diatonic — supplied by no diatonic mode whatever, and therefore extra-modal in every mode. The raised sixth that smooths the melodic path to the raised seventh is extra-modal as well — though §5 shows that the raised sixth is not an independent change, arriving instead as an inseparable part of the Dominant-ization.

The finding is when each element arrived, at which cadential position, in what order, how far apart — and then when, and in what manner, each element departed.

### 4. The rise

#### The Dominant-ization — the raised seventh, and the raised seventh's melodic repair. Established practice by the fourteenth century. Position: cadential pre-tonic.

The cadential inflection that raises the seventh degree — *musica ficta*, applied under the rubric *causa pulchritudinis* — is attested repeatedly from the fourteenth century onward; the rubric pairing (inflection *causa necessitatis*, to remove a forbidden interval, against inflection *causa pulchritudinis*, to sharpen a cadence) runs through the fifteenth-century sources surveyed in Berger (1987) and Bent (2002). Marchetto of Padua (1317–18) goes further, discussing the tuning of the inflected semitone narrower than a natural semitone — a tightened approach to the goal note.

In the corpora the inflection appears as the raised-seventh share of seventh-degree notes in minor-destination pieces: 4.9–7.8% in the fifteenth-century cohorts, rising to 14.0–15.4% by 1580–1619. The Dominant-ization precedes both other changes by at least a century and a half.

**The melodic repair.** Raising the seventh in a mode with a flat sixth creates an augmented second between the two degrees, an interval the repertories all but never traverse: once in 341,005 JRP notes, never in Palestrina's 153,963, seven times in Tasso's 76,445 (§5). The repair is to raise the sixth as well when a line passes beside the raised seventh. Pedagogy treats the raised sixth as a separate development, the "melodic minor" adjustment. The corpora do not: as §5 demonstrates, the rule *raise the sixth when a raised seventh is adjacent* operates at 79.7–93.9% in every corpus from 1420 to 1750 — high throughout, with no monotone trend. The raised sixth does not arrive later than the raised seventh; the raised sixth arrives with the raised seventh. What rises eightfold across those centuries — the raw raised-sixth rate, from 2.4% to 17.6% — is not the rule strengthening but the frequency of the rule's trigger increasing, which is the Dominant-ization spreading.

The Dominant-ization therefore has two faces: a raised seventh at the cadential pre-tonic, and a raised sixth wherever a line approaches the raised seventh. Note the limit of the Dominant-ization: the Dominant-ization rebuilds the cadential pre-tonic and leaves the cadential tonic alone. A Dorian piece in 1450 raises the seventh at the cadence and then lands on a bare octave-and-fifth, or on a minor sonority.

#### The Major-ization — the Picardy third. Under 5% before 1520; complete by c. 1565. Position: cadential tonic.

The cadential tonic falls in three stages, and the middle stage is what makes the third stage significant.

**Stage one: no third at all.** In the fourteenth-century trecento corpus, 99.0% of pieces (102 of 103) end on a cadential tonic containing no third — a bare octave or fifth. The question *major or minor?* cannot yet be asked.

**Stage two: thirds enter, and the entering thirds are minor.** Across the fifteenth century the no-third share of minor-destination endings falls from 93.5% (composers born 1420–39) to 72.4% (born 1440–59). The thirds that enter are the modal thirds: in the 1440–59 birth cohort, 26.3% of all minor-destination endings carry a minor third and 1.2% a major third, the remainder closing without any third.

**Stage three: the third becomes obligatorily major.** Among endings that carry a third: 4.4% major in the 1440–59 birth cohort (7 of 159, JRP); **40.0%** in 1540–59 (4 of 10, CRIM); **100.0%** in 1560–79 (15 of 15, CRIM); 99.0% in Palestrina (574 of 580, c. 1554–94); 100.0% (128 of 128), 97.4% (38 of 39) and 100.0% (15 of 15) in the Tasso corpus through 1649. From under five per cent to categorical inside roughly one generation, c. 1540–1565 — confirmed by two corpora with different editors, formats and repertories. Categorical here is §2's law criterion — totals in the sampled vocal repertories — not a claim over every region and genre. Zarlino's discussion of the minor triad as the less perfect division of the fifth is contemporaneous (1558).

Stage two is what distinguishes the Major-ization from a drift. Had the major third simply arrived along with thirds in general, the Major-ization would amount to no more than "cadential tonics acquired thirds." Instead a modal note was added, established across a century, and then systematically overridden by an extra-modal note. Both positions of the two-chord cadential nucleus — the cadential pre-tonic and the cadential tonic — are now extra-modal.

#### The Fortification — the augmented sixth. Noise-level through 1650; established by c. 1740; still rising at 1800. Position: cadential pre-pre-tonic.

The augmented sixth belongs to no diatonic mode: flat sixth degree in the bass, raised fourth above the flat sixth, the two converging by contrary semitones onto the cadential pre-tonic. The augmented sixth is a double leading-tone to the cadential pre-tonic — an extra-diatonic chord serving an extra-modal chord.

Two independent detection methods were used: diatonic-spelling simultaneity in the Humdrum corpora, and interval-name detection via chordification in the keyboard corpora. Through 1650 the augmented sixth registers only at detection-noise level: 18 events in 1.2 million notes of the Renaissance corpora — sixteen of the eighteen canonically voiced, all treated here as cross-relation and editorial noise pending event-level adjudication (Appendix III) — with the chromatic madrigalists included; Bach's chorales carry 3 in 370. Then, with medium held roughly constant across four keyboard corpora: Scarlatti (c. 1740) 0.73 per 1,000 verticalities, Haydn 2.67, Mozart 3.63, Beethoven 4.64.

Three observations locate the augmented sixth. The augmented sixth concentrates in minor: 6.13 per 1,000 in movements ending minor against 3.21 in movements ending major. The augmented sixth's bass note is the flat sixth degree — the one cadence-adjacent degree that the Dominant-ization and the Major-ization left modal, and a degree that Ionian lacks and must borrow from minor. And the augmented sixth's position within movements is broad, peaking mid-movement: by the Classical corpora the augmented sixth has generalized from final cadences to structural dominants at large.

#### The shape of the rise

**Spacing.** From the Dominant-ization to the Major-ization: at least a century and a half. From the Major-ization's completion to the Fortification's establishment: roughly **175 years**. Three changes across four centuries. This is not one event with several symptoms.

**Order.** The three changes occupy three adjacent positions of the final cadence — the Dominant-ization the cadential pre-tonic, the Major-ization the cadential tonic, the Fortification the cadential pre-pre-tonic — but position is not the ordering variable: the sequence runs neither tonic-outward nor outer-inward, and the cadential tonic is rebuilt after the cadential pre-tonic. What orders the sequence is how Ionian-izing each change is. Audit the seven modes for each installed feature:

| Change | Feature installed | Modes natively possessing the feature |
|---|---|---|
| Dominant-ization | semitone below the final; in mature chordal form, a cadential pre-tonic of dominant-seventh quality | as scale degree: Ionian and Lydian; as chord: **Ionian alone** — Lydian's fifth-degree seventh chord is of major-seventh quality |
| Major-ization | major third at the cadential tonic | Ionian, Lydian, Mixolydian — three of seven |
| Fortification | augmented sixth at the cadential pre-pre-tonic | **none**, Ionian included |

The Dominant-ization installs Ionian's signature: the one cadential feature that identifies Ionian uniquely among the seven modes. The Major-ization installs a feature Ionian shares with two other modes — three of the seven modes. The Fortification installs a feature possessed by no mode at all: the Fortification makes the final cadence resemble Ionian's not one degree more, fortifying instead the approach to the already-rebuilt cadential pre-tonic. The sequence therefore runs in strictly decreasing order of Ionian-izing effect: the unique identifier first, the shared feature second, the feature Ionian itself lacks last. Position falls out as a corollary: the cadential pre-pre-tonic is rebuilt last, and empirically only after both nucleus positions — no fifteenth-century augmented-sixth practice exists, and none in a repertory whose cadential tonics are still minor.

### 5. Two scales that are not scales

§4 treats the raised sixth as part of the Dominant-ization rather than as a change in the raised sixth's own right. The measurements supporting that placement establish something larger.

Pedagogy teaches minor as a scale in three forms: natural, harmonic (raised seventh), and melodic (raised sixth and seventh ascending, natural descending). If harmonic and melodic minor are scales, each makes a testable prediction. If harmonic and melodic minor are instead descriptions of the residue left by the Dominant-ization, each makes a different one.

**Harmonic minor's defining interval does not occur.** Melodic occurrences of the augmented second between the flat sixth and the raised seventh, in Aeolian and Phrygian pieces: **1** in 341,005 notes (JRP), **0** in 153,963 (Palestrina), 7 in 76,445 (Tasso). A scale is a melodic object — an ordered succession of steps a line may traverse — and an object whose characteristic step cannot be traversed is not a scale. Harmonic minor is a vertical description: raise the seventh inside the cadential pre-tonic, leave the sixth alone in the subdominant chord, then write the contents of both chords on a single staff as though the contents formed a line. The augmented second is not a step; the augmented second is the gap between two chords, which is why the corpora show the augmented second all but uncrossed.

**Melodic minor's rule names the wrong variable.** For every sixth-degree note in Aeolian and Phrygian pieces, the raised-sixth rate, split by direction and by proximity to a raised seventh within two notes:

| Corpus | ASC, near ♯7 | ASC, far | DESC, near ♯7 | DESC, far |
|---|---|---|---|---|
| JRP c. 1420–1550 | **87.4%** (n=223) | 4.0% (n=15,147) | — (n=20) | 0.6% (n=29,902) |
| Palestrina c. 1554–94 | **93.9%** (n=507) | 18.0% (n=5,932) | **77.4%** (n=328) | 10.3% (n=12,922) |
| Tasso 1571–1649 | **79.7%** (n=128) | 22.1% (n=2,686) | **37.0%** (n=73) | 4.7% (n=6,205) |
| Bach chorales c. 1720–50 | **87.5%** (n=272) | 33.1% (n=1,306) | 28.8% (n=80) | 13.2% (n=2,665) |

Holding direction constant, proximity multiplies the rate by 22×, 5.2×, 3.6× and 2.6×. In Palestrina, descending lines beside a raised seventh take the raised sixth 77.4% of the time — four times the rate of ascending lines that are not near a raised seventh. Direction is not the governing variable; adjacency to the raised seventh is. The rule survives in pedagogy because raised sevenths are usually approached from below, so "near a raised seventh" and "ascending" correlate heavily: the pedagogy encoded the correlate and lost the cause.

**The conditional rate is flat.** The conditional rate — raise the sixth, given a raised seventh adjacent, ascending — reads 87.4%, 93.9%, 79.7% and 87.5% across corpora spanning 1420 to 1750, while the raw raised-sixth rate rises eightfold. The rule was in force at full strength from the earliest corpus measured; what grew was the frequency of the rule's trigger. The sixteenth-century rise in raised sixths is the Dominant-ization's spread, observed through the Dominant-ization's own melodic repair — which is why this paper counts three changes and not four.

**What the two scales are.** Both describe the region around the raised seventh. Harmonic minor is the Dominant-ization described vertically; melodic minor is the Dominant-ization described horizontally. Nineteenth-century pedagogy inherited a repertory saturated with extra-modal raised sixths and sevenths, needed to teach that repertory, and scales are what pedagogy teaches — so pedagogy produced two, and harmonic minor contains a step the repertory forbids. The three-forms taxonomy is a filing scheme laid over an accumulation, and the filing scheme files one change twice. (Full analysis: the companion study *Two Scales That Are Not Scales*.)

### 6. Around the changes: the seven-mode field during the rise

**Part of the seven-mode field was removed rather than modified.** Lydian falls from 8.0% of works (composers born before 1440) to 2.9% to 0.0%, standing at 1.2% in 1571–1649; contemporaneously, Glarean (1547) files F-final pieces carrying a one-flat signature as transposed Ionian rather than as Lydian at all. Locrian never exceeds 0.4% in any corpus. Phrygian falls differently: 14.1% of sacred works against 2.9% of secular in the same period — Phrygian persists where repertory is bound to chant and has largely gone where repertory is not — and Phrygian's characteristic semitone-above-the-final survives into common-practice minor by relocation, becoming the iv⁶–V half cadence, bass falling ♭6→5, approaching the cadential pre-tonic rather than the cadential tonic. The Fortification is that relocated semitone with a second semitone added beneath the relocated semitone.

**The category proportions never moved.** Grouping modes by destination, the major/minor balance stands at 38.6/61.0 in 1420–1550 and 39.0/60.6 in 1571–1649. Ionian's own share of finals is likewise flat: 19.2% to 18.9% across two centuries. The rise did not move pieces onto C; the rise operated inside categories that stayed where the categories were.

### 7. The fall

#### The Major-ization shattered, 1740–1830

The Picardy third at the cadential tonic of minor-mode movements, measured across seven corpora:

| Corpus | Date | Minor endings | Picardy, closed endings | 95% CI |
|---|---|---|---|---|
| Tasso | 1580–99 | 128 | 128/128 = 100.0% | [97.1–100.0] |
| Tasso | 1600–19 | 39 | 38/39 = 97.4% | [86.8–99.5] |
| Bach chorales | c. 1720–50 | 138 | 130/138 = **94.2%** | [89.0–97.0] |
| Scarlatti sonatas | c. 1740 | 20 | 1/4 = **25.0%** | [4.6–69.9] |
| Haydn + Mozart sonatas | c. 1760–90 | 12 | 1/8 = 12.5% | [2.2–47.1] |
| Beethoven sonatas | c. 1795–1822 | 24 | 6/19 = 31.6% | [15.4–54.0] |
| Chopin preludes + mazurkas | c. 1830–45 | 31 | 3/21 = **14.3%** | [5.0–34.6] |
| Hooktheory popular song | c. 1960–2020 | — | 366/2,778 = **13.2%** | [12.0–14.5] |

The Minor-endings column counts all tonic-rooted minor endings, open closes included; the Picardy column's denominator is closed endings alone.

Three observations. **The collapse began inside the common practice**: Bach and Scarlatti overlap in date and stand seventy points apart, the chorale being the church-bound genre and the keyboard sonata the leading edge — a contrast that confounds genre with date, and one whose Scarlatti cell holds four closed endings (interval [4.6–69.9]). **The collapse completed by the 1830s, and the endpoints measured since coincide**: Chopin's 14.3 percent and modern popular song's 13.2 percent are the same number. No repertory between the 1840s and the modern corpus is measured here, so constancy across the interval is an inference from two agreeing endpoints, not a series. **The keyboard repertoire also found a third answer**: sixteen of Scarlatti's twenty minor endings, and a third of Chopin's, close on a bare octave or fifth — the fourteenth century's ending returned, declining the choice the Major-ization had forced.

#### The Dominant-ization bent

The raised-seventh share of seventh-degree notes in minor-destination pieces: 4.9 to 7.8 percent in the fifteenth-century cohorts; 14.0 to 15.4 percent in 1580–1619; **12.4 percent** (7,467 of 60,214) in modern Aeolian popular song. Four centuries of style change — the seconda pratica, the galant, Romanticism, the collapse of common practice, the rise of recorded popular music — moved the raised-seventh rate by three points. Modern songwriters raise the seventh where the raised seventh points somewhere, at 12.4 percent of opportunities, exactly as Monteverdi's contemporaries did at 15.4.

#### The Fortification rose through the fall

Between 1740 and 1820 the Major-ization fell from 94 percent (the chorale corpus) toward 14 while the Fortification rose sixfold; from Scarlatti forward the two series run in the same keyboard corpora. The De-Ionian-ization of the cadential tonic and the continued arming of the cadential pre-pre-tonic ran concurrently. The Fortification's modern fate is not measured here, and cannot be measured in the Hooktheory corpus: Hooktheory's annotators encode chords by sound, an augmented sixth is enharmonically identical in sound to a dominant seventh, and the spelling that defines the augmented sixth does not survive Hooktheory's sound-based encoding.

#### After the release

Modern popular song, 26,175 entries with modes declared by the annotators: Ionian 50.4%, Aeolian 39.3%, Mixolydian 3.9%, Dorian 3.8%, Phrygian 1.1%, Lydian 1.0%, Locrian 0.3%, with 0.3% of songs declaring a scale that matches no diatonic mode.

Aeolian returned, declared as Aeolian at two-fifths of the repertoire, and the release divided into three facts. The Dominant-ization persists, unchanged. The Major-ization reversed completely. And the category structure did not reverse at all: Dorian, the single most common mode in 1500 at 37 percent, stands at 3.8; Phrygian at 1.1; Lydian at 1.0; Locrian at 0.3; Ionian and Aeolian together hold 89.7 percent. The pruning of the seven-mode field — the part of the Ionian-ization that operated by removal rather than by grafting — outlived the grafts by centuries and shows no sign of reversing.

### 8. The teaching record

The teaching literature is a corpus written by the Ionian-ization's own witnesses, and the teaching literature's dates can be laid against the corpus dates at every transition.

**The rise's earliest pedagogy states the Dominant-ization as conditional.** The fifteenth-century rubric *causa pulchritudinis* — an inflection for beauty — names an option, and the rubric names the option a century after the fourteenth-century practice the rubric describes. From that rubric to the modern rule "raise the sixth and seventh ascending," the teaching literature always gave the raised seventh a condition, and never stated the raised seventh as a law.

**The Major-ization's rationale arrives mid-transition.** The corpus transition runs c. 1540–1565; Zarlino's account of the minor triad as the less perfect division of the fifth is 1558 — theory rationalizing a change already half complete.

**The law's prescriptive era speaks in Simpson.** Simpson's *Compendium of Practical Musick* (1667; examined here in the 1722 printing) treats the major third at the close of a flat-key piece as standing practice and legislates only the third's voicing, judging "the sharp 3d more proper for an inward part at conclusion" — a teaching text written inside the law's window, presupposing the law rather than instituting the law.

**The Major-ization's obituary arrives twenty-five years after the leading edge abandons the Major-ization.** The leading-edge collapse begins by the 1740s; Rousseau's *Dictionnaire de musique* coins "tierce de Picardie" in 1768 (the volume is dated 1767) — and coins the term, by Rousseau's own account, as a joke. Rousseau reports that ending minor pieces on a major chord was *formerly a law*, and that composers now end with the chord suited to the piece's mode. Rousseau's entry names the Picardy third at the moment of the Picardy third's obsolescence, attests the Picardy third's former status as a law in that exact word, and locates the Picardy third's last stronghold in church music.

**The Fortification's codification trails the Fortification's establishment by fifteen to forty years, and the Fortification's classroom form by nearly a century.** Composers establish the augmented sixth by 1740; Marpurg derives the augmented sixth as an altered tertian harmony in the 1750s; Rameau declares in 1760 that the augmented sixth has no fundamental bass and cannot be inverted; Kirnberger treats the augmented sixth in *Die Kunst des reinen Satzes* (1771–79); Vogler and Gottfried Weber systematize the altered-tertian account after 1800; and the Italian, French, and German labels arrive last of all, as classroom mnemonics with no real geographic basis.

**The magnification is measured, and the magnification then became self-perpetuating.** Bach's chorales — the church-bound, pedagogy-adjacent genre — hold the Major-ization at 94.2 percent in the same decades that Scarlatti's sonatas hold the Major-ization at 25. C. P. E. Bach then published his father's chorales in the 1760s–80s; the collections entered classroom use, became a standard teaching corpus of harmony instruction, and remain in classroom use today. The most Major-ized repertoire of the 1740s thereby entered the teaching canon — which is why textbooks still teach the Picardy third while composers use the Picardy third in one closed minor ending out of seven. A teaching corpus can carry the Major-ization for two hundred and fifty years after the Major-ization's death.

**The taxonomy finishes last of all.** The three-forms filing of minor completed only in the twentieth century, when the term "natural minor" entered common use — three hundred years after the practice that the three-forms scheme files.

The summary fact, stated once: at every measured transition — the rubric after the practice, Zarlino mid-rise, Rousseau after the collapse, Marpurg through Kirnberger after the establishment, the taxonomy last — the written record moves a generation or more behind the composed record, and Simpson writes from inside the Major-ization's window, presupposing rather than instituting. In none of the sources examined — the ficta rubrics, Glarean, Zarlino, Simpson, Rousseau, Marpurg, Rameau, Kirnberger, Vogler, Weber, and the three-forms taxonomy — does a prescription precede the practice the prescription describes; the Purcell-revised Playford (1694) remains unexamined and stands as a named test.

### 9. What any explanation must satisfy

Part I is agnostic about causes. Part I's shape is not. Six constraints fall out of the data.

**C1 — Seriality of the rise.** Three changes across four centuries, roughly 175 years between the Major-ization's completion and the Fortification's establishment. Any single-event cause — a taste shift, a generational turn, a technological moment — is excluded.

**C2 — Ordering by Ionian-izing effect.** The three changes arrive in strictly decreasing order of Ionian-izing effect: the unique identifier, then the shared feature, then a feature no mode possesses. An adequate explanation must produce that gradient. The gradient also carries the positional dependency: the least Ionian-izing change, whose function is to approach the rebuilt cadential pre-tonic, appears only after the nucleus is rebuilt.

**C3 — Dependency structure.** One apparent change is not independent: the raised sixth arrives with the raised seventh, the conditional rate high (79.7–93.9%) in every corpus across three centuries. An adequate explanation must distinguish changes from consequences — must say why the raised seventh's melodic repair follows instantly while the cadential tonic's rebuilding waits a century and a half, and the cadential pre-pre-tonic's rebuilding another hundred and seventy-five years.

**C4 — Three-way reversibility.** The De-Ionian-ization split the three outcomes: the Major-ization shattered (94 to 14 in ninety years, the Chopin-era and modern endpoints coinciding); the Dominant-ization bent (three points in four centuries); the emptied categories never refilled (Dorian 37 percent to 3.8). Perception did not change in 1740, and perception did not change in 1950. Any purely perceptual explanation predicts the changes rising together and falling together, and the changes did neither.

**C5 — Concurrency of rise and fall.** Between 1740 and 1820 the Major-ization fell while the Fortification rose — both series in the keyboard corpora from Scarlatti forward, the collapse's chorale-corpus starting point noted. Any account that treats 1740–1820 as a single motion — elaboration, simplification, decline — must explain why the same decades moved two adjacent cadential positions in opposite directions at once.

**C6 — The lag.** The written record trails the composed record at every transition measured here, by fifteen to a hundred years, and in the sources examined no prescription precedes the practice the prescription describes. Any explanation in which theory or teaching drives the changes is excluded — and any explanation that appeals to written rules must locate the operative rule in practice, with the writing as the rule's record rather than the rule's engine.

---

## Part II — The explanation

### 10. Candidates, ranked against the constraints

**(a) A taste shift toward major sonority.** Fails C1, the changes being serial rather than simultaneous; fails C2, since a preference for major thirds has no reason to reach the cadential tonic a century before the cadential pre-pre-tonic; fails C5, since a taste for major cannot rise and fall at adjacent positions at once. Retained only as a possible local contributor to the Major-ization.

**(b) Perceptual superiority.** Huron's derivation of voice-leading norms from auditory principles (2001, 2006) plausibly explains why the operative rules were what the rules were — why semitones pull, why the tritone was policed. As a direct cause of the rise and fall, perception fails C4: hearing is constant, and the fall split the three outcomes along a line hearing does not draw. Perception belongs underneath the explanation rather than in the explanation.

**(c) Vernacular assimilation.** Glarean's account (1547) presents the added modes as already current outside the church repertory; perhaps learned practice merely caught up with popular practice. Vernacular assimilation satisfies C1, being a standing pull, but not C2 — nothing in vernacular priority explains the Ionian-izing gradient — and vernacular assimilation is silent on C3, C4 and C5. The corpora give vernacular practice a limited but real role: secular repertory led on subtraction, having shed Phrygian (2.9 percent secular against 14.1 sacred) long before sacred music did. A contributing current, not the mechanism.

**(d) Theory-driven change.** Perhaps the treatises taught the changes and composers complied. C6 excludes theory-driven change outright: the treatises trail the composers at every transition, and one cannot cause what one follows. The teaching record's actual role appears under (e).

**(e) The fixed-point conjecture.** Polyphonic practice operated under two maintenance rules, applied by singers wherever cadences were made: inflect to remove the tritone against the final, and inflect to supply the cadential semitone. The rules are practiced rules; the treatises that name the rules — *causa necessitatis*, *causa pulchritudinis* — are the rules' record, written a century after the practice, exactly as C6 requires. Jointly the two rules specify one diatonic configuration — raised seventh present, tritone-with-the-final absent — and exactly one mode satisfies both without alteration: Ionian, whose final cadence, once seventh chords standardize, is V7–I. The conjecture: **these standing practiced rules carried every mode's final cadence toward that one stable configuration; the rise of §4 is the record of the carrying; and the fall of §7 is what the carried structure did when the styles enforcing each part of the structure changed, each part failing according to each part's own kind.**

Against the constraints:

The conjecture satisfies **C1** because the rules were standing — applied at every cadence, for centuries — a constant force producing serial change as each solution's residue became the next target: the rebuilt cadential pre-tonic leaves the cadential tonic mismatched, and the cadential tonic is made major; the rebuilt cadential pre-tonic stands unprepared, and a cadential pre-pre-tonic is built for the rebuilt cadential pre-tonic.

The conjecture satisfies **C2** because the two rules, taken jointly, are a specification of precisely the feature that is unique to Ionian: the cadential semitone rule commands the raised seventh, the tritone rule requires the perfect fourth, and those two degrees are exactly the tendency-tone pair of the dominant seventh. The rules do not describe Ionian and command imitation; the rules command two inflections whose joint product is the one cadential machine only Ionian possesses natively. The Dominant-ization is the rules executed — which is why the most Ionian-izing alteration comes first: the Dominant-ization is the only alteration the rules directly command. The remaining changes are consequent rather than commanded, each harmonizing another cadential position with what the Dominant-ization installed, and each adding less resemblance than the last because the identifier is already in place — the cadential tonic matched to the rebuilt pre-tonic (the Major-ization), the rebuilt pre-tonic given a preparation (the Fortification), a preparation that Ionian never needed and cannot natively build.

The conjecture satisfies **C3** because the conjecture distinguishes two kinds of consequence. The raised sixth repairs a defect internal to a single line — an unsingable interval — and a line either works or does not work, so the repair is immediate and the repair's rate is flat from the first. The Picardy third and the augmented sixth repair defects in the relation between chords, and a relation between chords becomes audible as a problem only after the surrounding harmonic apparatus develops. Immediate melodic repair, delayed harmonic repair: the conjecture predicts the dependency structure observed.

The conjecture satisfies **C4** because the three outcomes had three structures, and structure fixes fate. The Major-ization had hardened into a **law**, and a law has two states: while the enforcing style holds, compliance is total, because the alternative has stopped being available to a competent practitioner — as a minor final chord had stopped being available between 1565 and 1740, in the way parallel fifths had stopped being available. When the enforcing style loosens, no seventy-percent version of the law exists to retreat to; "always" becomes "composer's choice" in one step, and the rate falls immediately to wherever taste sits — two centuries at ceiling, a ninety-year fall, then endpoints two centuries apart that coincide. The Dominant-ization was always a **choice** — *causa pulchritudinis* names a condition, not a duty — and a choice has a continuum of states, so a choice has nothing to shatter: a rule of the form "apply this where the condition holds" survives any change of style that leaves the condition still occurring somewhere, which is why four centuries moved the raised-seventh rate by three points. And the emptied **categories** never refilled because a category, once emptied, has no condition under which the category refills: laws shatter, choices bend, and categories stay empty. Perception explains none of the three curves; the three conventions' statuses explain all three curves.

The conjecture satisfies **C5** because the two concurrent motions served different cadential positions. The Major-ization decorated the arrival, and the arrival's law broke with the galant loosening; the Fortification served the still-standing Dominant-ized cadential pre-tonic, and the Fortification spread with the styles that used the Fortification. One structure falling while another structure rises is exactly what independent structures do, and is inexplicable only to an account that insists 1740–1820 had one direction.

The conjecture satisfies **C6** by construction, and C6 in turn assigns the teaching literature the teaching literature's real role: a trailing mirror and a magnifier. The treatises record the practiced rules a generation late, encode each convention in the kind — law or choice — that the convention's corpus curve independently displays, and magnify whatever repertoire the treatises carry: the chorale corpus, embalmed as teaching material in the 1760s–80s, carried the shattered Major-ization into classrooms for two hundred and fifty years. The teaching literature is evidence throughout, and engine nowhere.

**What the conjecture does not claim, and cannot exclude.** The conjecture does not claim intention: nobody aimed at Ionian, which had no name in church theory before 1547. The conjecture does not claim the rules were arbitrary: the rules' perceptual grounding (b) and vernacular reinforcement (c) are compatible substrates, and the true history is most likely (e) running on (b) with (c) alongside. What the conjecture cannot exclude is a hybrid in which vernacular practice supplied the direction and the practiced rules merely ratified vernacular practice; separating the hybrid from the conjecture requires corpus work on secular monophony before 1500 — mode-and-cadence rates in the trouvère, Minnesang and early song repertories — which does not yet exist in analyzable form. That is the conjecture's open flank.

### 11. Objections

**"Ionian's share of finals never grew, so nothing converged."** §6 reports the flat share as data; no claim of migration is made. The sequence operates on cadential content, below the level a finals-count can detect: at final cadences the modes differ sevenfold in repair-need (Ionian 63.9% requiring no inflection against Aeolian's 8.5%) while the finals stay put. Rebuilding in place is the observation; migration would have indicated abandonment rather than convergence.

**"Aggregate cadence measures show no trend."** Correct, and expected. The repair-need rate computed over all cadences is flat at 23–24% in every cohort, because cadences landing away from a piece's final are mode-neutral — 22–24% in every genre and every period — and mode-neutral cadences outnumber mode-confirming cadences four to one. Nothing in §4 or §5 pools inert cadences with mode-confirming cadences.

**"The modes may not have been compositionally real (Powers)."** The finding is measured on sounding pitch content — thirds in cadential tonics, raised degrees, augmented-second occurrences, augmented-sixth simultaneities — and the conjecture invokes practiced rules, which are documented operations whatever name the operated-on objects carry. The objection dissolves a vocabulary; the sequence and the mechanism survive in any vocabulary.

**"Editorial ficta contaminates the counts."** The strongest technical objection, and the reason the argument rests on measures robust to editorial ficta. The Picardy third is a written note in a cadential tonic; the augmented sixth is a spelled simultaneity. Every raised-degree figure quoted above comes from a corpus that marks editorial accidentals explicitly (JRP, Tasso) or declares the corpus's modes (Palestrina); corpora satisfying neither condition are used only for measures independent of both. The augmented-second result in §5 is robust in the conservative direction: editors supplying ficta tend to create augmented seconds rather than suppress augmented seconds, and the observed count is near zero regardless.

**"The proximity result depends on the window."** The window is ±2 notes in the same voice, with ±1 and ±3 reported in Appendix III. The direction-versus-proximity comparison holds in all four corpora at every setting, and the decisive cell — descending-near exceeding ascending-far — is a within-setting comparison at each window.

**"The written rules postdate the practice, so the rules cannot be the cause."** Correct about the writing, and the conjecture agrees: the operative rules are the practiced rules, applied by singers at cadences, and the treatises are the practiced rules' record. C6 is a constraint the conjecture is built to satisfy, not an objection the conjecture must survive.

**What would falsify the finding.** Any of: the changes proving simultaneous under better dating; the Ionian-izing gradient inverting — a repertory establishing Picardy thirds before raised sevenths, or augmented sixths while the repertory's cadential tonics remain minor; a sixteenth-century augmented-sixth practice; the 1540–65 transition dissolving into a three-century drift; the raised sixth's conditional rate proving to rise over time; a dated corpus of minor endings between 1740 and 1830 holding the Picardy third at ceiling; a mainstream composition textbook after 1780 prescribing the major final third as exceptionless; a modern corpus with declared modes showing the raised seventh collapsed toward zero; or a prescription anywhere in the record that precedes the practice the prescription describes.

### 12. Coda: the cadence of changes

One structural observation, offered as an observation.

The sequence has the shape of the final cadence the sequence built. Each change resolves a tension the previous change created, and creates the tension the next change resolves — and does so, as a cadence does, on two time-scales at once. The raised seventh leaves an unsingable interval hanging in the line, and that interval is resolved immediately, in the same breath, the way an appoggiatura resolves. The raised seventh also leaves the cadential tonic mismatched to the rebuilt pre-tonic, and that mismatch is resolved a century and a half later; and the raised seventh leaves the rebuilt pre-tonic unprepared, and that preparation waits another hundred and seventy-five years. Immediate resolution and long suspension, running simultaneously: the near tension settled at once, the far tensions held across generations.

Then the sequence stops. After the Fortification there is no fourth change. The Ionian-ization, after four hundred years, ends at the moment the final cadence is completely rebuilt — rebuilt, in the end, past Ionian itself: minor's final cadence closes more heavily armed than Ionian's own, fortified by a chord that Ionian must borrow from minor to use. And a cadence is precisely that: motion whose function is to end motion.

The release did not wait for the arrival. While the Fortification was still rising, the Major-ization was already falling — 94 percent in Bach's chorales, 25 in Scarlatti, 14 by Chopin — a tone of the resolution sounding before the final chord, which music calls an anticipation. The Major-ization fell away, the Dominant-ization remained the choice the Dominant-ization had always been, and Aeolian — never destroyed, only rebuilt at Aeolian's edges — was simply there again, as Aeolian had been all along beneath the changes. The fermata lifted. The music moved on.

---

## Appendix I — Sources, Methods, and Data

### A. Sources

*Primary and pedagogical.* *Musica enchiriadis* (late 9th c.); Guido of Arezzo, *Micrologus* (c. 1026); Marchetto da Padova, *Lucidarium* (1317–18); the *causa necessitatis / causa pulchritudinis* tradition (Hughes 1972; Berger 1987); Glarean, *Dodecachordon* (1547); Zarlino, *Le istitutioni harmoniche* (1558; rev. 1589); Simpson, *A Compendium of Practical Musick* (1667; 1722 printing examined); Rameau, *Traité de l'harmonie* (1722), and Rameau's 1760 denial of the augmented sixth's fundamental bass; Rousseau, *Dictionnaire de musique* (1768, volume dated 1767; Waring's English translation 1779), art. "Tierce de Picardie"; Marpurg's altered-tertian derivation of the augmented sixth (1750s); Kirnberger, *Die Kunst des reinen Satzes in der Musik* (1771–79); the systematizations of Vogler and Gottfried Weber; C. P. E. Bach's editions of J. S. Bach's chorales (1765–69; 1784–87). The treatises are available through IMSLP and the Internet Archive.

*Scholarship.* Berger, *Musica Ficta* (1987); Bent, *Counterpoint, Composition, and Musica Ficta* (2002); Powers, "Tonal Types and Modal Categories" (1981) and "Is Mode Real?" (1992); Meier (1974/1988); Dahlhaus (1968/1990); Lester, *Between Modes and Keys* (1989); Christensen (1993); Dodds, *From Modes to Keys in Early Modern Music Theory* (2023); Huron, "Tone and Voice" (2001) and *Sweet Anticipation* (2006); Laudan (1977); Donahue, Simon & Dieleman, "Melody Transcription via Generative Pre-training" (2022) for the Hooktheory release.

### B. Corpora

| Corpus | Works used | Dating variable | Mode assignment | Editorial accidentals |
|---|---|---|---|---|
| Trecento (music21 corpus) | 103 | repertory c. 1325–1425 | final + signature | unmarked; corpus used only for third-presence |
| Josquin Research Project | 1,282 classifiable (1,278 with genre metadata) | composer birth cohorts | final + signature | marked; separable |
| CRIM | 259 | per-piece date_sort | not inferred; corpus used only for cadential-third measures | MEI accid vs accid.ges separable |
| Palestrina (music21 corpus) | 1,257 | c. 1554–94 | declared mode tags | unmarked |
| Tasso in Music Project | 499 | per-work publication date | final + signature | marked; separable |
| Bach chorales (Sapp) | 370 | c. 1720–50 | kern key designation | written text |
| Scarlatti / Haydn / Mozart / Beethoven sonatas (Sapp) | 65 / 25 / 69 / 103 movements | composer activity dates | key-finding per movement | written text |
| Chopin preludes + mazurkas (Sapp) | 24 + 52 | opus dates c. 1830–45 | key-finding per movement | written text |
| Hooktheory (Donahue release) | 26,175 songs | modern, c. 1960–2020 | annotator-declared scale | not applicable (pitch-class encoding) |

Scope restrictions, stated once. CRIM contributes only written-third measures (the Picardy transition), because CRIM mode inference was found unreliable and withdrawn; Appendix III records the withdrawal. Palestrina contributes raised-degree measures under declared modes with editorial status unmarked; §11's robustness argument covers the exposure. Hooktheory contributes no augmented-sixth measure, for the encoding reason given in §7, and carries no per-song dates.

### C. Operational definitions

1. **Mode inference (final + signature).** The final is the last sounding pitch class of the lowest voice; the signature is the encoded key signature; the pair maps to a mode label by the standard untransposed and one-flat-transposed grids. Palestrina uses the corpus's declared tags instead; the Bach chorales use the kern key designation; the keyboard and Chopin corpora use the Krumhansl–Schmuckler key-finding algorithm as implemented in music21, applied per movement.
2. **Raised degree.** A seventh- or sixth-degree note above the inferred final carrying a sharpening accidental, or a natural cancelling a signature flat, in the encoded text. In the corpora that mark editorial supply (JRP, Tasso), editorially supplied accidentals are excluded from headline rates and tallied separately.
3. **Closed and open endings.** A closed ending is a final tonic-rooted sonority containing a third; an open ending contains none. Picardy percentages are computed over closed endings only, with open counts reported beside the percentages.
4. **Final sonority.** In the vocal corpora, the last simultaneity of the piece. In the keyboard corpora, every note sounding at the final offset, sustain included; the sonority's root is the lowest pitch; a movement enters the ending counts only when that lowest pitch class equals the movement's inferred tonic.
5. **Augmented sixth.** Two detectors. Spelled-simultaneity: a flat sixth degree sounding against a raised fourth degree, any voicing, spelling intact. Interval-name: chordification followed by detection of the interval named augmented sixth. Rates are per 1,000 distinct verticalities of the chordified movement.
6. **Conditional raised-sixth rate.** Over sixth-degree notes in Aeolian and Phrygian pieces: *near* means a raised seventh within two notes in the same voice (the headline setting; ±1 and ±3 in Appendix III); direction is the sign of the next different pitch; each cell's rate is raised over raised-plus-natural.
7. **Augmented-second event.** An adjacent same-voice pair, flat sixth to raised seventh or the reverse, spelled as an augmented second.
8. **Hooktheory measures.** A song's mode, for the share table, is the scale of the song's first key annotation, mapped from the declared scale-degree intervals; 0.3% of songs declare a scale matching no diatonic mode and are reported as unclassified. The degree and ending measures use only songs whose key annotations all agree on tonic and scale. The raised-seventh rate is the share of Aeolian-song melody notes lying eleven semitones above the tonic, over melody notes lying ten or eleven semitones above the tonic (7,467 of 60,214). The Picardy rate is the share of Aeolian songs whose final tonic-rooted harmony carries a major third, over Aeolian songs whose final tonic-rooted harmony carries any third (366 of 2,778); the Ionian control is the same measure on Ionian songs (3,378 of 3,414 = 98.9%). `ht_measures.py` (Appendix II) computes all four measures.
9. **Pedagogical lag.** Treatise publication date minus the corpus establishment date of the practice the treatise records.

### D. Statistical conventions

Intervals are Wilson 95% confidence intervals throughout. Cells below roughly n=25 are reported with intervals and not interpreted alone; the JRP descending-near cell (n=20) is reported and not interpreted. The headline proximity window is ±2 and the headline cadence threshold is 2; Appendix III reports ±1, ±3, and thresholds 1 and 4, within which every ordering claim of §5 and §11 holds.

### E. Software

Python 3 with music21 (Cuthbert) for parsing, chordification, and key-finding; a custom kern parser for the raised-degree measures, written because music21's kern reader discards the editorial-accidental marker that definition C2 depends on; MEI read directly for CRIM. The analysis code is Appendix II.

### F. Data availability

Josquin Research Project: josquin.stanford.edu and github.com/josquin-research-project/jrp-scores. CRIM: crimproject.org. Tasso in Music Project: tassomusic.org and github.com/TassoInMusicProject/tasso-scores. Palestrina and trecento corpora: distributed with music21. Keyboard and chorale corpora: github.com/craigsapp — bach-370-chorales, scarlatti-keyboard-sonatas, haydn-piano-sonatas, mozart-piano-sonatas, beethoven-piano-sonatas, chopin-preludes, chopin-mazurkas. Hooktheory: the Donahue release accompanying "Melody Transcription via Generative Pre-training" (github.com/chrisdonahue/sheetsage). Every corpus is public; no licensed or private data enters any number in the paper.

### G. Confidence and known limitations

The post-Bach minor-movement cells are small (12 to 31), and the Bach-against-later contrast crosses a genre boundary (chorale against keyboard sonata) as well as a date; the 94-against-25 contrast is robust to both, and the fine structure between Scarlatti and Beethoven is not. Movement keys in the keyboard corpora come from an algorithm, not from declared keys. The claim that C. P. E. Bach's chorale editions were marketed for harmony study, and the editions' dates, are stated from general knowledge and were not verified against the volumes. Simpson's *Compendium* (1667) has been examined in the 1722 printing: Simpson treats the major final third of a flat-key piece as standing practice and legislates only the voicing, an attestation from inside the law's window. The Purcell-revised Playford (1694) remains unexamined. The Major-ization's status as a law rests on the corpus ceilings, on Simpson's mid-era attestation, and on Rousseau's retrospective attestation. The Fortification's modern rate is unmeasured for the reason given in §7. The Hooktheory corpus is undated per song, so the modern column is a pooled snapshot rather than a series. Zhu Zaiyu, the Zeng bells, and the comparative material of earlier drafts belong to a companion argument and are not load-bearing here.

Reproduction status, stated plainly. Validated against the published cells, exactly: `scale_cells.py` (the §5 joint table, all sixteen cells), `scale_marginals.py` (Test 1's augmented-second counts with note totals to the digit), `vocal_series.py` (Palestrina 574/580, the three Tasso period cells, trecento 102/103, and the Lydian, Phrygian, and destination series), `pscan.py` (the §7 ending table), and `ht_measures.py` (the four modern-song measures). Pending, with no validated driver: the augmented-sixth series — the listed `aug6.py` uses a per-note denominator and pairwise counting that can count one verticality more than once, and the distinct-verticality rebuild with the stated denominator, the minor–major split, the positional distribution, and an event list is the named next step; the CRIM final-third split; and the raised-degree series under editorial-provenance exclusion, for which the parser exposes the needed flags. The kern parser reads only the first pitch of a space-separated kern chord token and rejects divided staves; the vocal corpora used are one note per spine, and the keyboard analyses run through music21, so the exposure is confined to the chorale subset already disclosed in Appendix III. Recalibrations under the canonical-code policy: the JRP base is 1,282 classifiable works (1,278 with genre metadata); Locrian counts 5 of 1,282; and the fifteenth-century ending cells carry the driver's birth-cohort bases, stated in §4.

## Appendix II — Code

The scripts below are the analysis code, listed verbatim; the same files, together with the cached per-movement JSON results for every keyboard corpus and one superseded script (`picardy_scan.py`, an earlier ending scan replaced by `pscan.py`, generating no number in the paper), accompany the paper as `cadence-of-change-analysis.tar.gz`.

| Script | Computes | Sections |
|---|---|---|
| `kernparse.py` | kern parsing preserving the editorial-accidental marker | all raised-degree measures |
| `cadence.py` | final-cadence extraction, mode inference, cadential thirds | §4, §6 |
| `run_study.py` | JRP cadence detection and the repair-free series: thresholds, cohorts, notation provenance | §11; Appendix III B–C |
| `minorscales.py` | augmented-second events; marginal direction and proximity splits | §5 |
| `scale_cells.py` | joint direction-by-proximity cells and conditional rates, window-parameterized; reproduces the §5 table exactly | §5 |
| `scale_marginals.py` | driver for `minorscales.py`: augmented-second counts and marginal splits; reproduces §5's Test 1 exactly | §5 |
| `vocal_series.py` | mode-field tables, Lydian, Phrygian, and destination series, and the final-third stages across trecento, JRP, Palestrina, and Tasso; validated cell by cell | §4, §6; Appendix III D |
| `aug6.py` | spelled pairwise augmented-sixth detector over note pairs, per-note denominator; the distinct-verticality rebuild with the stated denominator and splits is pending (Appendix I G) | §4, interim |
| `mei_analyse.py` | CRIM MEI reader; partial — the minor–major final split is pending (Appendix I G) | §4, interim |
| `pscan.py` | keyboard and chorale ending scan: closed and open endings, Picardy rates, JSON caching | §7 |
| `ht_measures.py` | Hooktheory: mode shares, raised-seventh rate, Picardy rates and control | §7 |

### Running the code

Order of operations: download the corpora; run `vocal_series.py` for the mode-field tables and the final-third stages; `scale_cells.py` (extract the degree cache once, then report at any window) and `scale_marginals.py` for §5; `run_study.py` for the cadence and repair-free series; `pscan.py` for the ending scans (the JSON caches make re-runs incremental); `ht_measures.py` runs from the release file directly. Each headline number regenerates in minutes on an ordinary laptop; the full keyboard scans, parse-bound, take tens of minutes per corpus on first run and seconds from cache.

### kernparse.py

```python
"""Minimal Humdrum **kern parser that preserves accidental provenance.

Key point: JRP marks editorial accidentals with a trailing 'i'. We must keep
that distinction, so we do NOT use music21 (which normalises it away).
"""
import re, os

PC = {'c':0,'d':2,'e':4,'f':5,'g':7,'a':9,'b':11}
DIA = {'c':0,'d':1,'e':2,'f':3,'g':4,'a':5,'b':6}

note_re = re.compile(r'(\d+)(\.*)([a-gA-G]+)(-+|#+|n)?(i)?')

def parse_dur(num, dots):
    if num == 0:
        return 0.0
    base = 4.0 / num if num else 0.0
    if num == 0: base = 8.0
    total = base; add = base
    for _ in dots:
        add /= 2.0; total += add
    return total

def token_note(tok):
    """Return dict or None. Handles kern pitch: lowercase=c4 up, uppercase=below."""
    if tok in ('.', '') or tok.startswith('!') or tok.startswith('*') or tok.startswith('='):
        return None
    if 'r' in tok.split('[')[0].replace('rest',''):
        # rest token: digits + r
        if re.match(r'^[\d.]*r', tok.replace('[','').replace(']','')):
            m = re.match(r'^(\d+)(\.*)', tok)
            if m:
                num = int(m.group(1))
                d = parse_dur(num, m.group(2)) if num else 8.0
                return {'rest': True, 'dur': d}
            return {'rest': True, 'dur': 0.0}
    m = note_re.search(tok)
    if not m:
        return None
    num = int(m.group(1)); dots = m.group(2); letters = m.group(3)
    acc = m.group(4) or ''; ed = bool(m.group(5))
    dur = parse_dur(num, dots) if num else 8.0
    L = letters[0]
    n = len(letters)
    if L.islower():
        octv = 4 + (n - 1)
        step = L
    else:
        octv = 3 - (n - 1)
        step = L.lower()
    alter = 0
    if acc.startswith('-'): alter = -len(acc)
    elif acc.startswith('#'): alter = len(acc)
    elif acc == 'n': alter = 0
    midi = 12 * (octv + 1) + PC[step] + alter
    dstep = octv * 7 + DIA[step]          # diatonic step number
    return {'rest': False, 'dur': dur, 'midi': midi, 'dstep': dstep,
            'step': step, 'octv': octv, 'alter': alter,
            'acc_written': acc != '', 'editorial': ed,
            'tie_start': '[' in tok, 'tie_cont': '_' in tok, 'tie_end': ']' in tok}

def parse_file(path):
    """Return (meta, voices) where voices is list of event lists with onsets."""
    txt = open(path, encoding='utf-8', errors='ignore').read()
    meta = {}
    for k in ('AGN','COA','COM','CDT','OTL','jrpid','voices'):
        m = re.search(r'!!!' + k + r': *(.*)', txt)
        if m: meta[k] = m.group(1).strip()
    lines = txt.split('\n')
    kern_idx = None
    voices = None
    times = None
    keysig = None
    for line in lines:
        if not line or line.startswith('!'):
            continue
        cells = line.split('\t')
        if line.startswith('**'):
            kern_idx = [i for i, c in enumerate(cells) if c == '**kern']
            voices = [[] for _ in kern_idx]
            times = [0.0 for _ in kern_idx]
            continue
        if kern_idx is None:
            continue
        if line.startswith('*'):
            for c in cells:
                if c.startswith('*k['):
                    keysig = c[3:-1]
            # spine manipulation -> bail out of this file (only 106/1387)
            if any(c in ('*^', '*v', '*+', '*-') for c in cells):
                if any(c in ('*^', '*v', '*+') for c in cells):
                    return None, None
            continue
        if line.startswith('='):
            continue
        if len(cells) <= max(kern_idx):
            continue
        for vi, ci in enumerate(kern_idx):
            ev = token_note(cells[ci])
            if ev is None:
                continue
            ev['onset'] = times[vi]
            times[vi] += ev['dur']
            voices[vi].append(ev)
    meta['keysig'] = keysig or ''
    return meta, voices
```

### cadence.py

```python
"""Detect Renaissance clausulae (6->8 expanding, contrary stepwise) and classify
whether the diatonic context already supplies the semitone approach ('repair-free')
or whether the cadence rule demands an inflection ('repair-demanded')."""
import re
from kernparse import parse_file, PC, DIA

def ksig_alter(keysig):
    alt = {}
    for m in re.finditer(r'([a-g])([-#]+)', keysig or ''):
        alt[m.group(1)] = -len(m.group(2)) if m.group(2)[0] == '-' else len(m.group(2))
    return alt

def diatonic_midi(step, octv, alt):
    return 12 * (octv + 1) + PC[step] + alt.get(step, 0)

def sounding(voice, t, eps=1e-6):
    """Return the event sounding at time t (onset <= t < onset+dur), or None."""
    lo, hi = 0, len(voice) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        e = voice[mid]
        if e['onset'] > t + eps: hi = mid - 1
        elif e['onset'] + e['dur'] <= t + eps: lo = mid + 1
        else: return e
    return None

def find_cadences(voices, alt, min_arrival=2.0):
    """Yield cadence dicts. Baseline criterion:
       - two voices, diatonic 6th -> octave (or compound)
       - upper ascends one diatonic step, lower descends one diatonic step
       - both move at the same instant; arrival duration >= min_arrival
    """
    out = []
    n = len(voices)
    for a in range(n):
        for b in range(n):
            if a == b: continue
            up, lo = voices[a], voices[b]
            for k in range(1, len(up)):
                pen_u, arr_u = up[k-1], up[k]
                if pen_u['rest'] or arr_u['rest']: continue
                t_arr = arr_u['onset']
                if arr_u['dur'] < min_arrival: continue
                # lower voice must arrive at exactly the same instant
                idx = None
                for j in range(len(lo)):
                    if abs(lo[j]['onset'] - t_arr) < 1e-6:
                        idx = j; break
                if idx is None or idx == 0: continue
                arr_l, pen_l = lo[idx], lo[idx-1]
                if arr_l['rest'] or pen_l['rest']: continue
                if arr_l['dur'] < min_arrival: continue
                # penultimates must actually sound together
                if pen_u['onset'] + pen_u['dur'] <= pen_l['onset'] + 1e-6: continue
                if pen_l['onset'] + pen_l['dur'] <= pen_u['onset'] + 1e-6: continue
                # contrary stepwise motion
                if arr_u['dstep'] - pen_u['dstep'] != 1: continue
                if arr_l['dstep'] - pen_l['dstep'] != -1: continue
                # upper must be above lower at both points
                if pen_u['dstep'] <= pen_l['dstep']: continue
                # diatonic sixth -> octave/unison
                if (pen_u['dstep'] - pen_l['dstep']) % 7 != 5: continue
                if (arr_u['dstep'] - arr_l['dstep']) % 7 != 0: continue
                # diatonic (unaltered) semitone gap of the upper approach
                d_pen = diatonic_midi(pen_u['step'], pen_u['octv'], alt)
                d_arr = diatonic_midi(arr_u['step'], arr_u['octv'], alt)
                gap = d_arr - d_pen
                if gap not in (1, 2): continue
                if gap == 1:
                    cls = 'repair_free'
                    prov = 'n/a'
                else:
                    cls = 'repair_demanded'
                    if pen_u['alter'] > 0 and pen_u['acc_written']:
                        prov = 'editorial' if pen_u['editorial'] else 'source'
                    else:
                        prov = 'absent'
                out.append({'cls': cls, 'prov': prov, 'onset': t_arr,
                            'arr_dur': min(arr_u['dur'], arr_l['dur'])})
    # de-duplicate: one cadence per arrival instant (multiple voice pairs may fire)
    seen = {}
    for c in out:
        key = round(c['onset'], 4)
        if key not in seen or (c['cls'] == 'repair_demanded' and seen[key]['cls'] == 'repair_free'):
            seen[key] = c
    return list(seen.values())

SAC = {'Mass','Motet','Credo','Kyrie','Sanctus','Gloria','Agnus Dei','Agnus dei',
       'Mass section','Motet cycle','Requiem','Missa Brevis','Hymn','Lamentation',
       'Introit','Offertory','Pleni','Magnificat','Psalm'}
SEC = {'Chanson','Song','Rondeau','Virelai','Carnival Song','Combinative Chanson',
       'Motet-Chanson','Frottola','Ballade','Bergerette'}

def genre_class(agn):
    tags = {x.strip() for x in (agn or '').split(';')}
    if tags & SEC: return 'secular'
    if tags & SAC: return 'sacred'
    return None

def birth_year(cdt):
    if not cdt: return None
    m = re.search(r'(\d{4})', cdt)
    return int(m.group(1)) if m else None
```

### run_study.py

```python
import glob, json, math
from collections import defaultdict, Counter
import kernparse, cadence

FILES = sorted(glob.glob('jrp-scores/*/*.krn'))
THRESHOLDS = [1.0, 2.0, 4.0]

rows = []
skipped = 0
for f in FILES:
    try:
        meta, voices = kernparse.parse_file(f)
    except Exception:
        skipped += 1; continue
    if voices is None or not voices or not any(voices):
        skipped += 1; continue
    g = cadence.genre_class(meta.get('AGN'))
    if g is None:
        continue
    by = cadence.birth_year(meta.get('CDT'))
    alt = cadence.ksig_alter(meta.get('keysig'))
    rec = {'file': f, 'genre': g, 'birth': by,
           'composer': meta.get('COA') or meta.get('COM'),
           'ksig': meta.get('keysig'), 'runs': {}}
    for thr in THRESHOLDS:
        cs = cadence.find_cadences(voices, alt, thr)
        rec['runs'][thr] = {
            'n': len(cs),
            'free': sum(1 for c in cs if c['cls'] == 'repair_free'),
            'dem': sum(1 for c in cs if c['cls'] == 'repair_demanded'),
            'src': sum(1 for c in cs if c['prov'] == 'source'),
            'edi': sum(1 for c in cs if c['prov'] == 'editorial'),
            'abs': sum(1 for c in cs if c['prov'] == 'absent'),
        }
    rows.append(rec)

json.dump(rows, open('results.json', 'w'))
print('works analysed:', len(rows), ' skipped:', skipped)

def wilson(k, n):
    if n == 0: return (0, 0, 0)
    p = k / n; z = 1.96
    d = 1 + z*z/n
    c = (p + z*z/(2*n)) / d
    h = z*math.sqrt(p*(1-p)/n + z*z/(4*n*n)) / d
    return p, max(0, c-h), min(1, c+h)

print('\n=== REPAIR-FREE CADENCE RATE (immune to editorial supply) ===')
for thr in THRESHOLDS:
    print(f'\n-- arrival-duration threshold {thr} (semibreve=4) --')
    agg = defaultdict(lambda: [0, 0])
    for r in rows:
        d = r['runs'][thr]
        agg[r['genre']][0] += d['free']; agg[r['genre']][1] += d['n']
    for g in ('sacred', 'secular'):
        k, n = agg[g]
        p, lo, hi = wilson(k, n)
        print(f'  {g:8} {k:6}/{n:6} = {100*p:5.1f}%  [{100*lo:.1f}–{100*hi:.1f}]')

print('\n=== BY COMPOSER GENERATION (birth cohort), threshold 2.0 ===')
def cohort(b):
    if b is None: return None
    if b < 1420: return '<1420'
    if b < 1440: return '1420-39'
    if b < 1460: return '1440-59'
    if b < 1480: return '1460-79'
    return '1480+'
agg = defaultdict(lambda: [0, 0])
for r in rows:
    c = cohort(r['birth'])
    if c is None: continue
    d = r['runs'][2.0]
    agg[(c, r['genre'])][0] += d['free']; agg[(c, r['genre'])][1] += d['n']
print(f"{'cohort':10} {'genre':8} {'free/all':>14} {'rate':>7}   95% CI")
for c in ['<1420', '1420-39', '1440-59', '1460-79', '1480+']:
    for g in ('sacred', 'secular'):
        k, n = agg[(c, g)]
        if n == 0: continue
        p, lo, hi = wilson(k, n)
        print(f'{c:10} {g:8} {k:6}/{n:6} {100*p:6.1f}%   [{100*lo:.1f}–{100*hi:.1f}]')

print('\n=== NOTATION OF THE DEMANDED INFLECTION (source vs editor), threshold 2.0 ===')
agg = defaultdict(lambda: Counter())
for r in rows:
    d = r['runs'][2.0]
    agg[r['genre']]['src'] += d['src']; agg[r['genre']]['edi'] += d['edi']
    agg[r['genre']]['abs'] += d['abs']; agg[r['genre']]['dem'] += d['dem']
for g in ('sacred', 'secular'):
    a = agg[g]; dem = a['dem'] or 1
    print(f"  {g:8} demanded={a['dem']:6}  source={100*a['src']/dem:5.1f}%  "
          f"editorial={100*a['edi']/dem:5.1f}%  absent={100*a['abs']/dem:5.1f}%")

print('\n=== TOP COMPOSERS BY CADENCE COUNT (threshold 2.0) ===')
agg = defaultdict(lambda: [0, 0, None])
for r in rows:
    d = r['runs'][2.0]
    k = r['composer'] or '?'
    agg[k][0] += d['free']; agg[k][1] += d['n']; agg[k][2] = r['birth']
for k, (fr, n, b) in sorted(agg.items(), key=lambda x: -x[1][1])[:16]:
    if n < 200: continue
    p, lo, hi = wilson(fr, n)
    print(f'  {str(b):>5}  {k[:34]:34} {fr:5}/{n:6} {100*p:5.1f}%  [{100*lo:.1f}–{100*hi:.1f}]')
```

### minorscales.py

```python
"""Test whether harmonic/melodic minor behave as SCALES or as artifacts of cadential grafts.

Predictions if they are genuine scales:
  H1 harmonic minor: the b6->#7 augmented second occurs melodically (it is a scale step)
  H2 melodic minor : raised 6 is conditioned on DIRECTION (up yes, down no)
  H3 melodic minor : raised 6 is independent of raised 7 (both are just scale members)
Predictions if they are artifacts of the leading-tone graft:
  A1 aug2 avoided everywhere (already observed ~0)
  A2 raised 6 conditioned on PROXIMITY TO RAISED 7, not merely on direction
  A3 raised 6 concentrated in lines running up to the tonic (5-6-7-8), not general ascent
"""
import glob, math, re
from collections import Counter, defaultdict
import kernparse, cadence

def wil(k,n):
    if n==0: return (0,0,0)
    p=k/n; z=1.96; d=1+z*z/n
    c=(p+z*z/(2*n))/d; h=z*math.sqrt(p*(1-p)/n+z*z/(4*n*n))/d
    return p,max(0,c-h),min(1,c+h)

def analyse(voices, tpc):
    """tpc = tonic pitch class. Returns counters."""
    R=Counter()
    for v in voices:
        seq=[e for e in v if not e['rest']]
        deg=[(e['midi']-tpc)%12 for e in seq]
        for i,e in enumerate(seq):
            d=deg[i]
            if d not in (8,9): continue          # b6 or #6
            nxt = seq[i+1]['midi']-e['midi'] if i+1<len(seq) else None
            prv = e['midi']-seq[i-1]['midi'] if i>0 else None
            up = nxt is not None and nxt>0
            dn = nxt is not None and nxt<0
            raised = (d==9)
            if up: R[('dir','up','r' if raised else 'n')]+=1
            if dn: R[('dir','dn','r' if raised else 'n')]+=1
            # proximity to raised 7 (deg 11) within +/-2 notes
            win=[deg[j] for j in range(max(0,i-2),min(len(deg),i+3)) if j!=i]
            near7 = 11 in win
            R[('prox','y' if near7 else 'n','r' if raised else 'n')]+=1
            # is this note in a stepwise line reaching the tonic within 3 notes?
            tgt=False
            for j in range(i+1,min(len(deg),i+4)):
                if deg[j]==0: tgt=True; break
                if abs(seq[j]['midi']-seq[j-1]['midi'])>2: break
            R[('totonic','y' if tgt else 'n','r' if raised else 'n')]+=1
        # augmented seconds (3 semitones, adjacent letter names)
        for i in range(len(seq)-1):
            a,b=seq[i],seq[i+1]
            if abs(a['midi']-b['midi'])==3 and abs(a['dstep']-b['dstep'])==1:
                lo,hi=(a,b) if a['midi']<b['midi'] else (b,a)
                if (lo['midi']-tpc)%12==8 and (hi['midi']-tpc)%12==11:
                    R['aug2_b6_s7']+=1
                R['aug2_any']+=1
        R['notes']+=len(seq)
    return R
```

### scale_cells.py

```python
"""Joint direction-by-proximity cells for the raised sixth (paper section 5),
ported verbatim from the study's session code; window W parameterized.
Conventions: tonic = lowest final note across voices; JRP/Tasso mode inferred
from that final's letter plus signature; Palestrina mode from the declared
key tag (aeo/phr); Bach chorales included when the kern key tag is minor.
Direction: up when the next note is higher; repeats count as not-up.
Usage: scale_cells.py extract | report W
"""
import glob, json, os, re, sys
from collections import Counter
import kernparse
from music21 import corpus as m21corpus

DEG='cdefgab'; IONIAN={0:'c',1:'f',2:'b',3:'e',4:'a'}; SHARPION={1:'g',2:'d'}
ORDER=['Ionian','Dorian','Phrygian','Lydian','Mixolydian','Aeolian','Locrian']
FLAT6={'Aeolian','Phrygian'}

def mode_of(fin,nf,ns):
    ion=IONIAN.get(nf) if nf else (SHARPION.get(ns,'c') if ns else 'c')
    return ORDER[(DEG.index(fin)-DEG.index(ion))%7] if (ion and fin in DEG) else None

def jrp_mode(f,meta,bass):
    ks=meta.get('keysig') or ''
    m=mode_of(bass['step'], ks.count('-'), ks.count('#'))
    return m if m in FLAT6 else None
def pal_mode(f,meta,bass):
    m=re.search(r'\*[A-Ga-g][#-]?:(\w+)', open(f,encoding='utf-8',errors='ignore').read())
    return {'aeo':'Aeolian','phr':'Phrygian'}.get(m.group(1)) if m else None
def bach_mode(f,meta,bass):
    t=open(f,encoding='utf-8',errors='ignore').read()
    return 'Aeolian' if re.search(r'\*([a-g][#-]?):', t) else None

def extract():
    PD=sorted(str(x) for x in m21corpus.getCorePaths() if '/corpus/palestrina/' in str(x))[0].rsplit('/',1)[0]
    SETS=[('jrp', glob.glob('jrp-scores/*/*.krn'), jrp_mode),
          ('palestrina', glob.glob(PD+'/*.krn'), pal_mode),
          ('tasso', glob.glob('tmp_tasso-scores_/*/kern/*.krn'), jrp_mode),
          ('bach', glob.glob('b_bach-370-chorales/kern/*.krn'), bach_mode)]
    recs=[]
    for name,files,modefn in SETS:
        kept=0
        for f in sorted(files):
            try: meta,voices=kernparse.parse_file(f)
            except Exception: continue
            if voices is None or not any(voices): continue
            finals=[]
            for v in voices:
                e=[x for x in v if not x['rest']]
                if e: finals.append(e[-1])
            if not finals: continue
            bass=min(finals,key=lambda e:e['midi'])
            if modefn(f,meta,bass) is None: continue
            kept+=1
            recs.append({'corpus':name,'tpc':bass['midi']%12,
                         'voices':[[e['midi'] for e in v if not e['rest']] for v in voices]})
        print(f"{name}: {kept} pieces kept")
    json.dump(recs,open('scale_cells_cache.json','w'))

PUB={'jrp':{(1,1):(87.4,223),(1,0):(4.0,15147),(0,1):(0.0,20),(0,0):(0.6,29902)},
     'palestrina':{(1,1):(93.9,507),(1,0):(18.0,5932),(0,1):(77.4,328),(0,0):(10.3,12922)},
     'tasso':{(1,1):(79.7,128),(1,0):(22.1,2686),(0,1):(37.0,73),(0,0):(4.7,6205)},
     'bach':{(1,1):(87.5,272),(1,0):(33.1,1306),(0,1):(28.8,80),(0,0):(13.2,2665)}}

def report(W, check=False):
    recs=json.load(open('scale_cells_cache.json'))
    cells={c:Counter() for c in ('jrp','palestrina','tasso','bach')}
    for r in recs:
        t=r['tpc']; C=cells[r['corpus']]
        for mv in r['voices']:
            deg=[(m-t)%12 for m in mv]
            for i,d in enumerate(deg):
                if d not in (8,9): continue
                if i+1>=len(deg): continue
                up = mv[i+1]>mv[i]
                lo,hi=max(0,i-W),min(len(deg),i+W+1)
                near = any(deg[j]==11 for j in range(lo,hi) if j!=i)
                C[(up,near,d==9)]+=1
    print(f"window = +/-{W} notes, same voice")
    ok=True
    for corp in ('jrp','palestrina','tasso','bach'):
        C=cells[corp]; row=[]
        for up,near in ((1,1),(1,0),(0,1),(0,0)):
            r=C[(bool(up),bool(near),True)]; n=C[(bool(up),bool(near),False)]+r
            pct=100*r/n if n else float('nan')
            row.append(f"{pct:5.1f}% (n={n})")
            if check:
                p,pn=PUB[corp][(up,near)]
                if n!=pn or abs(pct-p)>0.06: ok=False; row[-1]+=f"  != pub {p}% (n={pn})"
        print(f"{corp:11} ASC-near {row[0]}   ASC-far {row[1]}   DESC-near {row[2]}   DESC-far {row[3]}")
    if check: print("VALIDATION:", "EXACT MATCH" if ok else "MISMATCH")

if __name__=='__main__':
    if sys.argv[1]=='extract': extract()
    else: report(int(sys.argv[2]), check=(len(sys.argv)>3 and sys.argv[3]=='check'))
```

### scale_marginals.py

```python
"""Marginal direction and proximity splits, plus augmented-second events
(paper section 5, Test 1), ported from the study's session code.
Uses minorscales.analyse; piece selection as in scale_cells.py."""
import glob, re, sys
from collections import Counter
import kernparse
from minorscales import analyse
from scale_cells import mode_of, FLAT6
from music21 import corpus as m21corpus

def gather(files, modefn, label):
    T=Counter(); nw=0
    for f in sorted(files):
        try: meta,voices=kernparse.parse_file(f)
        except Exception: continue
        if voices is None or not any(voices): continue
        finals=[]
        for v in voices:
            e=[x for x in v if not x['rest']]
            if e: finals.append(e[-1])
        if not finals: continue
        bass=min(finals,key=lambda e:e['midi'])
        if modefn(f,meta,bass) is None: continue
        nw+=1
        for k,v in analyse(voices, bass['midi']%12).items(): T[k]+=v
    T['works']=nw; T['label']=label
    return T

def jrp_mode(f,meta,bass):
    ks=meta.get('keysig') or ''
    m=mode_of(bass['step'], ks.count('-'), ks.count('#'))
    return m if m in FLAT6 else None
def pal_mode(f,meta,bass):
    m=re.search(r'\*[A-Ga-g][#-]?:(\w+)', open(f,encoding='utf-8',errors='ignore').read())
    return {'aeo':'Aeolian','phr':'Phrygian'}.get(m.group(1)) if m else None

if __name__=='__main__':
    PD=sorted(str(x) for x in m21corpus.getCorePaths() if '/corpus/palestrina/' in str(x))[0].rsplit('/',1)[0]
    SETS=[('JRP c.1420-1550', glob.glob('jrp-scores/*/*.krn'), jrp_mode),
          ('Palestrina c.1554-94', glob.glob(PD+'/*.krn'), pal_mode),
          ('Tasso 1571-1649', glob.glob('tmp_tasso-scores_/*/kern/*.krn'), jrp_mode)]
    PUB={'JRP c.1420-1550':(1,341005),'Palestrina c.1554-94':(0,153963),'Tasso 1571-1649':(7,76445)}
    ok=True
    for lab,fs,mf in SETS:
        T=gather(fs,mf,lab)
        a,n=T['aug2_b6_s7'],T['notes']
        pa,pn=PUB[lab]
        flag="OK" if (a,n)==(pa,pn) else f"!= pub {pa}/{pn}"
        if (a,n)!=(pa,pn): ok=False
        print(f"{lab:24} aug2(b6-#7)={a:3} in {n:7} notes   {flag}")
        up=(T[('dir','up','r')],T[('dir','up','n')]); dn=(T[('dir','dn','r')],T[('dir','dn','n')])
        py=(T[('prox','y','r')],T[('prox','y','n')]); pn2=(T[('prox','n','r')],T[('prox','n','n')])
        print(f"{'':24} ASC {100*up[0]/sum(up):5.1f}% ({up[0]}/{sum(up)})  DESC {100*dn[0]/sum(dn):5.1f}% ({dn[0]}/{sum(dn)})  NEAR {100*py[0]/sum(py):5.1f}%  FAR {100*pn2[0]/sum(pn2):5.1f}%")
    print("VALIDATION:", "EXACT MATCH" if ok else "MISMATCH")
```

### vocal_series.py

```python
"""Mode-field tables and final-third stages across the vocal corpora
(paper sections 4 and 6; Appendix III D). Conventions as validated in
scale_cells.py: finals are each voice's last sounding note; the bass final
is the lowest; JRP and Tasso modes from the bass final plus signature;
Palestrina modes from the declared key tag; trecento parsed via music21."""
import glob, re, sys, math
from collections import Counter, defaultdict
import kernparse, cadence
from scale_cells import mode_of
from music21 import corpus as m21corpus, converter

MAJOR={'Ionian','Lydian','Mixolydian'}; MINOR={'Dorian','Aeolian','Phrygian'}

def wil(k,n):
    if n==0: return (0,0,0)
    p=k/n; z=1.96; d=1+z*z/n
    c=(p+z*z/(2*n))/d; h=z*math.sqrt(p*(1-p)/n+z*z/(4*n*n))/d
    return 100*p,100*max(0,c-h),100*min(1,c+h)

def finals_of(voices):
    fs=[]
    for v in voices:
        e=[x for x in v if not x['rest']]
        if e: fs.append(e[-1])
    return fs

def third_of(finals):
    bass=min(finals,key=lambda e:e['midi']); b=bass['midi']%12
    pcs={e['midi']%12 for e in finals}
    return bass, ('major' if (b+4)%12 in pcs else 'minor' if (b+3)%12 in pcs else 'none')

def jrp():
    rows=[]
    for f in sorted(glob.glob('jrp-scores/*/*.krn')):
        try: meta,voices=kernparse.parse_file(f)
        except Exception: continue
        if voices is None or not any(voices): continue
        fs=finals_of(voices)
        if not fs: continue
        bass,third=third_of(fs)
        ks=meta.get('keysig') or ''
        md=mode_of(bass['step'], ks.count('-'), ks.count('#'))
        rows.append({'mode':md,'third':third,'genre':cadence.genre_class(meta.get('AGN')),
                     'birth':cadence.birth_year(meta.get('CDT'))})
    return rows

def tasso():
    rows=[]
    for f in sorted(glob.glob('tmp_tasso-scores_/*/kern/*.krn')):
        try: meta,voices=kernparse.parse_file(f)
        except Exception: continue
        if voices is None or not any(voices): continue
        fs=finals_of(voices)
        if not fs: continue
        bass,third=third_of(fs)
        ks=meta.get('keysig') or ''
        md=mode_of(bass['step'], ks.count('-'), ks.count('#'))
        t=open(f,encoding='utf-8',errors='ignore').read()
        y=re.search(r'!!!PDT[^0-9]*(\d{4})',t)
        rows.append({'mode':md,'third':third,'year':int(y.group(1)) if y else None})
    return rows

def palestrina():
    PD=sorted(str(x) for x in m21corpus.getCorePaths() if '/corpus/palestrina/' in str(x))[0].rsplit('/',1)[0]
    rows=[]
    for f in sorted(glob.glob(PD+'/*.krn')):
        try: meta,voices=kernparse.parse_file(f)
        except Exception: continue
        if voices is None or not any(voices): continue
        fs=finals_of(voices)
        if not fs: continue
        _,third=third_of(fs)
        m=re.search(r'\*[A-Ga-g][#-]?:(\w+)', open(f,encoding='utf-8',errors='ignore').read())
        rows.append({'tag':m.group(1) if m else None,'third':third})
    return rows

def trecento():
    paths=sorted(str(x) for x in m21corpus.getCorePaths() if '/corpus/trecento/' in str(x))
    nthird=tot=0
    for p in paths:
        try:
            s=converter.parse(p)
            ns=[n for n in s.flatten().notes]
            if len(ns)<10: continue
            end=max(float(n.offset)+float(n.duration.quarterLength) for n in ns)
            fin=[n for n in ns if float(n.offset)+float(n.duration.quarterLength)>=end-0.01]
            pcs=set(); lo=None
            for n in fin:
                for q in (n.pitches if n.isChord else [n.pitch]):
                    pcs.add(q.pitchClass)
                    if lo is None or q.midi<lo[0]: lo=(q.midi,q.pitchClass)
            tot+=1
            b=lo[1]
            if (b+3)%12 in pcs or (b+4)%12 in pcs: nthird+=1
        except Exception: continue
    return tot-nthird, tot

def cohort(b):
    if b is None: return None
    if b<1420: return '<1420'
    if b<1440: return '1420-39'
    if b<1460: return '1440-59'
    if b<1480: return '1460-79'
    return '1480+'

if __name__=='__main__':
    J=jrp()
    print(f"JRP works classified: {len(J)}")
    mc=Counter(r['mode'] for r in J if r['mode'])
    for m,c in mc.most_common(): print(f"  {m:11} {c:4} {100*c/len(J):5.1f}%")
    maj=sum(mc[m] for m in MAJOR); mn=sum(mc[m] for m in MINOR)
    print(f"  destination major {100*maj/len(J):.1f}%  minor {100*mn/len(J):.1f}%   Ionian share {100*mc['Ionian']/len(J):.1f}%")
    print("  Lydian by cohort/genre:")
    for co in ('<1420','1420-39','1440-59','1460-79','1480+'):
        for g in ('sacred','secular'):
            sub=[r for r in J if cohort(r['birth'])==co and r['genre']==g]
            if not sub: continue
            k=sum(1 for r in sub if r['mode']=='Lydian')
            p,l,h=wil(k,len(sub))
            print(f"    {co:8} {g:8} {k:3}/{len(sub):4} = {p:4.1f}% [{l:.1f}-{h:.1f}]")
    for g in ('sacred','secular'):
        sub=[r for r in J if r['genre']==g]
        k=sum(1 for r in sub if r['mode']=='Phrygian')
        print(f"  Phrygian {g}: {k}/{len(sub)} = {100*k/len(sub):.1f}%")
    print("  Minor-destination endings by cohort (all/none/minor/major; major of with-third):")
    for co in ('<1420','1420-39','1440-59','1460-79','1480+'):
        sub=[r for r in J if cohort(r['birth'])==co and r['mode'] in MINOR]
        if not sub: continue
        no=sum(1 for r in sub if r['third']=='none'); mi=sum(1 for r in sub if r['third']=='minor'); ma=sum(1 for r in sub if r['third']=='major')
        wt=mi+ma
        print(f"    {co:8} n={len(sub):4}  none {100*no/len(sub):5.1f}%  minor {100*mi/len(sub):5.1f}%  major {100*ma/len(sub):4.1f}%   major|third {ma}/{wt}"+(f" = {100*ma/wt:.1f}%" if wt else ""))
    P=palestrina()
    pm=[r for r in P if r['tag'] in ('dor','aeo','phr')]
    wt=[r for r in pm if r['third']!='none']; ma=sum(1 for r in wt if r['third']=='major')
    print(f"Palestrina: classified {len(P)}, minor-mode {len(pm)}, with-third {len(wt)}, major {ma}  ->  {ma}/{len(wt)}")
    T=tasso()
    print(f"Tasso works classified: {len(T)}")
    tc=Counter(r['mode'] for r in T if r['mode'])
    maj=sum(tc[m] for m in MAJOR); mn=sum(tc[m] for m in MINOR); tot=len([r for r in T if r['mode']])
    print(f"  destination major {100*maj/tot:.1f}%  minor {100*mn/tot:.1f}%   Ionian {100*tc['Ionian']/tot:.1f}%  Lydian {100*tc['Lydian']/tot:.1f}%")
    for lo,hi in ((1580,1600),(1600,1620),(1620,1660)):
        sub=[r for r in T if r['mode'] in MINOR and r['year'] and lo<=r['year']<hi]
        wt=[r for r in sub if r['third']!='none']; ma=sum(1 for r in wt if r['third']=='major')
        print(f"  {lo}-{hi-1}: minor n={len(sub)}, with-third {len(wt)}, major {ma}  ->  {ma}/{len(wt)}")
    nt,tt=trecento()
    print(f"Trecento: {nt}/{tt} end with no third")
```

### aug6.py

```python
"""Detect augmented sixths: 10 semitones apart, spelled as a SIXTH (dstep diff 5 mod 7).
A minor seventh is also 10 semitones but spans 6 diatonic steps, so spelling separates them."""
import glob, re, math
from collections import Counter, defaultdict
import kernparse, cadence

def simult_aug6(voices, fpc):
    """Return list of (lower_deg, upper_deg, resolves_to_dominant)."""
    hits=[]
    n=len(voices)
    evs=[[e for e in v if not e['rest']] for v in voices]
    for a in range(n):
        for b in range(a+1,n):
            A,B=evs[a],evs[b]
            i=j=0
            while i<len(A) and j<len(B):
                x,y=A[i],B[j]
                xs,xe=x['onset'],x['onset']+x['dur']
                ys,ye=y['onset'],y['onset']+y['dur']
                lo_t,hi_t=max(xs,ys),min(xe,ye)
                if hi_t-lo_t>1e-6:
                    hi,lw=(x,y) if x['midi']>y['midi'] else (y,x)
                    semi=hi['midi']-lw['midi']
                    dst=hi['dstep']-lw['dstep']
                    if semi%12==10 and dst%7==5:
                        # resolution: next note in each voice
                        ii = A.index(x)+1 if x is A[A.index(x)] else None
                        res=False
                        try:
                            nx=A[i+1]; ny=B[j+1]
                            hi2,lw2=(nx,ny) if hi is x else (ny,nx)
                            if (hi2['midi']-hi['midi'])==1 and (lw['midi']-lw2['midi'])==1:
                                res=True
                        except IndexError: pass
                        hits.append(((lw['midi']-fpc)%12,(hi['midi']-fpc)%12,res))
                if xe<ye: i+=1
                else: j+=1
    return hits

def scan(files, yearfn, label):
    out=defaultdict(lambda: [0,0,0])   # year-bin -> [aug6, resolving, notes]
    for f in files:
        try: meta,voices=kernparse.parse_file(f)
        except Exception: continue
        if voices is None or not any(voices): continue
        yr=yearfn(f,meta)
        if yr is None: continue
        finals=[]
        for v in voices:
            ev=[e for e in v if not e['rest']]
            if ev: finals.append(ev[-1])
        if not finals: continue
        fpc=min(e['midi'] for e in finals)%12
        h=simult_aug6(voices,fpc)
        nn=sum(len([e for e in v if not e['rest']]) for v in voices)
        out[yr][0]+=len(h); out[yr][1]+=sum(1 for x in h if x[2]); out[yr][2]+=nn
        out[yr].append(h) if False else None
    return out
```

### mei_analyse.py

```python
import glob, json, math, re
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
NS={'m':'http://www.music-encoding.org/ns/mei'}
def wil(k,n):
    if n==0: return (0,0,0)
    p=k/n; z=1.96; d=1+z*z/n
    c=(p+z*z/(2*n))/d; h=z*math.sqrt(p*(1-p)/n+z*z/(4*n*n))/d
    return p,max(0,c-h),min(1,c+h)

def parse_mei(path):
    """Return dict staff_n -> ordered list of (pnum, notated_accid_bool)."""
    try: tree=ET.parse(path)
    except Exception: return None
    root=tree.getroot()
    staves=defaultdict(list)
    for meas in root.iter('{http://www.music-encoding.org/ns/mei}measure'):
        for st in meas.iter('{http://www.music-encoding.org/ns/mei}staff'):
            n=st.get('n')
            for nt in st.iter('{http://www.music-encoding.org/ns/mei}note'):
                pn=nt.get('pnum')
                if pn is None: continue
                notated = nt.get('accid') is not None
                if not notated:
                    for a in nt.iter('{http://www.music-encoding.org/ns/mei}accid'):
                        if a.get('accid') is not None: notated=True
                staves[n].append((int(pn), notated))
    return dict(staves)

meta={p['piece_id']:p for p in json.load(open('crim_pieces.json'))}
rows=[]; bad=0
for f in sorted(glob.glob('crim_mei/*.mei')):
    pid=f.split('/')[-1].replace('.mei','')
    base=re.sub(r'_\d+$','',pid)
    m=meta.get(pid) or meta.get(base)
    if not m: 
        # mass movements: id like CRIM_Mass_0001_1
        m=meta.get('_'.join(pid.split('_')[:3]))
    if not m: bad+=1; continue
    yr=m.get('date_sort')
    if not yr or not (1400<=int(yr)<=1650): continue
    st=parse_mei(f)
    if not st: bad+=1; continue
    finals=[v[-1][0] for v in st.values() if v]
    if len(finals)<2: continue
    fin=min(finals); fpc=fin%12
    pcs={x%12 for x in finals}
    third='major' if (fpc+4)%12 in pcs else ('minor' if (fpc+3)%12 in pcs else 'none')
    d6n=d6r=d7n=d7r=0
    for v in st.values():
        for pn,_ in v:
            iv=(pn-fpc)%12
            if iv==8: d6n+=1
            elif iv==9: d6r+=1
            elif iv==10: d7n+=1
            elif iv==11: d7r+=1
    rows.append({'yr':int(yr),'third':third,'d6n':d6n,'d6r':d6r,'d7n':d7n,'d7r':d7r,
                 'genre':(m.get('genre') or {}).get('name'),
                 'comp':(m.get('composer') or {}).get('name')})
print("CRIM analysed:",len(rows)," unmatched/failed:",bad)

BINS=[(1500,1535,'1500-34'),(1535,1555,'1535-54'),(1555,1575,'1555-74'),(1575,1610,'1575-1609')]
print("\n=== CRIM: final sonority (all pieces; minor-vs-major final not yet split) ===")
for lo,hi,lab in BINS:
    sub=[r for r in rows if lo<=r['yr']<hi]
    if len(sub)<15: continue
    c=Counter(r['third'] for r in sub); n=len(sub)
    w3=[r for r in sub if r['third']!='none']
    k=sum(1 for r in w3 if r['third']=='major')
    p,l,h=wil(k,len(w3)) if w3 else (0,0,0)
    print(f"  {lab:11} n={n:3}  no3rd {100*c['none']/n:5.1f}%   among-with-3rd major = {k}/{len(w3)} = {100*p:5.1f}% [{100*l:.1f}-{100*h:.1f}]")
```

### pscan.py

```python
import glob, sys, json, os
from music21 import converter
def one(f):
    s=converter.parse(f)
    ns=[n for n in s.flatten().notes]
    if len(ns)<30: return None
    end=max(float(n.offset)+float(n.duration.quarterLength) for n in ns)
    fin=[n for n in ns if float(n.offset)+float(n.duration.quarterLength)>=end-0.01]
    pcs=set(); low=None
    for n in fin:
        ps=n.pitches if n.isChord else [n.pitch]
        for p in ps:
            pcs.add(p.pitchClass)
            if low is None or p.midi<low[0]: low=(p.midi,p.pitchClass)
    k=s.analyze('key'); t=k.tonic.pitchClass
    if low is None or low[1]!=t: return None
    third='major' if (t+4)%12 in pcs else ('minor' if (t+3)%12 in pcs else 'open')
    return [k.mode,third]
if __name__=='__main__':
    pat,out=sys.argv[1],sys.argv[2]
    files=sorted(set(glob.glob(pat)))
    done=json.load(open(out)) if os.path.exists(out) else {}
    for f in files:
        if f in done: continue
        try: done[f]=one(f)
        except Exception: done[f]=None
        json.dump(done,open(out,'w'))
    m=[v for v in done.values() if v and v[0]=='minor']
    print(out, "files:",len(done), "minor-rooted-final:",len(m),
          "maj:",sum(1 for v in m if v[1]=='major'),
          "min:",sum(1 for v in m if v[1]=='minor'),
          "open:",sum(1 for v in m if v[1]=='open'))
```

### ht_measures.py

```python
"""Hooktheory measures for A Cadence of Change (Appendix I, definition C8).
Input: HT.json.gz, the Donahue et al. (2022) Hooktheory release."""
import gzip, json, sys
from collections import Counter

MODES={(2,2,1,2,2,2):'Ionian',(2,1,2,2,1,2):'Aeolian',(2,1,2,2,2,1):'Dorian',
       (1,2,2,2,1,2):'Phrygian',(2,2,2,1,2,2):'Lydian',(2,2,1,2,2,1):'Mixolydian',
       (1,2,2,1,2,2):'Locrian'}

def song_key(e):
    """Return (tonic, mode) when every key annotation agrees; else None."""
    ks=e['annotations'].get('keys') or []
    if not ks: return None
    sigs={(k['tonic_pitch_class'],tuple(k['scale_degree_intervals'])) for k in ks}
    if len(sigs)!=1: return None
    t,iv=sigs.pop()
    return (t, MODES.get(iv))

def main(path='HT.json.gz'):
    d=json.load(gzip.open(path,'rt'))
    modes=Counter(); r7=[0,0]; pic={'Aeolian':[0,0],'Ionian':[0,0]}
    for e in d.values():
        ks=e['annotations'].get('keys') or []
        if ks:
            modes[MODES.get(tuple(ks[0]['scale_degree_intervals']),'other')]+=1
        sk=song_key(e)
        if sk is None or sk[1] is None: continue
        tonic,mode=sk
        if mode=='Aeolian':
            for n in (e['annotations'].get('melody') or []):
                rel=(n['pitch_class']-tonic)%12
                if rel==11: r7[0]+=1; r7[1]+=1
                elif rel==10: r7[1]+=1
        if mode in pic:
            hs=e['annotations'].get('harmony') or []
            if not hs: continue
            fin=max(hs,key=lambda h:h['offset'])
            if fin['root_pitch_class']%12!=tonic: continue
            iv=fin.get('root_position_intervals') or []
            if not iv: continue
            if iv[0]==4: pic[mode][0]+=1; pic[mode][1]+=1
            elif iv[0]==3: pic[mode][1]+=1
    N=sum(modes.values())
    print(f"N = {N}")
    for m,c in modes.most_common():
        print(f"  {m:11} {c:6} {100*c/N:5.1f}%")
    print(f"raised 7th (Aeolian melody): {r7[0]}/{r7[1]} = {100*r7[0]/r7[1]:.1f}%")
    for m in ('Aeolian','Ionian'):
        k,n=pic[m]
        print(f"Picardy, {m}: {k}/{n} = {100*k/n:.1f}%")

if __name__=='__main__':
    main(*sys.argv[1:])
```

## Appendix III — Sensitivity Analyses and Full Results

### A. Conventions

Composer-birth cohorts for the cadence measures: before 1420, 1420–39, 1440–59, 1460–79, 1480 and after. Cohorts for the mode-share series: born before 1440, 1440–59, 1460 and after. Cadence-arrival thresholds: 1, 2 and 4 units where a semibreve is 4, with 2 the headline setting. Proximity window for the raised-sixth cells: two notes in the same voice as the headline setting, with ±1 and ±3 reported in §E.

### B. The cadence detector and the repair-need rate in full

A cadence is detected as a two-voice progression in which a diatonic sixth expands to an octave or a compound equivalent by contrary stepwise motion, both voices arriving at the same instant, the arrival sustained past the threshold; several voice pairs firing at one instant collapse to one cadence. The penultimate upper-voice note's diatonic pitch is computed from the signature alone, so the repair-free classification is immune to editorial accidentals. Over all cadences in the Josquin Research Project corpus the repair-free rate is flat: 24.0% sacred and 23.6% secular at threshold 1, 23.7% and 23.0% at threshold 2, 22.9% and 20.4% at threshold 4; by cohort at threshold 2 the rate runs 22.3, 28.3, 23.4, 23.0, 19.0 percent (sacred) with no trend, and the sacred–secular gap runs opposite to the direction a vernacular-lead account would predict. Under a uniform distribution of cadence goals, two of seven degrees are approached from below by semitone, giving a 28.6% baseline; the observed rates sit slightly below that baseline and do not move. At final cadences the same instrument separates the modes sevenfold — Ionian 63.9% repair-free against Aeolian 8.5% — which is the contrast §11 cites: internal cadences are mode-neutral, final cadences are not.

### C. Editorial accidentals, quantified

Of repair-demanded cadences at threshold 2, source-notated accidentals supply the inflection in 1.8% (sacred) and 1.0% (secular); editors supply 24–28%; 71–74% are left bare. Notated cadential ficta is, quantitatively, almost not there — the reason definition C2 excludes editorial marks from headline rates and the reason the repair-free measure is built to need no accidentals at all.

### D. The seven-mode field, with intervals

Lydian by cohort, sacred: 8.0% [4.1–15.0] born before 1440, 2.9% [1.9–4.4] 1440–59, 0.0% [0.0–7.6] 1460 and after. The first transition's intervals overlap marginally — [4.1–15.0] against [1.9–4.4] — so the collapse's first step is strongly indicated rather than interval-separated; the second step, to zero, needs no interval argument. Locrian: 5 works of 1,282, 0.39% [0.17–0.91]. Phrygian: 14.1% of sacred works against 2.9% of secular, Wilson intervals non-overlapping. The destination proportions are stable across the same span — major-destination 38.6% to 39.0%, minor-destination 61.0% to 60.6% — and Ionian's own share of finals runs 19.2% to 18.9%.

### E. Raised-sixth window sensitivity

`scale_cells.py` reproduces the §5 table exactly at the pre-registered window — all sixteen cells, rates and denominators. The same cells at neighboring windows:

| Window | Corpus | ASC near ♯7 | ASC far | DESC near ♯7 | DESC far |
|---|---|---|---|---|---|
| ±1 | JRP | 99.5% (196) | 4.0% (15,174) | — (1) | 0.6% (29,921) |
| ±1 | Palestrina | 99.3% (431) | 18.6% (6,008) | **100.0%** (160) | 10.9% (13,090) |
| ±1 | Tasso | 95.7% (94) | 22.3% (2,720) | — (4) | 5.1% (6,274) |
| ±1 | Bach chorales | 99.5% (209) | 33.7% (1,369) | 60.9% (23) | 13.3% (2,722) |
| ±3 | JRP | 65.0% (303) | 4.0% (15,067) | 2.3% (131) | 0.6% (29,791) |
| ±3 | Palestrina | 79.3% (629) | 18.0% (5,810) | **60.9%** (593) | 9.7% (12,657) |
| ±3 | Tasso | 68.9% (164) | 22.0% (2,650) | 25.0% (144) | 4.6% (6,134) |
| ±3 | Bach chorales | 79.7% (350) | 31.8% (1,228) | 19.5% (236) | 13.1% (2,509) |

Three readings. The conditional rate rises toward adjacency — 95.7 to 99.5 percent at ±1 in every corpus — and dilutes at ±3, which is the signature of a rule governed by immediate adjacency rather than by region. The proximity effect exceeds the direction effect at every window in every corpus. And the decisive Palestrina comparison — descending-near exceeding ascending-far — holds at every setting: 100.0 against 18.6 at ±1, 77.4 against 18.0 at ±2, 60.9 against 18.0 at ±3. JRP's descending-near cell stays data-poor at every window (n = 1, 20, 131), and at ±3 reads 2.3%, below JRP's ascending-far: in the earliest corpus the descending repair is essentially absent, which is why §5 confines the descending claim to Palestrina and later. Sample composition entering the cells: 305 JRP pieces, 293 Palestrina, 131 Tasso, 177 Bach chorales — the chorale count reflecting the parser's exclusion of divided staves, a non-random exclusion noted in H.

### F. Augmented-sixth detection, in detail

Spelled-simultaneity detection: ten semitones spanning five diatonic steps, which separates an augmented sixth from a minor seventh (ten semitones, six steps). The fine-grained historical series: JRP c. 1440–1520, 18 events in 1.2 million notes (0.15 per 10,000), of which the canonical voicings — flat sixth below, raised fourth above — number sixteen, a count at the level of cross-relation and editorial noise; Palestrina and Tasso 1554–99, 5 events (0.05 per 10,000); Tasso 1600–19, zero; Tasso 1620–59, 2 events; Bach chorales, 3 in 370. The keyboard series (0.73, 2.67, 3.63, 4.64 per 1,000 verticalities) samples forty movements per corpus and counts every verticality containing the interval, functional or passing, so the keyboard rates are upper bounds on the chord proper. The Renaissance-to-Scarlatti jump crosses a medium boundary — vocal polyphony to keyboard — and keyboard texture generates more verticalities, so the trustworthy comparison is Scarlatti to Beethoven, which holds medium constant. The chorales' conspicuously low count is consistent with the augmented sixth being an instrumental and dramatic device before becoming a chorale-style device, and equally with the conservatism of chorale harmonization.

### G. CRIM: scope and withdrawal

CRIM was retrieved through the project's public JSON interface, 327 MEI files with per-piece `date_sort` values, the `accid` and `accid.ges` attributes preserving the notated-against-inferred distinction. CRIM's signature extraction proved imperfect: the mode counts come out Mixolydian-heavy (122 of 259), consistent with one-flat sources read as no-flat and transposed Dorian misfiled as Mixolydian. The misfiling shrinks the minor-destination sample rather than contaminating the minor-destination sample, so the written-third figures — the 40.0% and 100.0% cells of the Picardy transition — stand, and every CRIM raised-degree and mode-distribution figure is withdrawn. Two located but unretrieved resources would refine the transition's dating further: the Lost Voices / Du Chemin project (roughly 400 chansons printed 1549–68, MEI with editorial markup, served per piece without a bulk endpoint) and CMME.

### H. Detector and heuristic caveats

The cadence detector was run at three thresholds but has not been validated against human-annotated cadences; the detector will over-fire on non-structural contrary motion and under-fire on ornamented and evaded cadences, so the flat repair-free result is only as strong as the detector. Mode-from-final assignment misreads pieces ending on a bare fifth or with a crossing bass. The kern parser excludes divided staves — 105 JRP files, and roughly half the Bach chorales for the §5 cells — and divided staves cluster by genre, so the exclusion is non-random. The JRP editorial-supply rate (24–28%) reflects one project's ficta policy and supports no inference beyond the near-absence of source notation.
