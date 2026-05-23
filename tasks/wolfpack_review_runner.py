#!/usr/bin/env python3
"""
wolfpack_review_runner.py
=========================
Deterministic workflow state processor for wolfpack_review tasks.

PURPOSE: Machine-executable workflow state manager — NOT an autonomous intelligence system.
  - reduce Human API
  - standardize workflow execution
  - preserve observability
  - preserve governance
  - preserve auditability
  - preserve institutional continuity

MUST NOT:
  - perform autonomous reasoning
  - generate hidden chain-of-thought
  - autonomously deploy
  - autonomously modify doctrine
  - call external APIs
  - self-modify
  - bypass governance
  - create hidden state

USES: Python standard library only. No third-party dependencies.
"""

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

# =============================================================================
# CONFIGURATION — Hardcoded paths for deterministic behavior
# =============================================================================

REPO_ROOT = Path(__file__).resolve().parents[1]
TASKS_DIR = REPO_ROOT / "tasks"
INBOX_DIR = TASKS_DIR / "inbox"
RESULTS_DIR = TASKS_DIR / "results"
PROCESSED_REGISTRY = TASKS_DIR / "processed_registry.json"
TEMPLATE_MARKER = "_RESULT_TEMPLATE.md"

# Required fields in task files
REQUIRED_FIELDS = ["task_id", "workflow_type", "proposal", "requested_outputs"]
REQUIRED_WORKFLOW_TYPE = "wolfpack_review"

# Status values
STATUS_DISCOVERED = "discovered"
STATUS_VALIDATED = "validated"
STATUS_GENERATED = "generated"
STATUS_FAILED = "failed"

# =============================================================================
# LOGGING — Observable console logs with deterministic format
# =============================================================================

def log(workflow_id: str, task_id: str, event: str, detail: str = "") -> None:
    """Emit deterministic timestampped log line."""
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    log_line = f"[{timestamp}] WORKFLOW={workflow_id} TASK={task_id} EVENT={event} {detail}"
    print(log_line, flush=True)


def log_failure(workflow_id: str, task_id: str, reason: str) -> None:
    """Emit deterministic failure log line."""
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    print(f"[{timestamp}] WORKFLOW={workflow_id} TASK={task_id} EVENT=failed REASON={reason}", flush=True)


# =============================================================================
# STAGE 1 — TASK DISCOVERY
# =============================================================================

def discover_tasks() -> list[Path]:
    """
    Discover all pending task files in inbox.
    Returns list of Path objects for .md files not yet processed.
    """
    if not INBOX_DIR.exists():
        return []
    task_files = list(INBOX_DIR.glob("*.md"))
    # Filter out template files
    task_files = [f for f in task_files if TEMPLATE_MARKER not in f.name]
    return sorted(task_files)


# =============================================================================
# STAGE 2 — TASK VALIDATION
# =============================================================================

def strip_markdown(text: str) -> str:
    """Strip markdown bold/italic formatting for field matching."""
    return text.replace("**", "").replace("*", "").replace("#", "").strip()

def validate_task_file(path: Path) -> tuple[bool, list[str]]:
    """
    Validate task file structure.
    Returns (is_valid, list_of_missing_fields).
    """
    missing = []
    try:
        content = path.read_text(encoding="utf-8")
    except Exception as e:
        return False, [f"read_error:{e}"]

    # Normalize content for matching: strip markdown formatting
    normalized = strip_markdown(content)

    # Normalize underscores to spaces for field matching (task_id -> task id)
    normalized_for_check = normalized.lower().replace("_", " ")

    # Check required fields exist in content (case-insensitive on normalized)
    for field in REQUIRED_FIELDS:
        marker = field.replace("_", " ").title()
        # Check both exact field name and title-case marker
        if field.lower() not in normalized_for_check and marker.lower() not in normalized_for_check:
            missing.append(field)

    # Validate workflow type is wolfpack_review
    workflow_type_found = False
    for line in content.splitlines():
        line_lower = line.strip().lower()
        # Look for workflow type line with "wolfpack_review"
        if "workflow" in line_lower and "type" in line_lower:
            if REQUIRED_WORKFLOW_TYPE in line_lower:
                workflow_type_found = True
            break

    if not workflow_type_found and "workflow_type" in missing:
        missing.append("workflow_type_validation")

    return len(missing) == 0, missing


def load_registry() -> dict:
    """Load processed registry. Returns empty dict if file missing or invalid."""
    if not PROCESSED_REGISTRY.exists():
        return {"entries": []}
    try:
        content = PROCESSED_REGISTRY.read_text(encoding="utf-8")
        return json.loads(content)
    except Exception:
        return {"entries": []}


def is_already_processed(task_id: str) -> bool:
    """Check if task already appears in processed registry."""
    registry = load_registry()
    for entry in registry.get("entries", []):
        if entry.get("task_id") == task_id:
            return True
    return False


# =============================================================================
# STAGE 3 — METADATA EXTRACTION
# =============================================================================

