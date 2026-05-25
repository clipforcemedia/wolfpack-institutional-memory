---
title: "Wolfpack External Intelligence Layer v1"
document_type: "canon"
status: "construction_stage"
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
  - "external-intelligence"
  - "construction-stage"
  - "governance"
  - "market-research"
  - "vendor-monitoring"
  - "security-monitoring"
  - "batch-002"
related_ids:
  - "canon/SYSTEM_ARCHITECTURE.md"
  - "canon/WOLFPACK_CANON.md"
  - "canon/MEMORY_ARCHITECTURE.md"
  - "agents/OPPORTUNITY_RADAR.md"
  - "operations/EVENT_SCHEMA.md"
  - "operations/AUTOMATION_EXECUTION_MATRIX.md"
  - "runtime/RUNTIME_STATE_GOVERNANCE.md"
  - "DEC-001"
append_only: true
---

# Wolfpack External Intelligence Layer v1

> **Stage:** Construction (v0.1 system — not production live traffic)
> **Source:** Wolfpack institutional memory
> **Status:** Active — Canonical Governance Doctrine
> **Scope:** Read-only intelligence observation and reporting only — no execution
> **Activation Date:** 2026-05-25

---

## 1. Purpose

The Wolfpack External Intelligence Layer (EIL) defines how Wolfpack observes, collects, classifies, and reports on external signals — market data, vendor behavior, security events, competitor activity, regulatory changes, and operational intelligence — during the system construction stage.

**The EIL's singular purpose is to inform human decisions. It never makes them.**

EIL is not an execution layer. It does not deploy code, trigger workflows, mutate canon, authorize transactions, or bypass human approval. It is a research and monitoring layer that emits structured intelligence events for human review and Wolfpack governance processing.

EIL is explicitly bounded by the Wolfpack governance doctrine: all intelligence outputs pass through human review gates before any action is taken. No signal, no matter how high-scored, triggers autonomous execution.

---

## 2. Construction-Stage Role

Wolfpack operates in two stages:

| Stage | Description | EIL Role |
|---|---|---|
| **Construction** | System being built, configured, integrated — not yet handling live business traffic | EIL active: monitoring, research, signal collection, opportunity identification |
| **Production** | System live, handling real calls, real revenue | EIL active with elevated constraints: no market-signal-driven execution |

**Construction-stage definition:** The construction stage spans from initial system architecture through the point where Alice (voice AI receptionist) handles its first revenue-generating call without human review on every interaction. Until that threshold is crossed, Wolfpack is in construction.

**EIL in construction:** Maximum signal collection and research. Wolfpack is building the right thing — EIL provides the environmental intelligence to ensure decisions are well-informed. Every external signal is a potential data point for system correctness.

**EIL in production:** Constrained signal collection. The system is operating — external intelligence focuses on risk signals, regulatory changes, vendor failures, and security events. Market opportunity signals queue for review rather than triggering immediate action.

> **See also:** [System Architecture — DEC-001 execution worker doctrine](./SYSTEM_ARCHITECTURE.md)
> **See also:** [Runtime State Governance — Worker replaceability during construction](./runtime/RUNTIME_STATE_GOVERNANCE.md)

---

## 3. Intelligence Doctrine

**Core doctrine:** All external intelligence is advisory. Advisory signals may inform decisions but never constitute authorization for action.

| Doctrine | Statement |
|---|---|
| **Separation** | Intelligence and execution are separate layers. Intelligence observes and reports; execution acts. |
| **Human authority** | Every external intelligence signal requires human review before it can trigger action. No exception. |
| **No autonomous trigger** | A high-scored opportunity signal does not authorize deployment. A critical risk signal does not authorize rollback without human confirmation. |
| **Source neutrality** | Wolfpack does not trust vendors, competitors, or market analysts by default. Trust is earned through verification and placed in the source trust hierarchy (Section 7). |
| **Construction primetime** | The construction stage is the highest-value window for external intelligence — Wolfpack is making foundational decisions. EIL should be maximally useful during construction. |
| **Governance precedence** | If an intelligence signal contradicts established canonical doctrine, canon wins. External intelligence may not override canon. |

**The intelligence/execution separation is non-negotiable.** EIL is the eyes and ears of Wolfpack. It is not the hands.

> **See also:** [Wolfpack Canon — No uncontrolled autonomy](./WOLFPACK_CANON.md)
> **See also:** [Automation Execution Matrix — Human API doctrine](./operations/AUTOMATION_EXECUTION_MATRIX.md)

