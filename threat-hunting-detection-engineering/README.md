# Threat Hunting & Detection Engineering — Wazuh FIM

A hands-on macOS endpoint + Wazuh Manager (Ubuntu/OrbStack) SOC lab. This folder extends the [Mini SOC Alert Triage Lab](../README.md).

**Evidence status:** Default Wazuh **rule 550** fired on 29 October 2026 at 11:30:12 UTC (level 7, file modified). The **custom rule 100550 is a proposed rule, not yet deployed or validated on the live Wazuh Manager**. The hunting script is provided for offline review and is not claimed to have been executed against the private log dataset.

## Confirmed FIM experiment

- Monitored a dedicated macOS test directory with Wazuh agent v4.14.5.
- Temporarily configured scheduled FIM checks at 120 seconds.
- Appended a harmless test line to `test-alert.txt`.
- Observed default rule **550**, level **7**, `syscheck.event=modified`.
- Recorded size change **66 → 108 bytes**, and MD5/SHA1/SHA256 and mtime differences.
- Observed MITRE ATT&CK **T1565.001** tagging; controlled test, not a real intrusion.
- Saved and validated a local JSON alert evidence file. Personal machine identifiers and raw event JSON are intentionally not published.

See [Incident Report](INCIDENT_REPORT.md).

## Custom rule (not yet validated)

File: [fim_custom_rule.xml](fim_custom_rule.xml)

This proposed rule chains from built-in rule 550, matches the lab test filename, and uses custom rule ID **100550**, level **10**. Wazuh's documented FIM rule examples use the `file` field inside rule definitions. Review the matching fields with `wazuh-logtest` in your installation before enabling.

On the **Wazuh Manager VM**, after reviewing existing local rules:

```bash
sudo cp /var/ossec/etc/rules/local_rules.xml /var/ossec/etc/rules/local_rules.xml.backup
sudo nano /var/ossec/etc/rules/local_rules.xml
# Add the XML <group> block from fim_custom_rule.xml, outside other <group> blocks.
sudo /var/ossec/bin/wazuh-logtest
# Test with a fresh FIM event, check rule 100550.
# Only after validation: sudo systemctl restart wazuh-manager
```

**Do not** replace `local_rules.xml` wholesale or restart the manager before checking the actual configuration. A ruleset failure can disrupt the SOC lab. Built-in rule 550 remains the only confirmed result so far.

## Threat hunting

File: [hunt_fim.py](hunt_fim.py). Reads newline-separated Wazuh alert JSON **offline**, filters by monitored directory, prints timestamp/agent/rule/severity/path and changed attributes, then counts events.

```bash
python3 hunt_fim.py /path/to/alerts.json --contains soc-fim-lab
```

For the locally saved single-event evidence file on the VM:

```bash
python3 hunt_fim.py "$HOME/fim-detection-evidence.json"
```

Suggested hypotheses:
1. Do FIM modifications occur outside an authorised test window?
2. Are repeated changes concentrated on the same monitored files?
3. Are there unexpected created/deleted events or level increases?
4. Does changing a monitored file result in an expected scheduled alert?

These are hunting questions, **not confirmed findings**.

## Scope / safety

No real malware, unauthorised access, or exploitation performed. Do not commit raw production alerts, endpoint IPs, usernames, hostname, tokens, or authentication secrets to a public GitHub repository.

## Reference

[Wazuh — Creating custom FIM rules](https://documentation.wazuh.com/current/user-manual/capabilities/file-integrity/creating-custom-fim-rules.html) | [Wazuh — Custom rules](https://documentation.wazuh.com/current/user-manual/ruleset/rules/custom.html) | [Wazuh — Testing rules](https://documentation.wazuh.com/current/user-manual/ruleset/testing.html)
