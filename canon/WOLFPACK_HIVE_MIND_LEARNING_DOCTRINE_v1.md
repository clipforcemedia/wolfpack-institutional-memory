---
title: "Wolfpack Hive Mind Learning Doctrine v1"
document_type: "canon"
status: "active"
version: "1.0"
created: "2026-05-25"
updated: "2026-05-25"
source_type: "internal"
provenance:
  source: "wolfpack-institutional-memory"
  source_type: "internal"
  ingested_by: "Eterna / Wolfpack"
  ingest_date: "2026-05-25"
  batch: "STAGE_1_BATCH_002B"
tags:
  - "canon"
  - "learning"
  - "hive-mind"
  - "governance"
  - "institutional-memory"
  - "batch-002"
related_ids:
  - "canon/WOLFPACK_EXTERNAL_INTELLIGENCE_LAYER_v1.md"
  - "canon/WOLFPACK_CANON.md"
  - "canon/MEMORY_ARCHITECTURE.md"
  - "canon/SYSTEM_ARCHITECTURE.md"
  - "agents/OPPORTUNITY_RADAR.md"
  - "operations/INCIDENT_LOG.md"
  - "operations/LESSONS_LEARNED.md"
  - "runtime/RUNTIME_STATE_GOVERNANCE.md"
  - "DEC-001"
append_only: true
---

# Wolfpack Hive Mind Learning Doctrine v1

> **Stage:** Active — Canonical Governance Doctrine
> **Activation Date:** 2026-05-25
> **Supersedes:** Ad-hoc inter-subsystem communication conventions (none formally documented prior)

---

## 1. Purpose

Wolfpack is a multi-subsystem architecture: External Intelligence Layer, Controlled Spend, Execution Workers, Opportunity Radar, Support Runtime, and Revenue System. Each subsystem generates operational intelligence from its domain.

The **Wolfpack Hive Mind Learning Doctrine** establishes the single governing principle for how all Wolfpack subsystems learn from each other:

> **All Wolfpack subsystems improve each other through structured, auditable, governed institutional memory — never through uncontrolled agent-to-agent autonomy.**

This doctrine closes the loop on every operational event. External signals, spend decisions, worker executions, opportunities, support incidents, and revenue results all feed back into memory to improve future decisions. The goal is governed institutional learning, not uncontrolled autonomous agents that directly command each other.

> **See also:** [Wolfpack Canon — No uncontrolled autonomy](./WOLFPACK_CANON.md)
> **See also:** [Memory Architecture — Institutional memory requirements](./MEMORY_ARCHITECTURE.md)

---

## 2. Core Doctrine

### 2.1 The Governing Principle

**No subsystem may directly command, trigger, or modify another subsystem without going through formal governance channels.**

This is the single most important rule. It means:
- EIL cannot authorize a deployment
- Opportunity Radar cannot spend money
- A runtime failure cannot automatically open a support ticket
- Revenue results cannot autonomously change workflow definitions

Every learning signal from one subsystem flows through: **structured memory entry → scoring/analysis → governance review when required → approved execution when appropriate → validation and logging → lessons learned back into memory**.

### 2.2 The Learning Imperative

**Every operational event is a learning opportunity — if it is not captured in institutional memory, it did not happen.**

The following categories of events MUST be captured in institutional memory:

| Event Type | Memory Location | Captured By |
|---|---|---|
| External intelligence signals | EIL register or `opportunities/` | EIL or Opportunity Radar |
| Spend decisions and outcomes | `operations/` or `decisions/` | Human / Deployment Governor |
| Worker execution results | `runtime/EXECUTION_HISTORY.jsonl` + `tasks/processed_registry.json` | wolfpack_review_runner.py |
| Runtime failures and recoveries | `operations/INCIDENT_LOG.md` | Runtime State Governance |
| Opportunity scores and outcomes | `opportunities/` | Opportunity Radar |
| Support incidents | `operations/INCIDENT_LOG.md` | Support Runtime or Human |
| Deployment outcomes | `deployments/` | Deployment Governor |
| Revenue results | `operations/` or `opportunities/` | Revenue System or Human |
| Lessons learned | `operations/LESSONS_LEARNED.md` | Any Wolfpack role |

### 2.3 Intelligence/Execution Separation

**EIL research may inform controlled spend decisions. EIL research may not trigger spending, deployment, canon mutation, or production changes.**

