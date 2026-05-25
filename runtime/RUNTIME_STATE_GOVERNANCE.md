---
title: "Runtime State Governance — Deterministic Worker and Task Execution Standards"
document_type: "governance"
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
  - "governance"
  - "worker"
  - "task"
  - "deterministic"
  - "batch-002"
related_ids:
  - "runtime/WORKER_LIFECYCLE.md"
  - "runtime/TASK_STATE_MODEL.md"
  - "canon/SYSTEM_ARCHITECTURE.md"
  - "agents/AGENT_GOVERNANCE.md"
  - "operations/INCIDENT_LOG.md"
append_only: true
---

# Runtime State Governance — Deterministic Worker and Task Execution Standards

> **Source:** Wolfpack institutional memory — runtime state governance layer  
> **Status:** Active — Canonical Governance Doctrine  
> **Activation Date:** 2026-05-24  
> **Supersedes:** Ad-hoc runtime conventions (none formally documented prior)

---

## Purpose

This document establishes formal governance standards for all deterministic task execution within the Wolfpack system. It defines:

- How execution workers operate within the Wolfpack governance framework
- How tasks are owned, leased, and released across worker sessions
- How state is preserved, recovered, and audited
- What state is prohibited from being stored outside formal channels

The goal is to ensure that **no task execution creates hidden state**, **no worker becomes a governance authority**, and **every task outcome is traceable to a deterministic decision**.

> **See also:** [Worker Lifecycle](./WORKER_LIFECYCLE.md) — State machine for execution workers  
> **See also:** [Task State Model](./TASK_STATE_MODEL.md) — State machine for task execution

---

## 1. Execution Worker Role

**Definition:** An execution worker is any automated process that performs task actions on behalf of the Wolfpack system. Within Wolfpack, the primary execution worker is OpenClaw.

| Property | Requirement |
|---|---|
| **Authority** | Zero autonomous authority. Workers execute only what governance gates approve |
| **Governance position** | Subordinate to all governance systems — never above them |
| **Permission scope** | Explicitly scoped permissions only — no blanket access to resources |
| **Observability** | Full logging required for every action taken |
| **Replaceability** | Must be replaceable at any time without loss of task state |

**See:** [System Architecture — OpenClaw as Replaceable Worker](./canon/SYSTEM_ARCHITECTURE.md)

---

## 2. Worker Replaceability Doctrine

**Principle:** Execution workers are stateless by design. All task state lives in institutional memory (GitHub), not in the worker process.

| Doctrine | Description |
|---|---|
| **No local state dependency** | Worker must not require local files or process memory to resume a task |
| **State in GitHub** | All task definitions, results, and audit records live in GitHub |
| **Replaceable on failure** | Any worker can be terminated and replaced without losing task progress |
| **Identical behavior guarantee** | New worker interpreting the same task file must produce the same result |

**DEC-001 Alignment:** OpenClaw is the current replaceable execution worker. Any equivalent worker (Claude Code, alternative OpenClaw instance, etc.) that reads the same task files and produces identical outputs is a valid replacement.

---

## 3. Task Ownership Rules

**Definition:** Task ownership defines which worker is responsible for a task at any given time.

| Rule | Description |
|---|---|
| **Claim establishes ownership** | A worker owns a task once it has claimed it and the claim is registered |
| **Exclusive ownership** | Only the owning worker may perform actions on a claimed task |
| **Ownership transfer prohibited** | A worker may not transfer ownership to another worker mid-execution |
| **Ownership release** | Ownership is released upon task completion, failure, or timeout |
| **Governance override** | Human operator or Deployment Governor may revoke ownership at any time |

**Ownership does not imply authority.** Owning a task means the worker has responsibility for executing it — not that the worker has decision-making power over it.

---

## 4. Task Leasing Rules

**Definition:** Task leasing is the time-bounded claim mechanism that prevents indefinite ownership and enables crash recovery.

| Rule | Description |
|---|---|
| **Lease duration** | Claimed tasks have a defined lease duration (typically one task cycle) |
| **Lease refresh** | Lease may be refreshed by the worker while actively executing |
| **Lease expiry triggers recovery** | When lease expires without completion, task returns to `pending` |
| **No automatic renewal** | Worker must explicitly renew the lease; automatic renewal is prohibited |
| **Lease under governance** | Human operator or Deployment Governor may revoke a lease at any time |

**Purpose:** Leasing prevents tasks from being permanently claimed by workers that become unavailable (crash, network loss, restarts).

---

## 5. Duplicate-Processing Prevention

**Definition:** Duplicate-processing prevention ensures the same task is not executed multiple times across worker sessions.

| Mechanism | Implementation |
|---|---|
| **Processed registry** | Append-only `processed_registry.json` records completed task IDs by commit hash |
| **Idempotency check** | Worker checks registry before processing — if task_id already recorded, skip |
| **Append-only enforcement** | Registry entries are never deleted, only added |
| **Commit-scoped tracking** | Registry tracks which commit produced the result, enabling rollback comparison |
| **Race condition prevention** | Claiming a task and recording completion are atomic within the same task cycle |

