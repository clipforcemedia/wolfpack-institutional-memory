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
  - "canon/WOLFPACK_HIVE_MIND_LEARNING_DOCTRINE_v1.md"
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

> **See also:** [Wolfpack Hive Mind Learning Doctrine — Governed inter-subsystem learning](./WOLFPACK_HIVE_MIND_LEARNING_DOCTRINE_v1.md)

---

## 2. Construction-Stage Role

Wolfpack operates in two stages:

| Stage | Description | EIL Role |
|---|---|---|
| **Construction** | System being built, configured, integrated — not yet handling live business traffic | EIL active: monitoring, research, signal collection, opportunity identification |
| **Production** | System live, handling real calls, real revenue | EIL active with elevated constraints: no market-signal-driven execution |

**Construction-stage definition:** The construction stage spans from initial system architecture through the point where Alice (voice AI receptionist) handles its first revenue-generating call without human review on every interaction. Until that threshold is crossed, Wolfpack is in construction.

**EIL in construction:** Maximum signal collection and research. Wolfpack is building the right thing — EIL provides the environmental intelligence to ensure foundational decisions are well-informed. Every external signal is a potential data point for system correctness.

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
| **Source neutrality** | Wolfpack does not trust vendors, competitors, or market analysts by default. Trust is earned through verification and placed in the source trust hierarchy (Section 8). |
| **Construction primetime** | The construction stage is the highest-value window for external intelligence — Wolfpack is making foundational decisions. EIL should be maximally useful during construction. |
| **Governance precedence** | If an intelligence signal contradicts established canonical doctrine, canon wins. External intelligence may not override canon. |

**The intelligence/execution separation is non-negotiable.** EIL is the eyes and ears of Wolfpack. It is not the hands.

> **See also:** [Wolfpack Canon — No uncontrolled autonomy](./WOLFPACK_CANON.md)
> **See also:** [Wolfpack Hive Mind Learning Doctrine — Governed inter-subsystem learning](./WOLFPACK_HIVE_MIND_LEARNING_DOCTRINE_v1.md)
> **See also:** [Automation Execution Matrix — Human API doctrine](./operations/AUTOMATION_EXECUTION_MATRIX.md)

---

## 4. Hive Mind Learning Doctrine

The Wolfpack Hive Mind Learning Doctrine (canon) is the governing layer for all EIL cross-subsystem influence. EIL is a primary signal generator in the Wolfpack hive mind loop:

```
external signal
  → EIL structured memory entry (append-only, provenance-tracked)
  → EIL scoring (BI/UR/VR/RE dimensions)
  → EIL signal classification (SIG-OPP, SIG-RSK, SIG-ALR, SIG-ADV, SIG-REG, SIG-COM)
  → Wolfpack governance review when required
  → human decision gate
  → controlled spend / Opportunity Radar / Worker / Support Runtime / Revenue System
  → outcome validation
  → lessons learned back into memory
  → (future decisions improved)
```

**EIL hive mind obligations:**

| Obligation | Requirement |
|---|---|
| EIL findings → institutional memory | All EIL signals produce structured memory entries in `memory/intelligence/` before influencing other subsystems |
| EIL may inform controlled spend scoring | SIG-RSK signals from vendor monitoring may inform controlled spend decisions; may not trigger spending |
| EIL may inform Opportunity Radar scoring | SIG-OPP signals from market research may inform opportunity scoring; may not approve opportunities |
| EIL may inform Worker design | EIL security signals and failure patterns may inform runtime hardening; may not mutate runtime behavior directly |
| EIL may inform AI Support Runtime | EIL support pattern signals may inform support logic improvements; may not modify customer-facing support logic without governance review |
| EIL may inform cash-flow system selection | EIL may identify vendors, pricing, alternatives for future spend reviews; may not launch businesses or deploy revenue systems |
| EIL may identify vendor risk | SIG-RSK signals for pricing changes, EOL, security concerns for future spend reviews |
| Worker results → EIL memory | Worker execution results, support issues, controlled spend outcomes, revenue outcomes must feed back into EIL-related memory where applicable |
| All cross-system learning → governed gates | No EIL signal directly commands another subsystem; all pass through memory → scoring → review → approval |

**No subsystem may directly command another subsystem without governance.** EIL findings are inputs to other subsystems — never authorizations.

> **See also:** [Wolfpack Hive Mind Learning Doctrine v1](./WOLFPACK_HIVE_MIND_LEARNING_DOCTRINE_v1.md)
> **See also:** [Memory Architecture — Source provenance requirements](./MEMORY_ARCHITECTURE.md)
> **See also:** [Event Schema — EIL event definitions](./operations/EVENT_SCHEMA.md)

---

## 5. Non-Goals

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
| **Autonomous rollback execution** | Rollback requires human authorization per rollback doctrine |
| **Autonomous opportunity approval** | Opportunity Radar approval requires human spend gate |

---

## 6. Approved Source Categories

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

---

## 7. Prohibited Sources and Behaviors

### 7.1 Prohibited Sources

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

### 7.2 Prohibited Behaviors

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
| **Direct command of workers from EIL signals** | No subsystem commands another without governance |
| **EIL-triggered opportunity approval** | Opportunity Radar requires human approval for all opportunities |
| **EIL-triggered spend authorization** | Controlled spend requires human spend gate — no EIL bypass |

