"""Configuration helpers for the Custom IDS MVP."""

from __future__ import annotations

from pathlib import Path


DEFAULT_RULES_PATH = Path("rules/linux_rules.yaml")
DEFAULT_LOG_PATH = Path("data/sample-linux.log")
DEFAULT_REPORT_PATH = Path("reports/alerts.md")
DEFAULT_JSON_PATH = Path("reports/alerts.json")
DEFAULT_SUMMARY_PATH = Path("reports/summary.json")
DEFAULT_TRIAGE_PATH = Path("reports/triage.md")
