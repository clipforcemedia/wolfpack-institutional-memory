# TASK STATE MODEL

> Enumerates every legal state a task may occupy in the shared registry,
> with entry/exit conditions and transition constraints.
> This model applies to all tasks managed under the wolfpack runtime
> governance layer.

---

## STATE SUMMARY TABLE

| State | Category | Leased | Retryable | Terminal |
|---|---|---|---|---|
| `pending` | open | No | — | No |
| `claimed` | open | Yes | — | No |
| `in_progress` | open | Yes | — | No |
| `completed` | terminal | No | — | Yes |
| `failed` | terminal | No | — | Yes |
| `blocked` | open | No | — | No |
| `skipped_already_processed` | terminal | No | — | Yes |
| `archived` | terminal | No | — | Yes |

---

## pending

**Description:** Task is queued and available for any eligible worker
to claim. No worker currently holds a lease.

**Entry conditions:**
- Task created for the first time
- Task transitioned from `abandoned` (lease expired)
- Task manually unarchived and re-queued
- `blocked` task dependency resolved

**Permitted transitions OUT:**
- `pending → claimed` (worker writes claim)

**Forbidden transitions:**
- Any transition from `pending` while another worker holds a valid lease

---

## claimed

**Description:** A worker has written a claim to the registry.
The task is leased. No other worker may claim it.

**Entry conditions:**
- A worker wrote `claimed` to the task registry
- Lease expiry timestamp recorded
- First heartbeat posted

**Permitted transitions OUT:**
- `claimed → in_progress` (worker begins execution)
- `claimed → pending` (worker released claim gracefully, rare)
- `claimed → abandoned` (lease expired, no heartbeat renewal)

**Forbidden transitions:**
- `claimed → completed` (must go through `in_progress`)

---

## in_progress

**Description:** Worker is actively executing the task.
Heartbeat being renewed. Task is leased.

**Entry conditions:**
- Worker confirmed execution has started
- Registry reflects `in_progress`
- Execution history log entry appended

**Permitted transitions OUT:**
- `in_progress → completed` (success)
- `in_progress → failed` (non-retryable failure)
- `in_progress → retry_pending` (retry-eligible failure)
- `in_progress → abandoned` (lease expiry mid-execution)

**Forbidden transitions:**
- `in_progress → pending` (no voluntary demotion)

---

## completed

**Description:** Task completed successfully. Terminal state.
Task registry and execution history both reflect terminal success.

**Entry conditions:**
- All work product produced
- Registry `state` set to `completed`
- Execution history last entry has `state: "completed"`
- Done criteria satisfied (see RUNTIME_STATE_GOVERNANCE §12)

**Permitted transitions OUT:**
- None (terminal)

**Notes:**
- Done is defined once both registry and log are terminal.
- No further automatic processing permitted.
- Human review may archive.

---

## failed

**Description:** Task failed. Terminal state. No automatic retry pending.

**Entry conditions:**
- Non-retryable exception thrown, OR
- `retry_count >= max_retries` (exhausted retry budget)

**Permitted transitions OUT:**
- None (terminal) — unless human reviewer manually transitions to `pending`

**Notes:**
- Failure record written to execution history.
- Registry reflects `failed`.
- Human review may unarchive and re-queue.

---

## blocked

**Description:** Task cannot be claimed because a dependency
has not yet resolved (e.g., prerequisite task not complete,
external resource unavailable).

**Entry conditions:**
- Task registered with `blocked` state, OR
- Dependency check failed at claim time
- Worker or system explicitly set `blocked`

**Permitted transitions OUT:**
- `blocked → pending` (dependency resolved)
- `blocked → archived` (dependency permanently unavailable)

**Forbidden transitions:**
- `blocked → in_progress` directly

---

## skipped_already_processed

**Description:** Task was found in the execution history log
with a prior terminal record. No further processing occurs.

**Entry conditions:**
- Worker checked execution history before claiming
- Prior terminal record found (`completed`, `failed`, `skipped`, or `archived`)

**Permitted transitions OUT:**
- None (terminal)

**Notes:**
- Prevents duplicate processing — a core duplicate-prevention safeguard.
- Recorded in registry and execution history for audit.

---

## archived

**Description:** Task is closed. No worker may claim it.
Typically set after human review of a `failed` task or end-of-life.

**Entry conditions:**
- Human reviewer archived after failure review
- Task explicitly archived (end-of-life)
- `skipped_already_processed` task archived after retention period

**Permitted transitions OUT:**
- `archived → pending` (human reviewer re-queues)

**Forbidden transitions:**
- Any automatic transition to `archived` without human action
  (except from `skipped_already_processed`)

---

## TRANSITION CONSTRAINT SUMMARY

```
pending      → claimed
claimed      → in_progress | abandoned
in_progress  → completed | failed | retry_pending | abandoned
retry_pending→ in_progress | failed
abandoned    → pending (auto-requeue) | task_claimed (by same/new worker)
failed       → (terminal, human review to re-queue)
completed    → (terminal)
skipped_already_processed → (terminal)
archived     → pending (human review only)
```

---

*Governance authority: wolfpack-institutional-memory / runtime/*
*Effective: 2026-05-24*