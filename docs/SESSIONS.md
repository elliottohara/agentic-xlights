# Worktrees and xLights sessions

For sequence work, keep the primary checkout for review and integration. Use a clean isolated worktree on a `codex/<task>` branch. Never overwrite another agent's or the user's dirty files.

The tested xLights build exposes at most two automation instances:

- Slot A: port 49913, launch `open -a xLights --args -a -s "<absolute song folder>"`.
- Slot B: port 49914, launch `open -n -a xLights --args -b -s "<absolute song folder>"`; set `XLIGHTS_API_PORT=49914` before importing the client.

Bind each slot to one worktree and one owner. Record ownership and branch in the song notes. Check running processes, API state, and existing notes before claiming a slot. Two agents can work on the same song only in separate worktree copies, with separate show-folder paths. A third API-backed GUI instance is not supported by the tested build.

The helper deliberately provides no auto-launch: launch explicitly only after establishing slot ownership and the desired show path. A responding API may belong to someone else's session.

Before switching branches, save and close the current sequence. If a checkout changes the layout, restart that slot. For a different song, restart with the new `-s` folder; keep the same slot flag. Shared macOS preferences can remember the other slot's directory, so always supply the flags explicitly.

When work is approved for integration, commit, merge from the clean primary checkout, push if requested, close the slot's sequence, and park the worktree on detached main. Leave unrelated work alone. Do not run concurrent heavy renders.

Local `Shows/` files are ignored by default. For versioned song work, use a separate private show repository or deliberately update ignore rules after reviewing its contents. Worktrees do not copy ignored local assets automatically; prepare the slot's show data before launching.
