# After Hours Market

**After Hours Market** is a Ren'Py visual novel / light management sim prototype about running a small neighborhood shop where ordinary errands slowly reveal something strange beneath the town gossip.

The first goal is a compact, playable Day 1 prototype with basic shop stats, recurring customers, and choices that affect cash, inventory, reputation, and stress.

## Status

Planning and scaffold stage.

## Core Stats

- `cash`: money available for shop decisions.
- `inventory`: simple stock count for sellable items.
- `reputation`: how the neighborhood feels about the shop.
- `stress`: how much pressure the player character is carrying.

## Local Setup Plan

Ren'Py is not assumed to be installed or on PATH yet.

Recommended Windows setup:

1. Download Ren'Py 8.5.2 from the official Ren'Py site.
2. Extract it somewhere stable, such as `C:\renpy-8.5.2-sdk`.
3. Launch `renpy.exe`.
4. Create or import this project once the project structure exists.
5. Run the game from the Ren'Py launcher during early development.

After Ren'Py is installed, document the local path in a non-committed note if needed.

## Repository Layout

- `AGENTS.md`: instructions for AI coding agents.
- `docs/game-design.md`: mechanics and milestone scope.
- `docs/renpy-setup.md`: Windows Ren'Py setup plan.
- `docs/story-bible.md`: tone, premise, characters, and setting.
- `docs/task-list.md`: incremental work list.
- `.github/copilot-instructions.md`: GitHub Copilot guidance.

## GitHub Remote

GitHub CLI is installed, but authentication may need repair. Check with:

```powershell
gh auth status
```

If auth is invalid, run:

```powershell
gh auth login -h github.com
```
