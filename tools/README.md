# tools

## captions_to_md.py

Converts a YouTube caption file (`.vtt` or `.srt`) into a clean Markdown
transcript.

YouTube's auto-captions use a rolling two-line display, so each cue repeats the
tail of the one before it. Stripping timestamps naively gives you every phrase
two or three times; this script reconstructs the underlying word stream by
appending only the genuinely new suffix of each cue. It also strips inline
`<c>` spans and word-level timing tags, unescapes HTML entities, groups the
result into timestamped paragraphs at sentence boundaries, and promotes
`SPEAKER:` prefixes to bold.

### Getting the captions

```sh
pip install yt-dlp
yt-dlp --write-auto-subs --write-subs --sub-langs en --sub-format vtt \
       --skip-download 'https://youtu.be/VIDEO_ID'
```

Prefer human-written subtitles (`--write-subs`) when the video has them; the
auto-generated track has no punctuation or casing, which makes for a noticeably
rougher transcript.

### Converting

```sh
python3 tools/captions_to_md.py 'Title [VIDEO_ID].en.vtt' \
    --title   'How To Command Belief Like a Cult Leader' \
    --speaker 'Joanna Wiebe' \
    --url     'https://youtu.be/VIDEO_ID' \
    -o transcripts/command-belief.md
```

Options: `--every SECONDS` tunes paragraph length (default 45),
`--no-timestamps` drops the per-paragraph time marks, `-o` sets the output path
(defaults to the input path with an `.md` extension).

### If there are no captions at all

Transcribe the audio locally, then feed the result through this script:

```sh
yt-dlp -x --audio-format mp3 -o talk.mp3 'https://youtu.be/VIDEO_ID'
whisper talk.mp3 --model medium --output_format vtt
```
