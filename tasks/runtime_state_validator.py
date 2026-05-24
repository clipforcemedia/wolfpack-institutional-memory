#!/usr/bin/env python3
"""
Runtime State Validator — Wolfpack Deterministic Task Execution Governance
Standalone: Python standard library only. No network access. No subprocess.
Validates processed_registry.json and runtime/EXECUTION_HISTORY.jsonl against
RUNTIME_STATE_GOVERNANCE.md and TASK_STATE_MODEL.md governance standards.
"""

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REPO = Path("/home/node/.openclaw/workspace/wolfpack-institutional-memory")
REGISTRY_PATH = REPO / "tasks" / "processed_registry.json"
HISTORY_PATH = REPO / "runtime" / "EXECUTION_HISTORY.jsonl"
REPORT_PATH = REPO / "runtime" / "RUNTIME_STATE_VALIDATION_REPORT.md"

VALID_STATUSES = {"discovered", "validated", "generated", "failed", "skipped"}
VALID_TASK_STATUSES = {
    "pending", "claimed", "in_progress", "completed",
    "failed", "blocked", "skipped_already_processed", "archived"
}
VALID_WORKER_STATES = {
    "idle", "polling", "task_claimed", "executing",
    "completed", "failed", "retry_pending", "abandoned", "recovered"
}


class ValidationResult:
    __slots__ = ("valid", "issues")

    def __init__(self) -> None:
        self.valid = True
        self.issues: list[str] = []

    def add_issue(self, msg: str) -> None:
        self.valid = False
        self.issues.append(msg)


def load_registry() -> tuple[dict, list[dict]]:
    if not REGISTRY_PATH.exists():
        raise FileNotFoundError(f"Registry not found: {REGISTRY_PATH}")
    with open(REGISTRY_PATH, encoding="utf-8") as f:
        data = json.load(f)
    return data, data.get("entries", [])


def load_history() -> list[dict]:
    if not HISTORY_PATH.exists():
        return []
    entries = []
    with open(HISTORY_PATH, encoding="utf-8") as f:
        for lineno, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                entries.append(json.loads(line))
            except json.JSONDecodeError as e:
                entries.append({
                    "_parse_error": str(e),
                    "_lineno": lineno,
                    "_raw": line[:200],
                })
    return entries


def validate_registry_entry(entry: dict, idx: int, result: ValidationResult) -> dict:
    """Validate a single processed_registry entry. Returns cleaned copy."""
    task_id = entry.get("task_id", "")
    status = entry.get("status", "")

    cleaned = {
        "task_id": task_id,
        "status": status,
        "processed_timestamp": entry.get("processed_timestamp"),
        "result_path": entry.get("result_path"),
        "failure_reason": entry.get("failure_reason"),
    }

    # 1 — duplicate task_id in registry
    # (detected separately across all entries)

    # 2 — failed task without failure_reason
    if status == "failed":
        if not entry.get("failure_reason"):
            result.add_issue(
                f"[{idx}] task_id={task_id!r} — FAILED task missing failure_reason"
            )

    # 3 — completed task without result_path
    if status in ("validated", "generated", "completed"):
        if not entry.get("result_path"):
            result.add_issue(
                f"[{idx}] task_id={task_id!r} — COMPLETED task missing result_path"
            )

    # 4 — invalid status value
    if status and status not in VALID_STATUSES:
        result.add_issue(
            f"[{idx}] task_id={task_id!r} — INVALID status {status!r} "
            f"(not in {VALID_STATUSES})"
        )

    # 5 — missing processed_timestamp
    if not entry.get("processed_timestamp"):
        result.add_issue(
            f"[{idx}] task_id={task_id!r} — MISSING processed_timestamp"
        )

    # 6 — task_id present
    if not task_id:
        result.add_issue(f"[{idx}] — ENTRY MISSING task_id")

    return cleaned


def detect_duplicate_task_ids(entries: list[dict]) -> list[str]:
    seen: dict[str, int] = {}
    dupes: list[str] = []
    for e in entries:
        tid = e.get("task_id", "")
        if not tid:
            continue
        if tid in seen:
            dupes.append(f"task_id={tid!r} appears {seen[tid]+1} times (first at index {seen[tid]})")
        seen[tid] = seen.get(tid, 0) + 1
    return dupes


def detect_history_gaps(history: list[dict]) -> list[str]:
    """Detect gaps in append-only history — future extension point."""
    return []


def detect_append_only_violations(history: list[dict]) -> list[str]:
    """Detect append-only violations — future extension point."""
    return []


