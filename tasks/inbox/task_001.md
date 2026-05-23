# Task 001 — Example Operational Proposal: Add Intake Summary Webhook

**Task ID:** task_001
**Timestamp:** 2026-05-23T03:47:00Z
**Status:** pending_review
**Proposed by:** Eterna
**Linked repo:** clipforcemedia/voice-ai

---

## Proposal Summary

Add an intake summary webhook to `voice_receptionist.py` that fires after every completed call intake. The webhook POSTs a JSON payload containing caller name, phone, reason, appointment details (if any), and timestamp to an admin-configurable URL.

---

## Motivation

Currently, call intake data is logged to the admin webhook only on specific events (appointment booked, message taken, transfer requested). An intake summary webhook would consolidate all intake data into a single payload after each call, making it easier for admin dashboards to ingest and display call records.

---

## Scope

### Files Allowed
- `voice_receptionist.py` — add `_fire_intake_summary()` function and call after call end
- `operations/DEPLOY_LOG.md` — append deployment entry
- `operations/INCIDENT_LOG.md` — append incident entry if rollback required

### Files Forbidden
- `requirements.txt` — no new dependencies (using existing `httpx` or `requests`)
- `.env` or any file with live credentials

---

## Proposed Implementation

```python
def _fire_intake_summary(call_sid: str, caller_number: str, intake_data: dict):
    """Fire intake summary webhook — called after each completed call."""
    url = os.environ.get("INTAKE_SUMMARY_WEBHOOK_URL", "")
    if not url:
        return
    payload = {
        "call_sid": call_sid,
        "caller_number": caller_number,
        "intake": intake_data,
        "timestamp": datetime.utcnow().isoformat()
    }
    try:
        requests.post(url, json=payload, timeout=5)
    except Exception as e:
        log.error(f"Intake summary webhook failed: {e}")
```

Called at call end (before cleanup) with collected intake state.

---

## Risk Level

`medium`

Reasons:
- Adds outbound HTTP call — potential timeout and error surface
- No PII stored beyond existing call log scope
- Rollback is trivial — remove function and call site

---

## Rollback Target

Commit: `91e4735c37daac67289f690c27e9a3a3962a13f3` (clean 408-line build)

---

## Validation Commands

```bash
# Syntax check
python3 -m py_compile voice_receptionist.py

# No new dependencies
grep "requests\|httpx" requirements.txt  # should be unchanged or already present

# No input_audio_transcription
grep "input_audio_transcription" voice_receptionist.py && echo "BLOCKED" || echo "CLEAN"

# No recordings.create
grep "recordings.create\|recording_webhook" voice_receptionist.py && echo "BLOCKED" || echo "CLEAN"

# Rollback command
git push https://TOKEN@github.com/clipforcemedia/voice-ai.git 91e4735:main
```

---

## Expected Outputs

1. Wolfpack Red Team Review (failure mode analysis)
2. Memory Keeper Continuity Review (state management audit)
3. Deployment Governor Decision (approve / block)
4. Eterna Final Recommendation
5. Next Action (proceed to implement or close task)
6. Definition of Done

---

## Append-Only Log Requirement

This task, its reviews, and its outcome will be logged in:
- `tasks/inbox/task_001.md` (this file — preserved, never deleted)
- `tasks/results/task_001_RESULT_TEMPLATE.md` (filled by Wolfpack reviewers)
- `operations/DEPLOY_LOG.md` (if approved and deployed)

---

*This is an example task demonstrating the deterministic Wolfpack review workflow.*
*Not a real deployment proposal.*