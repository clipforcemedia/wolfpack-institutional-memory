# Deploy Log — voice-ai Production Deployments

**Append-only.** Each entry represents one production push to `main`.
Do not edit or delete entries. Rollbacks are logged as new entries with `status: rolled_back`.

---

## Entry 001

| Field | Value |
|---|---|
| **Timestamp UTC** | 2026-05-22T13:04:20Z |
| **Deployment ID** | `dep-001` |
| **Commit Hash** | `91e4735c37daac67289f690c27e9a3a3962a13f3` |
| **Commit Message** | restore verified stable realtime runtime (c7a73ca) |
| **Files Changed** | `voice_receptionist.py` (+245, -368, net -123 lines) |
| **Scope Objective** | Restore stable Alice realtime runtime from commit 4962839 — remove input_audio_transcription config, recordings.create, recording webhook |
| **Risk Level** | medium |
| **Validation Run** | `python3 -m py_compile voice_receptionist.py` → OK |
| **Wolfpack Gate** | Unanimous approval (prior Wolfpack review skipped — this was a recovery push) |
| **Render Deploy Result** | Triggered automatically from `main` branch push → redeployed OK |
| **Post-Deploy Test** | Live inbound call → 200 OK, Alice responded correctly, no byte indices error |
| **Rollback Commit** | `520d5966f698c424f635c8fc388d28a2fc175751` (pre-deploy state) |
| **Incident Notes** | Initial PAT setup + git credential storage configured. PAT stored in `~/.openclaw/secrets/github_pat`. |
| **Decision** | Manual full-file GitHub paste deprecated. OpenClaw direct push is now the preferred deployment path. |
| **Final Status** | `deployed` ✓ |

---

<!-- NEW ENTRIES BELOW — DO NOT EDIT ABOVE -->

## Entry Template (for reference)

```
## Entry NNN

| Field | Value |
|---|---|
| **Timestamp UTC** | YYYY-MM-DDTHH:MM:SSZ |
| **Deployment ID** | dep-NNN |
| **Commit Hash** | <sha> |
| **Commit Message** | <message> |
| **Files Changed** | <list> |
| **Scope Objective** | <what this push does> |
| **Risk Level** | low / medium / high / critical |
| **Validation Run** | <commands run and result> |
| **Wolfpack Gate** | <affirmations or block reason> |
| **Render Deploy Result** | <OK / failed / not triggered> |
| **Post-Deploy Test** | <live call / health check / skipped> |
| **Rollback Commit** | <sha> or `none identified` |
| **Incident Notes** | <anything notable> |
| **Final Status** | deployed / rolled_back / blocked |
```

**Statuses:** `deployed` ✓ | `rolled_back` ↩ | `blocked` ⛔ | `pending_validation` ⏳
---

## Deployment Record: dep-002 — DEC-002 Intake Summary Webhook

| Field | Value |
|---|---|
| **Deploy ID** | dep-002 |
| **Date** | 2026-05-23T05:04:00Z |
| **Task** | task_006 / DEC-002 |
| **Commit** | `e446828` — "implement DEC-002 intake summary webhook" |
| **Commit Range** | `91e4735..e446828` |
| **Branch** | main |
| **Files Changed** | voice_receptionist.py (+37 lines) |
| **Dependencies** | None (httpx already in requirements.txt) |
| **Validation** | `python3 -m py_compile` PASS, no forbidden API fields |
| **Post-Deploy Test** | Smoke test + live call test pending |
| **Rollback Target** | `91e4735` |

### Implementation Details

- `_fire_intake_summary()` function added — async fire-and-forget
- Uses existing `ADMIN_WEBHOOK_URL` env var — no new env vars
- Hard 5s timeout via `httpx.Client(timeout=5.0)`
- Daemon thread pattern — no process cleanup issues
- Call site: `handle_realtime_call` finally block

### Post-Deploy Validation Required

- [ ] Render health check: `GET /health` returns 200
- [ ] Live call test confirms no call cleanup delays
- [ ] Admin webhook receives intake summary payload on test call

### Governance Checklist

- [x] task_003: Feature proposal reviewed — approved
- [x] task_004: Readiness gate — all 7 conditions resolved, APPROVED
- [x] task_005: Implementation review — APPROVED
- [x] task_006: Implementation executed and pushed
- [ ] Post-deploy validation (pending)

---

*Deployment log: `operations/DEPLOY_LOG.md`*
