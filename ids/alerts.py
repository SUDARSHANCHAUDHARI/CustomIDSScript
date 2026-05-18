"""Alert formatting for Custom IDS Script."""

from __future__ import annotations

from dataclasses import asdict
import json

from ids.rules import Alert

SEVERITY_ORDER = {"critical": 4, "high": 3, "medium": 2, "low": 1}


def format_terminal_alert(alert: Alert) -> str:
    return f"[{alert.severity.upper()}] {alert.timestamp} {alert.rule_id}: {alert.description} :: {alert.evidence}"


def summarize_alerts(alerts: list[Alert]) -> dict:
    """Return dashboard-friendly IDS alert summary."""
    return {
        "alerts": len(alerts),
        "high": sum(1 for alert in alerts if alert.severity == "high"),
        "medium": sum(1 for alert in alerts if alert.severity == "medium"),
        "rule_counts": {
            rule_id: sum(1 for alert in alerts if alert.rule_id == rule_id)
            for rule_id in sorted({alert.rule_id for alert in alerts})
        },
        "highest_severity": max(
            (alert.severity for alert in alerts),
            key=lambda severity: SEVERITY_ORDER.get(severity, 0),
            default="none",
        ),
    }


def build_markdown_report(alerts: list[Alert]) -> str:
    summary = summarize_alerts(alerts)
    sorted_alerts = sorted(alerts, key=lambda alert: SEVERITY_ORDER.get(alert.severity, 0), reverse=True)
    lines = [
        "# Custom IDS Alerts",
        "",
        f"- Alerts: {summary['alerts']}",
        f"- High severity: {summary['high']}",
        f"- Medium severity: {summary['medium']}",
        f"- Highest severity: `{summary['highest_severity']}`",
        "",
        "## Priority Queue",
        "",
    ]
    if not sorted_alerts:
        lines.append("No immediate analyst queue was generated.")
    for index, alert in enumerate(sorted_alerts[:5], start=1):
        lines.append(f"{index}. **{alert.severity}** {alert.rule_id}: {alert.description}")
    lines.extend(["", "## Alerts", ""])
    if not alerts:
        lines.append("No IDS rules matched the provided logs.")
    for alert in sorted_alerts:
        lines.extend(
            [
                f"## {alert.rule_id}",
                "",
                f"- Severity: {alert.severity}",
                f"- Timestamp: {alert.timestamp}",
                f"- Description: {alert.description}",
                f"- Evidence: `{alert.evidence}`",
                f"- Recommended action: {alert.recommended_action}",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def build_triage_report(alerts: list[Alert]) -> str:
    """Return compact IDS triage report."""
    summary = summarize_alerts(alerts)
    sorted_alerts = sorted(alerts, key=lambda alert: SEVERITY_ORDER.get(alert.severity, 0), reverse=True)
    lines = [
        "# Custom IDS Triage",
        "",
        f"- Alerts: {summary['alerts']}",
        f"- Highest severity: `{summary['highest_severity']}`",
        "",
        "## Rule Counts",
        "",
    ]
    for rule_id, count in summary["rule_counts"].items():
        lines.append(f"- `{rule_id}`: {count}")
    lines.extend(["", "## Analyst Queue", ""])
    if not sorted_alerts:
        lines.append("- No immediate analyst queue was generated.")
    for alert in sorted_alerts[:8]:
        lines.append(f"- `{alert.severity}` {alert.timestamp} {alert.rule_id}: {alert.description}")
    return "\n".join(lines).rstrip() + "\n"


def build_json_report(alerts: list[Alert]) -> str:
    return json.dumps([asdict(alert) for alert in alerts], indent=2) + "\n"
