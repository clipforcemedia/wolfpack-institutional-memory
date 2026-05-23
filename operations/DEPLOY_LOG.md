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