---

## 4. Non-Goals

The following are explicitly **not goals** of EIL:

| Non-Goal | Rationale |
|---|---|
| **Real-time trading or financial automation** | Financial actions require human approval — no exceptions |
| **Autonomous deployment** | Deployments require Wolfpack review gate + Deployment Governor approval |
| **Vendor lock-in introduction** | EIL monitors vendors but does not create dependency — vendor abstraction doctrine applies |
| **Canon mutation** | Canon is immutable without DEC entry + Wolfpack review |
| **Social engineering or competitive intelligence gathering through deception** | All intelligence collection is open-source / public information only |
| **Predictive decision-making** | EIL scores and reports signals; predictions require human interpretation |
| **Security exploitation research** | EIL monitors security signals for defensive awareness only — no offensive research |
| **Regulatory compliance automation** | Compliance requires legal review; EIL surfaces regulatory signals for human review only |
| **Customer data extraction** | EIL does not collect, process, or store customer personal data |

---

## 5. Approved Source Categories

EIL monitors only the following source categories:

| Category | Examples | Construction-Stage Priority |
|---|---|---|
| **Vendor product announcements** | Twilio release notes, OpenAI API changelogs, Render status page, AWS/Azure/GCP service announcements | HIGH |
| **Vendor incident and outage reports** | Status page incidents, incident postmortems, degradation reports | HIGH — construction-stage dependency risk |
| **Market and competitor monitoring** | Competitor pricing changes, product launches, market positioning shifts | MEDIUM |
| **Technical and security advisories** | CVEs affecting stack components, security framework updates, dependency vulnerability reports | HIGH |
| **Regulatory and compliance signals** | FCC regulation changes, AI disclosure requirements, industry standards updates | HIGH |
| **Open-source ecosystem monitoring** | Framework deprecations, library security advisories, tooling roadmap changes | MEDIUM |
| **Industry postmortems and lessons learned** | Public incident postmortems from similar systems (voice AI, telephony, SaaS) | HIGH |
| **Wolfpack operational telemetry** | Call success rates, failure modes, customer drop-off patterns (from internal logs only) | HIGH |
| **Customer feedback signals** | Feature requests, pricing sensitivity, competitive switching signals (from internal data only) | MEDIUM |
| **Market research publications** | IDC/Gartner reports, industry surveys, vertical market analysis | LOW — informational only |

**No proprietary or non-public intelligence.** EIL does not collect data from paywalled intelligence services, private Slack communities, confidential vendor roadmaps, or any source that requires non-disclosure agreements. All EIL intelligence is either publicly available or internally generated.

> **See also:** [Opportunity Radar — Market and Business Opportunity Detection](../agents/OPPORTUNITY_RADAR.md)
> **See also:** [Memory Architecture — Source provenance requirements](./MEMORY_ARCHITECTURE.md)

---

## 6. Prohibited Sources and Behaviors

### 6.1 Prohibited Sources

| Prohibited Source | Rationale |
|---|---|
| **Paywalled intelligence services** | Creates financial dependency; proprietary data cannot be verified |
| **Confidential vendor roadmaps** | NDA-protected information; may not be acted upon |
| **Social media direct messages** | Non-public information; collection without consent prohibited |
| **Competitor private communications** | Confidential information; collection prohibited |
| **Customer data from external parties** | Privacy violation risk |
| **Dark web or breach data** | Illegal to possess; prohibited regardless of apparent relevance |
| **Government classified or sensitive documents** | Legal and ethical prohibition |
| **Any source requiring deceptive collection methods** | Wolfpack does not misrepresent itself to collect information |

### 6.2 Prohibited Behaviors

| Prohibited Behavior | Governance Basis |
|---|---|
| **Autonomous code deployment triggered by external signal** | Wolfpack Review Gate required for all deployments |
| **Financial transaction triggered by market signal** | Human API required for all financial actions |
| **Canon mutation without DEC entry + Wolfpack review** | append_only: true; canonical integrity doctrine |
| **Direct database or system modification based on external intelligence** | Execution separation doctrine |
| **Vendor lock-in creation without governance approval** | Vendor abstraction doctrine |
| **Security penetration testing based on CVE intelligence** | EIL is defensive monitoring only |
| **Autonomous rollback without human confirmation** | Rollback doctrine requires human authorization |
| **Customer data forwarding or exfiltration** | Privacy and security doctrine |
| **Intelligence report falsification or manipulation** | Append-only integrity; governance trust |

