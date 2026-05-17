# Custom IDS Script

[![Python](https://img.shields.io/badge/Python-3.12-blue)](#) [![Status](https://img.shields.io/badge/status-MVP-green)](#) [![Security](https://img.shields.io/badge/security-defensive%20lab-purple)](#)

Simple Linux log IDS that evaluates local rules and emits terminal, Markdown, and JSON alerts.

- **Portfolio group:** Cybersecurity lab project
- **Status:** MVP implemented, tested, committed, and pushed to GitHub
- **GitHub:** https://github.com/SUDARSHANCHAUDHARI/CustomIDSScript
- **Local path:** `/Users/screencloudsudarshan/SUDARSHAN_CODE/sudarshan_repos/CyberSecurity/CustomIDSScript`

## MVP Snapshot

This repository includes a working MVP with safe sample data, deterministic detection or analysis logic, local tests, and generated output reports where relevant. It is ready for README/demo polish or deeper product work.

## Safe Use

This project is defensive and analysis-focused. Use only with logs, systems, repositories, and lab environments you own or have permission to assess.

## Core Features

- failed login detection
- suspicious command detection
- new user detection
- alert to terminal/Slack

## Quick Start

```bash
python3 -m ids.watcher
python3 -m unittest discover -s tests -p 'test_*.py'
```

The sample data is safe synthetic Linux activity.

## MVP Capabilities

- Loads local Linux IDS rules
- Detects failed SSH login attempts
- Detects suspicious shell command patterns
- Detects new local user creation
- Writes terminal output, Markdown reports, and JSON alerts

## Roadmap

- Polish sample output screenshots or terminal demos
- Add architecture diagram and deeper implementation notes
- Expand test coverage around edge cases
- Add Docker or local demo workflow where useful
- Prepare `v0.1.0-mvp` release notes
