"""Rule loading and evaluation for Linux log IDS checks."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Rule:
    rule_id: str
    description: str
    severity: str
    contains: list[str]


@dataclass(frozen=True)
class Alert:
    rule_id: str
    description: str
    severity: str
    evidence: str


def load_rules(path: Path) -> list[Rule]:
    rules: list[Rule] = []
    current: dict[str, object] | None = None
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or line == "items:":
            continue
        if line.startswith("- id:"):
            if current:
                rules.append(_rule_from_dict(current))
            current = {"id": line.split(":", 1)[1].strip(), "contains": []}
        elif current is not None and line.startswith("description:"):
            current["description"] = line.split(":", 1)[1].strip()
        elif current is not None and line.startswith("severity:"):
            current["severity"] = line.split(":", 1)[1].strip()
        elif current is not None and line.startswith("- "):
            contains = current.setdefault("contains", [])
            assert isinstance(contains, list)
            contains.append(line[2:].strip().strip('"'))
    if current:
        rules.append(_rule_from_dict(current))
    return rules


def _rule_from_dict(data: dict[str, object]) -> Rule:
    return Rule(
        rule_id=str(data["id"]),
        description=str(data.get("description", data["id"])),
        severity=str(data.get("severity", "medium")),
        contains=[str(item).lower() for item in data.get("contains", [])],
    )


def evaluate_line(line: str, rules: list[Rule]) -> list[Alert]:
    lower = line.lower()
    alerts: list[Alert] = []
    for rule in rules:
        if all(pattern in lower for pattern in rule.contains):
            alerts.append(Alert(rule.rule_id, rule.description, rule.severity, line))
    return alerts


def evaluate_logs(lines: list[str], rules: list[Rule]) -> list[Alert]:
    alerts: list[Alert] = []
    for line in lines:
        alerts.extend(evaluate_line(line, rules))
    return alerts
