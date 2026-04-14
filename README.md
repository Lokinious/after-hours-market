# After Hours Market

**After Hours Market** is a Ren'Py visual novel / light management sim prototype about running a small neighborhood shop where ordinary errands slowly reveal something strange beneath the town gossip.

The first goal is a compact, playable Day 1 prototype with basic shop stats, recurring customers, and choices that affect cash, inventory, reputation, and stress.

## Status

Day 1 prototype verified in Ren'Py 8.5.2. The repository contains minimal Ren'Py files in `game/`, and lint plus direct launch checks have succeeded.

## Core Stats

- `cash`: money available for shop decisions.
- `inventory`: simple stock count for sellable items.
- `reputation`: how the neighborhood feels about the shop.
- `stress`: how much pressure the player character is carrying.

## Local Setup Plan

Install Ren'Py 8.5.2 outside this repository, then launch or lint the project with your local SDK path.

Run lint:

```powershell
& '<path-to-renpy-sdk>\renpy.exe' '<path-to-after-hours-market>' lint
```

Run the game:

```powershell
& '<path-to-renpy-sdk>\renpy.exe' '<path-to-after-hours-market>' run
```

See `docs/setup-agent.md` and `docs/renpy-setup.md` for teammate onboarding and verified local setup notes.

## Repository Layout

- `AGENTS.md`: instructions for AI coding agents.
- `docs/game-design.md`: mechanics and milestone scope.
- `docs/renpy-setup.md`: Windows Ren'Py setup plan.
- `docs/setup-agent.md`: teammate onboarding and local setup guide.
- `docs/story-bible.md`: tone, premise, characters, and setting.
- `docs/task-list.md`: incremental work list.
- `.github/copilot-instructions.md`: GitHub Copilot guidance.
- `game/options.rpy`: minimal Ren'Py configuration.
- `game/script.rpy`: first playable Day 1 prototype script.

## GitHub Remote

GitHub CLI is installed, but authentication may need repair. Check with:

```powershell
gh auth status
```

If auth is invalid, run:

```powershell
gh auth login -h github.com
```
