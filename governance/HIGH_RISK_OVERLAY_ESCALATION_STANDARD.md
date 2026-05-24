---
title: "HIGH-Risk Overlay Escalation Standard — Doctrine Conflict Governance"
document_type: "governance"
status: "active"
version: "1.0"
created: "2026-05-24"
updated: "2026-05-24"
source_type: "internal"
provenance:
  source: "wolfpack-institutional-memory"
  source_type: "internal"
  ingested_by: "Eterna / Wolfpack"
  ingest_date: "2026-05-24"
  batch: "STAGE_1_BATCH_002B"
tags:
  - "governance"
  - "escalation"
  - "high-risk"
  - "overlay"
  - "batch-002"
related_ids:
  - "governance/HIGH_RISK_DECISION_WORKFLOW.md"
  - "governance/HIGH_RISK_CONFLICT_REGISTRY.md"
  - "governance/DOCTRINE_OVERLAY_RECONCILIATION_STANDARD.md"
  - "governance/OVERLAY_DECISION_LOG.md"
append_only: true
---

# HIGH-Risk Overlay Escalation Standard — Doctrine Conflict Governance

> **Source:** Wolfpack institutional memory — escalation governance layer  
> **Status:** Active �� Canonical Governance Doctrine  
> **Activation Date:** 2026-05-24  
> **Applies to:** All overlays classified as HIGH risk in the doctrine ingestion pipeline

---

## Purpose

This document establishes formal governance standards for handling **HIGH-risk doctrine overlays** — source documents that may contradict, supersede, or fragment existing canonical memory. It defines the escalation process, conflict categories, precedence enforcement, and activation gating requirements that must be satisfied before any HIGH-risk overlay can be canonicalized.

HIGH-risk overlays are the most dangerous class of doctrine ingestion events because they can introduce contradictions that silently corrupt the institutional memory, replace established governance with incompatible doctrine, or fragment canonical coherence across the Wolfpack system.

**This standard exists to ensure that no HIGH-risk overlay is ever activated without explicit human oversight and a formal conflict resolution process.**

---

## 1. Definition of HIGH-Risk Overlay

**Definition:** A HIGH-risk overlay is any source document that, during initial risk classification, is assessed as potentially containing one or more of:

| Risk Category | Indicator | Examples |
|---|---|---|
| **Contradiction** | Document claims the inverse or negates an existing canonical principle | "Agents may bypass governance" vs. "Agents may never bypass governance" |
| **Supersession** | Document purports to replace an existing canonical file or section | A new System Architecture doc that revises DEC-001 architecture |
| **Fragmentation** | Document introduces parallel doctrine that conflicts with existing canon structure | A new memory spec that contradicts the canonical Memory Architecture |
| **Authority conflict** | Document claims equal or higher canonical authority than existing canon | A vendor-produced spec claiming to supersede Wolfpack Canon |
| **Scope collision** | Document covers the same domain as an existing canon file with incompatible conclusions | A new deployment doctrine that contradicts DEPLOYMENT_GOVERNOR.md |

**Classification rule:** Any overlay that triggers one or more of these indicators must be classified as HIGH risk before extraction.

> **See also:** [Decision Workflow — HIGH Risk](./HIGH_RISK_DECISION_WORKFLOW.md) — step-by-step handling  
> **See also:** [Conflict Registry](./HIGH_RISK_CONFLICT_REGISTRY.md) — conflict tracking

---

## 2. Escalation Triggers

An overlay must be escalated to HIGH-risk governance when **any** of the following triggers are detected:

