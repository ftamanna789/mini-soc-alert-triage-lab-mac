#!/usr/bin/env python3
"""Offline threat-hunting review of Wazuh JSON-lines alert exports."""
import argparse
import collections
import json
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="Summarize FIM alerts in Wazuh alerts.json")
    parser.add_argument("path", type=Path, help="Local JSONL alerts export")
    parser.add_argument("--contains", default="soc-fim-lab", help="Only paths containing this text")
    args = parser.parse_args()
    count = 0
    events = collections.Counter()
    for line_number, line in enumerate(args.path.open(encoding="utf-8"), 1):
        try:
            alert = json.loads(line)
        except json.JSONDecodeError:
            print(f"Skipping invalid JSON at line {line_number}")
            continue
        fim = alert.get("syscheck") or {}
        path = fim.get("path", "")
        if not path or args.contains not in path:
            continue
        count += 1
        event = fim.get("event", "unknown")
        events[event] += 1
        rule = alert.get("rule", {})
        print(f'{alert.get("timestamp", "?")} | agent={alert.get("agent", {}).get("id", "?")} | '
              f'rule={rule.get("id", "?")} | level={rule.get("level", "?")} | '
              f'event={event} | file={path}')
        changed = fim.get("changed_attributes", [])
        if changed:
            print("  Changed:", ", ".join(changed))
    print(f"\nMatched FIM alerts: {count}")
    print("Events:", dict(events))

if __name__ == "__main__":
    main()
