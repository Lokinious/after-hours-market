# Dev Log

## 2026-04-13

- Created local project folder at `C:\Users\caleb\dev\after-hours-market`.
- Initialized a Git repository.
- Added AI-friendly project documentation.
- Added Ren'Py setup plan targeting Ren'Py 8.5.2.
- Checked GitHub CLI authentication; the active `Lokinious` token is invalid and needs `gh auth login -h github.com`.
- Paused before creating or importing Ren'Py project files.
- Hand-scaffolded minimal Ren'Py files in `game/options.rpy` and `game/script.rpy`.
- Built the first Day 1 prototype flow with cash, inventory, reputation, and stress variables.
- Launch verification is pending until Ren'Py 8.5.2 is installed or located.
- Re-authenticated GitHub CLI as `Lokinious`; authenticated `gh` commands may need normal system keyring access.
- Created private GitHub repository at `https://github.com/Lokinious/after-hours-market`.
- Pushed local `master` branch to `origin/master`.
- Fixed Day 1 moon salt outcome tracking so sold, credit, and kept paths produce distinct late-customer truth dialogue.
- Downloaded the official Ren'Py 8.5.2 SDK ZIP from `https://www.renpy.org/latest.html`.
- Verified SDK SHA-256 as `F85AC72C353CD14056AE0A9E25D8A2BD27232C0DE4B59E29EAD9114BD68B1FA4`.
- Extracted the SDK outside the repo to `C:\renpy-8.5.2-sdk` and recorded the path in gitignored `renpy-path.txt`.
- Set the Ren'Py launcher projects directory to `C:\Users\caleb\dev`.
- Confirmed Ren'Py version `8.5.2.26010301`.
- Ran Ren'Py lint successfully with no reported errors.
- Launched the project successfully with Ren'Py and stopped the test process after confirming it stayed running.
- Added teammate onboarding setup guide in `docs/setup-agent.md`.
