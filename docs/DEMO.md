# Demo

Run the included Linux log sample:

```bash
python3 -m ids.watcher
```

Expected output:

```text
Generated 3 alert(s)
```

Generated artifacts:

- `reports/alerts.json`
- `reports/summary.json`
- `reports/alerts.md`
- `reports/triage.md`

The sample demonstrates failed SSH login, suspicious reverse-shell style command, and new local user creation.
