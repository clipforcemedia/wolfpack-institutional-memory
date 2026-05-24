---
title: "Worker Lifecycle — Execution Worker State Machine"
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
  - "worker"
  - "lifecycle"
  - "state-machine"
  - "batch-002"
related_ids:
  - "runtime/RUNTIME_STATE_GOVERNANCE.md"
  - "runtime/TASK_STATE_MODEL.md"
append_only: true
---

# Worker Lifecycle — Execution Worker State Machine

> **Source:** Wolfpack institutional memory — runtime state governance layer  
> **Status:** Active — Canonical State Machine  
> **Activation Date:** 2026-05-24  
> **Governs:** All deterministic execution workers in the Wolfpack system

---

## Overview

This document defines the formal state machine for all execution workers operating within the Wolfpack system. Each worker transitions through defined states in response to events. No state transitions outside this model are permitted.

**States:** `idle` → `polling` → `task_claimed` → `executing` → `completed` / `failed` → `retry_pending` / `abandoned` → `recovered`

**See also:** [Runtime State Governance](./RUNTIME_STATE_GOVERNANCE.md) — Full governance standards  
**See also:** [Task State Model](./TASK_STATE_MODEL.md) — Task state machine

---

## State Definitions

### `idle`

**Definition:** Worker is initialized but not actively polling for tasks.

| Property | Value |
|---|---|
| **Heartbeat interval** | None (worker is not expected to be reachable) |
| **Task ownership** | None |
| **Entry events** | Worker process starts |
| **Exit events** | Worker begins polling interval |

**Valid transitions:** `idle` → `polling`

---

### `polling`

**Definition:** Worker is actively checking the task queue on a recurring interval.

| Property | Value |
|---|---|
| **Heartbeat interval** | Every 5 minutes |
| **Task ownership** | None |
| **Entry events** | Polling interval begins |
| **Exit events** | Task found and claimed → `task_claimed`; polling timeout → `idle` |

**Valid transitions:** `polling` → `task_claimed`, `polling` → `idle`

---

### `task_claimed`

**Definition:** Worker has successfully claimed a task and holds the lease. The task is now under this worker's ownership.

| Property | Value |
|---|---|
| **Heartbeat interval** | Every 60 seconds |
| **Task ownership** | Exclusive — task is owned until completion or lease expiry |
| **Entry events** | Task claim registered in task queue |
| **Exit events** | Claim confirmed and execution begins → `executing`; lease rejected → `idle`; unexpected error → `failed` |

**Constraints during `task_claimed`:**
- Worker must not begin execution until all pre-flight validations are complete
- Worker must refresh heartbeat every 60 seconds
- Worker must not transfer the claim to another worker

**Valid transitions:** `task_claimed` → `executing`, `task_claimed` → `idle`, `task_claimed` → `failed`

---

### `executing`

**Definition:** Worker is actively performing the task actions as defined in the task specification.

| Property | Value |
|---|---|
| **Heartbeat interval** | Every 60 seconds |
| **Task ownership** | Exclusive — task is owned through completion or failure |
| **Entry events** | Pre-flight validations passed, task actions begin |
| **Exit events** | All task actions completed successfully → `completed`; task actions failed → `failed`; lease expired → `abandoned` |

**During `executing`, the worker must:**
- Write progress entries to execution history at each milestone
- Maintain heartbeat every 60 seconds
- Not modify the task specification itself
- Not create hidden state (per Runtime State Governance §11)

**Valid transitions:** `executing` → `completed`, `executing` → `failed`, `executing` → `retry_pending`, `executing` → `abandoned`

---

### `completed`

**Definition:** Worker has successfully completed all task actions and recorded the outcome.

| Property | Value |
|---|---|
| **Heartbeat interval** | None required after completion |
| **Task ownership** | Released — task is now `completed` in task state model |
| **Entry events** | All outputs written, execution history entry appended, processed registry updated |
| **Exit events** | Worker returns to polling → `polling`; worker shuts down → `idle` |

**Entry requirements (all must be true):**
- [ ] All task outputs written to designated paths
- [ ] Execution history entry appended with outcome summary
- [ ] Processed registry entry recorded with task_id and commit hash
- [ ] Task state model transitioned to `completed`

**Valid transitions:** `completed` → `polling`, `completed` → `idle`

---

### `failed`

**Definition:** Worker attempted task execution but could not complete it. Failure may be recoverable or non-recoverable.

| Property | Value |
|---|---|
| **Heartbeat interval** | None required after failure |
| **Task ownership** | Released — task is now `failed` in task state model |
| **Entry events** | Non-recoverable error; or max retries exceeded; or governance violation |
| **Exit events** | Incident logged, worker returns to polling → `polling`; worker shuts down → `idle` |

**Upon entering `failed`, the worker must:**
- [ ] Write failure reason to execution history
- [ ] Increment `retry_count` on the task
- [ ] If recoverable and under max retries → transition to `retry_pending`
- [ ] If non-recoverable or max retries exceeded → leave in `failed`, log incident
- [ ] Notify governance via incident log

