"""CLI log watcher for Custom IDS Script."""

from __future__ import annotations

import argparse
from pathlib import Path

from ids.alerts import build_json_report, build_markdown_report, format_terminal_alert
from ids.config import DEFAULT_JSON_PATH, DEFAULT_LOG_PATH, DEFAULT_REPORT_PATH, DEFAULT_RULES_PATH
from ids.rules import evaluate_logs, load_rules


def load_log_lines(path: Path) -> list[str]:
    return [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip() and not line.startswith("#")]


def main() -> None:
    parser = argparse.ArgumentParser(description="Run Linux log IDS rules against a file")
    parser.add_argument("--rules", type=Path, default=DEFAULT_RULES_PATH)
    parser.add_argument("--log", type=Path, default=DEFAULT_LOG_PATH)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT_PATH)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON_PATH)
    args = parser.parse_args()

    alerts = evaluate_logs(load_log_lines(args.log), load_rules(args.rules))
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(build_markdown_report(alerts), encoding="utf-8")
    args.json.write_text(build_json_report(alerts), encoding="utf-8")
    for alert in alerts:
        print(format_terminal_alert(alert))
    print(f"Generated {len(alerts)} alert(s)")


if __name__ == "__main__":
    main()
