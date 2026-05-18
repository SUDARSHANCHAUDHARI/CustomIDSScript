# Production Readiness

## Current Status

This repository has a working local MVP with deterministic rule evaluation, safe sample logs, generated reports, and tests. It is not production complete yet.

## Required Before Public Release

- Add tail-follow mode with checkpointing and log rotation handling.
- Add richer YAML parsing and rule schema validation.
- Add structured logging without leaking secrets.
- Add allowlist/suppression workflow with audit history.
- Add Slack/webhook delivery with secret-safe config handling.
- Add retention controls for collected alert artifacts.
- Run dependency and secret scans before release.

## Definition of Done

- CI passes on pull requests.
- README has setup, usage, and security notes.
- Sample data is safe to publish.
- Error paths are handled clearly.
- No secrets or local machine paths are committed.
