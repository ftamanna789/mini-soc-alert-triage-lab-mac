# SOC Investigation — Authorised FIM modification test

**Date:** 29 October 2026 (UTC)  
**Status:** Closed for this controlled test  
**Classification:** Benign positive / authorised laboratory activity

## Executive summary

A macOS Wazuh agent detected an intentional text-file modification using scheduled File Integrity Monitoring (FIM). The Wazuh manager issued default **rule 550**, severity **7**, at **11:30:12 UTC**. The event was a detection-engineering exercise, **not** evidence of malicious intrusion.

## Evidence-based findings

| Field | Observed value |
|---|---|
| Agent | 001 (macOS) |
| Wazuh | v4.14.5 |
| Rule | 550 — Integrity checksum changed |
| Level | 7 |
| Event | modified |
| FIM mode | scheduled |
| File | soc-fim-lab/test-alert.txt |
| Size | 66 → 108 bytes |
| Changed attributes | size, mtime, md5, sha1, sha256 |
| MITRE tag | T1565.001 (Stored Data Manipulation) |
| Detection timestamp | 2026-10-29T11:30:12.216+0000 |

The test-file content was extended deliberately. The manager-side alert contained old/new checksums and modification times. A separate JSON evidence file was created in the local VM and successfully validated with `python3 -m json.tool`. The original evidence file remains local; **it has not been uploaded to this public repository**.

## Analyst determination

This is an **expected detection of authorised change**. A MITRE technique tag describes relevant behaviour, not proof of an attacker or compromise. Scope is limited to this one controlled FIM event. No attack attribution is claimed.

## Follow-up

1. Apply and test the proposed custom rule in the VM.
2. Run the hunting script on an approved local alert export.
3. Verify rule ID 100550 against a fresh controlled event before marking custom detection as proven.
4. Restore the temporary 120-second FIM scan frequency to the intended operational interval after testing.