**Penalty for prohibited behavior:** Any EIL-driven workflow that violates these prohibitions constitutes a governance incident. The workflow halts immediately, the incident is logged per the incident log standard, and the relevant Wolfpack role must review before continuation.

---

## 8. Source Trust Hierarchy

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

| Condition | Adjustment |
|---|---|
| Source has financial incentive | Down-weight one level (e.g., 2 → 3) |
| Source has competitive relationship | Down-weight one level |
| Signal confirmed by 2+ independent sources | Upgrade to next level above highest source |
| Signal contradicts established canon | Level 1-3: escalate to Wolfpack review; Level 4-6: ignore |
| Signal from blocked jurisdiction | Level 6 — informational only |

---

## 9. Signal Classification

All EIL signals are classified into one of the following signal classes. Classification determines review urgency and routing.

| Signal Class | Description | Review Urgency |
|---|---|---|
| **SIG-OPP** | Opportunity — revenue potential, market positioning, competitive advantage | Opportunity Radar review; human spend gate if spend required |
| **SIG-RSK** | Risk — vendor EOL, security vulnerability, regulatory change, cost increase | Wolfpack review within 72 hours; immediate if critical |
| **SIG-ALR** | Alert — active incident, active exploitation, active vendor outage | Immediate human alert; Wolfpack review within 24 hours |
| **SIG-ADV** | Advisory — informational, no immediate action required | Weekly EIL digest; Wolfpack review monthly |
| **SIG-REG** | Regulatory — compliance change, legal requirement, government action | Legal review; Wolfpack review |
| **SIG-COM** | Competitive — competitor activity, market shift, positioning change | Opportunity Radar review; informational if no spend |

**EIL signals may be compound:** A single external event may trigger multiple signal classes. Example: a vendor EOL announcement may trigger both SIG-RSK (risk of dependency) and SIG-OPP (opportunity to reposition competitively). Both are logged and routed independently.

> **See also:** [Event Schema — Signal classification standards](./operations/EVENT_SCHEMA.md)
> **See also:** [Opportunity Radar — Signal routing](../agents/OPPORTUNITY_RADAR.md)

---

## 10. Intelligence Scoring Model

EIL applies a 4-dimensional scoring model to each signal. Composite score determines priority and routing.

### 10.1 Dimensions

| Dimension | Abbr | Description | Score Range |
|---|---|---|---|
| **Business Impact** | BI | Effect on Wolfpack's revenue, cost, or competitive position | 1–5 |
| **Urgency** | UR | Time sensitivity — how quickly must action be taken | 1–5 |
| **Vendor Risk** | VR | Dependency risk, migration cost, vendor stability | 1–5 |
| **Relevance** | RE | How directly the signal applies to Wolfpack's current architecture and strategy | 1–5 |

### 10.2 Composite Score

**Composite = (BI × 0.4) + (UR × 0.3) + (VR × 0.2) + (RE × 0.1)**

| Composite Score | Priority | Action |
|---|---|---|
| 4.5 – 5.0 | **P0 — Critical** | Immediate human review; escalate to Wolfpack review within 24 hours |
| 3.5 – 4.4 | **P1 — High** | Human review within 72 hours; Wolfpack review |
| 2.5 – 3.4 | **P2 — Medium** | Wolfpack review within weekly cycle; Opportunity Radar integration if SIG-OPP |
| 1.5 – 2.4 | **P3 — Low** | Log; review in monthly EIL digest |
| 1.0 – 1.4 | **P4 — Minimal** | Log; informational only |

### 10.3 Construction-Stage Adjustments

During construction stage, weighting adjustments apply:

| Adjustment | Rationale |
|---|---|
| **UR up-weight ×1.3** | Construction-stage decisions are time-sensitive; foundational tech choices have long-term effects |
| **VR up-weight ×1.2** | Vendor dependency risk is elevated during construction (no production fallback yet) |
| **BI down-weight ×0.8** | Revenue impact is lower during construction (no live traffic yet) |

### 10.4 EIL Score vs. Opportunity Radar
EIL scores are independent from Opportunity Radar scores. EIL scores assess intelligence quality and urgency; Opportunity Radar scores assess revenue potential.

| Opportunity Radar Score | EIL BI Score | EIL Composite Adjustment |
|---|---|---|
| 5 — immediate | 5 (Business Impact = 5) | EIL composite may be elevated by 0.5 during construction stage |
| 4 — high | 4 | Standard composite |
| 3 — medium | 3 | Standard composite |
| 2 — low | 2 | Down-weighted during construction |
| 1 — reject | 1 | Logged; no further action |

> **See also:** [Opportunity Radar — Opportunity Scoring](../agents/OPPORTUNITY_RADAR.md)

---

## 11. Noise Filtering

External intelligence generates noise. EIL applies noise filtering to prevent signal overflow from drowning governance attention.

### 11.1 Noise Categories

| Noise Type | Definition | Filter Action |
|---|---|---|
| **Vendor hype** | Marketing language describing minor releases as revolutionary | Down-weight BI score; flag as marketing |
| **Market speculation** | Unconfirmed rumors treated as facts | Require Level 4+ verification before scoring |
| **Competitor vanity** | Competitor announcements that don't affect Wolfpack's market position | Score RE dimension at 1; log as low-relevance |
| **Historical duplication** | Signal already in intelligence register from previous scan | Deduplicate; update existing entry with new timestamp |
| **Out-of-scope signal** | Signal relevant to a market or technology Wolfpack has explicitly decided not to pursue | Mark as out-of-scope; do not score; log for record |
| **False correlation** | Two unrelated events presented as causally connected | Separate into distinct signals; score independently |

