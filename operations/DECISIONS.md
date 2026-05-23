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