> **See also:** [Task State Model — `skipped_already_processed`](./TASK_STATE_MODEL.md)

---

## 6. Crash Recovery Rules

**Definition:** Crash recovery defines what happens when a worker fails or becomes unavailable during task execution.

| Rule | Description |
|---|---|
| **Detect via heartbeat** | Worker absence detected when two consecutive heartbeat intervals are missed |
| **Task reverts to `pending`** | Any task with an expired lease returns to `pending` queue |
| **Lease expiry triggers recovery** | Expired lease means task is eligible for re-claim by any worker |
| **No rollback of partial execution** | If task wrote partial outputs before crash, those outputs remain |
| **Incident logged** | Worker crash must produce an incident entry in the incident log |
| **Recovered state documented** | Recovered tasks that are re-claimed must record recovery event in execution history |

**See also:** [Worker Lifecycle — `recovered` and `abandoned` states](./WORKER_LIFECYCLE.md)

---

## 7. Retry Rules

**Definition:** Retry rules govern when and how failed tasks are re-executed.

| Rule | Description |
|---|---|
| **Retry count tracked** | Each task carries a `retry_count` — incremented on each retry |
| **Max retries enforced** | Tasks exceeding `max_retries` move to `failed` — no further automatic retry |
| **Recoverable vs. non-recoverable** | Failures are classified: recoverable (retry allowed) vs. non-recoverable (immediate fail) |
| **Exponential backoff** | Retry intervals increase exponentially (base 2) for recoverable failures |
| **Non-recoverable failures** | Governance errors, permission denied, and data corruption are non-recoverable |
| **Human review for max retries** | Tasks reaching max retries require explicit human or Deployment Governor review |
| **Retry count reset on re-claim** | If task is re-claimed after max retries with explicit approval, count resets |

**Default retry parameters:**

| Parameter | Default Value |
|---|---|
| `max_retries` | 3 |
| `base_delay_seconds` | 30 |
| `backoff_multiplier` | 2 |
| `max_delay_seconds` | 300 |

---

## 8. Heartbeat Requirements

**Definition:** Heartbeat is the periodic signal a worker sends to indicate it is alive and processing a task.

| Requirement | Specification |
|---|---|
| **Heartbeat interval (polling)** | Every 5 minutes while worker is polling for tasks |
| **Heartbeat interval (executing)** | Every 60 seconds while worker is actively executing a task |
| **Missed heartbeat threshold** | Two consecutive missed heartbeats triggers `dead` state for worker |
| **Heartbeat target** | Worker writes heartbeat timestamp to a heartbeat log in institutional memory |
| **Heartbeat is not task progress** | Heartbeat only confirms worker process is alive — not that task is progressing |
| **Task progress must be observable** | Actual task progress must be logged in execution history, not just heartbeat |
| **Heartbeat under governance** | Heartbeat logging is read-only for workers; governed systems manage heartbeat configuration |

---

## 9. Append-Only Execution History

**Definition:** The execution history is an immutable, append-only record of every task lifecycle event.

| Property | Requirement |
|---|---|
| **Append-only** | Entries are only added — never modified or deleted |
| **Timestamp precision** | Every entry includes ISO-8601 UTC timestamp |
| **Worker identification** | Every entry includes worker/source identifier |
| **Task identification** | Every entry includes task_id |
| **State transitions** | Every entry records the state transition (from_state → to_state) |
| **Result payload** | Completed or failed tasks include result artifact path and outcome summary |
| **No personally identifiable information** | Execution history records task outcomes, not personal data |
| **Retain indefinitely** | Execution history is permanent institutional record — never pruned |
| **Format** | JSONL (one JSON object per line) for easy programmatic parsing |

**Execution history log location:** `operations/EXECUTION_HISTORY.jsonl`

> **See also:** [Incident Log](./operations/INCIDENT_LOG.md) — failures and governance events

---

## 10. Prohibited Hidden State

**Definition:** Hidden state is any state maintained by a worker or system component that is not visible in the formal execution history or institutional memory.

The following are **categorically prohibited** as hidden state:

| Prohibited State | Rationale |
|---|---|
| **Unlogged task outcomes** | All task results must be in execution history |
| **Worker-local caching of results** | Cached results outside institutional memory are not governed |
| **Inter-worker communication channels** | Workers may not coordinate via channels outside institutional memory |
| **Dynamic permission grants** | Workers may not grant themselves permissions not in the task spec |
| **Delayed task execution** | Tasks may not be queued for later execution outside the formal task queue |
| **State machine overrides** | Workers may not manually transition task state without going through formal channels |
| **Privately stored credentials** | Credentials must be in institutional memory or governance secrets management |
| **Hidden monitoring or metrics** | Any worker-side metrics collection must be declared in the task spec |