### 11.2 Noise Filter Rules

| Rule | Implementation |
|---|---|
| **Deduplication window** | Same signal from same source within 72 hours = duplicate |
| **Relevance threshold** | RE score below 2 = automatically P3 or P4 regardless of other dimensions |
| **Vendor announcement decay** | Vendor product announcements score VR at 3 maximum (marketing language) |
| **Competitor announcement decay** | Competitor announcements decay to P3 within 30 days unless action confirmed |

### 11.3 Attention Economy

To protect governance attention during construction:

- **Daily EIL digest:** Maximum 5 signals above P2 per day enter Wolfpack review queue
- **Weekly EIL summary:** All signals logged; P0/P1 signals highlighted
- **Monthly EIL report:** Full intelligence register review; trend analysis; noise filter effectiveness report

---

## 12. Vendor Monitoring

Wolfpack's primary external dependencies during construction are: Twilio, OpenAI Realtime API, Render, GitHub, and OpenClaw. EIL monitors these vendors for signals relevant to system stability, pricing, roadmap, and security.

### 12.1 Primary Vendor Watch List

| Vendor | Product | Watch Targets | Priority |
|---|---|---|---|
| Twilio | Voice media streams | Status page, API changelog, deprecation notices, pricing changes | HIGH |
| OpenAI | Realtime API | API changelog, model deprecations, pricing changes, capability changes | HIGH |
| Render | Deployment platform | Status page, pricing changes, feature deprecations | HIGH |
| GitHub | Institutional memory | API rate limit changes, pricing changes, feature deprecations | MEDIUM |
| OpenClaw | Execution worker | Release notes, security advisories, breaking changes | HIGH |

### 12.2 Vendor Signal Rules

| Signal Type | EIL Action |
|---|---|
| Vendor status page incident | Immediately classify SIG-ALR; score; emit event; alert human |
| API deprecation notice | Classify SIG-RSK; assess timeline; queue for Wolfpack review |
| Pricing increase | Classify SIG-OPP (opportunity to reposition) or SIG-RSK (cost increase) depending on context |
| Vendor EOL announcement | Classify SIG-RSK; score; assess migration path; escalate for Wolfpack review |
| Vendor security advisory | Classify SIG-RSK; escalate immediately; do not wait for next review cycle |
| Vendor new product announcement | Score as SIG-ADV; informational only — do not score as SIG-OPP unless market relevance confirmed |

### 12.3 Vendor Migration Intelligence

When a vendor signal triggers SIG-RSK at P1 or higher, EIL produces a vendor migration brief:

- Current vendor assessment (capability, cost, reliability)
- Alternative vendors identified (minimum 2 alternatives)
- Migration cost estimate (time, money, risk)
- Decision recommendation (migrate, wait, hybrid)
- Timeline recommendation

Vendor migration briefs are governance inputs — not deployment authorizations.

> **See also:** [Vendor Abstraction Doctrine — Vendor migration governance](./canon/VENDOR_ABSTRACTION_DOCTRINE.md)

---

## 13. Market and Competitor Monitoring

EIL monitors market and competitor signals for strategic intelligence. All competitor monitoring is open-source only — no proprietary data collection.

### 13.1 Market Monitoring Targets

| Target | What to Monitor | EIL Action |
|---|---|---|
| **Voice AI market** | Market size, growth rate, vertical segmentation | Quarterly market brief for Wolfpack review |
| **Pricing trends** | Competitor pricing changes, packaging changes | SIG-OPP or SIG-COM; score; log |
| **Feature trends** | Common feature announcements across competitors | SIG-ADV; informational |
| **Customer expectations** | Shifts in what customers expect from AI receptionists | SIG-OPP; score; feed to Opportunity Radar |

### 13.2 Competitor Monitoring Rules

| Rule | Rationale |
|---|---|
| **Open-source only** | No scraping, no paywalled data, no competitive intelligence services |
| **No direct competitor monitoring automation** | Manual review of public competitor websites and announcements |
| **Competitor pricing changes** | Score RE dimension carefully — pricing changes don't always affect Wolfpack |
| **Competitor product launches** | Classify SIG-COM; score VR; feed to Opportunity Radar for positioning analysis |
| **Competitor customer complaints** | Classify SIG-ADV; feed to AI Support Runtime for improvement signals |

### 13.3 Market Entry Opportunity Signals

When EIL identifies a market entry opportunity (new vertical, underserved segment, pricing gap):

1. Log signal with SIG-OPP classification
2. Score using 4-dimension model
3. If P2 or higher: produce market opportunity brief
4. Route to Opportunity Radar for revenue potential assessment
5. If Opportunity Radar score 4+: route to Wolfpack review gate
6. Human decision gate: proceed to opportunity brief development or archive

---

## 14. Incident and Postmortem Learning

EIL monitors public industry incidents and postmortems to extract systemic lessons before Wolfpack encounters similar failures.

### 14.1 Industry Incident Monitoring

| Incident Type | Source Priority | EIL Action |
|---|---|---|
| **Voice/telephony system failures** | HIGH — direct relevance | Score; log in `memory/failure-patterns/`; feed to runtime hardening review |
| **AI/ML system failures** | HIGH — direct relevance | Score; log in `memory/failure-patterns/`; feed to Worker design review |
| **Security breaches in similar systems** | HIGH — direct relevance | Score SIG-RSK; log in `memory/security-watch/`; escalate immediately |
| **SaaS platform outages** | MEDIUM — indirect relevance | Score; log in `memory/failure-patterns/`; assess relevance to Wolfpack stack |
| **General software engineering failures** | MEDIUM — knowledge value | Score; log in `memory/failure-patterns/`; informational |

