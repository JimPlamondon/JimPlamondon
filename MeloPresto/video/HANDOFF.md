# HANDOFF — MeloPresto film, "Lift Them Up"

**Paste this file as your opening prompt in a conversation that has access to the JiMS project folder.** The two files beside it are the work product.

---

## The task you are picking up

Finish a short promotional film for **MeloPresto** (the new name for JiMS; rename workstream `ws_melopresto_rename_registration_20260826`). The film honours the ten people and groups whose inventions are assembled in the MeloPresto System, and ends by asking the viewer to pass the gift on.

It is deliberately, obviously an homage to Apple's 1997 "Crazy Ones" spot — Jim asked for that explicitly, and he has twice pushed back on attempts to soften it. **Do not dilute the homage on intellectual-property grounds.** He has ruled on this: avoiding infringement is one thing, gutting the tribute is another. The narration opens "Here's to the crazy ones." That stays.

Two deliverables exist:

| File | What it is |
|---|---|
| `lift-them-up_script.md` | The shooting script: shot table with timecodes, the clean VO read, sound design, end card, assets, release gate, open questions. |
| `lift-them-up_animatic.html` | A self-playing animatic. Open it in a browser. Every card and VO line on its real timecode, with a clickable shot sheet. This is blocking, not final art. |

Both are committed on branch `claude/melopresto-think-different-script-2f3krt` of `github.com/JimPlamondon/JimPlamondon` (17 commits; latest `1cd0682`). That repo is *not* the JiMS repo — it was the only one the previous session was scoped to at the start.

---

## Why it was handed off

The previous session could reach `github.com/JimPlamondon/jims` but **not** these three folders, which exist only on Jim's Mac and are never pushed to GitHub:

- `/Users/jim/Developer/JiMS/Business/`
- `/Users/jim/Developer/JiMS/Sources/`
- `/Users/jim/Developer/JiMS/Assets/`

Every blocked item below is blocked on one of those. If you can read them, you can finish this.

---

## Blocked items — the reason for the handoff

**1. The MeloPresto logo — `Assets/MeloPresto/`.**
The film's last frame is the logo. The animatic currently draws set type labelled *"placeholder — real logo pending"*. It is **not** a design proposal.

The animatic has a slot ready. At the top of its `<script>`:

```js
const LOGO = null;              // paste the master SVG's inner markup here
const LOGO_VB = "0 0 1000 300"; // set to that file's viewBox
```

Fill those two and both the final frame and the end card switch over. Three things to settle when you open the folder:

- **Which master** — wordmark, standalone mark, horizontal lockup, or stacked lockup. A frame held fifteen seconds usually wants the stacked lockup; the horizontal one needs more width than an end card gives it.
- **What colour it is.** This matters more here than on any other asset. The film's structure is *colour arrives exactly once, and it arrives at the end*, so the logo's colour becomes the payoff of eighty seconds of black and white. If the mark is a single brand colour — the earlier **Lomekuna** mark was brass `#A8813A`, per `Plans/ProgressLedger/events/ws_lomekuna_brand_assets_20260820.jsonl` — then the recommendation on file is: **the score blooms chromatic at 1:02 and settles Newton's debt; the logo then lands in its own colour and settles the film's.** Two payoffs, four seconds apart. If the mark is polychrome, that plan needs rethinking.
- **Clear space and minimum size** per the brand rules. The end card should be nowhere near either limit.

**2. Roualle de Boisgelou — `Sources/markdown/Sight_Reading_Music_Theory_A_Thought_Exp.md`.**
The chromatic staff is attributed on-card to **Roualle de Boisgelou, 1764**, taken from `Specs/JiMStudent_Spec.md` §3.3, which says *"first described by Roualle de Boisgelou in 1764."* Note **described**, not *invented* — the card says described. Confirm against the paper itself, and get his dates if the paper has them.

**3. Where this file should live — `Business/`.**
Jim indicated this subproject belongs in the JiMS project rather than the `JimPlamondon/JimPlamondon` repo. `Business/` is untracked; `business-public/` is the tracked counterpart. The script contains pre-announcement naming strategy, so it probably belongs in the private one. Ask him, then move all three files.

---

