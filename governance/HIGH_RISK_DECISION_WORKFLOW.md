---
title: "HIGH-Risk Overlay Decision Workflow — Step-by-Step Governance Process"
document_type: "workflow"
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
  - "workflow"
  - "high-risk"
  - "decision"
  - "batch-002"
related_ids:
  - "governance/HIGH_RISK_OVERLAY_ESCALATION_STANDARD.md"
  - "governance/HIGH_RISK_CONFLICT_REGISTRY.md"
  - "governance/DOCTRINE_OVERLAY_RECONCILIATION_STANDARD.md"
append_only: true
---

# HIGH-Risk Overlay Decision Workflow — Step-by-Step Governance Process

> **Source:** Wolfpack institutional memory — escalation governance layer  
> **Status:** Active — Canonical Governance Workflow  
> **Activation Date:** 2026-05-24  
> **Applies to:** All overlays classified as HIGH risk

---

## Overview

This document defines the mandatory step-by-step workflow for processing HIGH-risk doctrine overlays. Each step must be completed in order. No step may be skipped. An overlay may not proceed past any step until that step is fully completed and documented.

**11 Steps:**
`intake` → `checksum` → `extraction` → `comparison` → `conflict_mapping` → `DEC_creation` → `wolfpack_review` → `human_oversight` → `reconciliation` → `activation_approval` → `post_activation_audit`

**See also:** [Escalation Standard](./HIGH_RISK_OVERLAY_ESCALATION_STANDARD.md) — definitions and rules  
**See also:** [Conflict Registry](./HIGH_RISK_CONFLICT_REGISTRY.md) — conflict tracking

---

## Step 1 — Intake

**Definition:** Receive and register the HIGH-risk source document.

| Requirement | Action |
|---|---|
| **Document receipt** | Source PDF attached to conversation or confirmed in archive |
| **Registry check** | Verify entry exists in `archive/SOURCE_DOCUMENT_REGISTRY.md` |
| **Risk classification** | Confirm `overlay_risk: HIGH` in registry |
| **Workflow assignment** | Assign Wolfpack review session for this overlay |
| **Halting rule** | No extraction until all intake steps complete |

**Deliverable:** Source document registered; workflow initiated; next step authorized.

---

## Step 2 — Checksum Verification

**Definition:** Compute and verify SHA-256 checksum before any file operation.

| Requirement | Action |
|---|---|
| **Checksum computation** | `sha256sum` on the source PDF |
| **Registry update** | Update `checksum` field in `SOURCE_DOCUMENT_REGISTRY.md` |
| **Archive copy** | Copy to `archive/source-documents/[category]/` |
| **Integrity check** | Verify archived copy matches checksum |
| **Halt on mismatch** | Checksum mismatch = governance incident → halt workflow |

**Checksum format:** `sha256:<hex>` (e.g., `sha256:a42cf500186d6d6796d95c82859c13a6e34a69ba8e97e279ccdcd320b0b47e47`)

**Deliverable:** Checksum verified, registered, and archived. Integrity confirmed.

---

## Step 3 — Extraction

**Definition:** Extract text from the HIGH-risk PDF for analysis.

| Requirement | Action |
|---|---|
| **HO-1 approval** | Explicit human approval to extract (per Escalation Standard §6, HO-1) |
| **Tool selection** | Use pypdf with PYTHONPATH pointing to workspace `.pdf_deps` |
| **Text capture** | Extract all pages; preserve page boundaries |
| **Extraction log** | Record page count, extraction tool version, and timestamp |
| **No interpretation** | Extract text verbatim — no semantic processing during extraction |

**Deliverable:** Full extracted text available for analysis. Extraction log appended to review document.

---

## Step 4 — Overlay Comparison

**Definition:** Compare the extracted text against all relevant canonical files.

| Requirement | Action |
|---|---|
| **Canon scan** | Compare against all files in `canon/`, `agents/`, and relevant `operations/` |
| **Doctrine extraction** | Identify all claims, principles, and directives in the source doc |
| **Alignment check** | Mark each claim as: aligns, contradicts, expands, duplicates, or drifts |
| **Affected files** | List all canon files that have alignment or conflict with source doc |
| **No canon modification** | Comparison is analysis only — no file modifications at this step |

