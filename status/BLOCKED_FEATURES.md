---
title: "Blocked Features — Wolfpack"
document_type: "document"
status: "active"
version: "0.1"
created: "2026-05-23"
updated: "2026-05-23"
source_type: "internal"
provenance: "wolfpack-institutional-memory"
tags:
  - "wolfpack"
related_ids: []
append_only: false
---
# Blocked Features — Wolfpack

**Updated:** 2026-05-23
**Status:** Active — do not implement without explicit Wolfpack review

---

## Blocked Features

| Feature | Blocked Since | Reason | Unblock Requirement |
|---|---|---|---|
| `input_audio_transcription` in Realtime session config | 2026-05-22 | Unsupported in current GA Realtime build; causes `unknown_parameter` errors | Stable hold — not to be re-enabled until Realtime API GA supports it |
| `recordings.create` via Twilio REST during active call | 2026-05-22 | Incompatible with current call leg; returns 21220 error | Requires call flow redesign and separate recording pipeline |
| Full-file manual paste deployment | 2026-05-22 | Causes code corruption and wrong artifact lineage | OpenClaw direct git push is required |
| Autonomous deployment without Wolfpack gate | 2026-05-22 | Governance violation | All production pushes require 6-role Wolfpack review |
| Manual GitHub repo creation via API | 2026-05-23 | PAT scope insufficient for repo creation | Requires fine-grained PAT with `repo` scope or manual creation |
| Recording webhook endpoint | 2026-05-22 | Twilio `recordings.create` rejected; webhook would receive failed recordings | Redesign recording pipeline before re-introducing |

---

## Restricted Features (Require Explicit Approval)

| Feature | Restriction | Rationale |
|---|---|---|
| New environment variables in Render | Must document in deploy log | Secrets exposure risk |
| Changes to `requirements.txt` | Must pass Wolfpack review | Dependency risk |
| New OpenAI API fields | Must verify GA compatibility | Unsupported field risk |
| Changes to Twilio webhook URL | Must validate Twilio accepts | Configuration risk |

---

## Previously Blocked, Now Cleared

| Feature | Cleared | Notes |
|---|---|---|
| OpenClaw direct GitHub push | 2026-05-22 | PAT auth established and validated |
| Append-only deploy log | 2026-05-22 | `operations/DEPLOY_LOG.md` created and operational |
| Wolfpack review gate | 2026-05-22 | 6-role review documented in `DEPLOYMENT_GOVERNANCE_CHECKLIST.md` |

---

*File maintained in `status/BLOCKED_FEATURES.md`*