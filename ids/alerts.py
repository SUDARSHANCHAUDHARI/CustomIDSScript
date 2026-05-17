"""Alert formatting for Custom IDS Script."""

from __future__ import annotations

from dataclasses import asdict
import json

from ids.rules import Alert


def format_terminal_alert(alert: Alert) -> str:
    return f"[{alert.severity.upper()}] {alert.rule_id}: {alert.description} :: {alert.evidence}"


def build_markdown_report(alerts: list[Alert]) -> str:
    lines = ["# Custom IDS Alerts", "", f"- Alerts: {len(alerts)}", ""]
    if not alerts:
        lines.append("No IDS rules matched the provided logs.")
    for alert in alerts:
        lines.extend(
            [
                f"## {alert.rule_id}",
                "",
                f"- Severity: {alert.severity}",
                f"- Description: {alert.description}",
                f"- Evidence: `{alert.evidence}`",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def build_json_report(alerts: list[Alert]) -> str:
    return json.dumps([asdict(alert) for alert in alerts], indent=2) + "\n"
