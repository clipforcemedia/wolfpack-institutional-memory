---
title: "Next Actions — Wolfpack / voice-ai"
document_type: "document"
status: "active"
version: "0.1"
created: "2026-05-23"
updated: "2026-05-24"
source_type: "internal"
provenance: "wolfpack-institutional-memory"
tags:
  - "wolfpack"
  - "milestone"
  - "dec-001"
related_ids:
  - "dec-001"
  - "task_002"
append_only: false
---
# Next Actions — Wolfpack / voice-ai

**Updated:** 2026-05-24

---

## Active Milestones

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
| 007 — Architecture Correction Canonized (DEC-001) | ✓ Complete | 2026-05-23 |
| 011 — Runtime State Governance Layer Created | ✓ Complete | 2026-05-24 |

---

## Next Action

| # | Action | Owner | Priority | Status |
|---|---|---|---|---|
| 1 | Create first real (non-example) wolfpack_review task | Eterna / Wolfpack | high | ✓ Completed (task_002) |

---

## Runtime Governance Layer

| # | Action | Owner | Priority | Status |
|---|---|---|---|---|
| 1 | Create runtime state governance layer (runtime/) | Eterna / Wolfpack | high | ✓ Complete (2026-05-24) |
| 2 | **Create executable runtime state validator after governance approval** | Eterna / Wolfpack | high | Pending |
| 3 | Batch 002B remaining overlays — OVL-20260524-001 (Strategic Doctrine), OVL-20260524-003 (OS Doc Pack — HIGH) | Eterna / Wolfpack | high | Pending |

---

## Implementation Notes

### DEC-001 Architecture Correction — Implemented

task_002 was the first real wolfpack_review task. All 4 Wolfpack roles (Opportunity Radar, Red Team, Deployment Governor, Memory Keeper) approved the architecture correction. Decision: `approve`.

**Corrected architecture (DEC-001):**
- OpenClaw/ClawBro: Replaceable execution worker (not primary control plane)
- ChatGPT/Eterna: Cognitive orchestration layer
- GitHub: Institutional memory and task bus
- Deterministic workflows/GitHub Actions/n8n: Preferred orchestration layer

**DEC-001 Status:** ✓ Implemented — canon files updated per Definition of Done.

### First Real Wolfpack Review Task (task_002)

**Status:** ✓ Complete — DEC-001 approved and implemented

The first real wolfpack_review task (task_002) was the architecture correction itself. It was validated, reviewed by all 4 Wolfpack roles, approved by Deployment Governor, and the correction was implemented across the canon files.

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

## Stage 1 — Canonical Memory Ingestion

| Step | Action | Owner | Status |
|---|---|---|---|
| 1 | Create canonical memory ingestion plan | Eterna / Wolfpack | ✓ Complete |
| 2 | Execute Stage 1 Batch 001 — ingest core doctrine specs | Eterna / Wolfpack | ✓ Complete |
| 3 | Create Batch 002 PDF source inventory | Eterna / Wolfpack | ✓ Complete |
| 4 | Create governed archival source layer | Eterna / Wolfpack | ✓ Complete |
| 5 | Execute Stage 1 Batch 002A — ingest core memory + governance specs | Eterna / Wolfpack | ✓ Complete |
| 6 | Create Batch 002A source registration workflow | Eterna / Wolfpack | ✓ Complete |
| 7 | Create doctrine overlay reconciliation governance | Eterna / Wolfpack | ✓ Complete |
| 8 | Review MEDIUM overlay-risk doctrine before Batch 002B ingestion | Eterna / Wolfpack | Pending |

**Active Next Action:** Review OVL-20260524-001 (Strategic Doctrine Expansion — MEDIUM) and OVL-20260524-003 (Operating System Doc Pack — HIGH, requires DEC entry) — OVL-20260524-002 (Agent Governance) now canonicalized as agents/AGENT_GOVERNANCE.md

*File maintained in `status/NEXT_ACTIONS.md`*