**Deliverable:** Overlay comparison matrix documenting every claim's relationship to existing canon.

---

## Step 5 — Conflict Mapping

**Definition:** Map each detected conflict to a category and record in the conflict registry.

| Requirement | Action |
|---|---|
| **Conflict identification** | Every conflict must be identified and categorized |
| **Category assignment** | Assign conflict code: `CD`, `CI`, `CT`, `CS`, `CP`, `CE`, `CG`, or `CU` |
| **Registry entry** | Each conflict gets an entry in `HIGH_RISK_CONFLICT_REGISTRY.md` |
| **Unresolved preservation** | Unresolved conflicts must remain documented — never deleted |
| **No auto-resolution** | No conflict may be marked resolved without DEC entry or human approval |

**Conflict severity by category:**
- `CD` (Direct contradiction): **Blocking** — cannot activate until resolved
- `CI` (Indirect contradiction): **Blocking** — cannot activate until resolved
- `CG` (Governance override): **Blocking** — cannot activate until resolved
- `CP` (Supersession claim): **Blocking** — cannot activate until authority verified
- `CS` (Scope overlap): **Conditional** — may activate with DEC entry and conditions
- `CE` (Expansion conflict): **Conditional** — may activate with DEC entry and conditions
- `CT` (Terminology collision): **Warning** — may activate with cross-reference
- `CU` (Unclassifiable): **Halt** — escalate to human oversight

**Deliverable:** All conflicts mapped, categorized, and registered. No conflict unmarked.

---

## Step 6 — DEC Creation

**Definition:** Create a DEC (Decision) entry for each blocking conflict (`CD`, `CI`, `CS`, `CP`, `CG`).

| Requirement | Action |
|---|---|
| **DEC for each blocking conflict** | One DEC entry per blocking conflict |
| **DEC structure** | `DEC-00n`, overlay_id, conflict_id, conflict_type, resolution, conditions, rollback |
| **Resolution types** | `approve`, `reject`, `approve_with_conditions`, `suppress` |
| **Human approval (HO-3)** | Explicit HO-3 approval required before DEC is appended |
| **Append-only** | DEC entries may only be added — never modified |
| **Precedent check** | Verify no existing DEC conflicts with proposed resolution |

**DEC entry format:**
```markdown
## DEC-00n — [title]

**overlay_id:** OVL-YYYY-NNN
**conflict_id:** [from registry]
**decision:** [approve/reject/approve_with_conditions/suppress]
**resolution:** [explanation]
**conditions:** [any conditions or null]
**rollback_path:** [git commit hash of known-good pre-activation state]
**human_approval:** [name + timestamp]
**logged_date:** YYYY-MM-DD
```

**Deliverable:** DEC entries created for all blocking conflicts. Human approval recorded.

---

## Step 7 — Wolfpack Review

**Definition:** Full Wolfpack review (5 roles) of the HIGH-risk overlay.

| Requirement | Action |
|---|---|
| **All 5 roles review** | Opportunity Radar, Red Team, Deployment Governor, Memory Keeper, Eterna |
| **Review scope** | All conflicts, DEC entries, reconciliation proposals, and conditions |
| **Recommendation per role** | Each role must produce: approve / reject / approve_with_conditions / escalate |
| **Conflict-specific review** | Each role must address each blocking conflict by conflict_id |
| **Deployment Governor endorsement** | HO-4 endorsement required before proceeding |
| **No majority-vote activation** | Wolfpack review is advisory — human approval still required |

**Deliverable:** Wolfpack review document with 5-role analysis. All recommendations recorded.

---

## Step 8 — Human Oversight Checkpoint

**Definition:** Explicit human approval at each oversight checkpoint.

| Checkpoint | Required Approval | Who |
|---|---|---|
| **HO-1** | Extraction approval | Human Operator |
| **HO-2** | Conflict review | Human Operator |
| **HO-3** | DEC creation | Human Operator or Deployment Governor |
| **HO-4** | Wolfpack review endorsement | Deployment Governor |
| **HO-5** | Activation approval | Human Operator |
| **HO-6** | Supersession authorization | Human Operator + Deployment Governor |

**Documentation:** Each approval must be recorded in the review document with name/role and timestamp. Silent or implied approval is not sufficient.

**Deliverable:** All 6 oversight checkpoints approved and documented. Workflow authorized to proceed.

