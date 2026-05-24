---
title: "Session Recovery Protocol — Wolfpack Agentic Execution"
document_type: "protocol"
status: "active"
version: "0.1"
created: "2026-05-24"
updated: "2026-05-24"
source_type: "internal"
provenance: "wolfpack-institutional-memory"
tags:
  - "wolfpack"
  - "session-recovery"
  - "agentic"
  - "governance"
related_ids:
  - "OVL-20260524-003"
  - "HAPI-002"
append_only: false
---
# Session Recovery Protocol

**Version:** 0.1 | **Status:** Active | **Created:** 2026-05-24

---

## 1. Purpose

This protocol defines how Wolfpack agents recover from session interruption, context loss, and amnesia events. It ensures every interrupted workflow can be safely reconstructed from repository state without requiring human re-explanation of intent, scope, or prior decisions.

Session amnesia — the loss of conversational context between agent turns — is a known failure mode of stateless execution workers. This protocol eliminates the dependency on human memory by establishing repo-first recovery as the canonical doctrine.

---

## 2. Failure Modes Covered

| Failure Mode | Description |
|---|---|
| **Session amnesia** | Agent loses prior conversation context on refresh/reconnect |
| **Worker crash** | Execution process terminates mid-workflow |
| **Network timeout** | Long-running command times out, state unclear |
| **Unexpected termination** | Agent killed, session ends without graceful shutdown |
| **Duplicate execution risk** | Same task started twice due to unclear prior state |
| **Terminal/session reset** | Human closes terminal, reconnects to fresh session |
| **Context injection failure** | Human-provided context is incomplete or contradictory |

---

## 3. Agent/Session Amnesia Rule

> **When an agent session loses context, the agent MUST treat the repository — not the human — as the authoritative source of truth.**

Human memory is fallible and bandwidth-limited. The agent MUST NOT ask the human to re-explain prior decisions unless the repo-first bootstrap checks fail to produce sufficient context.

**Amnesia detection triggers:**
- Agent receives a task that references a workflow_id, task_id, or overlay_id not present in current session context
- Agent is asked to "resume" something without being provided the prior state
- Human provides a repo path that differs from any previously known path in the session

---

## 4. Repo-First Recovery Doctrine

Every recovery begins with repository inspection before any other action:

```
1. Verify repo path exists and is a valid git repository
2. Determine current branch
3. Pull latest state from remote
4. InspectEXECUTION_HISTORY.jsonl for last activity
5. Inspect processed_registry.json for task state
6. Read relevant workflow/overlay files to reconstruct intent
7. Proceed only after full context is established
```

The agent MUST NOT make decisions, write files, or take actions until bootstrap checks confirm the current state of the repository.

---

## 5. Canonical Source Hierarchy During Recovery

When sources conflict, the following hierarchy resolves priority:

| Priority | Source | Rationale |
|---|---|---|
| 1 | `canon/` files | Immutable approved doctrine |
| 2 | `governance/` files | Active governance decisions |
| 3 | `runtime/EXECUTION_HISTORY.jsonl` | Append-only execution log |
| 4 | `tasks/processed_registry.json` | Task completion record |
| 5 | `status/NEXT_ACTIONS.md` | Human-authored intent |
| 6 | Human chat messages | Fallback when repo is silent |

---

## 6. Required Bootstrap Checks

Before resuming any interrupted workflow, the agent MUST verify:

- [ ] Repo path confirmed: `git rev-parse --show-toplevel`
- [ ] Current branch confirmed: `git branch --show-current`
- [ ] Git remote confirmed: `git remote -v`
- [ ] Git status checked: `git status`
- [ ] Recent commits inspected: `git log --oneline -10`
- [ ] Unstaged changes inspected: `git diff --stat`
- [ ] Target workflow files exist: per workflow_id
- [ ] `EXECUTION_HISTORY.jsonl` last entry read (if exists)
- [ ] `processed_registry.json` last entries read (if exists)
- [ ] No duplicate artifact paths detected

---

## 7. Working Tree Reconciliation Rules

| Scenario | Rule |
|---|---|
| Uncommitted changes exist | Inspect with `git diff`. Classify as governance (commit) or noise (restore). Never silently discard. |
| Conflicting overlay file | Do not overwrite. Escalate per DOCTRINE_OVERLAY_RECONCILIATION_STANDARD.md |
| Processed registry has gaps | Do not backfill. Report gap, continue only if safe. |
| History file missing | Treat as empty (append-only design). Log as issue, continue. |
| Canonical file modified | HALT. Do not proceed. Human must review before any action. |

---

## 8. Interrupted Workflow Recovery Rules

| Phase | Action |
|---|---|
| **Workflow identification** | Read relevant overlay/workflow files. Match against EXECUTION_HISTORY.jsonl last entry. |
| **Context reconstruction** | Read all referenced files in the last known workflow. |
| **Duplicate prevention** | Check processed_registry.json for task_id already completed. |
| **Safe resumption point** | Resume AFTER the last logged entry. Do not re-execute completed steps. |
| **Validation before action** | Run runtime_state_validator.py before any writes. |
| **Governance gate** | Do not proceed past any DEC/approval gate without explicit sign-off. |

---

## 9. Duplicate-Prevention Rules

- Every task_id MUST be checked against `processed_registry.json` before execution
- If task_id exists with status `completed` or `validated`, the task is SKIPPED — do not re-execute
- If task_id exists with status `failed`, the task MAY be retried after root cause review
- If task_id exists with status `in_progress` or `claimed`, HALT — a concurrent worker may be active
- EXECUTION_HISTORY.jsonl is append-only. No edits. No deletes. Gaps are logged, not backfilled.

---

## 10. Terminal/Session Reset Handling

When the agent reconnects to a fresh terminal or session:

1. Immediately run bootstrap checks (Section 6)
2. Do not assume any prior state — variables, working directory, and memory are all reset
3. Read `status/NEXT_ACTIONS.md` to establish human-authored intent
4. Check `EXECUTION_HISTORY.jsonl` for any in-flight workflows
5. Only then communicate with the human

---

## 11. When to Halt vs. Resume

| Condition | Decision |
|---|---|
| Canon file modified | **HALT** — requires human review |
| Unresolved HIGH-risk conflict | **HALT** — requires DEC escalation |
| Duplicate task detected | **HALT** — requires human confirmation |
| Validator FAIL | **HALT** — requires governance remediation |
| No governance artifact found for workflow | **HALT** — require explicit human authorization |
| Context too sparse to determine intent | **ASK** — provide what was found, ask for missing context |
| All bootstrap checks pass, state clear | **RESUME** — proceed per recovery manifest |

---

## 12. Definition of Done

Recovery is complete when ALL of the following are true:

- [ ] Bootstrap checks (Section 6) all pass
- [ ] Current branch and remote confirmed
- [ ] Last known workflow state reconstructed from repo files
- [ ] No duplicate executions detected
- [ ] No canon files modified during recovery
- [ ] runtime_state_validator.py returns PASS
- [ ] Next action identified and communicated to human
- [ ] All created/modified files committed and pushed (if governance scope)
- [ ] EXECUTION_HISTORY.jsonl entry appended for recovery event

---

## Related Files

- `runtime/SESSION_RECOVERY_CHECKLIST.md` — step-by-step bootstrap checklist
- `runtime/EXECUTION_RESUME_MANIFEST.md` — resumable workflow manifest format
- `operations/HUMAN_API_DEPENDENCY_LOG.md` — human dependency and failure log
- `status/NEXT_ACTIONS.md` — human-authored next action register

---

*Append-only. Protocol changes require Wolfpack governance approval.*