def extract_metadata(path: Path) -> dict:
    """
    Extract structured metadata from task file.
    Returns dict with: task_id, workflow_type, created_timestamp, status
    """
    metadata = {
        "task_id": None,
        "workflow_type": None,
        "created_timestamp": None,
        "status": None,
        "source_path": str(path),
    }

    try:
        content = path.read_text(encoding="utf-8")
    except Exception:
        return metadata

    lines = content.splitlines()
    for line in lines:
        line_stripped = line.strip()
        # Strip markdown bold/italic for field matching
        line_clean = line_stripped.replace("**", "").replace("*", "").strip()
        line_lower = line_clean.lower()

        if line_lower.startswith("task id"):
            parts = line_clean.split(":", 1)
            if len(parts) == 2:
                metadata["task_id"] = parts[1].strip()
        elif line_lower.startswith("workflow type"):
            parts = line_clean.split(":", 1)
            if len(parts) == 2:
                metadata["workflow_type"] = parts[1].strip()
        elif line_lower.startswith("timestamp"):
            parts = line_clean.split(":", 1)
            if len(parts) == 2:
                metadata["created_timestamp"] = parts[1].strip()
        elif line_lower.startswith("status"):
            parts = line_clean.split(":", 1)
            if len(parts) == 2:
                metadata["status"] = parts[1].strip()

    return metadata


# =============================================================================
# STAGE 4 — TEMPLATE LOADING
# =============================================================================

def find_result_template(task_id: str) -> Path | None:
    """
    Find existing result template for given task_id.
    Returns Path or None.
    """
    expected_name = f"{task_id}{TEMPLATE_MARKER}.md"
    expected_path = RESULTS_DIR / expected_name
    if expected_path.exists():
        return expected_path
    # Fallback: search
    for p in RESULTS_DIR.glob(f"{task_id}{TEMPLATE_MARKER}.md"):
        return p
    return None


# =============================================================================
# STAGE 5 — RESULT GENERATION
# =============================================================================

def generate_result_path(task_id: str, status: str) -> Path:
    """
    Generate deterministic result path.
    Format: tasks/results/{task_id}_RESULT_{status}_{timestamp}.md
    """
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    filename = f"{task_id}_RESULT_{status}_{timestamp}.md"
    return RESULTS_DIR / filename


def generate_result_file(metadata: dict, validation_result: str) -> tuple[Path | None, str]:
    """
    Generate result file from task metadata.
    Returns (result_path, failure_reason_or_empty_string).
    """
    task_id = metadata.get("task_id") or "unknown"
    workflow_type = metadata.get("workflow_type") or "unknown"
    created_ts = metadata.get("created_timestamp") or "unknown"

    # Find the source task path for proposal content
    source_path = metadata.get("source_path")
    proposal_text = ""
    if source_path:
        try:
            content = Path(source_path).read_text(encoding="utf-8")
            # Extract proposal section
            in_proposal = False
            for line in content.splitlines():
                if line.strip().lower().startswith("## proposal"):
                    in_proposal = True
                    continue
                if in_proposal and line.startswith("## "):
                    in_proposal = False
                if in_proposal:
                    proposal_text += line + "\n"
        except Exception:
            proposal_text = "[proposal extraction failed]"

    # Build result content
    processed_ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    result_lines = [
        f"# Task {task_id} Result — Workflow Processing Record",
        "",
        f"**Task ID:** {task_id}",
        f"**Workflow Type:** {workflow_type}",
        f"**Source Timestamp:** {created_ts}",
        f"**Processed Timestamp:** {processed_ts}",
        f"**Status:** {STATUS_VALIDATED}",
        "",
        "---",
        "",
        "## Workflow Processing Record",
        "",
        f"**Validation Result:** {validation_result}",
        "",
        "## Proposal Reference",
        "",
        proposal_text.strip(),
        "",
        "---",
        "",
        "*Generated by: wolfpack_review_runner.py*",
        "*This file is machine-generated. Manual edits must preserve append-only integrity.*",
    ]

    result_path = generate_result_path(task_id, STATUS_VALIDATED)
    try:
        RESULTS_DIR.mkdir(parents=True, exist_ok=True)
        result_path.write_text("\n".join(result_lines), encoding="utf-8")
        return result_path, ""
    except Exception as e:
        return None, f"write_error:{e}"


# =============================================================================
# STAGE 6 — REGISTRY UPDATE
# =============================================================================