**Valid transitions:** `failed` → `retry_pending`, `failed` → `polling`, `failed` → `idle`

---

### `retry_pending`

**Definition:** Task failed but is eligible for retry under the retry policy.

| Property | Value |
|---|---|
| **Heartbeat interval** | None required during retry wait |
| **Task ownership** | Released — task returns to queue after backoff delay |
| **Entry events** | Recoverable failure with retries remaining |
| **Exit events** | Backoff delay elapsed → `polling` (task re-queued); governance override → `failed` |

**During `retry_pending`, the worker must:**
- [ ] Wait the configured backoff delay before re-polling
- [ ] Not re-claim the task during the backoff period
- [ ] Not modify the task specification or retry count during backoff

**Retry backoff formula:** `delay_seconds = min(base_delay_seconds × (2 ^ retry_count), max_delay_seconds)`

**Valid transitions:** `retry_pending` → `polling`, `retry_pending` → `failed`

---

### `abandoned`

**Definition:** Worker lost the task lease (crash, network failure, missed heartbeats) before completing execution.

| Property | Value |
|---|---|
| **Heartbeat interval** | N/A — worker is unreachable |
| **Task ownership** | Released — lease expired, task returns to `pending` |
| **Entry events** | Lease expired without completion; or two consecutive missed heartbeats |
| **Exit events** | Worker restarts and recovers → `recovered`; worker shutdown → `idle` |

**Upon detecting `abandoned` state:**
- Task must be moved to `pending` in task state model (lease recovery)
- Any partial outputs remain in place (not rolled back)
- Incident must be logged in incident log
- Other workers may now claim the task

**Valid transitions:** `abandoned` → `recovered`, `abandoned` → `idle`

---

### `recovered`

**Definition:** Worker has restarted after an abandonment event and has resumed operation.

| Property | Value |
|---|---|
| **Heartbeat interval** | Every 5 minutes (polling mode) |
| **Task ownership** | None (previously owned task was abandoned and returned to pending) |
| **Entry events** | Worker process restarts after abandonment |
| **Exit events** | Worker begins polling → `polling`; worker shuts down → `idle` |

**Upon entering `recovered`, the worker must:**
- [ ] Check for any tasks that were abandoned during the previous session
- [ ] Log recovery event in execution history
- [ ] Confirm the abandoned task is back in `pending` state (not still claimed)
- [ ] Resume normal polling behavior

**Key distinction from `idle`:** `recovered` implies the worker is recovering from a previous failure or abandonment event. `idle` implies a clean startup with no prior session failure.

**Valid transitions:** `recovered` → `polling`, `recovered` → `idle`

---

## State Transition Summary

| From State | Valid Exit States |
|---|---|
| `idle` | `polling` |
| `polling` | `task_claimed`, `idle` |
| `task_claimed` | `executing`, `idle`, `failed` |
| `executing` | `completed`, `failed`, `retry_pending`, `abandoned` |
| `completed` | `polling`, `idle` |
| `failed` | `retry_pending`, `polling`, `idle` |
| `retry_pending` | `polling`, `failed` |
| `abandoned` | `recovered`, `idle` |
| `recovered` | `polling`, `idle` |

---

## Prohibited Transitions

The following transitions are **not permitted** under any circumstances:

| Prohibited Transition | Reason |
|---|---|
| `executing` → `idle` | Worker cannot abandon a task mid-execution without logging failure |
| `task_claimed` → `completed` | All tasks must go through `executing` — no skip |
| `abandoned` → `executing` | Worker cannot resume same task after abandonment |
| `failed` → `completed` | Failed tasks may not self-transition to completed |
| `retry_pending` → `executing` | Worker may not re-enter executing state without going through polling |
| Any state → `task_claimed` (from different worker) | Task may not be double-claimed |

---

## Heartbeat Requirements by State

| State | Heartbeat Required | Interval |
|---|---|---|
| `idle` | No | — |
| `polling` | Yes | Every 5 minutes |
| `task_claimed` | Yes | Every 60 seconds |
| `executing` | Yes | Every 60 seconds |
| `completed` | No | — |
| `failed` | No | — |
| `retry_pending` | No | — |
| `abandoned` | No | — |
| `recovered` | Yes (when polling) | Every 5 minutes |

---

## Relationship to Task State Model

Each worker state corresponds to a task state in the Task State Model. The two state machines are synchronized:

| Worker State | Task State |
|---|---|
| `polling` | Task is `pending` |
| `task_claimed` | Task is `claimed` |
| `executing` | Task is `in_progress` |
| `completed` | Task is `completed` |
| `failed` | Task is `failed` |
| `retry_pending` | Task is `pending` (re-queued after backoff) |
| `abandoned` | Task is `pending` (lease expired, returned to queue) |
| `recovered` | Task is `pending` |
| `idle` | No task |

> **See also:** [Task State Model](./TASK_STATE_MODEL.md) — Full task state definitions

---

*Canonical — GitHub is the source of truth.*