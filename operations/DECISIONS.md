# Initial Architectural Decisions

- OpenClaw will act as persistent operational memory infrastructure
- Human API doctrine is officially adopted
- Conversational realism is prioritized before feature expansion
- Voice interaction quality is the current primary product surface
- Operational lessons must be documented continuously
- Async websocket systems should use block/function replacement strategies during debugging
- Minimize human engineering actions whenever possible
---

# DEC-001 — Corrected v0.1 Architecture: OpenClaw Demoted to Replaceable Execution Worker

**Date:** 2026-05-23
**Decision:** Approve architecture correction
**Task:** task_002

## Context

The v0.1 canon incorrectly positioned OpenClaw/ClawBro as the "primary control plane" and "central OS" of the Wolfpack system. This documentation error introduced risk of future architectural decisions being made on incorrect premises.

## Decision

Correct the v0.1 architecture to accurately reflect runtime roles:

| Component | Corrected Role | Replaceable |
|---|---|---|
| ChatGPT/Eterna | Cognitive orchestration layer | No (core identity) |
| GitHub | Institutional memory, task bus, canonical state | No (canonical source) |
| Deterministic workflows / GitHub Actions / n8n | Preferred orchestration layer | Low (portable) |
| OpenClaw/ClawBro | Replaceable execution worker | Yes (swappable) |
| Human API | Governance gate, exception handling | N/A |

## Rationale

- OpenClaw is a replaceable execution worker in practice — not the primary control plane
- ChatGPT/Eterna owns cognitive orchestration — the actual reasoning layer
- GitHub owns institutional memory and canonical state — the actual source of truth
- Deterministic workflows own orchestration scheduling — the actual automation layer
- OpenClaw remains available as optional sandbox/execution infrastructure when preferred

## Risk Assessment

- **Documentation-only change** — no production code affected
- **Trivial rollback** — revert git commit `6d7e009`
- **Zero operational risk** — corrects rather than changes system behavior
- **Net positive** — eliminates risk of incorrect future architectural decisions

## Status

`approved` — implementation pending

## References

- Task: `tasks/inbox/task_002.md`
- Result: `tasks/results/task_002_RESULT_validated_20260523T043458Z.md`
- Wolfpack Review: All 4 roles approved (Opportunity Radar, Red Team, Deployment Governor, Memory Keeper)

---

*Decision: DEC-001 — 2026-05-23*

---

# DEC-002 — Intake Summary Webhook Candidate

**Date:** 2026-05-23
**Decision:** Pending implementation approval — candidate once blocked conditions resolved
**Task:** task_003

## Context

The Wolfpack review for task_003 evaluated a proposal to add an intake summary webhook to Alice (voice_receptionist.py). The review was scoped as review-only with no implementation. The Wolfpack review concluded the feature is a viable future implementation candidate subject to blocked conditions being resolved.

## Decision

Designate the intake summary webhook as a **future implementation candidate** pending resolution of the following blocked conditions:

| # | Blocked Condition | Resolution Required |
|---|---|---|
| 1 | Webhook URL env var | `INTAKE_SUMMARY_WEBHOOK_URL` env var used — no hardcoded URLs |
| 2 | Async fire + 5s timeout | Call cleanup must not block on webhook delivery |
| 3 | Error handling | On failure: log error, do not propagate, call continues |
| 4 | No CRM writes or auto-followups | Single POST only — no external system writes |
| 5 | No new dependencies | Use existing httpx or requests only |
| 6 | Preflight validation | Must pass: no `input_audio_transcription`, no `recordings.create` |
| 7 | Post-deploy smoke test | Live call test confirming no cleanup delays |

## Opportunity Assessment

- **Priority:** 4/5 (high operational value, clear customer need)
- **Risk Level:** medium (webhook timeout surface, mitigated by async + timeout guard)
- **Rollback:** Trivial — remove function and call site, revert to `91e4735`
- **Dependencies:** None (httpx/requests already present)

## Wolfpack Review Summary

| Role | Decision |
|---|---|
| Opportunity Radar | high — candidate for implementation |
| Red Team | acceptable (with blocked conditions) |
| Deployment Governor | pending implementation approval |
| Memory Keeper | endorses — no memory fragmentation |

## Status

`pending implementation approval` — blocked until conditions resolved

## References

- Task: `tasks/inbox/task_003.md`
- Result: `tasks/results/task_003_RESULT_validated_20260523T044442Z.md`
- Wolfpack Review: All 4 roles evaluated (Opportunity Radar, Red Team, Deployment Governor, Memory Keeper)

---

*Decision: DEC-002 — 2026-05-23*
