from pathlib import Path
import unittest

from ids.alerts import build_markdown_report, build_triage_report, format_terminal_alert, summarize_alerts
from ids.rules import evaluate_logs, load_rules
from ids.watcher import load_log_lines


ROOT = Path(__file__).resolve().parents[1]


class CustomIDSTests(unittest.TestCase):
    def test_loads_rules(self) -> None:
        rules = load_rules(ROOT / "rules/linux_rules.yaml")

        self.assertEqual(3, len(rules))
        self.assertEqual("failed-login", rules[0].rule_id)

    def test_evaluates_sample_logs(self) -> None:
        rules = load_rules(ROOT / "rules/linux_rules.yaml")
        alerts = evaluate_logs(load_log_lines(ROOT / "data/sample-linux.log"), rules)
        ids = {alert.rule_id for alert in alerts}

        self.assertEqual({"failed-login", "suspicious-command", "new-user"}, ids)
        self.assertEqual("May 18 09:00:01", alerts[0].timestamp)
        self.assertTrue(alerts[0].recommended_action)

    def test_formats_alerts(self) -> None:
        rules = load_rules(ROOT / "rules/linux_rules.yaml")
        alerts = evaluate_logs(["sshd: Failed password for root"], rules)

        self.assertIn("[MEDIUM]", format_terminal_alert(alerts[0]))
        self.assertIn("failed-login", build_markdown_report(alerts))

    def test_builds_summary_and_triage(self) -> None:
        rules = load_rules(ROOT / "rules/linux_rules.yaml")
        alerts = evaluate_logs(load_log_lines(ROOT / "data/sample-linux.log"), rules)
        summary = summarize_alerts(alerts)
        triage = build_triage_report(alerts)

        self.assertEqual(3, summary["alerts"])
        self.assertEqual("high", summary["highest_severity"])
        self.assertIn("Custom IDS Triage", triage)


if __name__ == "__main__":
    unittest.main()