The path from intelligence to action always requires a human decision point. EIL generates SIG-OPP signals. The controlled spend system receives them. A human approves or rejects the spend.

> **See also:** [External Intelligence Layer — Governance Boundaries](../canon/WOLFPACK_EXTERNAL_INTELLIGENCE_LAYER_v1.md)

---

## 3. Hive Mind Learning Flow

The correct learning flow is a closed, governed loop:

```
external signal / operational event
  ↓
structured memory entry         ← first contact: captured in institutional memory
  ↓
scoring or analysis layer       ← Opportunity Radar, EIL, or Governance scores
  ↓
governance review when required ← Wolfpack review gate; human approval gate
  ↓
approved execution when appropriate ← Deployment Governor; Human API
  ↓
validation and logging          ← wolfpack_review_runner.py; validator stage 8
  ↓
lessons learned back into memory ← LESSONS_LEARNED.md; INCIDENT_LOG; memory entry
  ↓
(future decisions improved by structured institutional memory)
```

### 3.1 Memory Entry Stage

Every event entering the learning loop produces a structured memory entry. The entry must include:
- Event type and classification (SIG-OPP, SIG-RSK, etc.)
- Source subsystem
- Timestamp (ISO-8601 UTC)
- Structured description
- Affected components
- Recommended action (if any)

### 3.2 Scoring / Analysis Stage

The scoring layer applies domain-specific logic:
- **EIL** applies the 4-dimension intelligence scoring model (BI/UR/VR/RE)
- **Opportunity Radar** applies the 5-point opportunity scoring model
- **Runtime State Governance** applies the task state validation model
- **Deployment Governor** applies the deployment readiness assessment

### 3.3 Governance Review Stage

| Signal Type | Review Required |
|---|---|
| SIG-ALR (Alert — active incident) | Immediate human alert; Wolfpack review within 24 hours |
| SIG-RSK (Risk — vendor/EOL/security) | Wolfpack review within 72 hours |
| SIG-OPP (Opportunity — revenue potential) | Opportunity Radar review; human spend gate if spend required |
| SIG-REG (Regulatory) | Legal review; Wolfpack review |
| Spend decision | Deployment Governor + human approval |
| Canon mutation request | DEC entry + Wolfpack review |
| Runtime failure | Runtime State Governance + incident log |
| New opportunity identification | Opportunity Radar brief → Wolfpack review |

### 3.4 Execution Stage

Only approved signals reach execution. Unapproved signals are logged and queued.

### 3.5 Validation and Logging Stage

After execution, the outcome is validated and logged:
- `EXECUTION_HISTORY.jsonl` records task lifecycle
- `RUNTIME_STATE_VALIDATION_REPORT.md` confirms registry integrity
- `INCIDENT_LOG.md` records any failures
- `LESSONS_LEARNED.md` captures the systemic lesson

### 3.6 Lessons Learned Stage

Every execution outcome — success or failure — feeds back into memory:
- **Successful deployments** → Document outcome in `deployments/`
- **Failed deployments** → Incident log + root cause in `INCIDENT_LOG.md`
- **Runtime failures** → Recovery event in `EXECUTION_HISTORY.jsonl` + lessons in `LESSONS_LEARNED.md`
- **Vendor failures** → EIL update + vendor risk re-score + `INCIDENT_LOG.md`
- **Revenue outcomes** → Opportunity Radar outcome record + revenue analysis
- **Support incidents** → `INCIDENT_LOG.md` + improvement action in `LESSONS_LEARNED.md`

---

## 4. EIL Relationship

**EIL research may inform controlled spend decisions.**

EIL generates signals. Those signals are scored and classified. SIG-OPP signals from EIL feed into Opportunity Radar. If EIL identifies a vendor risk (SIG-RSK) that requires migration spend, the controlled spend system receives the signal — but human approval gates all spending.

EIL never directly commands the spend system. The flow is: **EIL signal → structured memory entry → scoring → governance review → human decision on spend**.

EIL findings also improve vendor monitoring: a vendor EOL notice scored by EIL feeds into the vendor watch list update and the next Wolfpack review cycle.

> **See also:** [External Intelligence Layer — Signal Classification](../canon/WOLFPACK_EXTERNAL_INTELLIGENCE_LAYER_v1.md)

---

## 5. Controlled Spend Relationship

**Controlled spend decisions may use EIL and vendor-watch intelligence.**