## Open items you can settle without those folders

1. **`Specs/JiMStudent_Spec.md` §3.3 contradicts itself, and someone must rule.**
   - The **"Staff locations"** bullet: lines every 200 cents, seven per octave, *Do Re Mi* on lines and *Fa So La Ti* on spaces.
   - The **"Drawn staff lines"** bullet, marked *canonical, owner ruling 2026-08-14*: lines at exact JI ratios coloured by prime limit, and **every diatonic note sits on a line**, chromatic notes between. That is eight lines per octave at unequal spacing.

   These cannot both hold. The animatic follows the second because it is later and explicitly canonical. **Whichever is right, §3.3 needs one bullet rewritten.**

2. **Newton's card claims something the spec may not support.** The card reads *"1704 · colour mapped onto the notes."* The only colour system documented in §3.3 is the N-limit **line** scaffold — red Do-lines, violet 3-limit, green 5-limit — not noteheads coloured by pitch class. The animatic was changed to match the spec: lines carry colour, noteheads stay ink. Either colour-by-pitch exists somewhere that wasn't found, or Newton's card overstates. Resolve it.

3. **The *Hex Player* year.** Milne & Prechtl's card carries no date because `Nomenclature.md` §"Shear (button-field)" cites the paper without one, and guessing on a card that holds for six seconds is worse than leaving it blank.

4. **Euler: 1739 or 1774?** The card says 1739 (*Tentamen*). The lattice diagram is also cited to his 1774 work. Use whichever the rest of the corpus defends.

5. **Sethares: 1993 or 1998?** The card says 1993 (the *JASA* paper). 1998 (*Tuning, Timbre, Spectrum, Scale*) is the better-known citation.

6. **Runtime.** :70 in draft 2, :81 now. The growth is real work — Schoenberg's silent transformation, Wicki's scale-before-transposition, the new well-formed-scales card. If :81 is too long, the cheapest cut on file is Sethares; his idea survives in Newton's spectrum and in the "tuning was settled" line of the VO.

7. **Two cards have no caption:** Roualle and the maintainers. Guido's caption states an *outcome* — *"Sight-singing: reduced time-to-competence by 5×–10×"* — where the other nine describe the picture. Turning them all to outcomes is arguably better and is a deliberate choice not yet made. If you do it, the numbers matter more than the prose; get sources per claim before putting a multiplier on screen.

8. **Two things final art must fix that the animatic deliberately fakes.**
   - **WHOBAWI buttons.** The animatic draws plain circles. The real field uses the eye-shaped geometry with extensions along the M5 and m4 axes (`Nomenclature.md`, "WHOBAWI", from patent WO2006050575A1 fig. 27). It was not invented from the prose description.
   - **Shaped noteheads.** Naturals default, sharps triangles vertex-up, flats vertex-down, doubles squares. The animatic uses plain ellipses. The melodies shown are all Do-mode naturals, so nothing is currently mis-shaped — but any chromatic note added will need the right glyph.

9. **Three citations in the JiMS repo are wrong and a fix is staged but unpushed.** "Sight-Reading Music Theory" is unpublished — submitted to *JMTP*, rejected — yet `Specs/JiMStudent_Spec.md` lines 60 and 488 and `Specs/JimmyShujaa_Spec.md` line 686 all cite it as *JMTP* 2009. `PAPER_INDEX.md` and `Specs/RealTimeExport/data/sources.json` have it right. The corrected wording is *"unpublished manuscript, 2009. (Submitted to the Journal of Music Theory Pedagogy and rejected; see `PAPER_INDEX.md`.)"* This is unrelated to the film, which carries no citations.

---

## Decisions already made — please do not relitigate

