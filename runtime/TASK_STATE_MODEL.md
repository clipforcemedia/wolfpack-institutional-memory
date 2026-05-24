---
title: "Task State Model — Deterministic Task Execution State Machine"
document_type: "state-machine"
status: "active"
version: "1.0"
created: "2026-05-24"
updated: "2026-05-24"
source_type: "internal"
provenance:
  source: "wolfpack-institutional-memory"
  source_type: "internal"
  ingested_by: "Eterna / Wolfpack"
  ingest_date: "2026-05-24"
  batch: "STAGE_1_BATCH_002B"
tags:
  - "runtime"
  - "task"
  - "state-machine"
  - "deterministic"
  - "batch-002"
related_ids:
  - "runtime/RUNTIME_STATE_GOVERNANCE.md"
  - "runtime/WORKER_LIFECYCLE.md"
  - "operations/INCIDENT_LOG.md"
append_only: true
---

# Task State Model — Deterministic Task Execution State Machine

> **Source:** Wolfpack institutional memory — runtime state governance layer  
> **Status:** Active — Canonical State Machine  
> **Activation Date:** 2026-05-24  
> **Governs:** All deterministic task execution in the Wolfpack system

---

## Overview

This document defines the formal state machine for all tasks executed by the Wolfpack deterministic execution system. Each task transitions through defined states in response to worker events and governance decisions. No state transitions outside this model are permitted.

**States:** `pending` → `claimed` → `in_progress` → `completed` / `failed` / `blocked` / `skipped_already_processed` / `archived`

**See also:** [Runtime State Governance](./RUNTIME_STATE_GOVERNANCE.md) — Full governance standards  
**See also:** [Worker Lifecycle](./WORKER_LIFECYCLE.md) — Worker state machine

---

## State Definitions

### `pending`

**Definition:** Task is in the queue and available for a worker to claim.

| Property | Value |
|---|---|
| **Task ownership** | None — task is available for claim |
| **Lease status** | No active lease |
| **Entry events** | Task created; task returned from `claimed` (lease expired); task returned from `failed` (retry) |
| **Exit events** | Worker claims task → `claimed`; worker checks and finds already processed → `skipped_already_processed` |

**While in `pending`, the following are prohibited:**
- No worker may execute actions on the task without a formal claim
- No modification to task specification
- No state transitions except `claimed` or `skipped_already_processed`

**Valid transitions:** `pending` → `claimed`, `pending` → `skipped_already_processed`

---

### `claimed`

**Definition:** A worker has claimed the task and holds the lease. The task is under exclusive ownership.

| Property | Value |
|---|---|
| **Task ownership** | Exclusive — assigned worker holds the lease |
| **Lease duration** | Configured per task type (default: one task cycle) |
| **Entry events** | Worker submits claim, claim registered in task queue |
| **Exit events** | Pre-flight validation passed → `in_progress`; validation failed → `failed`; lease expired without claim confirmation → `pending` |

**While in `claimed`, the following are required:**
- Worker must complete pre-flight validations within the lease period
- Worker must send heartbeat every 60 seconds
- Worker must not transfer the claim to another worker

**Valid transitions:** `claimed` → `in_progress`, `claimed` → `failed`, `claimed` → `pending`

---

### `in_progress`

**Definition:** The worker is actively executing the task actions as defined in the task specification.

| Property | Value |
|---|---|
| **Task ownership** | Exclusive — assigned worker is actively executing |
| **Heartbeat** | Every 60 seconds (worker-side) |
| **Entry events** | Pre-flight validations passed, worker begins action execution |
| **Exit events** | All actions completed successfully → `completed`; action failed → `failed`; lease expired → `pending` (abandoned) |

**While in `in_progress`, the following are required:**
- Worker must write progress entries to execution history at each milestone
- Worker must maintain heartbeat every 60 seconds
- Worker must not create hidden state (per Runtime State Governance §11)
- Worker must not modify the task specification

**Valid transitions:** `in_progress` → `completed`, `in_progress` → `failed`, `in_progress` → `pending`

---

### `completed`

**Definition:** The task has been fully and successfully executed. All outputs are written, all logs are appended.

| Property | Value |
|---|---|
| **Task ownership** | Released |
| **Lease status** | Released |
| **Entry events** | Worker confirms all outputs written, execution history entry appended, processed registry updated |
| **Exit events** | None — terminal state |

**Entry requirements (all must be true before transitioning to `completed`):**
- [ ] All task outputs written to designated output paths
- [ ] Execution history entry appended (`EXECUTION_HISTORY.jsonl`)
- [ ] Processed registry entry recorded (`processed_registry.json`)
- [ ] No pending retry conditions
- [ ] No pending human review requirements

**Rollback of `completed`:** If a `completed` task is later found to have produced incorrect results:
1. Task state is NOT changed in the execution history (history is append-only)
2. A new task is filed for corrective action
3. An incident is logged in `INCIDENT_LOG.md`

**Valid transitions:** None — terminal state

---

### `failed`

**Definition:** The task could not be completed. The failure may be recoverable or non-recoverable.

| Property | Value |
|---|---|
| **Task ownership** | Released |
| **Lease status** | Released |
| **Entry events** | Non-recoverable error; max retries exceeded; governance violation; pre-flight validation failure |
| **Exit events** | Retry eligible → `pending` (after backoff delay per retry policy); max retries exceeded → terminal `failed` |

**Failure classification:**

| Classification | Description | Retry Allowed |
|---|---|---|
| **Recoverable** | Transient error (network timeout, resource temporarily unavailable) | Yes — up to max_retries |
| **Non-recoverable** | Governance violation, permission denied, data corruption, invalid task spec | No — immediate terminal failure |

