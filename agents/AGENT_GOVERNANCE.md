---
title: "Agent Governance — Wolfpack AI Agent Operational Standards"
document_type: "agent"
status: "active"
version: "1.0"
created: "2026-05-24"
updated: "2026-05-24"
source_type: "external"
provenance:
  source: "WOLFPACK_AGENT_GOVERNANCE_v1.pdf"
  source_type: "external"
  source_url: "archive://wolfpack/batch_002/governance/WOLFPACK_AGENT_GOVERNANCE_v1.pdf"
  ingested_by: "Eterna / Wolfpack"
  ingest_date: "2026-05-24"
  source_pdf: "archive://wolfpack/batch_002/governance/WOLFPACK_AGENT_GOVERNANCE_v1.pdf"
  batch: "STAGE_1_BATCH_002B"
  checksum: "sha256:a42cf500186d6d6796d95c82859c13a6e34a69ba8e97e279ccdcd320b0b47e47"
tags:
  - "ai-agent"
  - "governance"
  - "doctrine"
  - "batch-002"
  - "additive"
related_ids:
  - "OVL-20260524-002"
  - "agents/DEPLOYMENT_GOVERNOR.md"
  - "agents/RED_TEAM.md"
  - "agents/MEMORY_KEEPER.md"
  - "agents/OPPORTUNITY_RADAR.md"
  - "agents/ETERNA_COMMAND.md"
  - "governance/reviews/OVL-20260524-002_REVIEW.md"
append_only: true
---

# Agent Governance — Wolfpack AI Agent Operational Standards

> **Source:** `WOLFPACK_AGENT_GOVERNANCE_v1.pdf`
> **Archive:** `archive://wolfpack/batch_002/governance/WOLFPACK_AGENT_GOVERNANCE_v1.pdf`
> **Overlay Review:** [OVL-20260524-002](./governance/reviews/OVL-20260524-002_REVIEW.md) — Approved Additive Integration
> **Checksum:** `sha256:a42cf500186d6d6796d95c82859c13a6e34a69ba8e97e279ccdcd320b0b47e47`
> **Status:** Active — Canonical Governance Doctrine
> **Activation Date:** 2026-05-24

---

## Purpose

This document establishes formal build-phase doctrine and operational standards for AI agents operating within the Wolfpack ecosystem. The purpose is to:

- Define operational governance standards for all Wolfpack AI agents
- Prevent uncontrolled autonomy, hidden execution, and governance bypass
- Preserve governance integrity, operational survivability, and institutional intelligence

This is **additive doctrine** — it supplements and confirms existing Wolfpack canonical memory without overwriting any existing canonical file.

---

## Core Governance Doctrine

| Doctrine | Description |
|---|---|
| **Agents subordinate to governance** | All Wolfpack agents operate under governance systems, never above them |
| **No rollback/approval bypass** | No agent may bypass rollback or approval mechanisms under any circumstance |
| **Production safety overrides convenience** | Operational safety always takes precedence over automation convenience |

**See also:** [Wolfpack Canon — Core Doctrine](./canon/WOLFPACK_CANON.md)

---

## Agent Functional Taxonomy

Wolfpack agents operate across five functional classes. These are **operational classes** that describe what an agent does — complementary to the role-based definitions in individual agent files.

> **Terminology note:** These class names (Observer, Analyst, Operator, Executor, Governor) are **functional categories** from the AGENT_GOVERNANCE spec. They map to the specific named roles (Eterna, Red Team, etc.) as defined in individual agent files. See the Terminology Mapping section below for the full cross-reference.

| Class | Description | Wolfpack Role Alignment |
|---|---|---|
| **Observer** | Read-only state retrieval — monitors and reports without modification | Maps to [Memory Keeper](./agents/MEMORY_KEEPER.md) — institutional memory monitoring |
| **Analyst** | Summarization and recommendation generation | Maps to [Opportunity Radar](./agents/OPPORTUNITY_RADAR.md) and [Red Team](./agents/RED_TEAM.md) — analysis and recommendation |
| **Operator** | Bounded workflow actions — executes within defined boundaries | Maps to [Eterna](./agents/ETERNA_COMMAND.md) — cognitive orchestration within bounds |
| **Executor** | Approved runtime execution — performs authorized actions | Maps to OpenClaw (replaceable execution worker per DEC-001) |
| **Governor** | Deployment governance authority — final approval for production | Maps to [Deployment Governor](./agents/DEPLOYMENT_GOVERNOR.md) |

---

## Terminology Mapping

This table maps the AGENT_GOVERNANCE functional class names to existing Wolfpack specific role definitions.

