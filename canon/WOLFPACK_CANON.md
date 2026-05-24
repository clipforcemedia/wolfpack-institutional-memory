---
title: "Wolfpack Canon — Core Doctrine"
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
# Wolfpack Canon — Core Doctrine

**Version:** 0.1
**Effective:** 2026-05-22
**Status:** Corrected and authoritative

---

## 1. What Wolfpack Is

Wolfpack is **governed operational intelligence infrastructure** — not autonomous AI swarms, not hype-driven agent frameworks, not a self-modifying consciousness.

Wolfpack exists to:
- Reduce repetitive routing, copy/paste, fragmented cognition, and manual state management
- Provide deterministic, auditable, append-only operational intelligence
- Enable autonomous execution within defined governance gates
- Preserve institutional memory across agent sessions and human operators

---

## 2. What Wolfpack Is Not

- **Not autonomous AI agents running without oversight** — Human API reduction means reducing repetitive work, not removing human review gates
- **Not a self-modifying system** — No uncontrolled self-modification, no agent sprawl, no governance bypass
- **Not infrastructure for its own sake** — Every component must serve a defined operational purpose
- **Not a replacement for human judgment** — Wolfpack executes; humans govern

---

## 3. Governing Principles

### 3.1 Corrected v0.1 Architecture

```
ChatGPT/Eterna (cognitive orchestration layer)
    ↓
GitHub (institutional memory — canonical source of truth)
    ↓
Workflow orchestration (GitHub Actions, n8n, explicit task states)
    ↓
Controlled execution workers (OpenClaw, Render, etc.)
    ↓
Append-only logs (deploy log, incident log, decision log)
    ↓
Governance review (Wolfpack review gate before production push)
```

### 3.2 Preferred Orchestration

Deterministic workflows over autonomous agents:
- GitHub Actions for CI/CD
- n8n for business process automation
- Explicit task states (pending → running → done → verified)
- Append-only logs for audit trail
- No event-driven agent loops without governance

### 3.3 Human API Reduction

Human API reduction means:
- Removing repetitive routing steps
- Eliminating copy/paste transport of information
- Consolidating fragmented cognition into unified memory
- Automating manual state management

Human API reduction does **NOT** mean:
- Removing oversight or review gates
- Allowing uncontrolled autonomy
- Bypassing governance checkpoints
- Giving agents self-modifying authority

---

## 4. Forbidden Drift Patterns

The following patterns are **never permitted**:

| Pattern | Description |
|---|---|
| **Agent sprawl** | Proliferating autonomous agents without defined purpose and governance |
| **Hidden autonomy** | Systems that act without human knowledge or review capability |
| **Governance bypass** | Mechanisms that circumvent Wolfpack review gates |
| **Uncontrolled self-modification** | Agents or systems that modify their own logic, memory, or directives |
| **Memory fragmentation** | State split across uncoordinated systems with no unified source of truth |
| **Hype-driven complexity** | Building infrastructure because it's trending, not because it serves a defined need |
| **Autonomous deployment** | Pushing to production without Wolfpack review gate |

---

## 5. Roles and Responsibilities

| Role | Responsibility |
|---|---|
| **ChatGPT/Eterna** | Cognitive orchestration — task decomposition, decision synthesis, doctrine maintenance |
| **GitHub** | Institutional memory — canonical source of truth, versioned artifacts, audit trail |
| **OpenClaw** | Replaceable execution worker — executes defined tasks within defined scope |
| **Wolfpack** | Governance — review gate, architecture integrity, failure mode analysis |
| **Deployment Governor** | Final approval — blocks or approves production pushes |
| **Human Operator** | Ultimate authority — can override any automated decision |

---

## 6. Canon Maintenance

- Canon files live in `canon/` directory of `wolfpack-institutional-memory` repo
- Canon is append-only; corrections are logged as new versions, not overwritten
- Doctrine changes require explicit Wolfpack review and human affirmation
- All canonical documents are synced from this repo to workspace operations docs

---

## 7. Drift Detection

If any of the following are observed, they constitute a governance violation requiring immediate review:

1. OpenClaw executing tasks without corresponding task spec or Wolfpack gate
2. Files modified in workspace without corresponding deploy log entry
3. Secrets or credentials appearing in logs, task outputs, or chat responses
4. Autonomous deployment without governance review
5. Agent modifying its own directives or memory without human review
6. Institutional memory (GitHub) out of sync with workspace state

---

*This canon supersedes any previous Wolfpack doctrine. It is authoritative as of 2026-05-22.*