### 14.2 Postmortem Learning Standards

When EIL captures a public postmortem, the learning entry must include:

- **What happened:** Concise description of the incident
- **Root cause:** Technical root cause (not organizational blame)
- **Detection:** How was the incident detected; time to detection
- **Resolution:** How was it resolved; time to resolution
- **Systemic lesson:** What Wolfpack can learn from this incident
- **Recommended action:** Any Wolfpack process, architecture, or monitoring change suggested by the lesson

### 14.3 Wolfpack Operational Telemetry

EIL also monitors Wolfpack's own operational telemetry (internal logs only):

| Telemetry Signal | EIL Action |
|---|---|
| Call success rate drop | Classify SIG-ALR if drop > 10%; classify SIG-RSK if drop 5–10% |
| Unusual failure pattern | Classify SIG-RSK; log in `memory/failure-patterns/`; feed to Wolfpack review |
| Customer drop-off pattern | Classify SIG-OPP (improvement opportunity) or SIG-ADV (informational) |
| API latency spike | Classify SIG-ALR if direct customer impact; SIG-RSK if indirect |

---

## 15. Security and Platform Risk Monitoring

EIL monitors security and platform risk signals relevant to Wolfpack's technology stack.

### 15.1 CVE Monitoring

| CVE Signal | EIL Action |
|---|---|
| CVE in Wolfpack's direct dependencies (Twilio, OpenAI, Render, GitHub, OpenClaw) | Classify SIG-RSK; escalate immediately; assess patch timeline |
| CVE in indirect dependencies (Python packages, npm packages) | Classify SIG-RSK; score; queue for Wolfpack review |
| CVE with active exploitation in wild | Classify SIG-ALR; immediate human alert; Wolfpack review within 24 hours |
| CVE with no known exploit | Classify SIG-RSK; log; Wolfpack review within 72 hours |

### 15.2 Security Signal Classification

| Security Signal | Classification | Urgency |
|---|---|---|
| Active exploitation of Wolfpack stack component | SIG-ALR | Immediate — human alert |
| Known CVE in Wolfpack stack (no patch available) | SIG-RSK | High — Wolfpack review within 72 hours |
| Known CVE in Wolfpack stack (patch available) | SIG-RSK | High — assess patch urgency |
| Security advisory for Wolfpack stack (no CVE) | SIG-ADV | Medium — Wolfpack review monthly |
| Security trend relevant to Wolfpack architecture | SIG-RSK | Medium — Wolfpack review monthly |

### 15.3 Platform Risk Signals

| Platform Risk | EIL Action |
|---|---|
| Platform deprecation announcement | Classify SIG-RSK; assess migration path; log in `memory/vendor-watch/` |
| Platform pricing increase | Classify SIG-RSK (cost) or SIG-OPP (repositioning opportunity); score; log |
| Platform breach or data exposure | Classify SIG-ALR; immediate human alert; assess Wolfpack exposure |
| Platform service discontinuation | Classify SIG-RSK; log in `memory/vendor-watch/`; assess alternatives |

> **See also:** [Runtime State Governance — Security hardening during construction](./runtime/RUNTIME_STATE_GOVERNANCE.md)

---

## 16. Controlled Spend Intelligence Support

**Scope note:** This section defines how EIL supports controlled spend decisions. The full controlled spend governance system is deferred/backlog — this section defines only the EIL → controlled spend intelligence interface.

### 16.1 EIL → Controlled Spend Information Flow

EIL provides the following intelligence to the controlled spend system:

| Intelligence Type | Format | When Provided |
|---|---|---|
| Vendor pricing changes | SIG-RSK alert with cost impact estimate | Upon detection |
| Vendor risk scores | Quarterly vendor watch list update | Quarterly |
| Market cost benchmarks | Annual market intelligence report | Annually |
| Alternative vendor options | Vendor migration brief (see Section 12.3) | On SIG-RSK P1+ from vendor monitoring |
| Competitor pricing intelligence | Market monitoring digest | Monthly |

### 16.2 EIL Limitations for Controlled Spend

| Limitation | Rationale |
|---|---|
| EIL does not authorize spend | Human approval required for all financial decisions |
| EIL does not calculate spend amounts | EIL provides information; controlled spend system calculates amounts |
| EIL does not approve vendors | Vendor approval goes through Deployment Governor + Wolfpack review |
| EIL does not track spend outcomes | Controlled spend system tracks outcomes; feeds back to EIL for vendor risk re-scoring |

### 16.3 Spend Intelligence Memory

EIL spend intelligence is stored in `memory/spend-intelligence/`:

- `memory/spend-intelligence/vendor-pricing/` — vendor pricing history and forecasts
- `memory/spend-intelligence/market-benchmarks/` — industry cost benchmarks
- `memory/spend-intelligence/spend-outcomes/` — controlled spend outcomes for vendor risk calibration (written by controlled spend system, read by EIL)

**Controlled spend governance files are not created by EIL.** The controlled spend governance system itself (DEC entries, spend thresholds, approval workflows) is a separate governance workstream deferred until after construction stage.

