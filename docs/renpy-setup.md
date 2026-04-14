# Ren'Py Setup

Ren'Py is installed outside this repository and can be used through the Windows launcher or direct CLI commands.

## Target Version

- Ren'Py 8.5.2
- Stable release checked during planning: January 3, 2026

## Windows Install Path

- SDK path: `C:\renpy-8.5.2-sdk`
- Executable: `C:\renpy-8.5.2-sdk\renpy.exe`
- Launcher projects directory: `C:\Users\caleb\dev`
- Project path: `C:\Users\caleb\dev\after-hours-market`

## Local Path Notes

The local Ren'Py path is recorded in `renpy-path.txt`. That file is intentionally ignored by Git and should not be committed.

## Verified Commands

Check the installed version:

```powershell
& 'C:\renpy-8.5.2-sdk\renpy.exe' --version
```

Run lint:

```powershell
& 'C:\renpy-8.5.2-sdk\renpy.exe' 'C:\Users\caleb\dev\after-hours-market' lint
```

Run the game directly:

```powershell
& 'C:\renpy-8.5.2-sdk\renpy.exe' 'C:\Users\caleb\dev\after-hours-market' run
```

## Verification Result

- Ren'Py version check returned `Ren'Py 8.5.2.26010301`.
- Lint completed successfully with no reported errors.
- Direct launch completed successfully; the game process stayed running during the launch check.
- Lint generated ignored files such as `.rpyc`, `game/cache/`, and `game/saves/`. These must not be committed.
