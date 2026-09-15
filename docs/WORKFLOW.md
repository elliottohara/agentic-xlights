# From song to reviewed show

## 1. Establish inputs

Identify the exact media cut, duration, desired style, frame interval, and master layout. Follow `SETUP.md` to prepare the song's own show folder. Read its notes before resuming existing work.

Inspect models, groups, submodels, face definitions, and views in xLights. Use the actual display as the source of truth.

## 2. Engineer the song's layout

Open the song folder in xLights. Build song-specific groups for musical roles and useful prop parts. Choose group membership and member order deliberately. Arrange views and sequencer rows so related musical voices sit together. Document these choices in song notes.

The song layout can diverge from the master. Master changes do not propagate automatically; compare and selectively incorporate them when requested. Preserve hand-maintained submodels and face definitions.

## 3. Plan music before effects

Mark sections and energy changes, then beats, bars, and important instrument events using xLights timing tools. Map instruments to visual voices: rhythmic prop parts, sustained outline bases, melodic motion, vocal faces, and matrix content. Plan matrices early so video and house lighting complement each other.

Inspect buffer styles and settings in authorized reference sequences through xLights. Detailed choreography may need separate prop parts rather than whole-prop effects. Group order and buffer style determine how motion reads; preview the result.

Use short full-display accents sparingly. Preserve dark valleys and calm passages. Avoid accidental double-rendering from overlapping groups and scattered chases caused by non-geographic node order. Establish song-specific palette and face rules from the user's preferences.

## 4. Timing and singing faces

Reuse existing timing tracks only for the identical media cut, and import each track once through the GUI. For new timings, use xLights timing and lyric tools, refine against the media, and verify phrase boundaries and phonemes. Separate voices when different props sing different lines.

Check face definitions exactly, including trailing spaces, and inspect custom colors before assuming a palette controls the face. Review lip sync in playback. If the agent cannot access the audio, state that limitation and do not claim to have verified synchronization by ear.

## 5. Author, render, iterate

Coordinate ownership as described in `SESSIONS.md`. Start with a representative phrase including a transition. Create and edit effects through computer control. Confirm the selected model, layer, time range, and settings before applying each change.

Render and inspect the preview. Verify geometry, contrast, motion direction, lyrics, and synchronization. Check effect bounds, overlaps, missing assets, and whether groups render as intended. Extend the successful design across the song with section-specific variation.

A successful save does not prove the sequence looks good. Record which preview ranges were actually inspected and which checks remain outstanding.

## 6. Handoff

Save and update `AGENT NOTES.md` with the editing owner, files changed, layout choices, timing sources, preview locations, completed ranges, and unresolved issues. Include the current GUI state and exact next action. Verify asset paths again if a song is moved.
