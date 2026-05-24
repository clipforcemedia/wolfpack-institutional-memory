---
title: "Incident Log — voice-ai Production Incidents"
document_type: "document"
status: "active"
version: "0.1"
created: "2026-05-23"
updated: "2026-05-23"
source_type: "internal"
provenance: "wolfpack-institutional-memory"
tags:
  - "incident"
  - "milestone"
  - "wolfpack"
related_ids:
  - "inc-001"
  - "dep-001"
  - "milestone 004"
append_only: false
---
# Incident Log — voice-ai Production Incidents

**Append-only.** Each entry represents one production incident — failure, rollback, regression, or governance violation.
Do not edit or delete entries. Resolution is tracked per entry.

---

## Incident 001

| Field | Value |
|---|---|
| **Incident ID** | `inc-001` |
| **Timestamp UTC** | 2026-05-22T13:04:20Z |
| **Affected System** | `voice-ai` / Alice receptionist |
| **Severity** | `high` |
| **Trigger** | Manual full-file paste deployment of modified `voice_receptionist.py`; `input_audio_transcription` config present in session update payload |
| **Symptoms** | static/noisy audio; `unknown_parameter` for `session.input_audio_transcription`; byte indices error; 404 during bad artifact deployment; Twilio `recordings.create` rejected with 21220 |
| **Root Cause** | Unsupported realtime transcription config in session payload; manual full-file paste introduced code corruption; wrong artifact lineage during rollback attempts; REST recording attempt incompatible with current call leg |
| **Impact** | Alice unresponsive during multiple live calls; call intake failures; lead misses |
| **Rollback Action** | OpenClaw pushed commit `91e4735` (restored from commit `4962839`, 408-line clean build) to `main`; Render auto-redeployed |
| **Recovery Validation** | Live inbound call → 200 OK; Alice responded correctly; no byte indices error; no `recordings.create` error; no `input_audio_transcription` error |
| **Prevention Action** | Manual full-file paste deprecated for production; deployment governance checklist required before all pushes; deploy log required; OpenClaw direct GitHub push is preferred deployment path; no recording/transcription changes until stable runtime hold period passes |
| **Linked Deployment** | `dep-001` |
| **Linked Milestone** | Milestone 004 |
| **Final Status** | `resolved` ✓ |

---

<!-- NEW ENTRIES BELOW — DO NOT EDIT ABOOW -->

## Entry Template (for reference)

```
## Incident NNN

| Field | Value |
|---|---|
| **Incident ID** | inc-NNN |
| **Timestamp UTC** | YYYY-MM-DDTHH:MM:SSZ |
| **Affected System** | <system> |
| **Severity** | low / medium / high / critical |
| **Trigger** | <what initiated the incident> |
| **Symptoms** | <observable failures> |
| **Root Cause** | <why it happened> |
| **Impact** | <user-visible or business impact> |
| **Rollback Action** | <what was rolled back and how> |
| **Recovery Validation** | <how recovery was confirmed> |
| **Prevention Action** | <gates or changes to prevent recurrence> |
| **Linked Deployment** | dep-NNN or none |
| **Linked Milestone** | Milestone NNN or none |
| **Final Status** | resolved / ongoing / escalated |
```

**Severities:** `low` (degraded, no user impact) | `medium` (partial outage) | `high` (major user impact) | `critical` (business down)
**Statuses:** `resolved` ✓ | `ongoing` 🔴 | `escalated` ↗ | `blocked` ⛔