**Enforcement:** Any task runner that creates hidden state is subject to governance incident response. Human operator or Deployment Governor may halt the worker immediately.

---

## 11. Definition of Done

A task is considered **complete** when all of the following are true:

| Criterion | Verification |
|---|---|
| Task state is `completed` | Formal state transition recorded in task state model |
| All outputs written to designated paths | Output paths exist and contain expected content |
| Execution history entry written | Entry with task_id, outcome, timestamp in `EXECUTION_HISTORY.jsonl` |
| Processed registry entry recorded | `processed_registry.json` updated with task_id and commit hash |
| No active retries | `retry_count` is 0 or task has explicitly succeeded |
| No pending escalation | If task required human review, review decision is recorded |

**Partial completion is not completion.** If a task writes some outputs but fails before completing all required actions, it is in `failed` state — not `completed`.

**Rollback of completion:** If a completed task is found to have produced incorrect results, it must be:
1. Marked `failed` (not deleted from history)
2. An incident logged in `INCIDENT_LOG.md`
3. A new task filed for corrective action

---

## 12. Relationship to Existing Wolfpack Governance

| Governance File | Relationship |
|---|---|
| [System Architecture](./canon/SYSTEM_ARCHITECTURE.md) | Confirms OpenClaw as replaceable worker — aligned |
| [Agent Governance](./agents/AGENT_GOVERNANCE.md) | Confirms scoped permissions and observability — aligned |
| [Deployment Governor](./agents/DEPLOYMENT_GOVERNOR.md) | Confirms human review for failed/max-retry tasks — aligned |
| [Incident Log](./operations/INCIDENT_LOG.md) | Confirms incident logging for crashes and failures — aligned |
| [Wolfpack Canon](./canon/WOLFPACK_CANON.md) | Confirms no uncontrolled autonomy — aligned |

---

## 13. Automatic Post-Workflow Validation (Stage 8)

**Definition:** Every invocation of `wolfpack_review_runner.py` MUST execute `runtime_state_validator.py` as a mandatory post-processing step before reporting completion.

| Requirement | Specification |
|---|---|
| **Trigger** | After ALL task processing stages (1–7) complete, before workflow exits cleanly |
| **Script location** | `tasks/runtime_state_validator.py` |
| **Execution method** | Subprocess call via `sys.executable` — no import coupling |
| **Timeout** | 60 seconds — timeout treated as validation FAIL |
| **Log output** | Append entry to `runtime/VALIDATOR_EXECUTION_LOG.jsonl` (JSONL, append-only) |
| **Report output** | `runtime/RUNTIME_STATE_VALIDATION_REPORT.md` updated on each run |
| **Failure behavior** | Exit code 2 — workflow tasks succeed but validator rejects state; silent continuation PROHIBITED |
| **Success behavior** | Exit code 0 — both tasks and validator passed |

**Validator execution log schema (VALIDATOR_EXECUTION_LOG.jsonl):**

```json
{"timestamp":"2026-05-25T05:10:00Z","workflow_id":"wolfpack_review_runner_v1","validator_exit_code":0,"validator_result":"PASS","issues_count":0}
```

| Field | Type | Description |
|---|---|---|
| `timestamp` | ISO-8601 UTC | When validator was invoked |
| `workflow_id` | string | Source workflow identifier |
| `validator_exit_code` | int | Exit code from validator script; -1=not found, -2=timeout, -3=error |
| `validator_result` | string | "PASS", "FAIL", "SKIP", "TIMEOUT", "ERROR", "UNKNOWN" |
| `issues_count` | int | Number of validation issues detected |

**Governance enforcement:**
- Exit code 0: workflow complete, validator passed — clean exit
- Exit code 1: one or more tasks failed during execution — failure exit
- Exit code 2: all tasks succeeded but validator rejected state — **HALT exit** (silent continuation prevented)

This ensures that a corrupt registry, duplicate task entries, or missing result paths will never pass silently into institutional memory.

---

## References

| Reference | Description |
|---|---|
| [Worker Lifecycle](./WORKER_LIFECYCLE.md) | Formal state machine for execution workers |
| [Task State Model](./TASK_STATE_MODEL.md) | Formal state machine for task execution |
| [System Architecture — DEC-001](./canon/SYSTEM_ARCHITECTURE.md) | OpenClaw as replaceable worker |
| [Agent Governance](./agents/AGENT_GOVERNANCE.md) | Agent operational standards |
| [Execution History](./operations/EXECUTION_HISTORY.jsonl) | Append-only task execution log |
| [Validator Execution Log](./runtime/VALIDATOR_EXECUTION_LOG.jsonl) | Append-only validator invocation history |
| [Runtime State Validator](./tasks/runtime_state_validator.py) | Standalone validation script |

---

*Canonical — GitHub is the source of truth.*