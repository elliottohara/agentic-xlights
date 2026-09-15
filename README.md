# agentic-xlights

Build musical xLights shows with GPT agents. Designed for a Codex + GPT-6 Astra workflow: inspect the real layout, plan the musical voices, author through xLights, render, review, and iterate.

**Every song is its own xLights show folder.** Each gets a layout copy so groups, submodels, views, and display ordering can be tuned for that song. The master layout stays user-owned. Shared assets use relative links; layouts never automatically sync.

This is a fresh toolkit extracted from a working show project. No songs, sequences, personal layouts, controller configurations, or purchased media are included.

## Start here

Requirements: Python 3.10+, Git, and a local GUI installation of xLights. The launch helper targets macOS; on other platforms launch xLights yourself with the appropriate automation slot and show folder. Folder setup uses symlinks, which may need additional permissions on Windows.

1. Clone this repository and open it in Codex.
2. Select GPT-6 Astra if your Codex account exposes it. Model selection belongs to your agent host; this repository does not change global settings or require a separate OpenAI API key.
3. Point the agent at [AGENTS.md](AGENTS.md). For another agent host, explicitly tell it to read that file and the linked workflow.
4. Create a local show root such as `Shows/Christmas/` and place your master `xlights_rgbeffects.xml` there, with any shared assets you own. `Shows/` contents are ignored by default so local display data stays out of this public toolkit.
5. Scaffold a song:

```bash
python3 Tools/setup_song.py --show Shows/Christmas --song "My Song 2026"
```

This prepares folders and notes; create the actual `.xsq` later through xLights. Start xLights with the **absolute song folder** as `-s`, never the shared show root.

```bash
open -a xLights --args -a -s "$PWD/Shows/Christmas/Sequences/My Song 2026"
```

Before authoring, verify the running instance's show folder in the UI and the open sequence's path, duration, and media through the API. A responsive port alone does not identify its show folder.

## Give your agent a task

> Read AGENTS.md and docs/WORKFLOW.md. Use GPT-6 Astra in the agent host. Start a new song in its own show folder using my master layout. Inspect available models and submodels, propose the song's groups and view ordering, and document the musical plan before adding effects. Render and review a representative section before building the rest.

## What is here

- [AGENTS.md](AGENTS.md): portable agent contract.
- [Song workflow](docs/WORKFLOW.md): musical planning, timing, layout tuning, and visual review.
- [xLights API lessons](docs/XLIGHTS.md): settings, deletion, rendering, and known pitfalls.
- [Concurrent sessions](docs/SESSIONS.md): separate worktrees and the two automation slots.
- `Tools/setup_song.py`: repeatable song scaffolding that preserves existing layouts and notes.
- `Tools/xlights_api.py`: standard-library HTTP client adapted from the original project.
- `templates/SONG_NOTES.md`: continuity and review checklist for each song.

Run the offline checks with `python3 -m unittest discover -s tests -v`. They do not start xLights or drive lights. Live rendering must be checked on your own display.

For agent instruction discovery, see [OpenAI's AGENTS.md documentation](https://developers.openai.com/codex/guides/agents-md). This project is independent of OpenAI and xLights.
