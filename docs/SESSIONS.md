# One editor at a time

Use the normal checkout and computer control of the xLights GUI.

## File ownership

Only one agent may edit a given file at a time. Check the current task and song notes and coordinate with any active editor before editing. Record the owner and files in the song notes. Notes record coordination; they are not an automatic lock.

Treat a sequence and its song layout as one editing task when xLights can save both. Shared assets also need one editor. Preserve unrelated dirty files and coordinate with the user if they are editing the same files.

## GUI ownership

Only one agent controls xLights at a time. Different target files do not make simultaneous mouse and keyboard control safe. Confirm the visible show folder, sequence, media, and duration at the beginning of the session.

Inspect the current selection before each edit and observe the result afterward. Save regularly. Save and close the sequence before switching songs or replacing files on disk; reopen and verify if the files have changed outside xLights.

## Handoff

Save the work and update `AGENT NOTES.md` with completed ranges, layout changes, inspected previews, outstanding issues, and the next action. Explicitly release file and GUI ownership before another agent continues. Commit intended changes and push when requested.

Local `Shows/` contents are ignored by default. Use a private show repository for versioned personal show data, or deliberately review what may be published before changing ignore rules.
