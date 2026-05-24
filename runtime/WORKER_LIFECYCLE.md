# WORKER LIFECYCLE

> Enumerates every legal state a deterministic execution worker
> may occupy, with entry/exit conditions, permitted actions,
> and transition triggers.

---

## STATE MAP

```
idle ──► polling ──► task_claimed ──► executing ──► completed
                                       │              │
                                       ▼              ▼
                                   failed ◄── retry_pending
                                       │
                                       ▼
                               abandoned ◄── (lease expiry)
                                       │
                                       ▼
                                   recovered
```

---

## idle

**Description:** Worker has started, holds no task, and is not polling.

**Entry conditions:**
- Worker process has spawned
- Initialization complete (identity confirmed, registry reachable)

**Permitted actions:**
- Begin polling
- Log heartbeat (worker-level, not task-level)

**Exit triggers:**
- `poll` signal → `polling`

---

## polling

**Description:** Worker is actively scanning the task registry for
unclaimed `pending` tasks.

**Entry conditions:**
- Worker entered `polling` from `idle`
- Polling interval has elapsed (if recurring)

**Permitted actions:**
- Read task registry
- Check execution history for prior processing
- Evaluate duplicate-prevention conditions

**Exit triggers:**
- Task found, duplicate detected → `skipped_already_processed` (task), remain `polling`
- Task found, eligible → `task_claimed`
- No task found → back to `idle` (or wait interval then re-poll)

---

## task_claimed

**Description:** Worker has written a claim record to the registry.
It holds a valid lease. The task is now owned by this worker.

**Entry conditions:**
- Registry write of `claimed` state succeeded
- Lease duration recorded
- First heartbeat posted

**Permitted actions:**
- Read task input
- Begin deterministic processing
- Renew heartbeat

**Exit triggers:**
- Processing begins (internal) → `executing`
- Lease expires before processing starts → `abandoned`
- Worker shut down gracefully → `idle`

---

## executing

**Description:** Worker is performing the task's deterministic work.
Heartbeat is being renewed on schedule.

**Entry conditions:**
- Worker has transitioned from `task_claimed`
- Processing loop has started

**Permitted actions:**
- Perform computation / external I/O
- Write partial progress to task registry (optional, not required)
- Renew heartbeat per schedule
- Handle exceptions internally

**Exit triggers:**
- Work completes successfully → `completed`
- Work fails with retry-eligible error → `retry_pending`
- Work fails with non-retryable error → `failed`
- Heartbeat missed twice → `abandoned`

---

## completed

**Description:** Task has reached a terminal success state.
Registry updated, execution history appended. Worker holds no further
obligation.

**Entry conditions:**
- All work product produced
- Registry state set to `completed`
- Append-only log entry written with `state: "completed"`
- Done criteria satisfied (registry + log both terminal)

**Permitted actions:**
- Log final completion record
- Return to `idle` for next task

**Exit triggers:**
- None. This is a terminal worker state.

---

## failed

**Description:** Task failed in a non-retryable way, or retry budget
is exhausted. Registry updated. Execution history appended.

**Entry conditions:**
- Exception not retry-eligible, OR
- `retry_count >= max_retries`

**Permitted actions:**
- Log failure reason
- Transition registry to `failed`
- Append to execution history
- Return to `idle`

**Exit triggers:**
- None. Terminal. Human review may later unarchive.

---

## retry_pending

**Description:** Task failed with a retry-eligible error. Worker has
incremented `retry_count` in the registry. Task is temporarily off
the queue.

**Entry conditions:**
- Execution threw a retry-eligible exception
- `retry_count < max_retries`

**Permitted actions:**
- Write `failed` with retry_pending flag to execution history
- Increment retry counter in registry
- Wait for backoff interval
- Re-enter at `task_claimed` for same task

**Exit triggers:**
- Backoff expires → `task_claimed` (same task, incremented retry)
- Max retries reached during backoff → `failed`

---

## abandoned

**Description:** Worker held a lease but failed to renew the heartbeat
within the lease window. Task is no longer owned. Any worker may reclaim.

**Entry conditions:**
- Lease expired with no heartbeat renewal
- Registry updated to `pending` by lease manager

**Permitted actions:**
- Log abandonment
- Return to `idle`

**Exit triggers:**
- Task re-claimed by this or another worker → `task_claimed`
- No re-claim, worker shut down → `idle`

---

## recovered

**Description:** Worker re-claimed an abandoned task and resumed
execution. The task never left the system; only ownership changed.

**Entry conditions:**
- Worker detected `pending` task with prior execution history
- Worker confirmed lease was expired (not stolen)
- Worker wrote new claim record

**Permitted actions:**
- Resume from last known state (read prior execution history)
- Continue execution from point of failure
- Renew heartbeat normally

**Exit triggers:**
- Work completes → `completed`
- Failure again → `failed` or `retry_pending`

---

*Governance authority: wolfpack-institutional-memory / runtime/*
*Effective: 2026-05-24*