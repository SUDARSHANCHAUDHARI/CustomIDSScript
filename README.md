# Custom IDS Script

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](#requirements)
[![Status](https://img.shields.io/badge/status-MVP-green)](#status)
[![Security](https://img.shields.io/badge/security-defensive%20lab-purple)](#safe-use)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Lightweight rule-based Linux intrusion detection. Evaluates YAML rules against `auth.log`, syslog, and shell history to emit terminal, Markdown, and JSON alerts.

---

## Overview

Custom IDS Script is a defensive analysis tool for small Linux servers, kiosks, and lab environments. It loads YAML rule files describing detection patterns (failed logins, suspicious commands, new user creation, sudo abuse) and applies them to log lines, producing actionable alerts with timestamps and recommended response actions.

## Features

- Loads YAML detection rules from a local directory
- Detects failed SSH login attempts
- Detects suspicious shell command patterns
- Detects new local user creation
- Adds timestamps and recommended response actions to alerts
- Writes terminal output, Markdown report, JSON alerts, summary JSON, and triage handoff

## Requirements

- Python 3.10 or newer
- Linux, macOS, or Windows
- No third-party Python packages (standard library only)
- Optional: Docker for the demo container

## Installation

```bash
git clone https://github.com/SUDARSHANCHAUDHARI/CustomIDSScript.git
cd CustomIDSScript
pip install .
```

This registers the `custom-ids` CLI command.

To run without installing:

```bash
python3 main.py --help
```

## Usage

Evaluate the included sample Linux log against the bundled rules:

```bash
python3 main.py --log data/sample-linux.log --rules rules/linux_rules.yaml --out-dir reports
```

Generated outputs in `reports/`:

- `alerts.md` — Markdown alert report
- `alerts.json` — structured alert list
- `summary.json` — counts and severity breakdown
- `triage.md` — analyst triage checklist

## Project Structure

```
CustomIDSScript/
├── ids/            Rule loader, watcher, alert formatter
├── rules/          YAML detection rules
├── data/           Safe sample Linux logs
├── reports/        Example generated output
├── docker/         Dockerfile + compose support
├── docs/           Architecture, security notes, demo
├── tests/          Unit tests
├── main.py         CLI entrypoint
├── pyproject.toml  Package metadata
└── LICENSE
```

## Testing

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
```

## Docker Demo

```bash
docker compose run --rm custom-ids-demo
```

## Safe Use

This project is defensive and analysis-focused. Use only with logs and lab environments you own or have explicit written permission to assess. The included sample log and rules are synthetic and safe for public demo use.

## Status

Working CLI MVP with tests, sample data, and Docker support.

## Roadmap

- Watch-mode for tailing live log files
- More rule types (regex chains, time-window correlation)
- Configurable severity scoring
- Slack / webhook alert delivery
- GitHub release `v0.1.0-mvp`

## License

Released under the [MIT License](LICENSE). You are free to use, modify, and distribute this software with attribution.

## Author

**Sudarshan Chaudhari** — [SudarshanTechLabs](https://github.com/SUDARSHANCHAUDHARI)
Bangkok, Thailand

For inquiries: open an issue on [GitHub](https://github.com/SUDARSHANCHAUDHARI/CustomIDSScript/issues).
