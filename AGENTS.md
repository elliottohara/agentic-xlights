# Agentic xLights — agent contract

Build intentional, musical xLights sequences with GPT-6 Astra using computer control. Respect the user's model selection and existing work.

## Read first

- Read `docs/SETUP.md` for a new song, `docs/WORKFLOW.md` before sequencing, and `docs/SESSIONS.md` before taking control of xLights.
- Read the song's `AGENT NOTES.md` before editing and update it after significant work.
- Inspect the actual display. Never assume a developer's paths, prop names, or controller topology.

## Song boundaries

- Every song lives at `<Show>/Sequences/<Song>/` and is its own xLights show folder.
- Copy the master layout once. Each song owns its `xlights_rgbeffects.xml`; tune its groups, group member order, submodels, views, and sequencer row order for the music.
- Preserve existing song layouts and notes when resuming. Never silently refresh a customized layout from the master.
- Leave the master layout and controller configuration alone unless the user requests changes to them.
- Keep song media, timing templates, and previews with the song. Verify asset paths after copying a layout.
- Shared assets require coordination before edits; changing a shared file can affect other songs.
- Do not migrate existing songs or publish personal show data unless requested.

## Editing

- Use the normal checkout. One agent edits a file at a time; coordinate ownership and handoffs. Do not set up worktrees.
- Only one agent controls the xLights GUI at a time. Coordinate with the user if they are editing too.
- Use computer control to create sequences, edit layouts and effects, import timings, save, render, and review.
- Inspect the visible UI before acting. Confirm the active show folder, sequence, selected model/layer, time range, and relevant settings. Observe the result after changes; do not click blindly through a long chain.
- Use the host's supported computer-control tools. Do not introduce Python, an automation API, or a scripting pipeline as a prerequisite or fallback without a user request.
- If a control is unavailable or ambiguous, inspect the UI and explain the concrete blocker rather than switching authoring methods silently.
- Save before switching songs. Close a sequence before replacing its files on disk. Preserve unrelated dirty files.
- Delete effects through the GUI; do not fake deletion with Off effects or move unwanted effects into dark windows.
- Import each timing track once. Avoid overlapping effects on the same element/layer.
- Inspect existing submodels before designing custom node selections. Preserve hand-maintained ranges and face definitions.
- Keep physical light output disabled unless the user requests a live hardware test.

## Quality and handoff

- Plan sections, instrument timings, palette, energy, matrix content, and prop roles before bulk authoring.
- Match buffer styles and group ordering to geometry. Inspect working references and preview results rather than guessing.
- Build and review a representative passage first. Use contrast, purposeful layering, and beat-locked accents.
- Render and inspect previews. Never claim to have watched an uninspected preview or heard audio you could not access.
- Record changed ranges, layout choices, verification, remaining issues, and exact resume steps in song notes.
- Save and hand off file and GUI ownership explicitly. Commit only intended changes; push when requested.

## Repository maintenance

Keep this repository focused on instructions and templates for computer control. Check documentation links and consistency after edits. Validate sequencing work in xLights through observed UI state and rendered previews.
