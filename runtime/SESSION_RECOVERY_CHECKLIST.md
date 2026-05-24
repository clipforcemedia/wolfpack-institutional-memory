---
title: "Session Recovery Checklist — Wolfpack Agentic Execution"
document_type: "checklist"
status: "active"
version: "0.1"
created: "2026-05-24"
updated: "2026-05-24"
source_type: "internal"
provenance: "wolfpack-institutional-memory"
tags:
  - "wolfpack"
  - "session-recovery"
  - "checklist"
  - "governance"
related_ids:
  - "SESSION_RECOVERY_PROTOCOL"
  - "EXECUTION_RESUME_MANIFEST"
append_only: false
---
# Session Recovery Checklist

**Version:** 0.1 | **Status:** Active | **Created:** 2026-05-24

> Execute this checklist before resuming ANY interrupted workflow. Each step is required. Do not skip steps. Do not proceed past a failed step without resolution.

---

## Pre-Flight: Repo Verification

### Step 1 — Verify Repo Path
```bash
git rev-parse --show-toplevel
```
**Expected:** Absolute path to the wolfpack repository root  
**Fail:** Path does not end in `wolfpack-institutional-memory` → STOP, confirm correct path with human

### Step 2 — Verify Current Branch
```bash
git branch --show-current
```
**Expected:** `main` or approved workflow branch  
**Fail:** Detached HEAD → STOP, determine last known commit before proceeding

### Step 3 — Verify Git Remote
```bash
git remote -v
```
**Expected:** `origin` pointing to `clipforcemedia/wolfpack-institutional-memory`  
**Fail:** Wrong remote → STOP, do not push to unknown remote

### Step 4 — Pull Latest State
```bash
git pull origin $(git branch --show-current)
```
**Expected:** Already up to date or fast-forward merge  
**Fail:** Merge conflict → STOP, do not force-merge, escalate to human

---

## State Inspection

### Step 5 — Check Git Status
```bash
git status
```
**Expected:** Clean or only expected uncommitted governance files  
**Fail:** Canon files modified → **HALT**, do not proceed

### Step 6 — Inspect Recent Commits
```bash
git log --oneline -10
```
**Expected:** Consistent commit chain with expected workflow IDs  
**Fail:** Unexpected commits → STOP, inspect commit diffs before proceeding

### Step 7 — Inspect Unstaged Changes
```bash
git diff --stat
```
**Expected:** Only governance/runtime files changed  
**Fail:** Canon files in diff → **HALT**, do not proceed

### Step 8 — Inspect Target Workflow Files
```bash
# Verify workflow-specific files exist before proceeding
# Example for OVL workflows:
ls governance/reviews/OVL-XXXXXXXX-XXX_REVIEW.md
ls runtime/EXECUTION_HISTORY.jsonl
ls tasks/processed_registry.json
```
**Expected:** All referenced files present  
**Fail:** Missing file → STOP, determine last known state before proceeding

---

## Validation

### Step 9 — Run runtime_state_validator.py
```bash
python3 tasks/runtime_state_validator.py
```
**Expected:** Output `Validation: PASS`, exit code 0  
**Fail:** Output `Validation: FAIL` or non-zero exit → **HALT**, resolve all reported issues before proceeding

### Step 10 — Inspect Execution History
```bash
tail -5 runtime/EXECUTION_HISTORY.jsonl
```
**Expected:** Last entry reflects the workflow being resumed  
**Fail:** Empty or contradictory → STOP, read full history to reconstruct last state

### Step 11 — Inspect Processed Registry
```bash
python3 -c "import json; r=json.load(open('tasks/processed_registry.json')); print(json.dumps(r['entries'][-3:], indent=2))"
```
**Expected:** Last 3 entries show expected task statuses  
**Fail:** Duplicate task_id detected → **HALT**, do not re-execute

---

## Duplicate Prevention

### Step 12 — Confirm No Duplicate Artifacts
```bash
# Check for duplicate overlay review files
ls governance/reviews/ | sort | uniq -d
```
**Expected:** No duplicate filenames  
**Fail:** Duplicates detected → **HALT**, review and resolve before proceeding

---

## Safe Action Gate

### Step 13 — Determine Next Safe Action

Based on all checks above:

| All Checks Pass | Decision |
|---|---|
| ✅ YES | → Proceed with workflow resumption per EXECUTION_RESUME_MANIFEST.md |
| ❌ NO | → Report findings to human, wait for direction |
| ⚠️ PARTIAL | → Document what is unknown, ask human for clarification |

---

## Completion

After recovery completes, append to EXECUTION_HISTORY.jsonl:
```json
{"event": "session_recovery", "timestamp": "<ISO-8601>", "checks_passed": true/false, "resumed_workflow_id": "<id>"}
```

---

## Related Files

- `runtime/SESSION_RECOVERY_PROTOCOL.md` — full protocol
- `runtime/EXECUTION_RESUME_MANIFEST.md` — manifest format for resumable workflows

---

*Append-only. Checklist changes require Wolfpack governance approval.*