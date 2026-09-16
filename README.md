# agentic-xlights

Build musical xLights shows with GPT-6 Astra using computer control. The agent works in the xLights interface: inspect the layout, arrange groups, author effects, render, watch, and refine.

**Every song gets its own show folder**, with an independent layout for its groups, submodels, views, and ordering. **One agent edits a file at a time, and one agent controls the GUI at a time.** Use the normal checkout.

This repository contains instructions and a song-notes template. No songs, sequences, personal layouts, controller configurations, or purchased media are included.

## Start here

You need xLights and an agent host with computer-control access to your desktop. Select GPT-6 Astra in your host when available. No Python, automation server, or separate OpenAI API key is required by this repository. Git is useful for cloning and tracking changes; the instructions can also be downloaded.

1. Open this repository in your agent host and point it at [AGENTS.md](AGENTS.md).
2. Provide your master show folder and the song's exact media file.
3. Have the agent follow [song setup](docs/SETUP.md) to create a separate show folder and copy the layout without changing the master.
4. Open that song folder in xLights, verify the layout and media, then tune groups and ordering for the song.
5. Build a representative passage, render it, inspect the preview, and iterate before extending the sequence.

## Give your agent a task

> Read AGENTS.md. Use computer control to work in xLights. Create a separate show folder for this song using a copy of my master layout. Inspect the models and submodels, tune the song's groups and ordering, and record the musical plan in its AGENT NOTES.md. Build and review a representative passage before continuing. Only one agent may edit a given file or control the GUI at a time.

## Instructions

- [AGENTS.md](AGENTS.md): agent contract.
- [Song setup](docs/SETUP.md): folders, independent layout, assets, and notes.
- [Song workflow](docs/WORKFLOW.md): musical planning, authoring, and visual review.
- [Editing sessions](docs/SESSIONS.md): ownership and handoffs.
- [Song notes template](templates/SONG_NOTES.md): copy into each song folder as `AGENT NOTES.md`.

Shows belong in `Shows/`. Track actual sequences, layouts, and timing templates in Git, and original song media in Git LFS. Generated previews, playback exports, caches, and backups are excluded entirely. See [storage policy](docs/STORAGE.md). Install and initialize Git LFS before adding media; it is not needed to read these instructions or operate xLights.

This project is independent of OpenAI and xLights.
