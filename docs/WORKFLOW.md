# From song to reviewed show

## 1. Establish inputs

Identify the exact audio/video cut, duration, desired style, frame interval (25 ms is a useful starting point), and master layout. Do not assume timings from another cut align. Inspect the actual XML for names, trailing spaces, model membership, submodels, face definitions, and views.

Run `Tools/setup_song.py` to make `<Show>/Sequences/<Song>/`. The layout is copied once; subsequent runs preserve it and the song notes. No sequence is fabricated. Media and scripts belong in the song's `Media/` and `Tools/`; timing templates in its `Timing Templates/`.

## 2. Engineer the song's layout

Launch xLights against the song folder. Build song-specific groups for musical roles and useful part banks. Choose group membership and member order deliberately. Arrange views and sequencer rows so related musical voices sit together; ensure authoring targets are in the master view. Document these choices in song notes.

The song layout may diverge from the master. Changes in the master do not propagate automatically: compare and selectively merge them when requested. Reload the show in xLights after external layout edits. Shared network/asset links still affect every song using those assets.

## 3. Plan music before effects

Mark sections and energy changes, then beats/bars and important instrument events. Map instruments to visual voices: rhythmic prop parts, sustained outline bases, melodic motion, vocal faces, and matrix content. Plan matrices early so video and house lighting complement each other.

Inspect render/buffer styles from any authorized reference sequences. Whole-prop effects alone do not recreate detailed part-bank choreography. Useful patterns include a slow base on spokes, texture on rings, and brief accent hits on arrows or other distinct parts. Actual settings depend on the layout and xLights version.

Use short full-display accents sparingly. Preserve dark valleys and calm passages. Avoid static filling everywhere, accidental double-rendering from overlapping groups, and scattered chases on groups with non-geographic node order. Agree song-specific palette and face rules with the user; no hard-coded assumptions about their props.

## 4. Timing and singing faces

Reuse existing tracks only for the identical media cut. Import each name once. For new lyric timing, a useful optional pipeline is audio extraction, word transcription, alignment to canonical lyrics, human correction, then xLights dictionary phonemes. Sung vocals may be lost by voice-activity detection; inspect the result. Snap marks to frames and verify against the audio, especially phrase starts.

Lyric tracks use phrase, word, and phoneme layers. Separate voices when different props sing different lines. Check face definition names exactly, including trailing spaces, and inspect custom colors before assuming a palette controls the face.

## 5. Author, render, iterate

Coordinate file and GUI ownership as described in `docs/SESSIONS.md`. Use computer control to create the sequence in xLights, save to an absolute path, and verify its media and duration in the UI. Start with a representative phrase including a transition. Author effects through the GUI, render, and inspect the video/GUI preview. For explicitly chosen API work, consult `docs/XLIGHTS.md`. Verify geometry, contrast, motion direction, lyrics, and synchronization. Extend the successful design across the song, with section-specific variation.

API success and valid XML cannot prove a sequence looks good. Check effect bounds, overlaps, target membership, missing assets, and visual output. Create export directories before rendering. Document any live checks you could not run.

## 6. Handoff

Update `AGENT NOTES.md` with the editing owner, files being edited, layout choices, timing sources, scripts, preview locations, completed ranges, and unresolved issues. Keep tools reproducible and paths checkout-relative wherever possible; xLights may still store absolute media paths, which need verification after moving a song.
