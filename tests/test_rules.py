from pathlib import Path
import unittest

from ids.alerts import build_markdown_report, format_terminal_alert
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

    def test_formats_alerts(self) -> None:
        rules = load_rules(ROOT / "rules/linux_rules.yaml")
        alerts = evaluate_logs(["sshd: Failed password for root"], rules)

        self.assertIn("[MEDIUM]", format_terminal_alert(alerts[0]))
        self.assertIn("failed-login", build_markdown_report(alerts))


if __name__ == "__main__":
    unittest.main()