> **See also:** [Wolfpack Hive Mind Learning Doctrine — Controlled Spend Relationship](./WOLFPACK_HIVE_MIND_LEARNING_DOCTRINE_v1.md)

---

## 17. Opportunity Radar Integration

EIL integrates with Opportunity Radar as a primary signal source for market opportunity identification.

### 17.1 EIL → Opportunity Radar Signal Flow

| EIL Signal | Opportunity Radar Action |
|---|---|
| Market pricing gap identified | Opportunity Radar scores revenue potential; produces brief |
| Competitor weakness identified | Opportunity Radar scores competitive advantage potential |
| Underserved vertical identified | Opportunity Radar assesses market size and fit |
| Customer expectation shift | Opportunity Radar scores feature opportunity potential |

### 17.2 Opportunity Radar → EIL Feedback

| Feedback Type | EIL Memory Update |
|---|---|
| Opportunity scored by Opportunity Radar | EIL logs opportunity score and classification in `memory/intelligence/` |
| Opportunity pursued | EIL monitors competitor response and market reaction |
| Opportunity succeeded | EIL updates vendor and market intelligence with outcome data |
| Opportunity failed | EIL reviews whether market intelligence was incorrect; updates scoring model |

### 17.3 Joint Scoring Protocol

When EIL and Opportunity Radar both score the same signal:

1. EIL scores first: BI/UR/VR/RE dimensions → composite priority
2. Opportunity Radar scores second: revenue potential (P1–P5)
3. If EIL composite ≥ 3.5 (P1/P0) AND Opportunity Radar ≥ 4: escalate to Wolfpack review immediately
4. If EIL composite ≥ 2.5 (P2) OR Opportunity Radar ≥ 3: include in weekly Wolfpack review cycle
5. Otherwise: log and review in monthly EIL digest

---

## 18. Runtime Worker Intelligence Support

EIL provides runtime worker intelligence for design and hardening decisions.

### 18.1 EIL → Worker Design Information Flow

| Intelligence Type | When Provided | Worker Impact |
|---|---|---|
| Security CVE in execution environment | Upon detection | Runtime hardening; patch assessment |
| Failure pattern from industry incidents | Monthly digest | Worker error handling improvements |
| OpenClaw release notes | Upon release | Feature adoption assessment |
| Execution environment stability signals | Quarterly | Worker reliability design review |

### 18.2 Worker → EIL Feedback

| Worker Output | EIL Memory Update |
|---|---|
| Execution failure record | Log in `memory/failure-patterns/`; feed to industry incident correlation |
| Validation failure record | Log in `memory/security-watch/` or `memory/failure-patterns/` depending on type |
| OpenClaw behavioral anomaly | Score as SIG-RSK; log in `memory/intelligence/`; escalate if P1+ |
| Worker recovery event | Log in `memory/failure-patterns/` with recovery pattern for future reference |

### 18.3 Runtime Hardening Triggers

EIL may trigger a Wolfpack review of runtime worker design when:

| Trigger | Threshold | Action |
|---|---|---|
| Security CVE in execution environment | Any CVE in OpenClaw, Python, or Linux kernel | Score SIG-RSK; Wolfpack review within 72 hours |
| Industry failure pattern matches Wolfpack architecture | 2+ similar incidents in 90 days | Score SIG-RSK; Wolfpack review |
| OpenClaw breaking change | Any breaking change in minor version | Score SIG-RSK; Wolfpack review |
| Execution environment instability | 3+ failures in 30 days attributable to environment | Score SIG-ALR; immediate human alert |

> **See also:** [Runtime State Governance — Worker replaceability](./runtime/RUNTIME_STATE_GOVERNANCE.md)

---

## 19. AI Support Runtime Intelligence Support

