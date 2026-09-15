# Set up a song show folder

Use ordinary file operations in the desktop file manager or your agent host, then computer control of xLights. No setup script is needed.

## 1. Establish the inputs

Identify the master show folder, exact song name, and exact media cut. Check whether the song folder already exists. If it does, read its notes and preserve its layout, sequence, and assets.

## 2. Prepare the folder

Create this structure under the chosen show root:

```
<Show>/Sequences/<Song>/
  xlights_rgbeffects.xml
  AGENT NOTES.md
  Media/
  Timing Templates/
  Previews/
```

Copy the master's `xlights_rgbeffects.xml` into the new song folder as a regular, independent file. Never make the song layout a link to the master. Do not overwrite a layout that is already there.

Copy `templates/SONG_NOTES.md` to `AGENT NOTES.md` and replace the `{song}` and `{show}` placeholders. Create the actual `<Song>.xsq` later in xLights; do not create an empty placeholder file.

## 3. Make assets available

Place the song's media in `Media/`. Copy the supporting assets needed by the layout, such as face images, images, palettes, or effect media, into the song folder while preserving their relative structure. Verify paths in xLights because copied layouts and sequences may reference absolute paths elsewhere.

If an established show already shares assets, keep that arrangement and document the locations. Shared assets do not have to be duplicated, but changes to them affect other songs. Symlinks are optional, not a setup requirement.

If the song needs an existing controller configuration, copy `xlights_networks.xml` from the master into the song folder. Keep it unchanged unless the user requests controller changes. Keep physical output disabled during authoring and preview.

## 4. Open and verify in xLights

Save and close any current sequence. Select the new song folder as the show folder through xLights. Verify the displayed folder and layout; reopen xLights against that folder if the change has not taken effect.

Create a new musical sequence through the GUI, select the exact media file and frame interval, and save it as `<Song>.xsq` inside the song folder. Verify duration, media, model availability, and asset rendering.

Tune groups, group member order, submodels, views, and sequencer rows in this song's layout. Record those choices in the song notes. Master layout changes do not automatically propagate to existing songs.