**Penalty for prohibited behavior:** Any EIL-driven workflow that violates these prohibitions constitutes a governance incident. The workflow halts immediately, the incident is logged per the incident log standard, and the relevant Wolfpack role must review before continuation.

---

## 7. Source Trust Hierarchy

All external sources are classified in a trust hierarchy. Higher trust requires less verification; lower trust requires stronger corroboration.

| Level | Source Type | Trust Weight | Verification Required |
|---|---|---|---|
| **1 — Verified internal** | Wolfpack operational logs, incident records, customer interaction data | Maximum | None — internal provenance guaranteed |
| **2 — Official vendor documentation** | Twilio status page, OpenAI changelog, Render docs, official CVE databases | High | Cross-reference with official URL only |
| **3 — Public official statements** | Official blog posts, press releases, regulatory agency announcements | High | Source URL verification; no second-hand reporting |
| **4 — Peer-reviewed or widely cited** | IDC/Gartner public reports, academic security papers, established industry analysts | Medium | Corroboration with at least one Level 2 source |
| **5 — Community-sourced intelligence** | GitHub security advisories, Stack Overflow, HackerNews, public postmortems | Medium-low | Multiple independent sources required |
| **6 — Unverified speculation** | Reddit threads, anonymous sources, unconfirmed Twitter reports | Low | Not acted upon; informational only |

**Trust adjustment rules:**
- A Level 6 source corroborated by two Level 4+ sources may be elevated to Medium-low trust
- A Level 1–3 source contradicted by two Level 1–3 sources from different organizations triggers escalation
- No source below Level 4 may authorize action without human review

> **See also:** [Runtime State Governance — Append-only integrity](./runtime/RUNTIME_STATE_GOVERNANCE.md)

---

## 8. Signal Classification

Every external intelligence signal is classified into one of six categories upon ingestion:

| Class Code | Class Name | Description | Example |
|---|---|---|---|
| **SIG-OPP** | Opportunity Signal | External event creating potential business value | Competitor raises price; market gap identified |
| **SIG-RSK** | Risk Signal | External event creating potential system or business risk | Vendor announces end-of-life for dependency |
| **SIG-ALR** | Alert Signal | Immediate attention required; time-sensitive | Vendor outage affecting live system; active CVE in use |
| **SIG-ADV** | Advisory Signal | Informational; no immediate action but useful for planning | New regulatory guidance published; industry trend |
| **SIG-REG** | Regulatory Signal | Compliance-relevant; requires legal or governance review | AI disclosure regulations; data residency requirements |
| **SIG-COM** | Competitive Signal | Competitor activity; context for strategic decisions | Competitor launches competing product; pricing change |

**Multi-classification rule:** A signal may carry multiple class codes (e.g., SIG-RSK + SIG-ALR for an active vendor outage). The most severe class governs the escalation path.

---

## 9. Intelligence Scoring Model

Signals are scored across four dimensions, then combined into a composite score.

### 9.1 Scoring Dimensions

| Dimension | Weight | Description |
|---|---|---|
| **Business Impact** (BI) | 40% | How significantly does this affect revenue, customer acquisition, or system value? |
| **Urgency** (UR) | 30% | How time-sensitive is this signal? |
| **Verifiability** (VR) | 20% | How well-supported is this signal by trusted sources? |
| **Relevance** (RE) | 10% | How directly does this affect Wolfpack's current construction scope? |

### 9.2 Score Calculation

```
Composite Score = (BI × 0.40) + (UR × 0.30) + (VR × 0.20) + (RE × 0.10)
```

Each dimension scores 1–5:
- **5** — Critical/severe
- **4** — High/significant
- **3** — Medium/moderate
- **2** — Low/minor
- **1** — Negligible/informational

### 9.3 Score Levels

| Composite Score | Level | Label | Required Action |
|---|---|---|---|
| 4.5 – 5.0 | **P0** | Immediate | Escalate to human immediately; alert all Wolfpack roles |
| 3.5 – 4.4 | **P1** | High | Wolfpack review within 24 hours; human gate active |
| 2.5 – 3.4 | **P2** | Medium | Queue for Wolfpack review within 72 hours |
| 1.5 – 2.4 | **P3** | Low | Log to intelligence register; inform on next review cycle |
| 1.0 – 1.4 | **P4** | Informational | Log only; no review required unless manually requested |