def append_registry_entry(metadata: dict, validation_result: str, result_path: Path | None, failure_reason: str) -> tuple[bool, str]:
    """
    Append entry to processed_registry.json.
    Append-only: never overwrites existing entries.
    Returns (success, failure_reason_or_empty_string).
    """
    registry = load_registry()

    task_id = metadata.get("task_id") or "unknown"
    processed_ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    # Determine status
    if failure_reason:
        status = STATUS_FAILED
    elif result_path:
        status = STATUS_VALIDATED
    else:
        status = STATUS_FAILED
        failure_reason = failure_reason or "unknown_failure"

    new_entry = {
        "task_id": task_id,
        "workflow_type": metadata.get("workflow_type") or "unknown",
        "created_timestamp": metadata.get("created_timestamp") or "unknown",
        "processed_timestamp": processed_ts,
        "status": status,
        "result_path": str(result_path) if result_path else None,
        "validation_result": validation_result,
    }

    if failure_reason:
        new_entry["failure_reason"] = failure_reason

    # Append-only: add new entry
    if "entries" not in registry:
        registry["entries"] = []
    registry["entries"].append(new_entry)

    # Write back — preserve UTF-8
    try:
        PROCESSED_REGISTRY.write_text(
            json.dumps(registry, indent=2, ensure_ascii=False),
            encoding="utf-8"
        )
        return True, ""
    except Exception as e:
        return False, f"registry_write_error:{e}"


# =============================================================================
# STAGE 7 — COMPLETION LOGGING
# =============================================================================

def log_completion(workflow_id: str, task_id: str, result_path: Path | None) -> None:
    """Log successful completion."""
    result_str = str(result_path) if result_path else "none"
    log(workflow_id, task_id, "completed", f"RESULT_PATH={result_str}")


# =============================================================================
# MAIN WORKFLOW ORCHESTRATOR
# =============================================================================

def run_workflow() -> dict:
    """
    Execute full deterministic workflow.
    Returns summary dict for observability.
    """
    workflow_id = "wolfpack_review_runner_v1"
    summary = {
        "workflow_id": workflow_id,
        "discovered": 0,
        "validated": 0,
        "generated": 0,
        "failed": 0,
        "results": [],
    }

    # Stage 1: Discovery
    task_files = discover_tasks()
    summary["discovered"] = len(task_files)
    log(workflow_id, "none", "stage1_discovered", f"COUNT={len(task_files)}")

    for task_file in task_files:
        task_id = task_file.stem
        log(workflow_id, task_id, "stage1_discovered", f"PATH={task_file}")

        # Skip if already processed
        if is_already_processed(task_id):
            log(workflow_id, task_id, "skipped_already_processed", "")
            continue

        # Stage 2: Validation
        is_valid, missing = validate_task_file(task_file)
        validation_result = "valid" if is_valid else f"missing:{','.join(missing)}"
        log(workflow_id, task_id, "stage2_validated", f"RESULT={validation_result}")

        if not is_valid:
            # Failure path: log, record, continue
            log_failure(workflow_id, task_id, f"validation_failed:{validation_result}")
            metadata = extract_metadata(task_file)
            append_registry_entry(metadata, validation_result, None, f"validation_failed:{validation_result}")
            summary["failed"] += 1
            summary["results"].append({"task_id": task_id, "status": STATUS_FAILED, "reason": validation_result})
            continue

        # Stage 3: Metadata extraction
        metadata = extract_metadata(task_file)
        extracted_task_id = metadata.get("task_id")
        log(workflow_id, task_id, "stage3_extracted", f"TASK_ID={extracted_task_id}")

        # Stage 4: Template check
        template_path = find_result_template(task_id)
        log(workflow_id, task_id, "stage4_template_check", f"RESULT={'found' if template_path else 'not_found'}")

        # Stage 5: Result generation
        result_path, gen_failure = generate_result_file(metadata, validation_result)
        if gen_failure:
            log_failure(workflow_id, task_id, f"generation_failed:{gen_failure}")
            append_registry_entry(metadata, validation_result, None, gen_failure)
            summary["failed"] += 1
            summary["results"].append({"task_id": task_id, "status": STATUS_FAILED, "reason": gen_failure})
            continue

        log(workflow_id, task_id, "stage5_generated", f"RESULT_PATH={result_path}")

        # Stage 6: Registry update
        reg_success, reg_failure = append_registry_entry(metadata, validation_result, result_path, "")
        if reg_failure:
            log_failure(workflow_id, task_id, f"registry_update_failed:{reg_failure}")
            summary["failed"] += 1
            summary["results"].append({"task_id": task_id, "status": STATUS_FAILED, "reason": reg_failure})
            continue

        log(workflow_id, task_id, "stage6_registry_updated", f"REGISTRY={PROCESSED_REGISTRY.name}")

        # Stage 7: Completion
        log_completion(workflow_id, task_id, result_path)
        summary["validated"] += 1
        summary["generated"] += 1
        summary["results"].append({"task_id": task_id, "status": STATUS_VALIDATED, "result_path": str(result_path)})

    # Final summary log
    log(workflow_id, "summary", "workflow_complete",
        f"DISCOVERED={summary['discovered']} VALIDATED={summary['validated']} GENERATED={summary['generated']} FAILED={summary['failed']}")

    return summary


# =============================================================================
# ENTRY POINT
# =============================================================================

if __name__ == "__main__":
    summary = run_workflow()
    # Exit code: 0 if no failures, 1 if any failures
    sys.exit(0 if summary["failed"] == 0 else 1)