Before any spend decision is made, the controlled spend system may consult:
- EIL vendor monitoring reports (active SIG-RSK signals)
- Vendor watch list risk scores
- Market positioning intelligence
- Competitor pricing signals

The controlled spend system does not receive autonomous authorization from EIL. The flow is: **vendor intelligence → controlled spend analysis → governance review → human spend approval → execution**.

All spend decisions are logged in `operations/DECISIONS.md` or a dedicated spend log. Spend outcomes feed back into EIL — a vendor migration that costs significant engineering time updates the vendor risk score.

> **See also:** [Runtime State Governance — Worker replaceability](../runtime/RUNTIME_STATE_GOVERNANCE.md)

---

## 6. Worker Relationship

**Worker execution results must feed back into institutional memory.**

The execution worker (OpenClaw) produces structured results on every task cycle. These results are not discarded — they feed the Wolfpack learning loop:

| Worker Output | Learning Destination |
|---|---|
| Task completion record | `EXECUTION_HISTORY.jsonl` + `tasks/processed_registry.json` |
| Validation report | `RUNTIME_STATE_VALIDATION_REPORT.md` |
| Runtime failure record | `operations/INCIDENT_LOG.md` + `LESSONS_LEARNED.md` |
| Deployment outcome | `deployments/` + Wolfpack review |
| Execution gap or anomaly | Wolfpack review gate |

Worker results must not be cached locally outside institutional memory. All task state lives in GitHub. This is the replaceability doctrine from DEC-001: any equivalent worker reading the same task files produces the same results.

The wolfpack_review_runner.py enforces this: Stage 8 runs the runtime state validator after every workflow cycle, and validator failure prevents silent continuation.

> **See also:** [Runtime State Governance — Worker Lifecycle](../runtime/RUNTIME_STATE_GOVERNANCE.md)

---

## 7. Opportunity Radar Relationship

**Revenue outcomes must improve opportunity scoring.**

Opportunity Radar identifies market opportunities. Each opportunity gets a score. The outcome of pursuing (or not pursuing) that opportunity must feed back into the scoring model to improve future scores.

| Opportunity Event | Memory Destination | Learning Effect |
|---|---|---|
| Opportunity identified | `opportunities/OPPORTUNITY_BRIEFS.md` | Opportunity Radar brief created |
| Opportunity scored | Opportunity Radar scoring model | Score recorded on brief |
| Opportunity pursued (spend approved) | Spend log + `operations/DECISIONS.md` | Human decision recorded |
| Revenue outcome | Revenue log + `opportunities/` | Score accuracy validated; model calibrated |
| Opportunity rejected | `opportunities/` with rejection reason | Future scoring calibrated |

Revenue outcomes are the ultimate validation of Opportunity Radar accuracy. If an opportunity scored P1 but generated no revenue, the scoring model must be reviewed. If an opportunity scored P3 but generated significant revenue, that signals a scoring calibration need.

> **See also:** [Opportunity Radar — Opportunity Scoring](../agents/OPPORTUNITY_RADAR.md)

---

## 8. Support Runtime Relationship

**Support issues must improve future product and workflow design.**

Every support incident is a learning opportunity. Wolfpack must not repeatedly encounter the same support issue without capturing the systemic lesson.

| Support Event | Memory Destination | Learning Effect |
|---|---|---|
| Support incident logged | `operations/INCIDENT_LOG.md` | Incident record created |
| Root cause identified | `operations/INCIDENT_LOG.md` (postmortem) | Systemic cause documented |
| Workflow or product improvement | `operations/LESSONS_LEARNED.md` | Improvement action assigned |
| Recurring pattern identified | Wolfpack review | DEC entry or workflow change |

Support issues that reveal a design flaw must not be resolved as one-off fixes. The governance requirement: every recurring support incident (same issue appearing 2+ times) triggers a Wolfpack review to identify the systemic cause.

> **See also:** [Incident Log Standard](../operations/INCIDENT_LOG.md)
> **See also:** [Lessons Learned Standard](../operations/LESSONS_LEARNED.md)

---

## 9. Revenue System Relationship

Revenue outcomes close the Wolfpack feedback loop. The revenue system reports:

