---
title: "Wolfpack Review Runner — Operational Runbook"
document_type: "document"
status: "active"
version: "0.1"
created: "2026-05-23"
updated: "2026-05-23"
source_type: "internal"
provenance: "wolfpack-institutional-memory"
tags:
  - "wolfpack"
related_ids:
  - "task_002"
  - "task_001"
append_only: false
---
# Wolfpack Review Runner — Operational Runbook

**Effective:** 2026-05-23
**Version:** 1.0

---

## 1. Purpose

The `wolfpack_review_runner.py` is a deterministic, machine-executable workflow state processor for wolfpack_review tasks. It:

- Scans `tasks/inbox/` for pending task files
- Validates required fields and workflow structure
- Extracts structured metadata
- Generates result files with deterministic timestamps
- Updates `tasks/processed_registry.json` (append-only)
- Emits observable timestamped console logs

**The runner is NOT an autonomous intelligence system.** It cannot reason, deploy, call external APIs, or self-modify.

---

## 2. When to Use This Workflow

Use the wolfpack_review runner when:

- A task file exists in `tasks/inbox/` matching the required format
- You need deterministic, observable, governance-preserving workflow processing
- You want to reduce Human API involvement in task validation and status tracking
- Audit trail and replayability are required

Do NOT use this runner for:
- Autonomous decision making
- External API calls or network operations
- Code deployment or git operations
- Any task requiring AI inference or judgment

---

## 3. Required Input File Format

Task files must be placed in `tasks/inbox/` as `.md` files with the following structure:

```markdown
**Task ID:** task_XXX
**Timestamp:** YYYY-MM-DDTHH:MM:SSZ
**Status:** pending_review
**Workflow Type:** wolfpack_review
**Requested Outputs:** [list of outputs]

## Proposal Summary

[Description of the proposed change]

## Motivation

[Why this change is needed]

## Scope

### Files Allowed
- [list of files that may be modified]

### Files Forbidden
- [list of files that must not be modified]

## Risk Level

low | medium | high | critical

## Rollback Target

[commit hash of known-good state]

## Validation Commands

```bash
[exact commands to validate preflight]
```

## Expected Outputs

1. [output 1]
2. [output 2]
```

**Required Fields:**
| Field | Format |
|---|---|
| Task ID | `task_NNN` (e.g., task_002) |
| Timestamp | ISO-8601 UTC (e.g., 2026-05-23T04:30:00Z) |
| Status | `pending_review` |
| Workflow Type | `wolfpack_review` |
| Requested Outputs | Comma-separated or bulleted list |
| Proposal Summary | Markdown h2 section |
| Rollback Target | Commit hash |
| Validation Commands | Code block with exact commands |

---

## 4. Command to Run

```bash
cd /home/node/.openclaw/workspace/wolfpack-institutional-memory
python3 tasks/wolfpack_review_runner.py
```

**Exit codes:**
- `0` — All tasks processed, no failures
- `1` — One or more tasks failed validation or processing

---

## 5. Expected Outputs

### Console Logs (stdout)

Each execution produces timestamped logs:

```
[YYYY-MM-DDTHH:MM:SSZ] WORKFLOW=wolfpack_review_runner_v1 TASK=task_XXX EVENT=stage1_discovered PATH=...
[YYYY-MM-DDTHH:MM:SSZ] WORKFLOW=wolfpack_review_runner_v1 TASK=task_XXX EVENT=stage2_validated RESULT=valid
[YYYY-MM-DDTHH:MM:SSZ] WORKFLOW=wolfpack_review_runner_v1 TASK=task_XXX EVENT=stage3_extracted TASK_ID=task_XXX
[YYYY-MM-DDTHH:MM:SSZ] WORKFLOW=wolfpack_review_runner_v1 TASK=task_XXX EVENT=stage4_template_check RESULT=found|not_found
[YYYY-MM-DDTHH:MM:SSZ] WORKFLOW=wolfpack_review_runner_v1 TASK=task_XXX EVENT=stage5_generated RESULT_PATH=...
[YYYY-MM-DDTHH:MM:SSZ] WORKFLOW=wolfpack_review_runner_v1 TASK=task_XXX EVENT=stage6_registry_updated REGISTRY=processed_registry.json
[YYYY-MM-DDTHH:MM:MM:SSZ] WORKFLOW=wolfpack_review_runner_v1 TASK=task_XXX EVENT=completed RESULT_PATH=...
[YYYY-MM-DDTHH:MM:SSZ] WORKFLOW=wolfpack_review_runner_v1 TASK=summary EVENT=workflow_complete DISCOVERED=N VALIDATED=N GENERATED=N FAILED=N
```