| AGENT_GOVERNANCE Class | Wolfpack Role | Relationship | Notes |
|---|---|---|---|
| **Governor** | [Deployment Governor](./agents/DEPLOYMENT_GOVERNOR.md) | Confirmed alignment | Governor class = Deployment Governor role for production deployment authority |
| **Analyst** | [Opportunity Radar](./agents/OPPORTUNITY_RADAR.md) | Maps to | Analyst = Opportunity identification and recommendation |
| **Analyst** | [Red Team](./agents/RED_TEAM.md) | Maps to | Analyst = Failure mode analysis and adversarial review |
| **Observer** | [Memory Keeper](./agents/MEMORY_KEEPER.md) | Maps to | Observer = Read-only institutional memory retrieval and monitoring |
| **Operator** | [Eterna](./agents/ETERNA_COMMAND.md) | Maps to | Operator = Bounded cognitive orchestration and workflow action |
| **Executor** | OpenClaw (replaceable execution worker) | Maps to | Executor = Approved runtime execution (DEC-001 confirms OpenClaw as replaceable worker) |

**Key:** These are two classification systems operating at different levels:
- **Functional classes** (this doc): What the agent does operationally
- **Role definitions** (individual agent files): Who the agent is in the governance system

Both frameworks are compatible and complementary. No terminology conflict exists.

---

## Execution Constraints

| Constraint | Description |
|---|---|
| **Scoped permissions** | All execution requires explicitly scoped permissions — no blanket access |
| **Observability and logging** | All agent actions require full observability and logging |
| **Timeout policies** | Long-running execution loops require defined timeout policies |

**See also:** [Deployment Governor — Production Push Authority](./agents/DEPLOYMENT_GOVERNOR.md) (governance override confirmed)

---

## Approval Policies

| Policy | Description |
|---|---|
| **Irreversible actions require human approval** | Any action that cannot be undone requires explicit human sign-off |
| **Production deployments require governance review** | All production changes go through Wolfpack review gate before deployment |
| **Financial and outbound actions remain restricted** | Any action involving money movement or external communication requires additional approval |

---

## Kill Switch Requirements

| Requirement | Description |
|---|---|
| **Termination capability** | All runtime systems must have a defined termination capability — immediate halt without data loss |
| **Governance override** | Governance systems must be able to override active automation at any time |

> **Note:** Kill switch requirements are additive to existing Wolfpack doctrine. [Deployment Governor](./agents/DEPLOYMENT_GOVERNOR.md) serves as the primary kill switch authority for production deployments. This document establishes that kill switch capability is a required property of all Wolfpack runtime systems.

---

## Incident Handling

| Rule | Description |
|---|---|
| **All failures generate incidents** | Every failed execution attempt must produce an incident record |
| **Repeated failures escalate** | Agents experiencing repeated failures require escalation review |

**See also:** [Incident Log](./operations/INCIDENT_LOG.md)

---

## Definition of Done — Agent Operations

| Criterion | Requirement |
|---|---|
| **Deterministic boundaries** | All agents operate within defined, deterministic governance boundaries |
| **No uncontrolled autonomy** | No Wolfpack agent may exhibit uncontrolled autonomy in production |

---

## Relationship to Existing Wolfpack Canon

| Existing Canon | Relationship |
|---|---|
| [Wolfpack Canon](./canon/WOLFPACK_CANON.md) | Confirmed — "not autonomous AI agents" aligned with Core Governance Doctrine |
| [System Architecture](./canon/SYSTEM_ARCHITECTURE.md) | Confirmed — governance override and execution worker role confirmed |
| [Deployment Governor](./agents/DEPLOYMENT_GOVERNOR.md) | Confirmed — Governor class aligns with DEPLOYMENT_GOVERNOR role |
| [DEC-001 Architecture Correction](./canon/SYSTEM_ARCHITECTURE.md) | Confirmed — Executor class aligns with OpenClaw as replaceable execution worker |

---

## Unresolved Overlap Notes

| Note | Description | Resolution Status |
|---|---|---|
| **Scoped permissions** | Existing agent files do not explicitly define permission scopes | Additive — kill switch and scoped permissions noted as gap-fill for future agent docs |
| **Financial restrictions** | No existing Wolfpack doc explicitly restricts financial actions | Additive — financial restriction doctrine new; should be incorporated into DEPLOYMENT_GOVERNOR.md or a financial governance annex |
| **Functional vs. role taxonomy** | Two classification systems (classes vs. roles) may cause confusion if not explicitly mapped | Resolved — this document provides explicit terminology mapping above |

---

## References

| Reference | Description |
|---|---|
| [OVL-20260524-002 Overlay Review](./governance/reviews/OVL-20260524-002_REVIEW.md) | Full Wolfpack overlay review with 5-role analysis |
| [Overlay Decision Log](./governance/OVERLAY_DECISION_LOG.md) | Decision record for OVL-20260524-002 |
| [Deployment Governor](./agents/DEPLOYMENT_GOVERNOR.md) | Governor role — primary kill switch authority |
| [Wolfpack Canon](./canon/WOLFPACK_CANON.md) | Core doctrine — no uncontrolled autonomy |
| [DEC-001 Architecture Correction](./canon/SYSTEM_ARCHITECTURE.md) | OpenClaw demoted to replaceable execution worker |

---

*Canonical — GitHub is the source of truth. PDFs are archival source material only.*