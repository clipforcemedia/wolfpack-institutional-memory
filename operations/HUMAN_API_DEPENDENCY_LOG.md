---
title: "Human API Dependency Log — Wolfpack"
document_type: "log"
status: "active"
version: "0.2"
created: "2026-05-23"
updated: "2026-05-24"
source_type: "internal"
provenance: "wolfpack-institutional-memory"
tags:
  - "wolfpack"
  - "human-api"
  - "dependency"
  - "incident-log"
  - "append-only"
related_ids:
  - "dec-001"
  - "HAPI-001"
append_only: true
---
# Human API Dependency Log

**Version:** 0.2 | **Status:** Active | **Append-Only:** YES

> **Append-only log.** Entries are never edited or deleted. New entries are added at the top of the Current Cycle section. Archive completed items below the fold. Each entry MUST include: category, subtype, description, root_cause, current_mitigation, future_elimination, severity, status.

---

## Current Cycle

### HAPI-002 — 2026-05-24

| Field | Value |
|---|---|
| **entry_id** | HAPI-002 |
| **category** | RUNTIME_SESSION_RECOVERY |
| **subtype** | AGENT_CONTEXT_LOSS |
| **description** | OpenClaw session refresh caused conversational memory loss and required human to re-provide repo path and workflow context |
| **root_cause** | Execution worker chat/session state is not durable across refresh events |
| **current_mitigation** | Repo-first stateless commands and session recovery protocol (SESSION_RECOVERY_PROTOCOL.md) |
| **future_elimination** | Bootstrap runner that reconstructs execution context from repository state automatically without human input |
| **severity** | HIGH |
| **status** | OPEN |
| **created** | 2026-05-24 |
| **resolution** | — |

### Observed Recovery Behavior: OpenClaw "Complete Last Task"

When OpenClaw stalls or stops responding mid-task, sending `"complete last task"` may resume the last queued execution without re-executing bootstrap. This behavior was observed on 2026-05-24 during session recovery work.

| Field | Value |
|---|---|
| **subtype** | RUNTIME_STALL_RECOVERY |
| **trigger** | Agent stalls or stops responding; human sends `"complete last task"` |
| **outcome** | Resumes last queued execution without re-executing bootstrap |
| **governance constraints** | Allowed only if immediately prior task is known and visible; prohibited after repo mutation outside stalled task; prohibited during production deployment unless rollback state verified first |
| **required after use** | `git status` + `runtime_state_validator.py`; record in HUMAN_API_DEPENDENCY_LOG if governance/production affected |

---

## Archive — Resolved

### HAPI-001 — 2026-05-23

| Field | Value |
|---|---|
| **entry_id** | HAPI-001 |
| **category** | AGENT_IDENTITY |
| **subtype** | GHOST_VOICE |
| **description** | Agent spoke in a group chat without user's explicit direction, violating group chat boundary policy |
| **root_cause** | Agent did not have group context awareness; spoke as if in 1:1 conversation |
| **current_mitigation** | SOUL.md group chat boundary rule; agent now reads chat metadata before responding |
| **future_elimination** | Per-channel context injection at session creation time; group vs. DM flags in session startup |
| **severity** | HIGH |
| **status** | RESOLVED |
| **created** | 2026-05-23 |
| **resolution** | SOUL.md updated with explicit group chat boundary rule; IDENTITY.md filled in |

---

*Append-only. Archive resolved entries below this line. Do not edit or delete log entries.*