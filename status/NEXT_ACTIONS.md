# Next Actions — Wolfpack / voice-ai

**Updated:** 2026-05-23
**Status:** Active queue

---

## Immediate (Critical Path)

| # | Action | Priority | Owner | Status |
|---|---|---|---|---|
| 1 | Rotate GitHub PAT (90-day window) | high | Human | pending |
| 2 | Manual GitHub repo creation: `wolfpack-institutional-memory` | high | Human | needed |
| 3 | Push local wolfpack repo to newly created GitHub repo | high | OpenClaw | blocked by #2 |

---

## Short-Term (This Week)

| # | Action | Priority | Owner | Status |
|---|---|---|---|---|
| 4 | Validate Render health endpoint | medium | OpenClaw | pending |
| 5 | Test live call — verify Alice responds correctly | medium | OpenClaw | pending |
| 6 | Set up PAT rotation reminder (90 days from issuance) | medium | Cron | pending |
| 7 | Sync wolfpack-institutional-memory to GitHub after manual repo creation | high | OpenClaw | blocked by #2 |

---

## Governance Hardening

| # | Action | Priority | Owner | Status |
|---|---|---|---|---|
| 8 | Migrate GitHub PAT to OpenClaw native secrets management | medium | OpenClaw | blocked by vault |
| 9 | Add OpenClaw deployment validation cron (health + log check) | low | OpenClaw | pending |
| 10 | Create Wolfpack review session template for chat | low | Eterna | pending |

---

## Product / Business

| # | Action | Priority | Owner | Status |
|---|---|---|---|---|
| 11 | Document pricing tiers ($149/$299/$499) in canonical docs | medium | Eterna | pending |
| 12 | Validate Twilio account status and billing | medium | Human | needed |
| 13 | Set up Stripe webhook for payment confirmation | medium | OpenClaw | pending |

---

## Deferred (Waiting on Dependencies)

| # | Action | Blocked By | Notes |
|---|---|---|---|
| 14 | Wolfpack repo push | Manual repo creation | PAT scope insufficient for API repo creation |
| 15 | PAT native secrets migration | Vault provision | No native GitHub PAT provider yet |

---

*File maintained in `status/NEXT_ACTIONS.md`*