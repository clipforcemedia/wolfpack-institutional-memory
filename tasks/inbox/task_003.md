---
title: "Task 003 — Intake Summary Webhook: Review-Only Proposal"
document_type: "document"
status: "active"
version: "0.1"
created: "2026-05-23"
updated: "2026-05-23"
source_type: "internal"
provenance: "wolfpack-institutional-memory"
tags:
  - "task_003"
  - "wolfpack"
related_ids:
  - "task_003"
append_only: false
---
# Task 003 — Intake Summary Webhook: Review-Only Proposal

**Task ID:** task_003
**Timestamp:** 2026-05-23T04:44:00Z
**Status:** pending_review
**Workflow Type:** wolfpack_review
**Requested Outputs:** Opportunity/Value Review, Red Team Risk Review, Deployment/Governance Review, Memory/Continuity Review, v0.1 Safe Rollout Recommendation, Blocked Conditions, Definition of Done
**Proposed by:** Eterna
**Linked repo:** clipforcemedia/voice-ai

---

## Proposal Summary

Add an intake summary webhook to Alice (voice_receptionist.py) that fires after a successful call ends. The webhook produces a structured operational summary event containing:

- call_sid
- caller_number (phone)
- call_start_time
- call_end_time
- intake_type (appointment_booked | message_taken | transfer_requested | general_inquiry)
- intake_data (structured summary of what was collected)
- timestamp (UTC ISO-8601)

**This task is REVIEW-ONLY.** No implementation, no code changes, no deployment. The output of this task is a Wolfpack review recommending whether and how to safely implement this feature — or blocking conditions that must be met before consideration.

---

## Strict Scope Constraints

This task explicitly prohibits:
- **No voice-ai code changes** — review only, no implementation
- **No deployment** — no push to main, no Render deploy
- **No external API calls** — webhook is a design concept, not an implementation
- **No recording** — no recordings.create, no recording webhook
- **No transcription** — no input_audio_transcription
- **No CRM writes** — no external system writes
- **No auto-followups** — no automated outbound actions after webhook fires

The Wolfpack review should evaluate whether the design is safe to implement given these constraints, and define blocked conditions if the feature cannot be safely implemented under v0.1 constraints.

---

## Motivation

After each call, Alice produces a structured event that captures the outcome of the call. Currently, call outcomes are logged as webhook POSTs to the admin URL on specific events (appointment booked, message taken, transfer). An intake summary webhook would consolidate all call outcomes into a single structured event regardless of outcome type.

This is valuable for:
- Admin dashboards consuming call records
- CRM integrations receiving structured call outcomes
- Memory pipeline ingesting call summaries
- Audit trail completeness

---

## Files Allowed (if approved in future)

- `voice_receptionist.py` — add `_fire_intake_summary()` function and call site
- `operations/DEPLOY_LOG.md` — append if approved and deployed
- `operations/INCIDENT_LOG.md` — append if rollback required

---

## Files Forbidden

- No changes to `requirements.txt` (must use existing httpx or requests)
- No `.env` or credential files
- No `input_audio_transcription` configuration
- No `recordings.create` or recording webhook
- No Twilio recording configuration

---

## Risk Level

`medium`

Reasons for medium rating:
- Adds outbound HTTP call — potential timeout and error surface
- Introduces new failure mode (webhook delivery failure)
- However: no PII beyond existing call log scope, rollback is trivial

---

## Rollback Target

Commit: `91e4735c37daac67289f690c27e9a3a3962a13f3` (clean 408-line build — pre-intake-webhook)

---

## Validation Commands

```bash
# Syntax check (if implementation proposed)
python3 -m py_compile voice_receptionist.py

# No new dependencies (httpx or requests already present)
grep "httpx\|requests" requirements.txt

# No forbidden API fields
grep "input_audio_transcription" voice_receptionist.py && echo "BLOCKED" || echo "CLEAN"
grep "recordings.create\|recording_webhook" voice_receptionist.py && echo "BLOCKED" || echo "CLEAN"

# Rollback command (if approved)
git push https://TOKEN@github.com/clipforcemedia/voice-ai.git 91e4735:main
```

---

## Expected Outputs

1. **Opportunity/Value Review** — Does this serve a documented customer need or revenue path?
2. **Red Team Risk Review** — What are the failure modes? Are any blocked under v0.1 constraints?
3. **Deployment/Governance Review** — Can this be approved under current Wolfpack governance?
4. **Memory/Continuity Review** — Does this affect state management or institutional memory?
5. **v0.1 Safe Rollout Recommendation** — Proceed / Block / Conditions for proceed
6. **Blocked Conditions** — What must be true before this could be considered for implementation?
7. **Definition of Done** — What would a safe implementation look like?

---

## Append-Only Log Requirement

This task, its reviews, and its outcome will be logged in:
- `tasks/inbox/task_003.md` (this file — preserved, never deleted)
- `tasks/results/task_003_RESULT_*.md` (generated by runner)
- `operations/DECISIONS.md` (if decision reaches decision record)
