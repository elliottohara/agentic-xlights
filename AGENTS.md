# Agentic xLights — agent contract

Build intentional, musical xLights sequences with GPT, using GPT-6 Astra when selected and available in the host. Do not silently switch the user's model or change global agent settings.

## Read first

- Read `docs/WORKFLOW.md` before sequencing; `docs/XLIGHTS.md` before API authoring; `docs/SESSIONS.md` before owning a GUI session.
- Read the target song's `AGENT NOTES.md` before edits and update it after significant work.
- Resolve paths from this checkout. Never assume a developer's home path, prop names, or controller topology.

## Song boundaries

- Every song lives at `<Show>/Sequences/<Song>/` and is a standalone show folder.
- Scaffold with `python3 Tools/setup_song.py --show <Show> --song "<Song>"`.
- Each song owns a COPY of `xlights_rgbeffects.xml`. Explicitly tune its groups, group member order, views, and sequencer display order for its musical roles.
- Shared asset links are relative. Do not modify shared assets through a song's symlinks without authorization for that shared change.
- Never edit or refresh the master layout or network configuration without an explicit user request. Never silently replace a customized song layout.
- Never migrate existing songs into this public toolkit unless requested. Check redistribution rights before committing media or vendor sequences.

## Session and editing rules

- Use the normal checkout. Only one agent may edit a given file at a time; coordinate ownership before editing and hand it off explicitly. Do not create worktrees as part of the standard workflow.
- Use computer control of the xLights GUI by default. Only one agent controls the GUI at a time, even when editing different files. Verify the show folder, sequence path, duration, and media in the UI before changes; stop on a mismatch.
- Close a sequence before checking out files beneath it. Save before direct XML edits; back up, reopen, and verify afterward.
- Create and edit effects through the GUI. The API client is optional for tasks that call for it; read `docs/XLIGHTS.md` first and never use `setEffectSettings`, whose parsing can corrupt settings.
- Direct, backed-up `.xsq` edits are appropriate for deleting effects. Do not fake deletion with Off effects or shrinking effects into dark windows.
- Never fabricate EffectDB or palette indices. Import each timing track once. Effects on the same element/layer must not overlap.
- Inspect existing submodels before attempting custom grids or per-pixel work. Preserve hand-maintained ranges.
- Keep physical light output disabled unless the user requests a live hardware test.

## Quality and completion

- Plan sections, instrument timings, palette, energy, matrix content, and prop roles before bulk authoring.
- Use group buffer styles that fit their geometry; inspect reference settings instead of guessing.
- Build and review a representative passage first. Use contrast, purposeful layering, and beat-locked accents.
- Render, inspect previews, and distinguish visual evidence from XML/API checks. Never claim to have watched an uninspected preview.
- Record what changed, verification, remaining issues, and exact resume steps in song notes.
- Commit only the intended changes. Merge/push when requested; preserve unrelated user work.

## Toolkit changes

Run `python3 -m unittest discover -s tests -v`. Keep runtime tooling standard-library-only unless a dependency has a clear purpose. Do not require OpenAI credentials for local xLights utilities.
