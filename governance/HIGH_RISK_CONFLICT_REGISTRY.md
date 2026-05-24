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

---

## OVL-20260524-003 — Conflict Entries

### CFG-20260524-001 — Helm as Required Infrastructure Layer

| Field | Value |
|---|---|
| **conflict_id** | `CFG-20260524-001` |
| **overlay_id** | `OVL-20260524-003` |
| **affected_canon** | `canon/SYSTEM_ARCHITECTURE.md` |
| **conflict_type** | `CD` (Direct Contradiction) |
| **description** | OS Doc Pack §02 lists "Helm → operational infrastructure" as a core layer. Helm is a Kubernetes package manager. The existing SYSTEM_ARCHITECTURE.md makes no mention of Kubernetes, Helm, or container orchestration infrastructure. Helm is not present in any canonical document. |
| **canonical_claim** | SYSTEM_ARCHITECTURE.md does not mention Helm, Kubernetes, or container orchestration as required infrastructure |
| **incoming_claim** | "Core layers: ... Helm → operational infrastructure" (OS Doc Pack §02) |
| **precedence_ruling** | Active canonical memory (level 1) prevails. OS Doc Pack (level 3) cannot add required infrastructure without DEC entry + human approval. Helm is not optional in the OS Doc Pack architecture. |
| **blocking** | true |
| **resolution_state** | `pending` |
| **resolution** | null |
| **rollback_reference** | `031fb87` (pre-overlay state) |
| **reviewer_approvals** | { opportunity_radar: pending, red_team: pending, deployment_governor: pending, memory_keeper: pending, eterna: pending } |
| **created** | 2026-05-24 |
| **updated** | 2026-05-24 |

### CFG-20260524-002 — Wolfpack as Architectural Layer

| Field | Value |
|---|---|
| **conflict_id** | `CFG-20260524-002` |
| **overlay_id** | `OVL-20260524-003` |
| **affected_canon** | `canon/SYSTEM_ARCHITECTURE.md`, `canon/WOLFPACK_CANON.md` |
| **conflict_type** | `CT` + `CS` (Terminology Collision + Scope Overlap) |
| **description** | OS Doc Pack §02 lists "Wolfpack → governance/risk" as a core system layer. Existing canon defines Wolfpack as a governance review process (SYSTEM_ARCHITECTURE.md: "Wolfpack review gate (6 roles)"). The OS Doc Pack implies Wolfpack is a deployable technical component, which differs from the canonical definition. |
| **canonical_claim** | "Governance: Wolfpack review gate (6 roles), Deployment Governor approval" — Wolfpack is a process, not a system component |
| **incoming_claim** | "Core layers: ... Wolfpack → governance/risk" — Wolfpack is a layer in the architecture |
| **precedence_ruling** | Canon defines Wolfpack as review process. OS Doc Pack treats Wolfpack as system layer. Requires DEC entry to clarify relationship or reject supersession claim. |
| **blocking** | true |
| **resolution_state** | `pending` |
| **resolution** | null |
| **rollback_reference** | `031fb87` |
| **reviewer_approvals** | { opportunity_radar: pending, red_team: pending, deployment_governor: pending, memory_keeper: pending, eterna: pending } |
| **created** | 2026-05-24 |
| **updated** | 2026-05-24 |

### CFG-20260524-003 — 6 New Roles Without Canon Definitions

| Field | Value |
|---|---|
| **conflict_id** | `CFG-20260524-003` |
| **overlay_id** | `OVL-20260524-003` |
| **affected_canon** | `agents/DEPLOYMENT_GOVERNOR.md`, `agents/ETERNA_COMMAND.md`, `agents/MEMORY_KEEPER.md`, `agents/OPPORTUNITY_RADAR.md`, `agents/RED_TEAM.md` |
| **conflict_type** | `CS` (Scope Overlap) |
| **description** | OS Doc Pack §01 lists 11 "Core roles" (Eterna, Operator, Architect, Critic, Economist, Compliance Officer, Memory Keeper, Opportunity Analyst, Deployment Governor, UX Steward, Evolution Sentinel). Canon defines only 5 roles (Eterna, Red Team, Deployment Governor, Memory Keeper, Opportunity Radar). Six OS Doc Pack roles (Operator, Architect, Critic, Economist, Compliance Officer, UX Steward, Evolution Sentinel) have no canonical definitions. |
| **canonical_claim** | Canon defines exactly 5 roles; no canon file exists for Operator, Architect, Critic, Economist, Compliance Officer, UX Steward, or Evolution Sentinel |
| **incoming_claim** | "Core roles: Eterna, Operator, Architect, Critic, Economist, Compliance Officer, Memory Keeper, Opportunity Analyst, Deployment Governor, UX Steward, Evolution Sentinel" — all listed as authoritative Wolfpack roles |
| **precedence_ruling** | Canon role definitions (level 1) govern. New roles from OS Doc Pack (level 3) cannot become canonical without DEC entry + role definition files. |
| **blocking** | true |
| **resolution_state** | `pending` |
| **resolution** | null |
| **rollback_reference** | `031fb87` |
| **reviewer_approvals** | { opportunity_radar: pending, red_team: pending, deployment_governor: pending, memory_keeper: pending, eterna: pending } |
| **created** | 2026-05-24 |
| **updated** | 2026-05-24 |

### CFG-20260524-004 — Supabase as Approved Infrastructure

