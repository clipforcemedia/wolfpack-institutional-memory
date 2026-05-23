# System Architecture — voice-ai / Wolfpack v0.1

**Effective:** 2026-05-22
**Status:** Authoritative

---

## 1. System Overview

```
ChatGPT/Eterna
    └── Cognitive orchestration layer
    └── Task decomposition and decision synthesis

GitHub (clipforcemedia/voice-ai, clipforcemedia/wolfpack-institutional-memory)
    └── Institutional memory — canonical source of truth
    └── Versioned deployment artifacts
    └── Task bridge transport (public read, PAT write)
    └── Wolfpack governance docs

Workflow Orchestration
    └── GitHub Actions for CI/CD
    └── OpenClaw cron for polling/institutional tasks
    └── Append-only logs for audit trail

Execution Workers
    └── OpenClaw — primary agent runtime
    └── Render — voice_ai FastAPI deployment
    └── Twilio — phone line and media streams
    └── OpenAI Realtime API — voice AI brain

Governance
    └── Wolfpack review gate (6 roles)
    └── Deployment Governor approval
    └── Append-only deploy log
    └── Incident log for rollback events
```

---

## 2. Component Inventory

### 2.1 voice-ai Repo (`clipforcemedia/voice-ai`)
- **Purpose:** Production AI receptionist code
- **Key file:** `voice_receptionist.py` — FastAPI + Twilio Media Streams + OpenAI Realtime
- **Deployment:** Render (auto-deploys from `main`)
- **Governance:** Deployment Governance Checklist required before push

### 2.2 wolfpack-institutional-memory Repo
- **Purpose:** Operational intelligence infrastructure — canon, operations, decisions, logs
- **Structure:**
  - `canon/` — authoritative doctrine and architecture
  - `operations/` — deploy log, incident log, decisions, lessons learned
  - `opportunities/` — business opportunities, validation queue
  - `agents/` — role definitions (Eterna, Red Team, Deployment Governor, etc.)
  - `status/` — current state, blocked features, next actions
  - `tasks/inbox/` — pending task specs
  - `tasks/results/` — completed task results
  - `workflows/` — Wolfpack review workflow

### 2.3 OpenClaw
- **Purpose:** Replaceable execution worker — not the operating system
- **Functions:**
  - GitHub push (direct deployment)
  - Task spec execution
  - Cron-based polling (GitHub task bridge)
  - Operational documentation
- **Limitations:** Cannot self-modify canon, cannot bypass Wolfpack gate

### 2.4 Render
- **Purpose:** Production hosting for `voice_receptionist.py`
- **Deployment:** Auto-deploys from `main` branch
- **Health:** `/health` endpoint — returns `{"status": "ok"}`

### 2.5 Twilio
- **Purpose:** Phone line and real-time audio streaming
- **Interface:** TwiML webhook + WebSocket media stream
- **Integration:** `voice_receptionist.py` handles inbound calls and outbound TwiML

### 2.6 OpenAI Realtime API
- **Purpose:** Voice AI brain — real-time transcription, LLM response, tool calling
- **Model:** `gpt-4o-realtime-preview` or `gpt-realtime-2` (GA Realtime)
- **Scope:** Audio I/O only (not text + audio simultaneously)

---

## 3. Data Flow

### 3.1 Production Call Flow

```
Incoming call → Twilio → /inbound webhook
    → TwiML redirect to /stream/{call_sid}
    → WebSocket audio stream to OpenClaw
    → OpenAI Realtime (session.update + conversation loop)
    → Tool calling (book_appointment, take_message, transfer_to_human)
    → Audio response → Twilio → Caller
```

### 3.2 Deployment Flow

```
ChatGPT/Eterna task → GitHub task file (public)
    → OpenClaw polls → downloads → validates → executes
    → GitHub push to main → Render deploy
    → Health check → Live call test
    → Append-only deploy log
    → Wolfpack review gate (pre-deploy)
```

### 3.3 Governance Flow

```
Proposed change → Scope check → Preflight validation
    → Wolfpack review (6 roles) → Deployment Governor approval
    → Push to main → Render deploy
    → Post-deploy validation → Deploy log entry
    → Incident log if rollback needed
```

---

## 4. Forbidden Architectural Patterns

| Pattern | Reason |
|---|---|
| OpenClaw as central OS | OpenClaw is a replaceable execution worker, not the operating system |
| Autonomous deployment without gate | Wolfpack review required before all production pushes |
| Secrets in workspace | All secrets must be in `~/.openclaw/secrets/` or native secrets management |
| Agent self-modification | No component modifies its own directives without human review |
| Fragmented memory | GitHub is the canonical source of truth; workspace is derived |
| Hype-driven infrastructure | Every component must serve a defined operational purpose |

---

## 5. Communication Protocols

| Protocol | Use |
|---|---|
| GitHub raw URL | Public task spec transport (read-only for OpenClaw) |
| GitHub PAT + git push | OpenClaw deployment write path |
| Append-only logs | Deploy log, incident log, decision log |
| OpenClaw cron | Polling for GitHub task bridge |
| WebSocket | Real-time audio between Twilio and OpenClaw |

---

## 6. Version and State

| Component | Version | Notes |
|---|---|---|
| Canon | v0.1 | Corrected 2026-05-22 |
| voice_receptionist.py | 91e4735 | Stable realtime, 408 lines |
| OpenClaw | 2026.4.26 | Primary execution worker |
| Render | auto-deploy | Deploys from main |
| Twilio | active | Phone line active |
| OpenAI Realtime | GA | gpt-4o-realtime-preview |

---

*Architecture maintained in `canon/SYSTEM_ARCHITECTURE.md` — syncs to workspace `operations/SYSTEM_ARCHITECTURE.md`*