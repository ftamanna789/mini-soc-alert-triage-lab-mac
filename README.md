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
