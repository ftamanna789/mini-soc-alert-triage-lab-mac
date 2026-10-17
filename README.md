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


## Earlier dashboard evidence recovered from May 2026 conversations

The earlier discussion of screenshots, dated **6 May 2026**, recorded these **historical** Wazuh dashboard readings, well before the October service troubleshooting:

| View / metric | Earlier reported reading |
|---|---:|
| Threat Hunting — total events | 43,799 |
| Threat Hunting — level 12+ alerts | 0 |
| Threat Hunting — authentication failures | 1 |
| Threat Hunting — authentication successes | 3 |
| Endpoint overview — active agents | 1 |
| Earlier alert overview — medium alerts | 43,599 |

The readings above came from **different dashboard views/screenshot moments** and should not be added together or assumed to represent one common reporting window. An earlier screenshot also showed **no agents registered**; a subsequent endpoint screenshot recorded **one active agent**, consistent with progress during lab setup.

The endpoint screenshot identified macOS **15.7.4**, Apple **M3**, **16 GB** memory and Wazuh Agent **4.14.5**. Vulnerability and SCA counts from the same earlier work are preserved in the tables above. These are **historical pre-restart outcomes**, not claims about the October Manager's current health.

**Unverified later-recalled values:** “661 thousand”, “25”, and “118” were mentioned verbally in October, but their exact dashboard labels and reporting periods were not recovered. They are not represented as confirmed counts here.

## 17 October 2026 — pre-restart threat-hunting screenshots (12:20–12:27 BST)

The following findings are **transcribed from six Wazuh Threat Hunting screenshots captured between 12:20 and 12:27 BST**, before the subsequent Manager service troubleshooting. They demonstrate that the dashboard could query and display indexed alert documents at that time; they **do not independently prove a healthy Manager process or live agent–Manager connection** at the time of capture.

### Search and filtered results

- Threat Hunting → Events, query `rule.id: 510` (rootcheck host-based anomaly detection), manager `wazuh`, **Last 24 hours**: **26,711 hits** in the first screenshot. Visible document timestamps include 17 October 2026 around 11:43.
- The query included an exclusion of `/dev/.lxc/proc/*`-related data.file paths. Later screenshots showed another exclusion for `/dev/.lxc/sys/*` and a much smaller result set (the label is partially obscured by the details drawer and should not be treated as a verified exact total).
- The document details list includes manager-side agent `000` (`wazuh`) and macOS endpoint agent `001`. The macOS endpoint name/IP have been intentionally omitted from this public write-up.
- Rule `510`, severity level **7**, description **“Host-based anomaly detection event (rootcheck).”** The results represent rule matches, not confirmed incidents.

### Triage examples from the screenshots

| Observed finding | Source / Wazuh details | Analyst interpretation / next verification |
|---|---|---|
| Possible hidden file flagged in a `/dev/.lxc/sys/module/...` path | Manager agent `000`, rootcheck, rule 510, level 7 | Likely merits review as a container-/VM-specific filesystem artifact. Validate file path, container environment and rootcheck signature before raising as a security incident. |
| File `/dev/.lxc-boot-id` flagged as possible hidden file | Manager agent `000`, rootcheck, rule 510, level 7 | Check OrbStack/LXC environment and file provenance; the alert alone does not demonstrate malicious concealment. |
| TCP port **55555** flagged as hidden | macOS agent `001`, rootcheck, rule 510, level 7; message suggests a kernel-level rootkit or trojaned netstat as possibilities | **Unverified detection, not a confirmed rootkit.** Verify listening process and port state using trusted system tools, and check whether the environment/tool discrepancy can explain the warning. |
| Log file in `/var/log/Pulse Secure/Logging/` reportedly owned by root and writable by anyone | macOS agent `001`, rootcheck, rule 510, level 7 | Independently verify file mode, ownership and whether the file still exists. If confirmed, review permissions and remediate according to application requirements. |

The `rule.firedtimes` field visible in individual documents contained values such as 8,854, 2, 22,570, 1 and 22,569. **These are rule firing counters attached to event records; do not describe them as distinct confirmed alerts, incidents, or vulnerabilities.**

**Hidden dot-file detection (rootcheck):** During Threat Hunting I caught/investigated a possible hidden dot-file alert: `/dev/.lxc-boot-id` (Wazuh rule 510, level 7, manager-side agent `000`). The screenshot recorded **“File present on /dev. Possible hidden file.”** I treated this as a detection requiring verification, not evidence of a confirmed compromise. The `/dev/.lxc-*` filename indicates a likely link to the local LXC/OrbStack environment, which should be checked before escalating.

### SOC analyst actions and limits

1. Applied a rule-ID filter and inspected time-scoped matching events.
2. Opened individual alert documents and interpreted `agent.id`, `decoder.name`, `data.file`, `data.title`, `rule.level` and `rule.firedtimes`.
3. Compared manager-side LXC-related paths with macOS endpoint rootcheck findings, avoiding premature escalation of potentially environment-specific detections.
4. Identified follow-up validation for the hidden-port and writable-log-file findings. **Remediation and incident confirmation are not evidenced by these screenshots.**
5. Kept these historical dashboard findings separate from the later Wazuh Manager startup failure.

## Lab state before the October 2026 restart attempts

**Historical functioning lab (user-reported):** Before the later restart/troubleshooting sequence, the Wazuh lab had been used for dashboard monitoring, endpoint telemetry, threat-hunting review, vulnerability detection and security configuration assessment. The completed investigation and remediation results reported above belong to that earlier working period, **not** to a subsequently failed service state.

The user reports that Wazuh Manager was functioning before the restart attempts. There is no pre-restart `systemctl is-active` output in the evidence reviewed here to independently timestamp or validate that service state. In the troubleshooting transcript, `failed` was already observed at an early diagnostic check, *before the later explicitly recorded restart command*. Thus the evidence does **not** establish that the restart caused the failure.

The user also recalled historical alert figures described verbally as “661 thousand”, “25”, and “118”; their exact values, labels, time windows and meanings are **not yet verified**, and must not be reported as confirmed alert metrics. The screenshot available in this session shows **failed-service logs from 17 October**, not those earlier dashboard alert counts.

The following section records the **later operational troubleshooting**, separately from the historical SOC analysis.

## Troubleshooting log — 17 October 2026 (unresolved)

During later diagnostics of the local Wazuh dashboard/API, the Wazuh Manager service reported **`failed`**. The user says the lab had been working before the restart attempts; however, an early status check already returned `failed` before the explicitly documented restart. This is a subsequent operational issue, not a reversal of the earlier vulnerability-remediation results above.

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

Historical security findings and vulnerability counts in this README remain from earlier lab runs. The subsequent Manager/API connection issue has not been verified as resolved.