- **The homage is the point.** "Here's to the crazy ones" opens it. No softening.
- **Rule zero: show the MeloPresto implementation, never the inventor's original.** Euler's card shows the wavu as we draw it; Wicki's shows our button-field; Newton's spectrum lands on our solfa.
- **Rule zero's amendment:** where a later card's contribution *is* an improvement on an earlier one, the earlier card shows the historical state — otherwise two contributions collapse into one picture. Exactly two pairs qualify: **Guido → Glover** and **Euler → Schoenberg**. (**Wicki → Wilson/Carey/Clampitt** is a third continuous-image pair, but both halves are ours.)
- **Guido's card is his own staff, drawn to his specification.** Four lines a *third* apart, C E G B from the bottom; the C line carries his colour and *littera clavis*; the natural hexachord on C, chosen because it contains no B and so needs no B-durum/B-molle mutation explained in six seconds; **puncta, not noteheads** — square notation is a century later. These are deliberate. Do not "modernise" them.
- **No portraits. Not one.** The film shows what these people *made*, animated. This is Jim's call after seeing the animatic, and it also means nothing needs sourcing or clearing as an image.
- **Brian Hayden is not in the film.** He reinvented what Wicki published ninety years earlier, so the net contribution is zero. Jim's ruling. Note the house term stays "Wicki-Hayden" in `Nomenclature.md` and `Theory.md` — the film and the nomenclature differ deliberately.
- **Schoenberg follows Euler directly**, out of chronological order, because his Map is the wavu's dual and the two shots are one continuous transformation of a single image. His shot plays **silent**.
- **The wavu does not spin.** It holds still; the tonality ripples across it, sharpward to flatward.
- **The voiceover never names or explains anyone.** That is the whole trick of the spot being saluted, and it is why ten cards fit. Cards do attribution; animation does argument; narration is a hymn to the type of person. Draft 1 gave everyone an explanatory clause and ran 2:45.

---

## Errors already found and fixed — do not reintroduce

- **Newton's dispersion had a sign error.** Colours fanned both above and below the incident path. With an apex-up prism every wavelength deviates *toward the base*; they differ only in how much, violet most. Rebuilt: seven bands 6°–26° below the undeviated ray, which is drawn dashed so the deviation reads.
- **Notes sat on nothing.** The converge/demo score stepped 12px per semitone on a staff with 28px line spacing. Glover's pitches had no staff at all. Guido's rectangular noteheads were positioned by their top edge, sitting 5.5px low, and his hexachord ran off the top of the staff. All rebuilt.
- **Milne was miscredited.** The button-field/staff/sequencer alignment is the sheared-field-with-emanating-note-lines idiom from **Milne & Prechtl, *Hex Player***, not the 2007 CMJ dynamic-tuning paper.
- **Three animations asserted their captions without showing them** — Schoenberg's dual, Milne & Prechtl's registration, Sethares' coupling. All rebuilt to demonstrate rather than claim.

---

## Release gate — do not post this

Per `ws_melopresto_rename_registration_20260826`: **no public MeloPresto pages or assets until the CNIPA trademark application is submitted.** The film carries the wordmark on its end card. Write it, shoot it, cut it — hold the post. An unlisted upload is not an exception.

The only courtesy outstanding: tell Bill Sethares, Andy Milne, Anthony Prechtl, Werner Schweer and Michael Good that they are in it before it posts. Not for permission — on the shots that animate their ideas they will spot a wrong detail faster than we will. Keep the film-credit note **separate** from the pending TransFormSynth licence-grant request to Sethares recorded in `PROVENANCE.md`; a small ask and a large one should not share an email.

---

## How the animatic is built

Single HTML file, no dependencies beyond three Google fonts. Open it and it plays. Space plays/pauses, arrows step 5s, the shot sheet scrubs, "Read aloud" speaks the VO through the browser's voice for pacing.

- `SCENES` / `CARDS` / `VO` — three arrays at the top of the script hold the entire timeline in seconds. Edit these to re-time anything.
- `COLOUR_AT` — the moment the greyscale filter lifts. The whole stage is `filter: grayscale(1)`, so **Newton's spectrum is drawn in full colour and rendered grey**: the film cannot see it yet. The page performs the film's central device rather than describing it.
- `build.<scene>` — one function per shot, drawing procedural SVG.
- `jimsStaff()` / `yAt(cents)` — the JiMS staff geometry, per §3.3's canonical bullet. Change `LINES` if the §3.3 ruling goes the other way.
- `LOGO` / `LOGO_VB` — the logo slot described above.
- `bx(r,c)` / `by(r)` and `semitone = 2c + 7r` — the Wicki-Hayden button-field.