### Result File

Generated at `tasks/results/{task_id}_RESULT_{status}_{timestamp}.md`

Contains:
- Task ID, Workflow Type, Source Timestamp, Processed Timestamp, Status
- Validation Result
- Proposal Reference
- Machine-generated provenance footer

### Registry Entry

`tasks/processed_registry.json` receives one append entry per task:

```json
{
  "task_id": "task_001",
  "workflow_type": "wolfpack_review",
  "created_timestamp": "2026-05-23T03:47:00Z",
  "processed_timestamp": "2026-05-23T04:30:00Z",
  "status": "validated",
  "result_path": "tasks/results/task_001_RESULT_validated_20260523T043000Z.md",
  "validation_result": "valid"
}
```

---

## 6. Registry Behavior

- **Location:** `tasks/processed_registry.json`
- **Updates:** Append-only — never overwrite existing entries
- **Duplicates:** Already-processed tasks are skipped (by task_id lookup)
- **Format:** Valid JSON, UTF-8, indented with 2 spaces
- **Governance:** Registry is institutional operational state — preserved for auditability, replayability, and workflow lineage

---

## 7. Failure Handling

| Failure Type | Behavior |
|---|---|
| Invalid task file | Logged with missing fields, registry entry with status `failed` |
| Template not found | Stage 4 noted as `not_found`, processing continues |
| Result file write failure | Failure logged, registry updated with reason, runner continues |
| Registry write failure | Failure logged, runner halts gracefully with exit code 1 |
| Already processed | Skipped, logged as `skipped_already_processed` |

**No partial corruption:** Runner uses atomic write pattern (write to temp, then rename where supported).

**Failure log format:**
```
[YYYY-MM-DDTHH:MM:SSZ] WORKFLOW=wolfpack_review_runner_v1 TASK=task_XXX EVENT=failed REASON=validation_failed:missing:field_name
```

---

## 8. Append-Only Rule

The processed_registry.json is **append-only**:

- New entries are added to the `entries` array
- Existing entries are never modified or deleted
- A failed entry remains as a permanent audit record
- Result files are generated once with deterministic timestamp in filename — not overwritten

This preserves:
- **Auditability** — every processing attempt is recorded
- **Replayability** — registry allows reconstruction of processing history
- **Workflow lineage** — task_id → workflow_type → result_path chain is unbroken

---

## 9. What NOT to Do

The runner enforces strict constraints. It must NOT:

| Forbidden Action | Reason |
|---|---|
| Call external APIs | No network access by design |
| Execute shell commands | No subprocess execution |
| Push to GitHub | No deployment capability |
| Perform autonomous reasoning | Deterministic only — no AI inference |
| Modify task files | Read-only processing |
| Overwrite registry entries | Append-only enforcement |
| Call GitHub API | No github.com API calls |
| Self-modify | Runner is static — no self-modification |
| Bypass governance | All actions are observable and logged |

---

## 10. Definition of Done

A wolfpack_review runner execution is complete when:

- [ ] All tasks in `tasks/inbox/` have been processed
- [ ] Each task has a corresponding entry in `processed_registry.json`
- [ ] Each valid task has a result file in `tasks/results/`
- [ ] All logs show completed stages (stage1 through stage7)
- [ ] Summary line shows `FAILED=0` for clean execution
- [ ] Registry JSON is valid and parseable
- [ ] No partial files written (atomic or clean completion)

---

## Quick Reference

```bash
# Run the workflow
cd /home/node/.openclaw/workspace/wolfpack-institutional-memory
python3 tasks/wolfpack_review_runner.py

# Check registry
cat tasks/processed_registry.json | python3 -m json.tool

# Check results directory
ls -la tasks/results/

# View logs (last run)
python3 tasks/wolfpack_review_runner.py 2>&1
```

---

*Runbook: `operations/WOLFPACK_REVIEW_RUNBOOK.md`*
*Runner: `tasks/wolfpack_review_runner.py`*
*Registry: `tasks/processed_registry.json`*
