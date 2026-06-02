"""CLI entrypoint for Custom IDS Script."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from ids.alerts import build_json_report, build_markdown_report, build_triage_report, summarize_alerts
from ids.config import (
    DEFAULT_JSON_PATH, DEFAULT_LOG_PATH, DEFAULT_REPORT_PATH,
    DEFAULT_RULES_PATH, DEFAULT_SUMMARY_PATH, DEFAULT_TRIAGE_PATH,
)
from ids.rules import evaluate_logs, load_rules
from ids.watcher import load_log_lines


def main() -> None:
    parser = argparse.ArgumentParser(description="Custom IDS script")
    parser.add_argument("--log", type=Path, default=DEFAULT_LOG_PATH)
    parser.add_argument("--rules", type=Path, default=DEFAULT_RULES_PATH)
    parser.add_argument("--out-dir", type=Path, default=Path("reports"))
    args = parser.parse_args()

    rules = load_rules(args.rules)
    lines = load_log_lines(args.log)
    alerts = evaluate_logs(lines, rules)
    summary = summarize_alerts(alerts)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    (args.out_dir / "alerts.md").write_text(build_markdown_report(alerts), encoding="utf-8")
    (args.out_dir / "alerts.json").write_text(build_json_report(alerts), encoding="utf-8")
    (args.out_dir / "summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    (args.out_dir / "triage.md").write_text(build_triage_report(alerts), encoding="utf-8")
    print(f"Evaluated {len(lines)} log line(s), {len(alerts)} alert(s) generated")


if __name__ == "__main__":
    main()
