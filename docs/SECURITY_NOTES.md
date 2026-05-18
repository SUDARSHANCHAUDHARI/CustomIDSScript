# Security Notes

This project is defensive and analysis-only. Use it only with logs from systems you own or have permission to monitor.

## Data Handling

- Linux logs can contain usernames, hostnames, commands, IP addresses, and local paths.
- Redact production identifiers before sharing reports.
- Do not commit production `/var/log/auth.log`, shell history, or sudo logs.
- Sample data is synthetic and uses documentation IP ranges.

## Detection Caveats

- Rule matches are triage signals, not proof of compromise.
- Admin activity can look suspicious without change-window or user context.
- Use allowlists and reviewer approval before suppressing alerts.