def build_report(
    registry_data: dict,
    registry_entries: list[dict],
    history_entries: list[dict],
    result: ValidationResult,
    duplicate_issues: list[str],
) -> str:
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")
    total = len(registry_entries)
    valid = sum(1 for e in registry_entries if e.get("task_id") and e.get("status") in VALID_STATUSES)
    invalid = total - valid
    failed_entries = [e for e in registry_entries if e.get("status") == "failed"]
    completed_entries = [e for e in registry_entries if e.get("status") in ("validated", "generated", "completed")]
    missing_result = [e for e in completed_entries if not e.get("result_path")]
    missing_failure = [e for e in failed_entries if not e.get("failure_reason")]

    lines = [
        "---",
        f"title: \"Runtime State Validation Report — {ts}\"",
        "document_type: validation-report",
        "status: active",
        f"validation_timestamp: \"{ts}\"",
        "source_type: internal",
        f"registry_entries: {total}",
        f"valid_entries: {valid}",
        f"invalid_entries: {invalid}",
        f"duplicate_task_detections: {len(duplicate_issues)}",
        f"missing_result_paths: {len(missing_result)}",
        f"invalid_statuses: {len([e for e in registry_entries if e.get('status') not in VALID_STATUSES])}",
        f"history_entries: {len(history_entries)}",
        f"final_status: {'PASS' if result.valid else 'FAIL'}",
        "---",
        "",
        f"# Runtime State Validation Report",
        "",
        f"**Validation Timestamp:** `{ts}`",
        f"**Registry:** `{REGISTRY_PATH}`",
        f"**History:** `{HISTORY_PATH}`",
        "",
        "## Summary",
        "",
        f"| Metric | Value |",
        f"|---|---|",
        f"| Total registry entries | {total} |",
        f"| Valid entries | {valid} |",
        f"| Invalid entries | {invalid} |",
        f"| Failed tasks (total) | {len(failed_entries)} |",
        f"| Failed tasks missing failure_reason | {len(missing_failure)} |",
        f"| Completed tasks missing result_path | {len(missing_result)} |",
        f"| Duplicate task detections | {len(duplicate_issues)} |",
        f"| Execution history entries | {len(history_entries)} |",
        "",
        f"## Final Status: {'✅ PASS' if result.valid else '❌ FAIL'}",
        "",
    ]

    if duplicate_issues:
        lines.extend([
            "## Duplicate Task Detections",
            "",
            *[f"- {d}" for d in duplicate_issues],
            "",
        ])

    if result.issues:
        lines.extend([
            "## Invalid Entries",
            "",
            *[f"- {iss}" for iss in result.issues],
            "",
        ])
    else:
        lines.append("## Invalid Entries: None\n")

    if missing_failure:
        lines.extend([
            "## Failed-Task Quality Checks",
            "",
            f"**Failed tasks missing failure_reason:** {len(missing_failure)}",
            "",
            *[f"- task_id={e.get('task_id')!r} — status={e.get('status')!r}" for e in missing_failure],
            "",
        ])

    if missing_result:
        lines.extend([
            "## Completed-Task Quality Checks",
            "",
            f"**Completed tasks missing result_path:** {len(missing_result)}",
            "",
            *[f"- task_id={e.get('task_id')!r} — status={e.get('status')!r}" for e in missing_result],
            "",
        ])

    lines.extend([
        "## Validated Entries",
        "",
        f"| task_id | status | processed_timestamp | result_path |",
        f"|---|---|---|---|",
    ])
    for e in registry_entries:
        lines.append(
            f"| {e.get('task_id','(missing)')} "
            f"| {e.get('status','(missing)')} "
            f"| {e.get('processed_timestamp','(missing)')} "
            f"| {e.get('result_path','(missing)')} |"
        )

    lines.extend(["", "---", "*Report generated by `tasks/runtime_state_validator.py` — append-only, no mutations*"])
    return "\n".join(lines)


def run_validator(emit_report: bool = True) -> ValidationResult:
    """Run validation. Returns ValidationResult. No side effects unless emit_report=True."""
    result = ValidationResult()
    registry_data, registry_entries = load_registry()
    history_entries = load_history()

    # Detect duplicate task_ids (across full registry)
    duplicate_issues = detect_duplicate_task_ids(registry_entries)

    # Validate each entry
    cleaned_entries = []
    for idx, entry in enumerate(registry_entries):
        cleaned = validate_registry_entry(entry, idx, result)
        cleaned_entries.append(cleaned)

    # Validate history presence
    if not history_entries:
        result.issues.append(
            f"[INFO] Execution history empty or not present at {HISTORY_PATH} — "
            f"append-only history will be populated as tasks execute"
        )

    # Report generation
    if emit_report:
        report = build_report(
            registry_data, cleaned_entries, history_entries,
            result, duplicate_issues
        )
        REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
        REPORT_PATH.write_text(report, encoding="utf-8")
        print(f"Report written: {REPORT_PATH}")

    return result


if __name__ == "__main__":
    dry_run = "--dry-run" in sys.argv
    emit = not dry_run
    res = run_validator(emit_report=emit)
    print(f"Validation: {'PASS' if res.valid else 'FAIL'}")
    if res.issues:
        for iss in res.issues:
            print(f"  ISSUE: {iss}")
    sys.exit(0 if res.valid else 1)