| Trigger | Condition | Required Action |
|---|---|---|
| **T1 — Contradiction signal** | Source doc makes a claim that is the logical inverse or negation of an existing canonical statement | Immediate halt; escalate to DEC process |
| **T2 — Supersession claim** | Source doc explicitly states or implies it supersedes an existing canonical file | Immediate halt; require canonical authority verification |
| **T3 — Architecture revision** | Source doc modifies the Wolfpack architecture defined in DEC-001 or System Architecture | Immediate halt; require DEC entry before extraction |
| **T4 — Governance bypass** | Source doc describes a mechanism that bypasses, overrides, or neutralizes an existing governance gate | Immediate halt; require human oversight approval |
| **T5 — Silent overwrite detection** | Checksum verification reveals source doc may silently overwrite an existing canonical file | Immediate halt; require checksum clarification |
| **T6 — Terminology redefinition** | Source doc redefines a term already defined in existing canonical glossary | Flag as terminology drift; assess scope |
| **T7 — Precedent conflict** | Source doc cites a precedent (DEC, Wolfpack review) that the existing canon does not recognize | Require precedent verification |
| **T8 — Authority claim** | Source doc claims canonical authority (e.g., "this is the authoritative spec") without Wolfpack attribution | Require authority verification |

**Escalation is mandatory.** No HIGH-risk overlay may proceed past the risk classification step without triggering the escalation workflow. Failure to escalate a HIGH-risk overlay is a governance incident.

---

## 3. Conflict Categories

When a HIGH-risk overlay is compared against existing canon, conflicts are categorized as follows:

| Category | Code | Definition | Resolution Path |
|---|---|---|---|
| **Direct contradiction** | `CD` | Source doc explicitly negates an existing canonical statement | DEC entry required; human oversight required; may not be auto-resolved |
| **Indirect contradiction** | `CI` | Source doc's implications are incompatible with existing canonical conclusions | DEC entry required; Wolfpack review required |
| **Terminology collision** | `CT` | Source doc uses the same term with a different meaning, creating confusion | Cross-reference glossary; document mapping |
| **Scope overlap** | `CS` | Source doc covers canon territory with different conclusions | DEC entry required; determine which scope governs |
| **Supersession claim** | `CP` | Source doc claims to replace or revise existing canon | Require authority verification; if unverified, reject |
| **Expansion conflict** | `CE` | Source doc expands a canon section but introduces incompatible principles | DEC entry required; approve expansion vs. reject |
| **Governance override** | `CG` | Source doc attempts to override a governance decision (DEC, Wolfpack review) | Automatic rejection unless DEC explicitly authorizes supersession |
| **Unclassifiable** | `CU` | Conflict does not fit any defined category | Halt and escalate to human oversight; assign DEC review |

**Each detected conflict must be recorded in the [HIGH_RISK_CONFLICT_REGISTRY.md](./HIGH_RISK_CONFLICT_REGISTRY.md) before any resolution process begins.**

---

## 4. Truth-Authority Collision Rules

When a source document's claims collide with established canonical truth, the following rules determine which authority prevails:

### Rule 1 — Canonical Hierarchy Supreme

**Established canonical memory always prevails over incoming source documents unless a formal supersession process is completed.**

| Authority Level | Source | Override Requires |
|---|---|---|
| **1 — Active canonical memory** | `canon/` files with `status: active` | DEC entry + human approval + Wolfpack review |
| **2 — Approved DEC entries** | `governance/DECISIONS.md` and `OVERLAY_DECISION_LOG.md` | New DEC entry + human approval |
| **3 — Checksum-verified source docs** | Archived PDFs with registered SHA-256 | DEC entry + Wolfpack review + human approval |
| **4 — Extracted markdown** | `canon/` markdown from PDF extraction | Wolfpack review + human approval |
| **5 — Unreviewed uploads** | Source docs pending review | Full escalation workflow |

**No source document may jump authority levels.** A checksum-verified source doc (level 3) cannot override active canonical memory (level 1) without going through the full escalation process.

### Rule 2 — Supersession Requires Authority

A source document that claims to supersede or replace existing canon **must** provide evidence of authority to do so. Evidence required:

- Written authorization from Human Operator
- Written authorization from Deployment Governor
- New DEC entry specifically authorizing supersession

Without all three, the supersession claim is **rejected by default.**

### Rule 3 — No Silent Replacement

**Categorically prohibited:** A source document may not silently replace, revise, or override an existing canonical file without:
1. A formal DEC entry authorizing the change
2. A git history showing the old file marked `status: archived`
3. Human Operator approval of the replacement