EIL supports AI Support Runtime (the support system for Wolfpack's voice AI product) through pattern detection and improvement signals.

### 19.1 EIL → AI Support Runtime Information Flow

| Intelligence Type | When Provided | Support Runtime Impact |
|---|---|---|
| Industry support pattern (common failure modes) | Monthly digest | Support script improvement signals |
| Competitor support weakness | Quarterly | Product improvement opportunity |
| Customer expectation shift (support angle) | Upon detection | Support training topic |
| Security incident affecting similar products | Upon detection | Support readiness for customer inquiries |

### 19.2 AI Support Runtime → EIL Feedback

| Support Runtime Output | EIL Memory Update |
|---|---|
| Recurring support issue | Log in `memory/intelligence/` and `memory/failure-patterns/`; trigger Wolfpack review if 2+ occurrences |
| Support escalation pattern | Log in `memory/support-patterns/`; feed to product improvement review |
| Customer complaint trend | Score SIG-ADV or SIG-OPP; log in `memory/intelligence/`; feed to Opportunity Radar |
| Support metric anomaly | Classify SIG-RSK if systemic; SIG-ADV if isolated |

### 19.3 Support Pattern Memory

EIL maintains `memory/support-patterns/` for support-related intelligence:

- `memory/support-patterns/industry-patterns/` — industry-wide support issue patterns from public postmortems
- `memory/support-patterns/competitor-patterns/` — competitor support weakness observations
- `memory/support-patterns/technology-patterns/` — technology-related support issue patterns

> **See also:** [AI Support Runtime Doctrine — Pattern detection and improvement](./operations/SUPPORT_RUNTIME.md)

---

## 20. Revenue System Learning Support

EIL supports the revenue system through market intelligence that informs pricing, positioning, and revenue model decisions.

### 20.1 EIL → Revenue System Information Flow

| Intelligence Type | When Provided | Revenue System Impact |
|---|---|---|
| Competitor pricing change | Upon detection | Pricing model review |
| Market segment growth data | Quarterly | Revenue model segmentation |
| Customer willingness to pay signals | Upon detection (from internal data only) | Pricing sensitivity model |
| Revenue pattern analysis | Monthly | Revenue forecasting improvement |

### 20.2 Revenue System → EIL Feedback

| Revenue System Output | EIL Memory Update |
|---|---|
| Revenue outcome (success) | Log in `memory/revenue-patterns/`; update market intelligence with confirmed data |
| Revenue outcome (failure) | Log in `memory/revenue-patterns/` with failure analysis; update scoring model |
| Pricing sensitivity confirmed | Log in `memory/mrevenue-patterns/` with pricing sensitivity confirmation; feed to Opportunity Radar
| Revenue model pivot | Log in `memory/revenue-patterns/` with rationale; feed to Wolfpack review if significant |

### 20.3 Revenue Pattern Memory

EIL maintains `memory/revenue-patterns/` for revenue-related intelligence:

- `memory/revenue-patterns/pricing-intelligence/` — competitor and market pricing data
- `memory/revenue-patterns/outcomes/` — confirmed revenue outcomes for model calibration
- `memory/revenue-patterns/segment-analysis/` — market segment revenue performance

> **See also:** [Wolfpack Hive Mind Learning Doctrine — Revenue System Relationship](./WOLFPACK_HIVE_MIND_LEARNING_DOCTRINE_v1.md)

---

## 21. Memory Integration

EIL's institutional memory is organized under `memory/intelligence/` and related subdirectories. All EIL memory entries follow the Wolfpack memory architecture standards.

### 21.1 Memory Directory Structure

| Directory | Purpose | Entry Type |
|---|---|---|
| `memory/intelligence/` | Primary EIL signal register | Structured intelligence entries with scoring |
| `memory/vendor-watch/` | Vendor monitoring intelligence | Vendor assessment entries, risk scores, migration briefs |
| `memory/market-patterns/` | Market trend analysis | Market pattern entries with trend direction |
| `memory/competitive-analysis/` | Competitor monitoring | Competitor assessment entries, positioning analysis |
| `memory/failure-patterns/` | Industry and internal failure patterns | Postmortem learning entries, pattern signatures |
| `memory/security-watch/` | Security monitoring intelligence | CVE entries, security advisory assessments |
| `memory/spend-intelligence/` | Spend-related market intelligence | Vendor pricing history, cost benchmarks, spend outcomes |
| `memory/revenue-patterns/` | Revenue system intelligence | Pricing intelligence, revenue outcomes, segment analysis |

### 21.2 Memory Entry Schema

Every EIL memory entry includes:

```yaml
eid: EIL-YYYY-NNN          # EIL entry ID: year-sequence
timestamp: YYYY-MM-DDTHH:MM:SSZ  # ISO-8601 UTC
source: source_name         # Source classification per Section 8
signal_class: SIG-XXX      # Signal classification per Section 9
dimensions:
  bi: 1-5                   # Business Impact score
  ur: 1-5                   # Urgency score
  vr: 1-5                   # Vendor Risk score
  re: 1-5                   # Relevance score
composite: X.X              # Composite priority score
priority: P0-P4             # Priority classification
memory_path: memory/...     # Where this is stored
cross_system_routing:       # Which subsystems received this signal
  - Opportunity Radar
  - Controlled Spend
outcome:                   # Filled when signal resolves
  result: ...
  lessons: ...
append_only: true
```

### 21.3 Memory Retention

EIL memory entries are retained according to the following schedule:

| Entry Type | Retention | Rationale |
|---|---|---|
| SIG-ALR (Alert) | 2 years | Critical incidents; may recur |
| SIG-RSK (Risk) | 2 years | Vendor risk may resurface |
| SIG-OPP (Opportunity) | 1 year | Opportunities expire; market changes |
| SIG-ADV (Advisory) | 6 months | Informational; low-action value |
| SIG-REG (Regulatory) | 5 years | Regulatory history important |
| SIG-COM (Competitive) | 1 year | Competitor landscape changes fast |
| Vendor pricing history | 5 years | Long-term cost analysis |
| Failure pattern entries | 3 years | Pattern recognition value |
| Revenue pattern entries | 3 years | Revenue model calibration |

> **See also:** [Memory Architecture — Retention and archiving](./MEMORY_ARCHITECTURE.md)

---

## 22. Event Emission Standards

EIL emits structured events when signals are detected, scored, and routed. All EIL events follow the Wolfpack event schema.

### 22.1 EIL Event Taxonomy

| Event | Trigger | Routing |
|---|---|---|
| `intel.signal.detected` | External signal identified | → memory/intelligence/; → Wolfpack review if P1+ |
| `intel.risk.detected` | SIG-RSK signal scored P1+ | → memory/security-watch/ or memory/vendor-watch/; → human alert |
| `intel.vendor.changed` | Vendor status, pricing, or capability change | → memory/vendor-watch/; → controlled spend (informational) |
| `intel.failure.ingested` | Industry postmortem or failure pattern captured | → memory/failure-patterns/; → Wolfpack review |
| `intel.pattern.confirmed` | Signal confirmed by 2+ independent sources | → relevant memory/ directory; → Wolfpack review |
| `intel.opportunity.scored` | SIG-OPP signal scored P2+ | → Opportunity Radar; → Wolfpack review if P1+ |
| `intel.spend.signal.detected` | Signal with spend implications | → memory/spend-intelligence/; → controlled spend (informational) |
| `intel.security.signal.detected` | Security-relevant signal | → memory/security-watch/; → human alert if active exploitation |
| `intel.revenue.pattern.detected` | Revenue-relevant market pattern | → memory/revenue-patterns/; → Revenue System |
| `intel.support.pattern.detected` | Support-relevant pattern | → memory/support-patterns/; → AI Support Runtime |
| `intel.worker.pattern.detected` | Worker design-relevant pattern | → memory/failure-patterns/; → Wolfpack review |

### 22.2 Event Schema Compliance

All EIL events comply with the Wolfpack event schema:

```json
{
  "event": "intel.signal.detected",
  "eid": "EIL-2026-001",
  "timestamp": "2026-05-25T00:00:00Z",
  "source": "level_2_official_vendor",
  "source_url": "https://status.twilio.com",
  "signal_class": "SIG-ALR",
  "dimensions": { "bi": 4, "ur": 5, "vr": 5, "re": 4 },
  "composite": 4.4,
  "priority": "P1",
  "signal_summary": "Twilio media incident affecting US-East-1 region",
  "memory_path": "memory/intelligence/EIL-2026-001.md",
  "cross_system_routing": ["Opportunity Radar", "Wolfpack Review"],
  "human_review_required": true,
  "append_only": true
}
```

### 22.3 Event Emission Rules

| Rule | Requirement |
|---|---|
| Every signal produces an event | No silent detection — every EIL signal emits an event |
| Events are immutable | Once emitted, events are append-only — no deletion |
| Events are provenance-tracked | Source URL, timestamp, and classification always present |
| Compound signals emit multiple events | Each signal class triggers its own event |
| P0/P1 events trigger immediate alert | Human alert for SIG-ALR or P0/P1 composite scores |

> **See also:** [Event Schema — EIL event definitions](./operations/EVENT_SCHEMA.md)

---

## 23. Governance Boundaries

EIL operates within strict governance boundaries. These boundaries are non-negotiable.

### 23.1 Hard Boundaries

| Boundary | Definition | Enforcement |
|---|---|---|
| **Intelligence only** | EIL observes and reports; it does not act | No EIL event directly triggers execution |
| **Human review required** | All significant signals require human review before action | Stage 24 human review gate |
| **No financial authorization** | EIL may not authorize spend, payments, or financial transactions | Human API for all financial actions |
| **No canon mutation** | EIL may not modify canonical documents | DEC entry required for canon changes |
| **No production deployment** | EIL may not deploy code or change running systems | Wolfpack review gate for all deployments |
| **No customer data externalization** | EIL may not forward customer data outside Wolfpack | Privacy boundary enforcement |
| **No cross-subsystem commands** | EIL findings are inputs — not authorizations — to other subsystems | Governance layer enforces |

### 23.2 EIL Governance Constraints

| Constraint | Requirement |
|---|---|
| **No connectors** | EIL does not create automated data connections to external systems |
| **No scrapers** | EIL does not scrape websites or APIs for data collection |
| **No ingestion scripts** | EIL does not create automated data ingestion pipelines |
| **No autonomous internet agents** | EIL does not deploy agents that operate on the internet without human review |
| **No execution automation** | EIL does not create automated execution workflows |
| **No payment credential storage** | EIL does not store payment credentials in any form |

---

## 24. Human Review Gates

All EIL outputs pass through human review gates before any action is taken.

### 24.1 Gate Definitions

| Gate | Trigger | Reviewer | SLA |
|---|---|---|---|
| **Stage 24 — Human Alert** | SIG-ALR or P0 composite score | Human (immediate) | Immediate |
| **Stage 72 — Wolfpack Review** | SIG-RSK P1+ or SIG-OPP P1+ | Wolfpack (all 6 roles) | 72 hours |
| **Stage 168 — Weekly Review** | SIG-OPP P2+ or SIG-COM P2+ | Wolfpack ( Opportunity Radar lead) | Weekly cycle |
| **Stage 720 — Monthly Review** | SIG-ADV or SIG-REG | Wolfpack (legal if SIG-REG) | Monthly cycle |

### 24.2 Gate Routing Rules

| Signal | Routed To | Gate |
|---|---|---|
| SIG-ALR | Human + Wolfpack | Stage 24 immediate |
| SIG-RSK P0/P1 | Human + Wolfpack | Stage 24 / 72 |
| SIG-RSK P2/P3 | Wolfpack | Stage 168 / 720 |
| SIG-OPP P0/P1 | Human + Wolfpack + Opportunity Radar | Stage 24 / 72 |
| SIG-OPP P2 | Opportunity Radar | Stage 168 |
| SIG-ADV | Wolfpack | Stage 720 |
| SIG-REG | Legal + Wolfpack | Stage 72 |
| SIG-COM | Opportunity Radar | Stage 168 |

### 24.3 Gate Override Prohibition

**No EIL signal may bypass its assigned human review gate.** A SIG-RSK P1 signal scored by EIL may not be acted upon without Wolfpack review, regardless of how urgent the signal appears. The gate exists to ensure governance oversight — it cannot be overridden by the signal itself.

---

## 25. Human API Reduction Strategy

EIL's long-term goal is to reduce the number of decisions that require human input — not by bypassing humans, but by building sufficient institutional memory that routine decisions can be made faster through structured precedent.

### 25.1 Reduction Principles

| Principle | Description |
|---|---|
| **Precedent-based decisions** | When EIL has sufficient historical precedent (similar signals with known outcomes), decisions can be pre-routed to the correct subsystem with higher confidence |
| **Confidence thresholds** | Decision acceleration only when EIL confidence score ≥ 0.85 based on historical outcomes |
| **Human-in-the-loop preserved** | Humans are never removed from the decision — they receive faster, better-structured inputs |
| **Governance override** | Any human may override EIL routing recommendations at any time |

### 25.2 Reduction Triggers

| Trigger | Action |
|---|---|
| 10+ similar signals with identical outcomes | EIL may pre-route to subsystem with human confirmation request |
| 90%+ historical accuracy on signal classification | EIL confidence score elevated |
| 0 governance overrides in 90 days on a signal type | EIL may propose accelerated routing for that type |
| Any governance override | EIL routing confidence reset to baseline for that signal type |

### 25.3 Not Reduction Of

- Human review gates are never reduced
- Spend authorization thresholds are never reduced
- Canon mutation requirements are never reduced
- Wolfpack review gate requirements are never reduced

---

## 26. Retention Policies

EIL maintains intelligence records according to the following retention policies.

### 26.1 Signal Record Retention

| Record Type | Retention Period | Archive Trigger |
|---|---|---|
| Raw signal entries | 1 year from detection | Archive after 1 year if P3/P4 |
| Scored signal entries (P0/P1) | 2 years | Archive after 2 years |
| Scored signal entries (P2/P3) | 1 year | Archive after 1 year |
| Vendor assessment entries | 3 years | Archive after 3 years |
| Market pattern entries | 2 years | Archive after 2 years |
| Failure pattern entries | 3 years | Archive after 3 years |
| Security watch entries | 5 years | Archive after 5 years |

### 26.2 Archive Standards

Archived entries:
- Move to `archive/intelligence/` directory
- Maintain full provenance metadata
- Remain accessible for audit and pattern analysis
- Are never modified or deleted

### 26.3 Disposal

EIL never disposes of any record. All entries are either active or archived. No deletion.

> **See also:** [Memory Architecture — Retention and archiving](./MEMORY_ARCHITECTURE.md)

---

## 27. Escalation Rules

EIL escalation rules define how signals move from routine monitoring to urgent response.

### 27.1 Escalation Criteria

| Escalation Trigger | From | To |
|---|---|---|
| Signal confirmed by 2+ independent sources | Routine | Elevated |
| Signal contradicts established canon | Elevated | Wolfpack review |
| Signal matches known failure pattern | Routine | Wolfpack review |
| Signal scored P1+ and not reviewed within 72 hours | Routine | Human alert |
| Worker reports anomaly matching EIL signal | Routine | Wolfpack review |
| Support Runtime reports pattern matching EIL signal | Routine | Wolfpack review |

### 27.2 Escalation Path

```
Level 1 — Routine (P3/P4)
  → EIL memory entry + weekly review
  
Level 2 — Elevated (P2, or confirmed P3/P4)
  → EIL memory entry + Wolfpack weekly review
  
Level 3 — High (P1)
  → EIL memory entry + Wolfpack review within 72 hours + human alert
  
Level 4 — Critical (P0 or SIG-ALR)
  → EIL memory entry + immediate human alert + Wolfpack review within 24 hours
  
Level 5 — Canon Conflict
  → EIL memory entry + Wolfpack review + DEC entry required before any action
```

### 27.3 De-escalation

A signal may be de-escalated if:
- New information reduces the composite score by ≥ 1.0
- The signal is a false positive confirmed by Wolfpack review
- The signal is superseded by a more accurate signal from the same source

De-escalation is logged in the signal entry with rationale.

---

## 28. Definition of Done

EIL is operating correctly when ALL of the following are true:

| # | Criterion | Verification Method |
|---|---|---|
| 1 | Every detected external signal produces a memory entry | `memory/intelligence/` entries exist for all signals |
| 2 | Every signal is scored using the 4-dimension model | All entries have BI/UR/VR/RE dimensions and composite score |
| 3 | Every signal is classified into a signal class | All entries have signal_class field |
| 4 | Every P1+ signal triggers human review within SLA | Human review timestamp logged in entry |
| 5 | EIL never autonomously triggers execution | No EIL event directly in execution workflow |
| 6 | EIL findings pass through human review gate before any financial action | Spend records show human approval |
| 7 | EIL never mutates canon without DEC entry | No canon file modified by EIL |
| 8 | Worker execution results feed back into EIL memory | `memory/failure-patterns/` contains worker failure entries |
| 9 | Support Runtime patterns feed back into EIL memory | `memory/support-patterns/` contains support pattern entries |
| 10 | Revenue outcomes feed back into EIL memory | `memory/revenue-patterns/` contains outcome entries |
| 11 | No prohibited sources are in the intelligence register | Source verification on all entries |
| 12 | No prohibited behaviors occur | Governance audit log clean |
| 13 | All compound signals produce multiple events | One event per signal class |
| 14 | All events follow the event schema | Schema validation on all events |
| 15 | Validator runs after every workflow cycle | Stage 8 exit code 0 confirmed |

---

*Canonical — GitHub is the source of truth.*
*Wolfpack External Intelligence Layer v1 — 2026-05-25*
