# Ren'Py Setup

Ren'Py is not currently on PATH, so early development should use the Windows launcher.

## Target Version

- Ren'Py 8.5.2
- Stable release checked during planning: January 3, 2026

## Windows Install Path

Recommended:

1. Download Ren'Py 8.5.2 from the official Ren'Py site.
2. Extract the SDK to a stable path, for example `C:\renpy-8.5.2-sdk`.
3. Run `renpy.exe`.
4. In the launcher, set the projects directory to `C:\Users\caleb\dev`.
5. Import or create the `after-hours-market` project.

## Local Path Notes

If a local Ren'Py path needs to be recorded, put it in `renpy-path.txt`. That file is intentionally ignored by Git.

## Next Approval Point

Before adding generated or launcher-created Ren'Py files, confirm whether the project should be:

- Created through the Ren'Py launcher, then imported here.
- Hand-scaffolded in this repo with minimal `game/` files.
- Created elsewhere by Ren'Py and copied into this repository.