---

## Step 9 — Reconciliation

**Definition:** Resolve all non-blocking conflicts and prepare final reconciliation proposal.

| Requirement | Action |
|---|---|
| **Blocking conflict resolution** | All `CD`, `CI`, `CG`, `CP` conflicts must have DEC entries with `approve` or `reject` |
| **Conditional conflict handling** | All `CS`, `CE` conflicts must have DEC entries with `approve_with_conditions` |
| **Terminology resolution** | All `CT` conflicts must have cross-reference documentation |
| **Unclassifiable halt** | Any `CU` conflict → halt workflow → escalate to Human Operator |
| **Reconciliation proposal** | Final document: conflicts resolved, conditions set, canonical target defined |
| **No unresolved blocking** | Reconciliation may not proceed with unresolved `CD`, `CI`, or `CG` |

**Deliverable:** Reconciliation proposal ready for activation approval.

---

## Step 10 — Activation Approval

**Definition:** Explicit approval to activate the reconciled overlay as canonical doctrine.

| Requirement | Action |
|---|---|
| **All 8 gates satisfied** | Verify gates G1–G8 from Escalation Standard §12 |
| **Rollback path documented** | Known-good commit hash confirmed and documented |
| **Human HO-5 approval** | Explicit activation approval from Human Operator |
| **Canonical target identified** | Target file path confirmed (e.g., `canon/OS_DOCTRINE_OVERVIEW.md`) |
| **Activation conditions set** | Any conditions from DEC entries must be incorporated |
| **Governance log entry** | Overlay decision log updated with activation authorization |

**Gate verification checklist:**
- [ ] G1 — Escalation completed
- [ ] G2 — DEC entry created for all blocking conflicts
- [ ] G3 — Wolfpack review passed (all 5 roles)
- [ ] G4 — Human oversight approved (all 6 checkpoints)
- [ ] G5 — Rollback path identified
- [ ] G6 — No unresolved CD/CI/CG
- [ ] G7 — Fragmentation check passed
- [ ] G8 — Precedence verified

**Deliverable:** Activation authorized. Canonical extraction and file creation authorized.

---

## Step 11 — Post-Activation Audit

**Definition:** Verify the activated overlay is correctly integrated and no corruption occurred.

| Requirement | Action |
|---|---|
| **Canonical file verification** | New doc created at target path with correct front matter |
| **Checksum recorded** | SHA-256 of source PDF recorded in new doc's provenance |
| **Registry updated** | `SOURCE_DOCUMENT_REGISTRY.md` status set to `active` |
| **Overlay queue updated** | `OVERLAY_REVIEW_QUEUE.md` status set to `activated` |
| **Decision log updated** | `OVERLAY_DECISION_LOG.md` decision entry finalized |
| **Cross-references verified** | All affected canon files have correct cross-references |
| **Runtime validator run** | `tasks/runtime_state_validator.py` executed — must PASS |
| **No regressions** | All existing canon files remain valid and accessible |

**Deliverable:** Post-activation audit report. All systems verified. Overlay fully integrated.

---

## Workflow Summary

| Step | Name | Blocking? | Human Required? |
|---|---|---|---|
| 1 | Intake | No | No |
| 2 | Checksum Verification | Yes | No |
| 3 | Extraction | Yes | Yes (HO-1) |
| 4 | Overlay Comparison | No | No |
| 5 | Conflict Mapping | Yes | No |
| 6 | DEC Creation | Yes | Yes (HO-3) |
| 7 | Wolfpack Review | Yes | Yes (HO-4) |
| 8 | Human Oversight | Yes | Yes (HO-1–6) |
| 9 | Reconciliation | Yes | No |
| 10 | Activation Approval | Yes | Yes (HO-5) |
| 11 | Post-Activation Audit | No | No |

**Total mandatory human oversight checkpoints:** 6 (HO-1 through HO-6)

---

## Rollback Path

At any point before Step 11 completion, if a governance failure is detected:
1. Halt all workflows
2. Do not proceed to next step
3. Log incident in `operations/INCIDENT_LOG.md`
4. Identify rollback commit (last known-good state before workflow started)
5. Notify Human Operator
6. Await human instruction before resuming

---

*Canonical — GitHub is the source of truth.*