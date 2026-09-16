# Imported individual shows

Imported 43 standalone song/animation folders from Personal-Drive on 2026-09-16. Originals remain unchanged. Each folder keeps its own layout, sequence, and original media. Generated previews, render caches, playback files, backups, and old check reports are excluded.

## Verification

All copied XML was parsed. References into each source song folder were converted to paths relative to that song folder. Main sequence media paths were checked for existence. No new xLights rendering or visual review was performed for this file migration.

## Existing missing assets

The source audit already reported missing assets for Abracadabra and The Dead Dance. These are source gaps, not files removed by this import.

### 01 - Abracadabra

- `ImportedMedia/Abracadabra Lady Gaga/Images/Abracadabra Red Dress Tall.png`
- `ImportedMedia/Abracadabra Lady Gaga/Images/Big Red Hat 1.png`
- `ImportedMedia/Abracadabra Lady Gaga/Images/Big Red Hat 2.png`
- `ImportedMedia/Abracadabra Lady Gaga/Images/Big Red Hat 3.png`
- `ImportedMedia/Abracadabra Lady Gaga/Images/Cast Spell 2.png`
- `ImportedMedia/Abracadabra Lady Gaga/Images/Cast Spell.png`
- `ImportedMedia/Abracadabra Lady Gaga/Images/Devil Comes Around.png`
- `ImportedMedia/Abracadabra Lady Gaga/Images/GaGaPumpkin.png`
- `ImportedMedia/Abracadabra Lady Gaga/Images/Gothic Red Dress w Moon.png`
- `ImportedMedia/Abracadabra Lady Gaga/Images/LG Arms Wide.png`
- `ImportedMedia/Abracadabra Lady Gaga/Images/Lady In Red.png`
- `ImportedMedia/Abracadabra Lady Gaga/Images/Mystical Maze Landscape.png`
- `ImportedMedia/Abracadabra Lady Gaga/Images/Mystical Maze Portrait.png`
- `ImportedMedia/Abracadabra Lady Gaga/Images/Path Heart Moonlight.png`
- `ImportedMedia/Abracadabra Lady Gaga/Images/Red Dress on Fire.png`
- `ImportedMedia/Abracadabra Lady Gaga/Images/Swirling Circles.png`
- `ImportedMedia/Abracadabra Lady Gaga/Images/West Side Dust.png`
- `ImportedMedia/Abracadabra Lady Gaga/Shaders/Church Window.fs`
- `ImportedMedia/Abracadabra Lady Gaga/Videos/Halloween Fire.mp4`
- `ImportedMedia/Abracadabra Lady Gaga/Videos/Halloween Fire_1.mp4`
- `ImportedMedia/Abracadabra Lady Gaga/Videos/Particle_xFFects_07.mp4`
- `ImportedMedia/Abracadabra Lady Gaga/Videos/PsyBackgroud.mp4`
- `ImportedMedia/Abracadabra Lady Gaga/Videos/Ring of Fire.mp4`

### The Dead Dance

- `ImportedMedia/The Dead Dance Final/Images/Dead Doll.png`
- `ImportedMedia/The Dead Dance Final/Shaders/Colour Diffusion Flow.fs`
- `ImportedMedia/The Dead Dance Final/Shaders/Hex Play_xL.fs`
- `ImportedMedia/The Dead Dance Final/Shaders/Mobius Spiral_10_1.fs`
- `ImportedMedia/The Dead Dance Final/Videos/Ballroom 1.mp4`
- `ImportedMedia/The Dead Dance Final/Videos/Creature of the Night.mp4`
- `ImportedMedia/The Dead Dance Final/Videos/Creepy Dolly Walking.mp4`
- `ImportedMedia/The Dead Dance Final/Videos/Creepy Eyes.mp4`
- `ImportedMedia/The Dead Dance Final/Videos/Dancefloor.mp4`
- `ImportedMedia/The Dead Dance Final/Videos/Dancers 3.mp4`
- `ImportedMedia/The Dead Dance Final/Videos/Dancers 4.mp4`
- `ImportedMedia/The Dead Dance Final/Videos/Dancing Pumpkin_1.mp4`
- `ImportedMedia/The Dead Dance Final/Videos/Dead Dance Skeletons.mp4`
- `ImportedMedia/The Dead Dance Final/Videos/Halloween Cat Eyes Blinking_1.mp4`
- `ImportedMedia/The Dead Dance Final/Videos/Hallway Fog.mp4`
- `ImportedMedia/The Dead Dance Final/Videos/Haunting Mirror.mp4`
- `ImportedMedia/The Dead Dance Final/Videos/Mirror Cry 2_1.mp4`
- `ImportedMedia/The Dead Dance Final/Videos/Pawn.mp4`
- `ImportedMedia/The Dead Dance Final/Videos/Queen.mp4`
- `ImportedMedia/The Dead Dance Final/Videos/Shock Move 2.mp4`
- `ImportedMedia/The Dead Dance Final/Videos/Slowmotion Dancing 2.mp4`
- `ImportedMedia/The Dead Dance Final/Videos/Slowmotion Dancing.mp4`

## Included folders

- 01 - Abracadabra
- 03 - This Is Halloween
- 11 - I Saw Mommy Kissing Santa Claus 2
- 12-The-Monster-_feat.-Rihanna_
- Bad Romance (Extra Clean)
- Christmas in Hollis
- Crystallize
- Fancy Like
- Ghostbusters
- Ghostbusters 2
- GreatestShowWorking 2
- Gunna Get Stuck
- Happily Ever After
- Home for the Holidays
- Insomnia
- Monster Mash
- O Come O Come Emmanuel
- Shelfish Elf 2022
- Skrillex Medley
- Testing
- Testing 2
- `The Christmas Song ` (folder name includes a trailing space)
- The Dead Dance
- The Devil Went Down to Georgia
- The Imperial March
- Thriller
- Titanium
- Titanium 2
- We Will Rock You
- What Christmas Means to Me
- What Christmas Means to Me 2
- You Make It Feel Like Christmas
- animation
- bars_test
- heather bday
- proud_of_you 2
- static
- static halloween
- thanksgiving
- tree test
- tree test 2
- tune_t0
- tuneto-halloween

## Lossless media optimization — 2026-09-16

`WCMTM_Matrix 1.avi` is now included for both What Christmas Means to Me sequences using lossless FFV1 in AVI. All 6,409 decoded BGR24 frames match the raw original (SHA-256 `049e9f9844c347d5311b66f6b0faf79a80f24105934628232d090942ec10764a`); 40 fps and 160.225 seconds are unchanged. The two identical copies use one LFS object. Original files remain on Personal-Drive. Playback in xLights has not been reverified after conversion.

## Pending oversized media

`jackolatern.mp4` remains external in `static halloween` and `tuneto-halloween`. The 3,957,640,788-byte original is almost 12 hours long; lossless recompression of a sample increased its size. Both sequences last 30 seconds and start the video at zero. Approval to include only the used 30 seconds is pending. Full originals remain on the drive and in the local checkout.
