---
title: "Execution Resume Manifest — Wolfpack Workflow Recovery"
document_type: "manifest"
status: "active"
version: "0.1"
created: "2026-05-24"
updated: "2026-05-24"
source_type: "internal"
provenance: "wolfpack-institutional-memory"
tags:
  - "wolfpack"
  - "workflow-recovery"
  - "manifest"
  - "governance"
related_ids:
  - "SESSION_RECOVERY_PROTOCOL"
  - "SESSION_RECOVERY_CHECKLIST"
append_only: false
---
# Execution Resume Manifest

**Version:** 0.1 | **Status:** Active | **Created:** 2026-05-24

---

## Purpose

The Execution Resume Manifest is a machine-readable + human-readable document created at workflow interruption time. It records the complete state required to resume execution without human re-explanation.

It is NOT a scratch pad. It is a governed artifact stored in the repository that survives session death.

---

## Manifest Schema

```yaml
resume_id:           # Required. Unique ID for this recovery event. Format: RSMP-<YYYYMMDD>-<NNN>
workflow_id:         # Required. The workflow being resumed (e.g., OVL-20260524-003)
repo_path:           # Required. Absolute path to repo root
current_phase:       # Required. Named phase from TASK_STATE_MODEL.md (e.g., conflict_classification)
last_known_commit:   # Required. Git commit hash of last completed action
target_files:        # Required. List of files this workflow creates/modifies
required_context_files: # Required. Files that must exist and be read to resume
prohibited_actions:  # Required. Actions explicitly forbidden during this workflow
validation_commands: # Required. List of bash commands to validate safe resumption
completion_conditions: # Required. List of conditions that define "done"
recovery_note:       # Optional. Human-readable note explaining interruption
created_by:          # Required. Agent identifier
created_timestamp:   # Required. ISO-8601 UTC
```

---

## Field Definitions

### resume_id
Format: `RSMP-YYYYMMDD-NNN`  
Example: `RSMP-20260524-001`  
Uniquely identifies this recovery event. Multiple resumes of the same workflow get incrementing NNN.

### workflow_id
The workflow identifier from the triggering governance artifact.  
Examples: `OVL-20260524-003`, `task_002`, `dec-001`

### repo_path
Absolute filesystem path to the repository root.  
Value: `/home/node/.openclaw/workspace/wolfpack-institutional-memory`

### current_phase
Named phase from `runtime/TASK_STATE_MODEL.md`.  
Valid values: `discovery`, `validation`, `generation`, `review`, `approval`, `implementation`, `archival`

### last_known_commit
Full 40-character git SHA of the last commit that successfully advanced the workflow.  
Obtain with: `git rev-parse HEAD`

### target_files
Array of file paths (relative to repo root) that this workflow creates or modifies.  
Used for duplicate prevention and working-tree reconciliation.

### required_context_files
Array of file paths that MUST exist and be read before resuming.  
If any are missing, the agent cannot safely resume and must HALT.

### prohibited_actions
Array of action descriptions explicitly forbidden during this workflow.  
Examples: "Do not modify canon/ files", "Do not push to origin until DEC approval"

### validation_commands
Array of bash commands (as strings) that must return exit code 0 before resumption.  
Example: `["python3 tasks/runtime_state_validator.py", "git status --porcelain"]`

### completion_conditions
Human-readable list of conditions that, when ALL true, mean the workflow is complete.  
Used to determine when to stop recovering and report done.

---

## Example Manifest

```yaml
resume_id: RSMP-20260524-001
workflow_id: OVL-20260524-003
repo_path: /home/node/.openclaw/workspace/wolfpack-institutional-memory
current_phase: conflict_classification
last_known_commit: 7a3715d complete HIGH-risk conflict mapping for OVL-20260524-003
target_files:
  - governance/reviews/OVL-20260524-003_REVIEW.md
  - governance/reviews/OVL-20260524-003_CONFLICT_MAPPING.md
  - HIGH_RISK_CONFLICT_REGISTRY.md
  - OVERLAY_REVIEW_QUEUE.md
required_context_files:
  - governance/DOCTRINE_OVERLAY_RECONCILIATION_STANDARD.md
  - governance/HIGH_RISK_OVERLAY_ESCALATION_STANDARD.md
  - runtime/TASK_STATE_MODEL.md
  - runtime/SESSION_RECOVERY_PROTOCOL.md
prohibited_actions:
  - Do not modify canon/ files
  - Do not make DEC escalation decision without human approval
  - Do not commit overlay review until conflict classification is complete
validation_commands:
  - python3 tasks/runtime_state_validator.py
  - git status --porcelain
completion_conditions:
  - All 7 conflict classifications (CD/CI/CG/CP/CS/CE/CT/CU) complete
  - OVL-20260524-003_CONFLICT_MAPPING.md generated and reviewed
  - HIGH_RISK_CONFLICT_REGISTRY.md updated
  - OVERLAY_REVIEW_QUEUE.md updated
  - DEC escalation decision documented (or waived)
  - runtime_state_validator.py returns PASS
recovery_note: Session amnesia during OVL-20260524-003 conflict classification. Human re-provided repo path and workflow context.
created_by: openclaw-agent
created_timestamp: 2026-05-24T14:30:00Z
```

---

## Lifecycle Rules

1. **Creation:** Manifest is created at interruption time by the agent, committed immediately to preserve state
2. **Storage:** Saved as `runtime/resume/RSMP-<id>.md` in the repo
3. **Retrieval:** Next agent session reads manifest to reconstruct state before any action
4. **Completion:** When workflow completes, manifest is moved to `archive/` with `status: completed`
5. **Duplicate prevention:** If a manifest for the same `workflow_id` already exists and is not completed, HALT — concurrent recovery may be active

---

## Related Files

- `runtime/SESSION_RECOVERY_PROTOCOL.md` — full protocol
- `runtime/SESSION_RECOVERY_CHECKLIST.md` — bootstrap checklist

---

*Append-only. Schema changes require Wolfpack governance approval.*