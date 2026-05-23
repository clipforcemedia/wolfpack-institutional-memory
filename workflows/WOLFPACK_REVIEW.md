# Wolfpack Review Workflow — Deterministic Review Protocol

**Effective:** 2026-05-23
**Version:** 0.1
**Applies to:** All production proposals on `clipforcemedia/voice-ai`

---

## 1. Workflow Purpose

The Wolfpack Review Workflow is a deterministic, governance-gated review protocol for all production code changes. It converts the 6-role Wolfpack review into a structured, append-only, auditable workflow with defined inputs, processing stages, governance stages, and output requirements.

The goal is **repeatable governance** — not ad-hoc review. Every proposal goes through the same stages. Every output is logged. Every decision is documented.

---

## 2. Input Requirements

Every task submitted for Wolfpack Review must include:

| Field | Required | Description |
|---|---|---|
| Task ID | ✓ | Format: `task_NNN` |
| Timestamp | ✓ | ISO-8601 UTC |
| Status | ✓ | `pending_review` |
| Proposal Summary | ✓ | What this change does and why |
| Motivation | ✓ | What customer need or revenue path this serves |
| Files Allowed | ✓ | Explicit list — nothing outside this scope |
| Files Forbidden | ✓ | Explicit list — nothing in this scope |
| Risk Level | ✓ | `low` / `medium` / `high` / `critical` |
| Rollback Target | ✓ | Commit hash of known-good state |
| Validation Commands | ✓ | Exact commands to verify preflight checks |
| Expected Outputs | ✓ | List of outputs the workflow will produce |

---

## 3. Processing Stages

### Stage 1 — Intake Validation
**Owner:** OpenClaw (execution worker)

1. Receive task spec from `tasks/inbox/` or GitHub task bridge
2. Validate all required fields present (see Input Requirements)
3. If incomplete → return `incomplete_task` with list of missing fields
4. If complete → assign `task_XXX.md` and advance to Stage 2
5. Log intake in `tasks/pull_log.json` or `tasks/pull_history.jsonl`

### Stage 2 — Preflight Validation
**Owner:** OpenClaw (execution worker)

Run for every proposed change:
```bash
# 1. Syntax check
python3 -m py_compile voice_receptionist.py

# 2. Secrets scan
git diff HEAD~1 | grep -iE "secret|token|key|password" || echo "CLEAN"

# 3. Forbidden API fields
grep "input_audio_transcription\|recordings\.create\|recording_webhook" voice_receptionist.py && echo "BLOCKED" || echo "CLEAN"

# 4. Changed files
git diff --name-only HEAD~1

# 5. Scope verification — changed files must be in Files Allowed list
```

If any preflight check fails → **halt** → return failure reason to Eterna → do not advance.

### Stage 3 — Wolfpack Routing
**Owner:** OpenClaw (execution worker)

After preflight passes, route to each reviewer role in parallel:
- `opportunities/OPPORTUNITY_BRIEFS.md` → Opportunity Radar
- `agents/RED_TEAM.md` → Red Team
- `agents/DEPLOYMENT_GOVERNOR.md` → Deployment Governor
- `agents/MEMORY_KEEPER.md` → Memory Keeper

Each reviewer fills their section in `tasks/results/task_XXX_RESULT_TEMPLATE.md`.

---

## 4. Governance Stages

### Stage 4 — Opportunity Radar Review
**Owner:** Opportunity Radar

Reviews: market alignment, revenue potential, priority score
Output: `OPPORTUNITY_RADAR_REVIEW` section in result template

### Stage 5 — Red Team Review
**Owner:** Red Team

Reviews: failure modes, rollbackability, unsupported API fields
Output: `WOLFPACK_RED_TEAM_REVIEW` section in result template

### Stage 6 — Deployment Governor Review
**Owner:** Deployment Governor

Reviews: scope, risk, rollback target, all preflight checks
Output: `DEPLOYMENT_GOVERNOR_REVIEW` section in result template