**Upon entering `failed`, the following are required:**
- [ ] Failure reason written to execution history
- [ ] `retry_count` incremented
- [ ] If recoverable and under max retries → task re-enters retry_pending workflow
- [ ] If non-recoverable or max retries exceeded → terminal `failed`, incident logged
- [ ] Human operator notified via governance channels

**Valid transitions:** `failed` → `pending` (retry), `failed` → terminal

---

### `blocked`

**Definition:** The task cannot proceed due to a blocking condition that requires external resolution.

| Property | Value |
|---|---|
| **Task ownership** | Released |
| **Lease status** | Suspended |
| **Entry events** | Dependency not met; required resource unavailable; human review required before proceeding |
| **Exit events** | Blocking condition resolved → `pending`; governance override to `failed` → `failed` |

**Blocking conditions:**

| Condition | Resolution Path |
|---|---|
| **Dependency not met** | Upstream task completes → automatic transition to `pending` |
| **Required resource unavailable** | Resource comes available → manual transition to `pending` |
| **Human review required** | Human operator reviews and approves → manual transition to `pending` |
| **External API unavailable** | API comes available → automatic or manual transition to `pending` |

**While in `blocked`:**
- No worker may claim or execute the task
- The task does not consume retry count
- The blocking condition must be documented in the execution history

**Valid transitions:** `blocked` → `pending`, `blocked` → `failed`

---

### `skipped_already_processed`

**Definition:** The task was found to have already been successfully processed (duplicate detection).

| Property | Value |
|---|---|
| **Task ownership** | None — no worker assigned |
| **Lease status** | N/A |
| **Entry events** | Worker checks processed registry and finds task_id already recorded |
| **Exit events** | None — terminal state |

**Entry requirements:**
- [ ] Processed registry entry confirmed with matching task_id and commit hash
- [ ] No execution attempted
- [ ] Skipped entry appended to execution history

**This state is distinct from `failed`** — the task was intentionally skipped because it was already completed. No retry is appropriate.

**Valid transitions:** None — terminal state

---

### `archived`

**Definition:** The task has been preserved for audit purposes and is no longer in the active queue.

| Property | Value |
|---|---|
| **Task ownership** | None |
| **Lease status** | None |
| **Entry events** | Task completed and retained for long-term audit; or governance decision to archive |
| **Exit events** | None — terminal state |

**Archival criteria:**
- Task was in `completed`, `failed`, or `skipped_already_processed` state
- Task is older than the active retention window (typically 90 days)
- Governance has approved archival

**While in `archived`:**
- Task is removed from active queue but record is preserved
- Execution history entry remains in `EXECUTION_HISTORY.jsonl`
- Processed registry entry remains in `processed_registry.json`

**Valid transitions:** None — terminal state (from `completed`, `failed`, or `skipped_already_processed`)

---

## State Transition Summary

| From State | Valid Exit States |
|---|---|
| `pending` | `claimed`, `skipped_already_processed` |
| `claimed` | `in_progress`, `failed`, `pending` |
| `in_progress` | `completed`, `failed`, `pending` |
| `completed` | `archived` (optional) |
| `failed` | `pending` (if retry eligible), terminal (if non-recoverable or max retries) |
| `blocked` | `pending`, `failed` |
| `skipped_already_processed` | `archived` (optional) |
| `archived` | None — terminal |

---

## Prohibited Transitions

The following transitions are **not permitted** under any circumstances:

| Prohibited Transition | Reason |
|---|---|
| `pending` → `completed` | All tasks must be claimed and executed — no skip |
| `in_progress` → `blocked` | Blocking conditions must be identified at claim time, not mid-execution |
| `failed` → `completed` | Failed tasks may not self-transition to completed |
| `skipped_already_processed` → `in_progress` | Already-processed tasks may not be re-executed |
| `archived` → any state | Archived tasks are immutable |
| Any state → `claimed` (re-claim) | Active claim already exists |

---

## Relationship to Worker Lifecycle

Each task state corresponds to a worker state in the Worker Lifecycle Model:

| Task State | Worker State | Synchronization |
|---|---|---|
| `pending` | `polling` | Worker is checking queue |
| `claimed` | `task_claimed` | Worker owns the task |
| `in_progress` | `executing` | Worker is executing |
| `completed` | `completed` | Worker finished successfully |
| `failed` | `failed` | Worker encountered error |
| `pending` (retry) | `retry_pending` | Task waiting for backoff |
| `pending` (abandoned) | `abandoned` | Lease expired |
| `pending` (recovery) | `recovered` | Worker recovered from abandonment |
| `blocked` | `idle` or `polling` | No worker assigned |

> **See also:** [Worker Lifecycle](./WORKER_LIFECYCLE.md) — Full worker state definitions

---

## Duplicate Processing Prevention

**Mechanism:** Processed registry check before claim

| Step | Action |
|---|---|
| 1 | Worker checks `processed_registry.json` for task_id |
| 2 | If found → transition to `skipped_already_processed`, append execution history entry |
| 3 | If not found → worker claims task, transitions to `claimed` |
| 4 | On completion → append to processed_registry (append-only, no deletion) |

**Append-only enforcement:** Registry entries are never deleted. Re-processing of an archived task must be explicitly approved via governance.

---

## Heartbeat Requirements by State

| State | Worker Heartbeat Required | Interval |
|---|---|---|
| `pending` | No | — |
| `claimed` | Yes | Every 60 seconds |
| `in_progress` | Yes | Every 60 seconds |
| `completed` | No | — |
| `failed` | No | — |
| `blocked` | No | — |
| `skipped_already_processed` | No | — |
| `archived` | No | — |

---

*Canonical — GitHub is the source of truth.*