# RUNTIME STATE GOVERNANCE

> Governs all deterministic worker execution, task ownership, leasing,
> crash recovery, and append-only execution history.
> Effective for all task bridges and worker processes touching the
> wolfpack task registry.

---

## 1. PURPOSE

Runtime state governance defines the contractual rules by which
executable workers claim, process, complete, fail, and retire tasks
without duplicating work, losing ownership, or corrupting shared state.

It applies to every worker that reads from or writes to the shared task
registry and execution history log.

---

## 2. EXECUTION WORKER ROLE

An **execution worker** (hereafter "worker") is any autonomous process
that:

- Polls the task registry for `pending` tasks
- Claims a task by transitioning its state
- Performs deterministic computation or external I/O on behalf of a task
- Writes a completion or failure record to the append-only execution log
- Posts a heartbeat to indicate continued health

Workers are stateless with respect to each other. No inter-worker
communication is required or assumed.

---

## 3. WORKER REPLACEABILITY DOCTRINE

Any worker may be terminated and replaced by another at any time
without loss of task integrity, provided:

- The replacing worker observes the same task state machine
- No task is ever left in a terminal state while unprocessed
- The task registry is the single source of truth for ownership

**Corollary:** a worker that crashes mid-execution does not orphan a task.
The task remains in its last written state; a replacement worker may
reclaim it per the leasing rules.

---

## 4. TASK OWNERSHIP RULES

A task is **owned** by the worker that most recently wrote a
`claimed` or `in_progress` state transition to the registry.

Ownership is transferred only when:
- The current owner fails to renew its heartbeat (lease expiry)
- The task reaches a terminal state (`completed`, `failed`, `skipped_already_processed`, `archived`)

No two workers may simultaneously hold ownership of the same task.
The registry is the authoritative ownership ledger.

---

## 5. TASK LEASING RULES

Each claim includes an explicit **lease duration** — the maximum interval
between heartbeat updates before the claim is considered abandoned.

Default lease: **300 seconds (5 minutes)**.

A worker MUST renew its heartbeat before the lease expires if it is
still executing. Failure to renew constitutes lease expiry and grants
any waiting worker the right to reclaim the task.

A task whose lease expires is treated as `abandoned` and becomes
`pending` for re-claim by the next eligible worker.

---

## 6. DUPLICATE-PROCESSING PREVENTION

Before claiming a task, a worker MUST check the execution history log
for a prior record of processing.

If a record exists with a terminal state, the worker MUST transition
the task to `skipped_already_processed` and emit no output.

If a record exists with a non-terminal state (e.g., `in_progress` with
no subsequent terminal record), the worker MUST verify the heartbeat
is current before proceeding. If stale, the task MAY be reclaimed.

Duplicate processing is a governance violation.

---

## 7. CRASH RECOVERY RULES

| Crash point | Recovery action |
|---|---|
| Before claiming | No action. Task stays `pending`. |
| After claim written, before first heartbeat | Reclaimable immediately by any worker. |
| During execution, lease active | No action. Wait for lease expiry. |
| After completion written | No action. Task is terminal. |
| After failure written | No action. Task is terminal. |
| During heartbeat write | idempotent retry; task remains `in_progress`. |

A worker that restarts after a crash MUST re-inspect the registry
before re-claiming any task.

---

## 8. RETRY RULES

- A task in `failed` state MAY be retried at most **3 times**
  (configurable per task class).
- Each retry appends a new entry to the execution history log.
- Retry count is stored in the task registry (`retry_count` field).
- After 3 failures, the task transitions to `archived` and
  no further automatic retries are permitted.
- A human reviewer may manually unarchive and re-queue.

---

## 9. HEARTBEAT REQUIREMENTS

A worker MUST post a heartbeat for every task it owns at intervals
no greater than `lease_duration / 2`.

Heartbeat payload:
```
{
  "task_id": "<id>",
  "worker_id": "<id>",
  "claimed_at": "<ISO-8601>",
  "last_heartbeat_at": "<ISO-8601>",
  "state": "in_progress"
}
```

A worker that misses two consecutive heartbeat windows is considered
**non-responsive** and its tasks become eligible for lease expiry
and re-claim.

---

## 10. APPEND-ONLY EXECUTION HISTORY

The execution history log (`tasks/pull_history.jsonl` and any mirror)
is **append-only**. No entry may be deleted, modified, or overwritten.

Each line is a valid JSON record:

```json
{"task_id":"...","worker_id":"...","state":"...","timestamp":"...","lease_expires_at":"...","notes":"..."}
```

Append-only guarantees:
- Audit trail is never corrupted by concurrent writes
- Crash reconstruction is always possible from the log
- No hidden state — all transitions visible

---

## 11. PROHIBITED HIDDEN STATE

Workers MUST NOT maintain private state that affects task routing,
completion, or failure decisions outside the registry and execution log.

Specifically prohibited:
- In-memory task queues not persisted to the registry
- Filesystem-side task state not mirrored to the registry
- Inter-process locks or signals not reflected in the registry
- Conditional logic that skips a task based on data not in the registry

---

## 12. DEFINITION OF DONE

A task is **Done** when it has a terminal state recorded in both:

1. The task registry (`state` field is terminal)
2. The append-only execution history log (last entry is terminal)

Done is not recorded until both conditions are satisfied.
A task is **Done** only once. Re-processing a Done task is a governance
violation unless it transitions through `archived → pending`.

---

*Governance authority: wolfpack-institutional-memory / runtime/*
*Effective: 2026-05-24*
*Supersedes: none*