# Custom IDS Script

**Goal:** Simple IDS for Linux logs.

**MVP:** Watch logs and trigger alerts.

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

## Repository Status

This repository contains a working Custom IDS Script MVP with safe sample logs, deterministic rules, generated alerts, and tests.

## Production Foundation

- Private GitHub repository linked to `main`
- Initial MVP scaffold committed
- CI repository-health workflow
- Security policy
- Contribution guide
- Pull request and issue templates
- Production readiness checklist
- Safe ignore rules for local secrets and generated files
