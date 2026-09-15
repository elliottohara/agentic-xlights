# One editor at a time

Use the normal checkout and computer control of the xLights GUI. Worktrees and permanent API slots are not part of the standard workflow.

## File ownership

Only one agent may edit a given file at a time. Before editing, check the current task and song notes for ownership and coordinate with any active editor. Record the files being edited and the owner in the song notes. A note records coordination; it is not an automatic lock. Save and explicitly hand off ownership before another agent continues. Preserve unrelated dirty files and coordinate with the user if they are editing the same files.

Treat a sequence and its song layout as a single editing task when an xLights session can save both. Shared asset files also need one editor, even when accessed through different songs' symlinks.

## GUI ownership

Only one agent controls the xLights GUI at a time. Different target files do not make simultaneous mouse/keyboard control safe. Check the visible show folder and sequence before each editing session; verify media and duration before authoring.

Open the song's own show folder. Save and close the sequence before switching songs or replacing files on disk. After external layout edits, reload the show and verify the visible groups and ordering. Save, back up, and close the sequence before a direct XML edit; reopen afterward so an old GUI copy cannot overwrite it.

## Handoff

Save the work and update `AGENT NOTES.md` with completed ranges, layout changes, inspected previews, outstanding issues, and the next action. Release file and GUI ownership explicitly. Commit the intended changes and push when requested. No slot parking or worktree cleanup is needed.

## Optional API tooling

`Tools/xlights_api.py` remains available for explicitly chosen API work; see `docs/XLIGHTS.md`. Its two automation ports apply only to API-driven sessions and do not require worktrees. The same one-editor and GUI ownership rules still apply.

Local `Shows/` files are ignored by default. For versioned song work, use a separate private show repository or deliberately update ignore rules after reviewing its contents.
