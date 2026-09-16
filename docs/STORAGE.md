# Show source and media

Track the actual sequences, each song's layout, timing templates, notes, original song audio/video, and supporting assets needed to render the show.

Sequences (`.xsq`), layouts, model definitions, and notes use ordinary Git. Original audio, video, and binary image assets use Git LFS via `.gitattributes`. Git LFS is a storage dependency for media contributors, not an xLights authoring tool. Install and initialize Git LFS before adding media; without its filters, Git can accidentally commit full binaries instead of LFS pointers.

Generated previews, rendered playback (`.fseq` and `.eseq`), caches, and backups must never be committed, including through LFS. Save preview exports under the song's `Previews/` folder or `RenderCompare/`; both are ignored. A video inside `Media/` is assumed to be a source asset, so do not export previews there.

Use `<Show>/Sequences/<Song>/Media/` for song-specific media. Store genuinely shared source assets once under the show root and document their references. Keep each song's layout independent. Verify all referenced assets are available after a fresh checkout; files referenced outside the repository are not automatically included.

Before committing, review the staged file list for generated content, verify media appears in `git lfs ls-files`, and check that `.xsq` and layouts remain ordinary Git files. Ignore rules do not untrack files already committed. Do not force-add generated files.

The repository is public. Publish only source media and third-party assets that may be redistributed. Record any required assets that must be obtained separately. Adding the storage policy does not itself migrate any songs.