| Field | Value |
|---|---|
| **conflict_id** | `CFG-20260524-004` |
| **overlay_id** | `OVL-20260524-003` |
| **affected_canon** | `canon/SYSTEM_ARCHITECTURE.md` |
| **conflict_type** | `CS` (Scope Overlap) |
| **description** | OS Doc Pack §02 lists "Supabase" as approved v0.1 infrastructure alongside GitHub, OpenClaw, Render. SYSTEM_ARCHITECTURE.md defines execution workers as OpenClaw, Render, Twilio, OpenAI Realtime API. Supabase (a Firebase alternative) is not mentioned in any canonical document. |
| **canonical_claim** | SYSTEM_ARCHITECTURE.md does not list Supabase as infrastructure |
| **incoming_claim** | "Approved v0.1 infrastructure: ... Supabase" — listed as approved |
| **precedence_ruling** | Canon (level 1) does not include Supabase. OS Doc Pack (level 3) cannot approve Supabase as infrastructure without DEC entry. |
| **blocking** | true |
| **resolution_state** | `pending` |
| **resolution** | null |
| **rollback_reference** | `031fb87` |
| **reviewer_approvals** | { opportunity_radar: pending, red_team: pending, deployment_governor: pending, memory_keeper: pending, eterna: pending } |
| **created** | 2026-05-24 |
| **updated** | 2026-05-24 |

### CFG-20260524-005 — Opportunity Analyst vs. Opportunity Radar

| Field | Value |
|---|---|
| **conflict_id** | `CFG-20260524-005` |
| **overlay_id** | `OVL-20260524-003` |
| **affected_canon** | `agents/OPPORTUNITY_RADAR.md` |
| **conflict_type** | `CT` (Terminology Collision) |
| **description** | OS Doc Pack §01 and §06 use "Opportunity Analyst" as the role name. Canon uses "Opportunity Radar". Both refer to the same role concept (identifying profitable operational systems and recurring-revenue opportunities). |
| **canonical_claim** | agents/OPPORTUNITY_RADAR.md defines "Opportunity Radar — Market and Business Opportunity Detection" |
| **incoming_claim** | "Opportunity Analyst" in OS Doc Pack §01 core roles and §06 Opportunity Radar Spec |
| **precedence_ruling** | Terminology normalization recommended. Cross-reference document to map "Opportunity Analyst" to canonical "Opportunity Radar". No DEC entry required — CT classification. |
| **blocking** | false |
| **resolution_state** | `pending` |
| **resolution** | null |
| **rollback_reference** | null |
| **reviewer_approvals** | { opportunity_radar: pending, red_team: pending, deployment_governor: pending, memory_keeper: pending, eterna: pending } |
| **created** | 2026-05-24 |
| **updated** | 2026-05-24 |

### CFG-20260524-006 — Wolfpack Red Team vs. Red Team

| Field | Value |
|---|---|
| **conflict_id** | `CFG-20260524-006` |
| **overlay_id** | `OVL-20260524-003` |
| **affected_canon** | `agents/RED_TEAM.md` |
| **conflict_type** | `CT` (Terminology Collision) |
| **description** | OS Doc Pack §07 lists "Wolfpack Red Team" as a Core GPT. Canon uses "Red Team" as the role name. "Wolfpack Red Team" is likely a prompt-specific label. Both refer to the same adversarial review role. |
| **canonical_claim** | agents/RED_TEAM.md defines "Red Team — Adversarial Review Agent" |
| **incoming_claim** | "Wolfpack Red Team" in OS Doc Pack §07 GPT Role Prompts |
| **precedence_ruling** | Terminology normalization recommended. Cross-reference to document both names as the same role. No DEC entry required — CT classification. |
| **blocking** | false |
| **resolution_state** | `pending` |
| **resolution** | null |
| **rollback_reference** | null |
| **reviewer_approvals** | { opportunity_radar: pending, red_team: pending, deployment_governor: pending, memory_keeper: pending, eterna: pending } |
| **created** | 2026-05-24 |
| **updated** | 2026-05-24 |

### CFG-20260524-007 — Red Team Absent from Core Roles

| Field | Value |
|---|---|
| **conflict_id** | `CFG-20260524-007` |
| **overlay_id** | `OVL-20260524-003` |
| **affected_canon** | `agents/RED_TEAM.md` |
| **conflict_type** | `CT` (Terminology Collision) |
| **description** | OS Doc Pack §01 "Core roles" list does not include Red Team. Instead, "Wolfpack Red Team" appears in §07 GPT prompts. This could mean: (1) Red Team was intentionally omitted from Core roles, or (2) "Wolfpack Red Team" is the preferred name going forward, or (3) this is an oversight. |
| **canonical_claim** | agents/RED_TEAM.md defines Red Team as a canonical Wolfpack role |
| **incoming_claim** | Red Team not listed as a Core role in OS Doc Pack §01; "Wolfpack Red Team" used in §07 |
| **precedence_ruling** | Canon defines Red Team as an authoritative role. OS Doc Pack's exclusion or renaming requires clarification. Await human oversight decision. |
| **blocking** | false |
| **resolution_state** | `pending` |
| **resolution** | null |
| **rollback_reference** | null |
| **reviewer_approvals** | { opportunity_radar: pending, red_team: pending, deployment_governor: pending, memory_keeper: pending, eterna: pending } |
| **created** | 2026-05-24 |
| **updated** | 2026-05-24 |

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