| Revenue Event | Memory Destination | Learning Effect |
|---|---|---|
| New customer acquisition | `opportunities/` or `operations/` | Opportunity Radar outcome confirmed |
| Revenue per call metric | Operational logs | Performance baseline established |
| Customer churn signal | `opportunities/` | Opportunity Radar: churn risk scored |
| Pricing sensitivity signal | EIL or Opportunity Radar | Market intelligence updated |
| Upsell/cross-sell opportunity | `opportunities/` | Opportunity Radar brief created |

Revenue results must improve opportunity scoring (Section 7) and market intelligence (EIL). A revenue outcome that contradicts an Opportunity Radar prediction triggers a scoring model review.

---

## 10. Institutional Memory Requirements

For hive mind learning to function, institutional memory must be:

| Requirement | Standard |
|---|---|
| **Complete** | Every event in the learning loop must produce a memory entry |
| **Structured** | All entries follow the Wolfpack memory schema with YAML front matter |
| **Provenance-tracked** | Every entry identifies the source subsystem |
| **Timestamped** | Every entry uses ISO-8601 UTC timestamps |
| **Auditable** | `append_only: true` on all governance documents — no silent modification |
| **Accessible** | All Wolfpack roles can read; authorized roles can write |
| **Recoverable** | Memory lives in GitHub — replaceable worker doctrine applies |

> **See also:** [Memory Architecture — Institutional memory requirements](./MEMORY_ARCHITECTURE.md)

---

## 11. Prohibited Behaviors

These behaviors are categorically prohibited under the Hive Mind Learning Doctrine:

| Prohibition | Rationale |
|---|---|
| **Subsystem A directly commanding Subsystem B** | No autonomous inter-subsystem command without governance |
| **EIL triggering spend, deployment, or canon mutation** | Intelligence is advisory only — human decision required |
| **Worker results cached locally outside GitHub** | Hidden state — violates governance doctrine |
| **Support incident resolved without lessons learned entry** | Recurring failure pattern prevention requires documentation |
| **Opportunity score changed without governance review** | Scoring model integrity requires oversight |
| **Revenue outcome recorded without Opportunity Radar calibration** | Feedback loop closure requires model review |
| **Runtime failure silently recovered without incident log** | Append-only governance requires all events logged |
| **Vendor intelligence used without EIL scoring** | Unscored intelligence bypasses governance filters |
| **Canon mutation without DEC entry** | append_only + canonical hierarchy enforced |
| **Human API bypass for any action** | Human API is the governance gate — no bypass |

---

## 12. Governance Boundaries

The Hive Mind Learning Doctrine operates within the following boundaries:

| Boundary | Enforcement |
|---|---|
| **No subsystem is subordinate to another** | Wolfpack roles are equal — governance layer resolves conflicts |
| **All events enter through structured memory** | Unstructured signals are not in the learning loop |
| **Governance review gates all significant changes** | Wolfpack review gate for deployments, spend, canon changes |
| **Human approval gates all financial actions** | Human API for any spend above threshold |
| **Append-only on all governance records** | No silent deletion or modification of learning records |
| **Replaceable worker doctrine** | Worker results must be in GitHub — not in local memory |
| **No uncontrolled autonomous agents** | All agent actions observable and logged |
| **Source trust hierarchy applies** | External intelligence from untrusted sources not acted upon |

---

## 13. Definition of Done

The Hive Mind Learning Doctrine is operating correctly when ALL of the following are true:

| Criterion | Verification |
|---|---|
| Every significant operational event produces a memory entry | `operations/INCIDENT_LOG.md`, `LESSONS_LEARNED.md`, or `opportunities/` entries exist |
| EIL signals are scored and classified | SIG-OPP/RSK/ALR/ADV/REG/COM classification present on EIL events |
| Worker results feed back into institutional memory | `EXECUTION_HISTORY.jsonl` and `processed_registry.json` updated per cycle |
| Runtime failures are logged and reviewed | Incident log entries; Wolfpack review within 72 hours |
| Opportunity Radar scores are calibrated by revenue outcomes | Outcome records reference original opportunity scores |
| Support incidents produce lessons learned | Recurring support issues trigger Wolfpack review |
| No subsystem directly commands another | Governance layer is the only command path |
| EIL research informs but does not command spend | Spend decisions go through controlled spend + human approval |
| All learning entries are governed | No append-only violations; no silent modifications |
| Validator runs after every workflow cycle | Stage 8 validator exit code 0 confirmed on every run |

---

*Canonical — GitHub is the source of truth.*
*Wolfpack Hive Mind Learning Doctrine v1 — 2026-05-25*