# xLights automation lessons

These observations were learned in a working macOS show project in July 2026. Recheck behavior against your installed xLights version; they are not a promise about future releases.

## Transport and identity

The API accepts HTTP POST JSON at `http://127.0.0.1:49913/xlDoAutomation` (slot A) or port `49914` (slot B). Always use timeouts; unknown commands can hang. Startup show backups can block responses. `getVersion` proves readiness, not show-folder identity.

```python
from Tools import xlights_api as x

print(x.xl("getVersion", timeout=5))
print(x.xl("getOpenSequence", timeout=10))
# After checking the expected show folder, sequence path, length, and media:
x.add_effect("Exact model or Model/Submodel", 0, "On",
             "T_TEXTCTRL_Fadeout=.25",
             "C_BUTTON_Palette1=#FF0000,C_CHECKBOX_Palette1=1",
             1000, 2000)
x.save("/absolute/path/to/song/Song.xsq")
```

Use the actual target and an open sequence; the snippet is a recipe, not a runnable demo for a bundled layout.

## Authoring and deletion

- Effect names match UI spelling, e.g. `Color Wash`, not `ColorWash`.
- The API trims element names. Preserve settings values, especially face names with trailing spaces.
- Targets must be in the sequence master view. `Model/Submodel` can address existing submodels directly.
- Do not use `setEffectSettings`: observed colon-based parsing trims values, and JSON objects can report success without changing settings.
- Author with `addEffect` and its comma-separated `key=value` strings. To change effects, remove the intended originals with a backed-up XML edit and re-add them.
- No individual-effect delete command was available in the tested build. Save, back up, close, remove precisely scoped `<Effect>` elements, then reopen. Keep timing elements and unrelated layers intact. Prefer a dry-run report before deletion.
- `cloneModelEffects` from an empty source only clears as many target layers as the source contains. Use only when that whole scope is yours.
- Do not import an existing timing track name again: duplicate marks may result. Timing-track removal is a GUI task in the tested build.
- A transient HTTP 503 may occur. Mutation requests are not automatically retried by this client: inspect whether the effect landed before retrying to avoid duplicates.

## Geometry and faces

Group node order is not always geographic. A chase may look scattered unless the chosen buffer style matches the intended motion. Inspect `B_CHOICE_BufferStyle`, buffer transforms, group order, and camera settings in actual working references.

Faces with custom colors can ignore palettes; empty custom part colors may render white. With palette-driven faces, slots typically map to mouth, eyes, FaceOutline, FaceOutline2. Verify definitions and preview rather than overwriting prop ranges.

## Lifecycle

Opening a sequence outside the active show folder was observed to create an empty sequence silently. Verify `getOpenSequence` after opening. `changeShowFolder` did not reliably persist in the tested build: close/save and restart the identified slot for show changes. Never kill an instance without checking its PID, show directory, and ownership.

Create export parent folders before `exportVideoPreview`. Render calls can take a long time; stagger them across slots. Keep previews and render caches out of Git.

Upstream references: [xLights source](https://github.com/xLightsSequencer/xLights), automation dispatch in `src-ui-wx/automation/xLightsAutomations.cpp`, settings implementation in `src-core/utils/UtilClasses.cpp`, and `documentation/xlDo Commands.txt` in the source checkout. Consult the matching version before adding unfamiliar commands.
