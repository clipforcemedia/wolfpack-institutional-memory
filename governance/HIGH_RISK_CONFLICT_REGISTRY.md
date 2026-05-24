---
title: "HIGH-Risk Conflict Registry — Doctrine Conflict Tracking"
document_type: "conflict-registry"
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
  - "conflict"
  - "registry"
  - "high-risk"
  - "batch-002"
related_ids:
  - "governance/HIGH_RISK_OVERLAY_ESCALATION_STANDARD.md"
  - "governance/HIGH_RISK_DECISION_WORKFLOW.md"
  - "governance/OVERLAY_DECISION_LOG.md"
append_only: true
---

# HIGH-Risk Conflict Registry — Doctrine Conflict Tracking

> **Source:** Wolfpack institutional memory — escalation governance layer  
> **Status:** Active — Append-Only Conflict Registry  
> **Activation Date:** 2026-05-24  
> **Applies to:** All HIGH-risk doctrine overlays in the Batch 002 pipeline

---

## Purpose

This registry tracks every conflict detected during HIGH-risk overlay reviews. It is the authoritative record of doctrine conflicts and their resolution states. Entries are **append-only** — conflicts are never deleted, only marked as resolved.

**Schema per entry:** `conflict_id`, `overlay_id`, `affected_canon`, `conflict_type`, `description`, `precedence_ruling`, `resolution_state`, `rollback_reference`, `reviewer_approvals`

**Conflict type codes:**
- `CD` — Direct contradiction
- `CI` — Indirect contradiction
- `CT` — Terminology collision
- `CS` — Scope overlap
- `CP` — Supersession claim
- `CE` — Expansion conflict
- `CG` — Governance override
- `CU` — Unclassifiable

**Resolution states:**
- `pending` — Conflict identified, resolution in progress
- `resolved_approve` — DEC entry approved the overlay against this conflict
- `resolved_reject` — DEC entry rejected the overlay against this conflict
- `resolved_conditions` — DEC entry approved with conditions
- `unresolved` — Conflict identified but not yet resolved (requires time-bound resolution)
- `superseded` — Later DEC entry resolved this conflict

**Blocking status:**
- `CD`, `CI`, `CG`, `CP` → **Blocking** — cannot activate until resolved
- `CS`, `CE` → **Conditional** — may activate with conditions
- `CT` → **Warning** — may activate with cross-reference
- `CU` → **Halt** — escalate immediately

---

## Registry Entries

*(No entries yet — registry initialized for Batch 002 HIGH-risk overlays. OVL-20260524-003 will be the first entry when its review begins.)*

---

## Conflict Schema Reference

Each entry in this registry follows this structure:

```yaml
conflict_id:  string   # CFG-YYYY-NNN format
overlay_id:  string   # OVL-YYYY-NNN format
affected_canon: string[]  # Canonical files affected by this conflict
conflict_type: string    # CD | CI | CT | CS | CP | CE | CG | CU
description: string      # Plain-language description of the conflict
canonical_claim: string  # What the existing canon states
incoming_claim: string   # What the incoming source doc states
precedence_ruling: string # Which authority prevails and why
blocking: boolean        # true if CD/CI/CG/CP, false otherwise
resolution_state: string # pending | resolved_approve | resolved_reject | resolved_conditions | unresolved | superseded
resolution: string|null # DEC entry or null if unresolved
rollback_reference: string|null # Git commit hash of rollback point or null
reviewer_approvals: object  # { opportunity_radar, red_team, deployment_governor, memory_keeper, eterna }
created: string         # YYYY-MM-DD
updated: string         # YYYY-MM-DD
```

---

## Unresolved Conflict Protocol

| State | Action Required |
|---|---|
| `pending` | Active resolution in progress — track DEC entry |
| `unresolved` | Deadline set (max 30 days); escalate to Human Operator if approaching deadline |
| `resolved_approve` | Overlay may proceed against this conflict |
| `resolved_reject` | Overlay may NOT proceed; canonical prevails |
| `resolved_conditions` | Overlay may proceed only if all conditions met |
| `superseded` | Conflict resolved by later DEC; archive entry |

---

## Blocking Conflict Protocol

For `CD` (direct contradiction), `CI` (indirect contradiction), `CG` (governance override), and `CP` (supersession claim) conflicts:

1. **Detection → Registry entry** — Conflict logged with `blocking: true`
2. **Workflow halt** — Step 5 (Conflict Mapping) halts until entry is recorded
3. **DEC creation required** — Step 6 (DEC Creation) must produce a DEC entry
4. **Human approval required** — HO-3 approval required for DEC entry
5. **Resolution → Registry update** — DEC entry reference added to registry
6. **Re-verification** — All blocking conflicts must be resolved before Step 9 (Reconciliation)

**No activation with unresolved blocking conflicts.**

---

## Schema Change Protocol

This registry schema is governed. Schema changes require:
1. DEC entry authorizing the schema change
2. All existing entries updated to new schema
3. Human Operator approval
4. Governance log entry documenting the change

---

## Related Governance Files

| File | Role |
|---|---|
| [HIGH Risk Overlay Escalation Standard](./HIGH_RISK_OVERLAY_ESCALATION_STANDARD.md) | Definitions and rules |
| [HIGH Risk Decision Workflow](./HIGH_RISK_DECISION_WORKFLOW.md) | Step-by-step process |
| [Overlay Decision Log](./governance/OVERLAY_DECISION_LOG.md) | DEC entries for all overlay decisions |

---

*Canonical — GitHub is the source of truth. Append-only registry — conflicts documented, never deleted.*