### Rule 4 — Inversion Requires Explicit Label

If a source document contains a principle that is the logical inverse of an existing canonical principle, the inversion must be:
1. Explicitly labeled in the review document
2. Rejected by default unless DEC entry explicitly approves the inversion
3. Documented in the conflict registry with the `CD` (direct contradiction) category

---

## 5. Precedence Enforcement Requirements

The following requirements enforce the canonical precedence hierarchy for HIGH-risk overlays:

| Requirement | Description |
|---|---|
| **Pre-extraction halt** | No HIGH-risk overlay may be extracted until all escalation steps are complete |
| **Checksum before review** | SHA-256 checksum must be computed and registered before any extraction |
| **Precedence comparison** | All claims in the source doc must be compared against existing canon before activation |
| **Conflict catalog** | Every detected conflict must be catalogued in the conflict registry |
| **DEC entry for conflicts** | All `CD`, `CI`, `CS`, `CP`, `CG` conflicts require a DEC entry before resolution |
| **Wolfpack review gate** | All HIGH-risk overlays require Wolfpack review (5 roles) before activation |
| **Human oversight checkpoint** | All HIGH-risk overlays require explicit human approval before activation |
| **Append-only registry** | Conflict registry entries may only be added, never modified |

---

## 6. Mandatory Human Oversight Points

Human oversight is required at the following points in the HIGH-risk overlay workflow:

| Checkpoint | Required Action | Who |
|---|---|---|
| **HO-1 — Extraction approval** | Explicit approval to extract text from the HIGH-risk PDF | Human Operator |
| **HO-2 — Conflict review** | Review of all catalogued conflicts before DEC creation | Human Operator |
| **HO-3 — DEC approval** | Explicit approval of DEC entry before it is appended | Human Operator or Deployment Governor |
| **HO-4 — Wolfpack review endorsement** | Explicit endorsement of Wolfpack review outcome | Deployment Governor |
| **HO-5 — Activation approval** | Explicit approval to activate the canonicalized doc | Human Operator |
| **HO-6 — Supersession authorization** | Explicit written authorization for any supersession claim | Human Operator + Deployment Governor |

**No HIGH-risk overlay may proceed past any oversight checkpoint without explicit approval.** Silent or implicit approval is not sufficient.

---

## 7. Prohibited Automatic Activation

The following are **categorically prohibited** for HIGH-risk overlays:

| Prohibited Action | Rationale |
|---|---|
| **Automatic PDF extraction** | Extraction must be approved at HO-1 |
| **Automatic text processing** | Full workflow required before any activation |
| **Implicit consent** | No activation on silence or absence of objection |
| **Majority-vote activation** | Wolfpack review is advisory; human approval is required |
| **Automatic conflict resolution** | All conflicts require DEC entry or explicit human resolution |
| **Auto-rollback activation** | Rollback of HIGH-risk overlays requires human approval |
| **Silent merge** | No source doc may be merged into canon without explicit approval |
| **Precedent override** | Existing DEC entries may not be overridden without new DEC entry |

**Penalty for violation:** Activation of a HIGH-risk overlay in violation of this standard is a governance incident requiring immediate rollback, incident logging, and governance review.

---

## 8. Rollback Requirements

If a HIGH-risk overlay is activated in error or a contradiction is discovered post-activation:

| Requirement | Description |
|---|---|
| **Immediate halt** | All workflows against the activated doc halt immediately |
| **Incident log entry** | An incident must be logged in `operations/INCIDENT_LOG.md` |
| **State revert** | The document must be marked `status: archived` in git history (not deleted) |
| **Registry entry** | Conflict registry updated with rollback reference |
| **Affected canon restore** | All canon files that were affected must be reviewed for corruption |
| **Human notification** | Human Operator must be notified within 30 minutes |
| **Root cause analysis** | A postmortem must be filed documenting the failure |

**Rollback commit** must be identified before activation is approved. Rollback commit must be a known-good commit with no corruption.

---

## 9. Supersession Handling

When a source document claims to supersede an existing canonical file:

| Step | Action |
|---|---|
| **1** | Verify authority claim — require written authorization |
| **2** | If authority unverified → reject supersession claim, treat as overlay only |
| **3** | If authority verified → create DEC entry specifically for supersession |
| **4** | Old canonical file marked `status: superseded` with reference to new doc |
| **5** | New doc activated with explicit supersession note in front matter |
| **6** | All cross-references updated to point to new doc |
| **7** | Post-activation audit confirms all references updated |

**Without authority verification, supersession claims are rejected and the document is processed as an additive overlay only.**

---

## 10. Doctrine Fragmentation Prevention

**Definition:** Doctrine fragmentation occurs when two or more canonical files make incompatible claims about the same domain, creating contradictory operational guidance.

**Prevention rules:**

| Rule | Description |
|---|---|
| **Single-source doctrine** | Each operational domain must have exactly one authoritative canonical file |
| **Cross-reference enforcement** | New canonical files must cross-reference existing files in the same domain |
| **Conflict-on-ingest** | Any detected scope overlap must trigger DEC entry before activation |
| **Fragmentation audit** | Before activating a new canonical file, verify no existing file covers the same domain with incompatible conclusions |
| **Glossary check** | Verify no terminology in the new doc conflicts with the canonical glossary |

---

## 11. Unresolved Conflict Preservation

When conflicts cannot be resolved before a workflow deadline:

| Requirement | Description |
|---|---|
| **Conflict preserved in registry** | All unresolved conflicts must be recorded in `HIGH_RISK_CONFLICT_REGISTRY.md` |
| **No activation with unresolved CD/CI/CG** | Overlays with unresolved `CD` (direct contradiction) or `CI` (indirect contradiction) or `CG` (governance override) may NOT be activated |
| **Activation with unresolved CS/CE/CT** | Overlays with only scope (`CS`), expansion (`CE`), or terminology (`CT`) conflicts may be activated if conditions are met — requires DEC entry |
| **Time-bound resolution** | Unresolved conflicts must have a resolution deadline (max 30 days) |
| **Periodic review** | Unresolved conflicts must be reviewed at each governance review cycle |
| **Escalation on deadline miss** | Conflicts approaching deadline must be escalated to Human Operator |

---

## 12. Activation Gating Requirements

A HIGH-risk overlay may only be activated when **all** of the following gates are satisfied:

| Gate | Requirement | Verified By |
|---|---|---|
| **G1 — Escalation completed** | All escalation triggers resolved or documented | Eterna / Wolfpack |
| **G2 — DEC entry created** | All `CD`, `CI`, `CS`, `CP`, `CG` conflicts have DEC entries | Wolfpack review |
| **G3 — Wolfpack review passed** | All 5 roles have approved or formally escalated | Wolfpack review gate |
| **G4 — Human oversight approved** | All 6 oversight checkpoints have explicit approval | Human Operator |
| **G5 — Rollback path identified** | Known-good rollback commit documented | Deployment Governor |
| **G6 — No unresolved CD/CI/CG** | All direct, indirect, and governance-override conflicts resolved | Eterna / Wolfpack |
| **G7 — Fragmentation check passed** | No doctrinal fragmentation detected | Wolfpack review |
| **G8 — Precedence verified** | Source doc authority level confirmed; precedence hierarchy enforced | Eterna / Wolfpack |

**No exceptions.** An overlay with an unsatisfied gate may not be activated, regardless of urgency or external pressure.

---

## References

| Reference | Description |
|---|---|
| [HIGH Risk Decision Workflow](./HIGH_RISK_DECISION_WORKFLOW.md) | Step-by-step workflow for HIGH-risk overlays |
| [HIGH Risk Conflict Registry](./HIGH_RISK_CONFLICT_REGISTRY.md) | Conflict tracking registry |
| [Overlay Decision Log](./governance/OVERLAY_DECISION_LOG.md) | DEC entries for all overlay decisions |
| [Doctrine Overlay Reconciliation Standard](./DOCTRINE_OVERLAY_RECONCILIATION_STANDARD.md) | General overlay governance |

---

*Canonical — GitHub is the source of truth.*