**Scoring governance:** Scores are advisory only. A P0 score does not authorize autonomous action. A P4 score does not authorize dismissal — all signals are logged.

### 9.4 Opportunity Radar Alignment

For **SIG-OPP** signals, the Opportunity Radar scoring model (5/4/3/2/1 scale) maps to EIL scoring as follows:

| Opportunity Radar Score | EIL BI Score | EIL Composite Adjustment |
|---|---|---|
| 5 — immediate | 5 (Business Impact = 5) | EIL composite may be elevated by 0.5 during construction stage |
| 4 — high | 4 | Standard composite |
| 3 — medium | 3 | Standard composite |
| 2 — low | 2 | Down-weighted during construction |
| 1 — reject | 1 | Logged; no further action |

> **See also:** [Opportunity Radar — Opportunity Scoring](../agents/OPPORTUNITY_RADAR.md)

---

## 10. Noise Filtering

External intelligence generates noise. EIL applies noise filtering to prevent signal overflow from drowning governance attention.

### 10.1 Noise Categories

| Noise Type | Definition | Filter Action |
|---|---|---|
| **Vendor hype** | Marketing language describing minor releases as revolutionary | Down-weight BI score; flag as marketing |
| **Market speculation** | Unconfirmed rumors treated as facts | Require Level 4+ verification before scoring |
| **Competitor vanity** | Competitor announcements that don't affect Wolfpack's market position | Score RE dimension at 1; log as low-relevance |
| **Historical duplication** | Signal already in intelligence register from previous scan | Deduplicate; update existing entry with new timestamp |
| **Out-of-scope signal** | Signal relevant to a market or technology Wolfpack has explicitly decided not to pursue | Mark as out-of-scope; do not score; log for record |
| **False correlation** | Two unrelated events presented as causally connected | Separate into distinct signals; score independently |

### 10.2 Noise Filter Rules

| Rule | Implementation |
|---|---|
| **Deduplication window** | Same signal from same source within 72 hours = duplicate |
| **Relevance threshold** | RE score below 2 = automatically P3 or P4 regardless of other dimensions |
| **Vendor announcement decay** | Vendor product announcements score VR at 3 maximum (marketing language) |
| **Competitor announcement decay** | Competitor announcements decay to P3 within 30 days unless action confirmed |

### 10.3 Attention Economy

To protect governance attention during construction:

- **Daily EIL digest:** Maximum 5 signals above P2 per day enter Wolfpack review queue
- **Weekly EIL summary:** All signals logged; P0/P1 signals highlighted
- **Monthly EIL report:** Full intelligence register review; trend analysis;噪 noise filter effectiveness report

---

## 11. Vendor Monitoring

Wolfpack's primary external dependencies during construction are: Twilio, OpenAI Realtime API, Render, GitHub, and OpenClaw. EIL monitors these vendors for signals relevant to system stability, pricing, roadmap, and security.

### 11.1 Primary Vendor Watch List

| Vendor | Product | Watch Targets | Priority |
|---|---|---|---|
| Twilio | Voice media streams | Status page, API changelog, deprecation notices, pricing changes | HIGH |
| OpenAI | Realtime API | API changelog, model deprecations, pricing changes, capability changes | HIGH |
| Render | Deployment platform | Status page, pricing changes, feature deprecations | HIGH |
| GitHub | Institutional memory | API rate limit changes, pricing changes, feature deprecations | MEDIUM |
| OpenClaw | Execution worker | Release notes, security advisories, breaking changes | HIGH |

### 11.2 Vendor Signal Rules

| Signal Type | EIL Action |
|---|---|
| Vendor status page incident | Immediately classify SIG-ALR; score; emit event; alert human |
| API deprecation notice | Classify SIG-RSK; assess timeline; queue for Wolfpack review |
| Pricing increase | Classify SIG-OPP (opportunity to reposition) or SIG-RSK (cost increase) depending on context |
| Vendor EOL announcement | Classify SIG-RSK; score; assess migration path; escalate for Wolfpack review |
| Vendor security advisory | Classify SIG-RSK; escalate immediately; do not wait for next review cycle |
| Vendor new product announcement | Score as SIG-ADV; informational only — do not score as SIG-OPP unless market relevance confirmed |