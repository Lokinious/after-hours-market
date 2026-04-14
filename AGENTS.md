# Agent Instructions

This repository is for a small Ren'Py visual novel / light management sim prototype called **After Hours Market**.

## Project Goals

- Build a playable Day 1 prototype before expanding scope.
- Keep the game cozy, lightly strange, character-driven, and grounded in a small neighborhood shop.
- Favor simple Ren'Py script and clear data structures over premature systems.
- Make changes incrementally and keep commits small.

## Working Rules

- Read `README.md`, `docs/game-design.md`, `docs/story-bible.md`, and `docs/task-list.md` before making broad changes.
- Teammate onboarding lives in `docs/setup-agent.md`; update it when setup or contribution workflow changes.
- Keep `docs/task-list.md`, `docs/dev-log.md`, and this file updated when project status, workflow, or scope changes.
- Do not rewrite existing story tone or character direction without updating the story bible.
- Keep game variables visible and easy to reason about: cash, inventory, reputation, and stress.
- Prefer Ren'Py-native patterns unless there is a strong reason to add external tooling.
- Avoid committing generated Ren'Py build/cache output.

## Current Technical Context

- Target engine: Ren'Py 8.5.2.
- Ren'Py SDK is installed outside the repo at `C:\renpy-8.5.2-sdk`.
- Local SDK path is recorded in gitignored `renpy-path.txt`.
- Python 3.11.3, Git, Node/npm, GitHub CLI, and Codex CLI are available locally.
- GitHub CLI authentication can vary by keyring context; run `gh auth status` before remote operations.
- Remote repository: `https://github.com/Lokinious/after-hours-market` (`origin`, private).

## First Milestone

Create a playable Day 1 slice:

- Open shop.
- Review starting cash and inventory.
- Handle at least two customer interactions.
- Make at least one inventory or money choice.
- Change reputation and stress based on choices.
- End the day with a short summary.

## Current Project Structure

- `game/options.rpy`: minimal Ren'Py project configuration.
- `game/script.rpy`: Day 1 prototype script with shop stats and choices.
- `docs/dev-log.md`: chronological project notes.

Ren'Py 8.5.2 lint and launch verification succeeded from `C:\renpy-8.5.2-sdk\renpy.exe`.
