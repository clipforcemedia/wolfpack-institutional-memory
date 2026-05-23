# Next Actions — Wolfpack / voice-ai

**Updated:** 2026-05-23

---

## Active Milestones

| Milestone | Status | Notes |
|---|---|---|
| 001 — First Stable Local Agent Loop | ✓ Complete | 2026-05-21 |
| 002 — GitHub Task Bridge Proof of Life | ✓ Complete | 2026-05-21 |
| 002b — Full GitHub Task Pull Bridge | ✓ Complete | 2026-05-21 |
| 003 — Autonomous GitHub Polling | ✓ Complete | 2026-05-21 |
| 004 — OpenClaw Direct GitHub Deployment | ✓ Complete | 2026-05-22 |
| 005 — Canonical Initialization Audit | ✓ Complete | 2026-05-20 |
| 006 — Machine-Executable Workflow Layer | ✓ Complete | 2026-05-23 |

---

## Next Action

| # | Action | Owner | Priority | Status |
|---|---|---|---|---|
| 1 | Create first real (non-example) wolfpack_review task | Eterna / Wolfpack | high | pending |

---

## Implementation Notes

### First Real Wolfpack Review Task

The runner has been validated against `task_001.md` (example task). The next step is to create a real production task that exercises the full wolfpack review pipeline with actual reviewer inputs.

**Requirements for first real task:**
- Must be a genuine production proposal (not an example)
- Must include all required fields per `workflows/WOLFPACK_REVIEW.md`
- Must have a valid rollback target commit
- Must have validation commands that execute cleanly
- Will be routed through: Opportunity Radar → Red Team → Deployment Governor → Memory Keeper → Eterna synthesis

**Candidate scope:**
- Actual voice_ai feature request or bug fix
- Validated against preflight commands
- Approved by Deployment Governor before implementation

---

## Governance Gates

All production deployments require:

1. ✓ Wolfpack Review Gate (6 roles)
2. ✓ Syntax check (`python3 -m py_compile`)
3. ✓ Forbidden API field verification
4. ✓ Rollback target documented
5. ✓ Render smoke test
6. ✓ Alice live call verification (voice code only)

---

## Deferred / Backlog

| Item | Priority | Notes |
|---|---|---|
| Base44 client-facing web app integration | medium | Planned, not started |
| Stripe payment integration | medium | Planned, not started |
| Twilio account provisioning | high | Waiting on account setup |
| OpenAI account provisioning | high | Waiting on account setup |

---

*File maintained in `status/NEXT_ACTIONS.md`*
