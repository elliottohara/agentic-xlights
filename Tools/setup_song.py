#!/usr/bin/env python3
"""Prepare a standalone song show folder; never create or import a sequence."""
import argparse
from pathlib import Path
import shutil
import xml.etree.ElementTree as ET

SHARED = ('Faces', 'DownloadedFaces', 'ImportedMedia', 'Images', 'colorcurves',
          'palettes', 'valuecurves', 'mhpresets', 'xlights_networks.xml',
          'xlights_keybindings.xml', 'xlights_effectpresets.json')
TEMPLATE = Path(__file__).resolve().parents[1] / 'templates' / 'SONG_NOTES.md'


def setup_song(show, song):
    if (not song.strip() or song != song.strip() or song in ('.', '..')
            or any(c in song for c in '/\\\n\r\x00')):
        raise ValueError('Song must be one nonempty folder name without path separators.')
    show = Path(show).expanduser().resolve(strict=True)
    master = show / 'xlights_rgbeffects.xml'
    if not master.is_file():
        raise ValueError(f'Missing master layout: {master}')
    ET.parse(master)
    parent = show / 'Sequences'
    destination = parent / song
    if parent.is_symlink() or destination.is_symlink():
        raise ValueError('Sequences and song folder must be real directories.')
    layout = destination / 'xlights_rgbeffects.xml'
    notes = destination / 'AGENT NOTES.md'
    folders = ('Media', 'Media/Images', 'Timing Templates', 'Tools', 'Backups')
    for name in folders:
        path = destination / name
        if path.is_symlink() or (path.exists() and not path.is_dir()):
            raise ValueError(f'Expected a real directory: {path}')
    for path in (layout, notes):
        if path.is_symlink() or (path.exists() and not path.is_file()):
            raise ValueError(f'Expected an independent regular file: {path}')
    destination.mkdir(parents=True, exist_ok=True)
    for name in folders:
        (destination / name).mkdir(parents=True, exist_ok=True)
    if not layout.exists():
        with master.open('rb') as src, layout.open('xb') as dst:
            shutil.copyfileobj(src, dst)
    for name in SHARED:
        source, target = show / name, destination / name
        if source.exists() and not target.exists() and not target.is_symlink():
            target.symlink_to(Path('../..') / name, target_is_directory=source.is_dir())
    if not notes.exists():
        with notes.open('x') as out:
            out.write(TEMPLATE.read_text().format(song=song, show=show.name))
    return destination


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--show', required=True, type=Path)
    parser.add_argument('--song', required=True)
    args = parser.parse_args()
    try:
        result = setup_song(args.show, args.song)
    except (ValueError, OSError, ET.ParseError) as exc:
        parser.exit(1, f'Error: {exc}\n')
    print(f'Show folder ready: {result}')
    print('Existing layouts and notes were preserved. No sequence was created.')


if __name__ == '__main__':
    main()
