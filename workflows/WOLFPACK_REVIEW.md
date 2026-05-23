# Wolfpack Review — Workflow and Protocol

**Effective:** 2026-05-22
**Status:** Authoritative

---

## 1. Overview

Wolfpack review is the mandatory governance gate for all production code changes. Six roles participate; all must affirm before Deployment Governor approves push. Any role can block — blocked means halted until concern is resolved.

---

## 2. Roles and Affirmations

| Role | Responsibility | Must Affirm |
|---|---|---|
| **Operator** | Confirms sequence of changes is intentional | ✓ |
| **Architect** | Confirms system integrity — no breaking changes to call flow | ✓ |
| **Critic** | Identifies failure modes — acceptable or not | ✓ |
| **Compliance** | Checks privacy, data, legal exposure | ✓ |
| **Economist** | Confirms revenue or operational value | ✓ |
| **Deployment Governor** | Final approval or block | ✓ (final) |

---

## 3. Review Triggers

Wolfpack review is required for:
- All production pushes to `main` on `clipforcemedia/voice-ai`
- New feature introductions
- Changes to governance procedures
- New external integrations (Twilio, Stripe, OpenAI)
- Any change to `voice_receptionist.py`

Wolfpack review is **not** required for:
- Documentation-only changes (ops docs, canon updates)
- Task specs and task bridge changes
- Workspace operational files (no production impact)

---

## 4. Review Protocol

### Step 1 — Submit for Review

Before any production push, the proposing agent (Eterna or OpenClaw) must:
1. Fill out `DEPLOYMENT_GOVERNANCE_CHECKLIST.md` (scope, preflight, rollback)
2. Post the checklist to the current session / review context
3. Request explicit affirmation from each role

### Step 2 — Role Affirmations

Each role responds with one of:

```
OPERATOR: confirmed
ARCHITECT: confirmed
CRITIC: [concern noted] — [acceptable / not acceptable]
COMPLIANCE: confirmed
ECONOMIST: confirmed
GOVERNOR: [approve / block] — [reason if blocked]
```

### Step 3 — Governor Decision

If all roles affirm → Governor approves → push proceeds
If any role blocks → push halts → concern must be resolved → re-review

### Step 4 — Post-Deploy Validation

After push, Deployment Governor confirms:
- Render boot confirmed
- Health endpoint returns 200
- Live call test (if voice code changed)
- Logs reviewed for errors

---

## 5. Emergency Exception

Recovery pushes (rollbacks, incident resolution) may proceed with abbreviated Wolfpack review:
- Governor may approve on behalf of all roles if time is critical
- Post-incident review must occur within 24 hours
- Incident log updated with abbreviated review reasoning

---

## 6. Review Record

All Wolfpack reviews are logged in `operations/DEPLOY_LOG.md` with:
- Deployment ID
- Wolfpack gate result (affirmations or blocks)
- Governor decision
- Post-deploy validation result

---

## 7. Template

```
=== WOLFPACK REVIEW ===

Proposed: <what>
Commit: <hash>
Scope: <objective>
Risk: <level>
Rollback: <commit>

OPERATOR: <affirm/block>
ARCHITECT: <affirm/block>
CRITIC: <affirm/block + concern if any>
COMPLIANCE: <affirm/block>
ECONOMIST: <affirm/block>
GOVERNOR: <approve/block>

=== RESULT ===
```

---

*Workflow maintained in `workflows/WOLFPACK_REVIEW.md`*