### Stage 7 — Memory Keeper Continuity Review
**Owner:** Memory Keeper

Reviews: state management, memory fragmentation, secrets exposure, canon adherence
Output: `MEMORY_KEEPER_CONTINUITY_REVIEW` section in result template

### Stage 8 — Final Eterna Synthesis
**Owner:** Eterna

Synthesizes all reviewer inputs into final recommendation
Output: `FINAL_ETERNA_RECOMMENDATION` + `DECISION` sections

### Stage 9 — Decision and Logging
**Owner:** Deployment Governor

Final decision: `proceed` / `block` / `close_no_action` / `revise_and_resubmit`
Decision logged in:
- `tasks/results/task_XXX_RESULT_TEMPLATE.md` (filled, preserved)
- `operations/DEPLOY_LOG.md` (if approved and deployed)
- `operations/INCIDENT_LOG.md` (if rollback required)

---

## 5. Output Requirements

Every Wolfpack review produces:

| Output | File | Preservation |
|---|---|---|
| Reviewer inputs | `tasks/results/task_XXX_RESULT_TEMPLATE.md` | Append-only — never edited after submission |
| Final decision | `tasks/results/task_XXX_RESULT_TEMPLATE.md` | Append-only |
| Deployment record | `operations/DEPLOY_LOG.md` | Append-only |
| Incident record | `operations/INCIDENT_LOG.md` | Append-only (if rollback triggered) |

---

## 6. Append-Only Logging Rules

| Rule | Description |
|---|---|
| **No deletion** | Task specs, results, and log entries are never deleted — only updated with new status |
| **No in-place edits** | Completed review sections are written once and preserved |
| **No retroactive changes** | If a decision changes, a new log entry is appended — original entry preserved |
| **No secret values in logs** | Secrets never appear in task specs, results, or log entries |
| **No full diffs in logs** | Only file names and summary lines in deploy log — full diffs in git only |

---

## 7. Rollback and Governance Requirements

### Rollback Trigger Conditions
- Governor blocks → task closed, no push
- Post-deploy validation fails → rollback to target commit
- Incident triggers → rollback, incident log entry, post-mortem

### Rollback Protocol
```bash
git push https://TOKEN@github.com/clipforcemedia/voice-ai.git ROLLBACK_COMMIT:main
```

### Post-Rollback Validation
1. Confirm push succeeded: `git log --oneline -3`
2. Notify Deployment Governor
3. Log incident in `operations/INCIDENT_LOG.md`
4. Do not re-push until root cause identified

### Emergency Exception
Recovery pushes (rollbacks, incident resolution) may proceed with abbreviated review:
- Governor may approve on behalf of all roles if time is critical
- Post-incident review must occur within 24 hours
- Incident log updated with abbreviated review reasoning

---

## 8. Workflow Template Files

| File | Purpose |
|---|---|
| `tasks/inbox/task_XXX.md` | Task spec — input to the workflow |
| `tasks/results/task_XXX_RESULT_TEMPLATE.md` | Review result template — filled by reviewers |
| `workflows/WOLFPACK_REVIEW.md` | This file — workflow definition |
| `agents/DEPLOYMENT_GOVERNOR.md` | Governor's authority and checklist |
| `agents/RED_TEAM.md` | Red Team failure mode checklist |
| `agents/MEMORY_KEEPER.md` | Memory Keeper continuity requirements |
| `agents/OPPORTUNITY_RADAR.md` | Opportunity Radar scoring |

---

## 9. Status Transitions

```
pending_review
    ↓ [intake validated]
intake_complete
    ↓ [preflight passed]
preflight_passed
    ↓ [routed to reviewers]
in_review
    ↓ [all sections filled]
review_complete
    ↓ [Governor decision]
approved → proceed to implementation
blocked → task closed, no deployment
close_no_action → task closed, no deployment
revise_and_resubmit → task revised, re-enters workflow
```

---

*Workflow defined in `workflows/WOLFPACK_REVIEW.md` — version 0.1, 2026-05-23*