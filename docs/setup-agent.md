# Teammate Setup Guide

## Purpose

This guide helps a new teammate clone the repo, install Ren'Py, run the Day 1 prototype, and start contributing to **After Hours Market**.

## Repo Access

Repository: `https://github.com/Lokinious/after-hours-market`

Invited collaborators must accept the GitHub invitation before they can push branches or open pull requests from this repo. Collaborator invites are currently handled manually because GitHub CLI authentication may not work reliably in every local shell/keyring context.

## Team Members

- Caleb / Lokinious
- John Starr / johnstarr92
- OrnithoRJynchus

## Local Prerequisites

- Git
- GitHub CLI, optional but useful for cloning and PR work
- Ren'Py 8.5.2 SDK
- Codex CLI, optional
- A text editor or IDE

Python is bundled with Ren'Py for the game runtime. Do not require a separate Python install unless external tooling is added later.

## Clone And Setup

With GitHub CLI:

```powershell
gh repo clone Lokinious/after-hours-market
cd after-hours-market
```

Fallback with Git:

```powershell
git clone https://github.com/Lokinious/after-hours-market.git
cd after-hours-market
```

## Ren'Py Setup

Windows-oriented setup:

1. Download Ren'Py 8.5.2 from `https://www.renpy.org/latest.html`.
2. Extract the SDK outside the repo, for example `C:\renpy-8.5.2-sdk`.
3. Run `C:\renpy-8.5.2-sdk\renpy.exe`.
4. Set the projects directory to `C:\Users\caleb\dev` when working on Caleb's machine, or to the parent folder that contains your clone.
5. Open or import `after-hours-market`.
6. Launch the project from the Ren'Py launcher.

CLI checks, if your SDK path matches Caleb's:

```powershell
& 'C:\renpy-8.5.2-sdk\renpy.exe' --version
& 'C:\renpy-8.5.2-sdk\renpy.exe' 'C:\Users\caleb\dev\after-hours-market' lint
& 'C:\renpy-8.5.2-sdk\renpy.exe' 'C:\Users\caleb\dev\after-hours-market' run
```

Adjust paths if your clone or SDK lives elsewhere.

## Project Map

- `AGENTS.md`: instructions for AI coding agents working in this repo.
- `README.md`: project overview and quick local commands.
- `docs/game-design.md`: mechanics, scope, and Day 1 design notes.
- `docs/story-bible.md`: tone, setting, characters, and story constraints.
- `docs/task-list.md`: current setup and milestone checklist.
- `docs/dev-log.md`: chronological project notes.
- `docs/renpy-setup.md`: verified local Ren'Py setup and command notes.
- `game/options.rpy`: minimal Ren'Py configuration.
- `game/script.rpy`: Day 1 prototype script.

## Current Status

- Day 1 prototype script exists.
- Core variables exist: `cash`, `inventory`, `reputation`, and `stress`.
- Moon salt outcome tracking has been fixed.
- Ren'Py 8.5.2 launch and lint verification has succeeded on Caleb's machine.
- Teammates should still launch and lint the game locally after installing Ren'Py 8.5.2.

## First Good Teammate Tasks

- Install Ren'Py and verify the game launches.
- Run through Day 1 and report story or logic issues.
- Review `docs/story-bible.md` and suggest one customer idea.
- Review `game/script.rpy` for Ren'Py syntax or runtime problems.
- Improve Day 1 dialogue while preserving the cozy, lightly strange tone.
- Add a Day 2 planning note, but do not implement Day 2 until Day 1 is verified by the team.

## Contribution Workflow

- Create a branch per task.
- Keep commits small.
- Run or launch the game before opening a PR when possible.
- Do not commit generated Ren'Py files such as `.rpyc`, cache, saves, logs, build output, or SDK files.
- Update docs when changing mechanics, story direction, setup, or scope.

## Codex CLI Onboarding

From the repo root:

```powershell
codex .
```

Suggested first prompt:

```text
Read AGENTS.md, README.md, docs/setup-agent.md, docs/game-design.md, docs/story-bible.md, docs/task-list.md, and docs/dev-log.md. Summarize the current project status and suggest one small next task without editing files yet.
```

## Manual Fallback

Teammates who do not use Codex CLI can work directly from the docs:

1. Read `README.md`, `docs/game-design.md`, `docs/story-bible.md`, `docs/task-list.md`, and `docs/dev-log.md`.
2. Install Ren'Py 8.5.2 outside the repository.
3. Launch the project from the Ren'Py launcher.
4. Pick a small task from this guide or `docs/task-list.md`.
5. Create a branch, make the change, run or launch the game when possible, and open a pull request.

