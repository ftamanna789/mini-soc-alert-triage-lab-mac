# Mini SOC Alert Triage Lab on Mac Using Wazuh

## Project Overview

This project is a local SOC analyst lab built on macOS using Wazuh. The goal was to practice entry-level SOC analyst tasks such as endpoint monitoring, alert triage, vulnerability detection, MITRE ATT&CK mapping, security configuration assessment, remediation validation, and incident documentation.

The lab was completed without AWS or any paid cloud service.

## SOC Workflow Practiced

Detect → Triage → Investigate → Document → Recommend Fixes

## Lab Environment

| Component | Details |
|---|---|
| Endpoint | MacBook Air |
| CPU | Apple M3 |
| Memory | 16GB |
| Operating System | macOS Sequoia |
| SIEM/XDR | Wazuh |
| Wazuh Agent | v4.14.5 |
| Deployment | Local lab using Docker/OrbStack |

## Tools Used

- Wazuh SIEM/XDR
- Wazuh macOS Agent
- macOS Terminal
- Docker/OrbStack
- Wireshark
- macOS Software Update Tool

## Work Completed

- Installed and configured Wazuh locally
- Deployed the Wazuh agent on macOS
- Troubleshot Wazuh agent connectivity
- Verified endpoint telemetry collection
- Reviewed Threat Hunting events
- Reviewed Vulnerability Detection findings
- Reviewed Security Configuration Assessment results
- Applied macOS and Safari updates
- Compared vulnerability counts before and after remediation
- Documented findings using SOC-style notes

## Key Results

| Severity | Before Remediation | After Remediation | Reduction |
|---|---:|---:|---:|
| Critical | 10 | 7 | -3 |
| High | 61 | 51 | -10 |
| Medium | 165 | 123 | -42 |
| Low | 21 | 19 | -2 |
| Total | 257 | 200 | -57 |

## Security Configuration Assessment

| Result | Count |
|---|---:|
| Passed | 37 |
| Failed | 20 |
| Not Applicable | 2 |
| Score | 64% |

## MITRE ATT&CK Mapping

Observed activity was mapped to MITRE ATT&CK tactics including:

- Defense Evasion
- Privilege Escalation
- Initial Access
- Persistence

## Screenshots

Screenshots are stored in the `screenshots` folder. Sensitive information such as hostname, IP address, serial number, username, and passwords has been redacted.

## Analyst Summary

This project demonstrates practical SOC analyst skills. I onboarded a macOS endpoint into Wazuh, investigated vulnerability and security configuration findings, remediated endpoint risk through system and application updates, and documented before-and-after results.

The vulnerability count decreased from 257 total findings to 200 total findings after remediation, showing a measurable reduction in endpoint risk.

## Skills Demonstrated

- SIEM monitoring
- Endpoint onboarding
- Alert triage
- Vulnerability triage
- MITRE ATT&CK analysis
- Security configuration assessment
- Remediation validation
- SOC documentation
- Technical troubleshooting


## Troubleshooting log — 17 October 2026 (unresolved)

During a later attempt to access the local Wazuh dashboard/API, the Wazuh Manager service reported **`failed`**. This is a subsequent operational issue, not a reversal of the earlier vulnerability-remediation results above.

### Evidence observed

- OrbStack Linux VM memory: 7.8 GiB total, approximately 5.5 GiB available; swap 8.8 GiB total, 0 B used.
- VM root disk: 220 G total, 25 G used, 195 G available (12% used).
- `systemctl is-active wazuh-manager` returned `failed`.
- Systemd initially reported `TimeoutStartUSec=45s`. A local override was applied to set `TimeoutStartSec=180s`, followed by `systemctl daemon-reload`; restarting the Manager did **not** resolve the failure.
- The status screenshot shows `ExecStart=/usr/bin/env /var/ossec/bin/wazuh-control start` exiting with status 1, including: `ERROR: Another instance is locking this process.` The referenced lock path was `/var/ossec/var/start-script-lock`.
- The lock directory contained a `pid` file with PID `259`. The check `ps -p 259` returned no matching process; a separate `ps -ef | grep '[w]azuh-control'` check also showed none.
- The old lock directory was moved aside to `/var/ossec/var/start-script-lock.stale-259` on the first attempt (no error reported). A repeated move showed `No such file or directory` at the original path.
- **After the lock move, Manager status still returned `failed`.** The root cause remains unconfirmed. An updated `journalctl` log after the move had been requested but was not yet provided.
- The repeating `OrbStack update available` notice is informational and was not established as the cause.

### Next diagnostic step

Collect current service logs without changing the system:

```bash
orb -m wazuh sudo journalctl -u wazuh-manager -n 50 --no-pager -l
```

Review these alongside `/var/ossec/logs/ossec.log` before any further restart or filesystem changes.

> **Status:** Investigation in progress. Do not describe Wazuh Manager or API connectivity as restored until independently verified. Historical security findings and vulnerability counts in this README remain from earlier lab runs.

