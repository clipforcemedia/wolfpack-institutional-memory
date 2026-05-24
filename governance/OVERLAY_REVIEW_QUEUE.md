---
title: "Overlay Review Queue"
document_type: "overlay-registry"
status: "active"
version: "1.0"
created: "2026-05-24"
updated: "2026-05-24"
source_type: "internal"
provenance: "wolfpack-institutional-memory"
tags:
  - "governance"
  - "overlay"
  - "review-queue"
  - "batch-002"
related_ids:
  - "governance/DOCTRINE_OVERLAY_RECONCILIATION_STANDARD.md"
  - "governance/OVERLAY_DECISION_LOG.md"
append_only: true
---

# Overlay Review Queue

**Version:** 1.0
**Effective:** 2026-05-24
**Purpose:** Track all source documents requiring overlay review before canonical activation.

> **Append-only queue.** Entries are added as documents are identified. Status transitions are appended as new entry blocks. Completed entries remain visible for audit trail.

---

## Queue Schema

Each queue entry contains:

| Field | Type | Description |
|---|---|---|
| `overlay_id` | string | `OVL-YYYYMMDD-NNN` — unique per entry |
| `source_doc` | string | Source document filename and archive path |
| `canonical_target` | string | Target canonical markdown path |
| `overlay_type` | enum | `contradiction`, `contradiction-partial`, `duplication`, `expansion`, `gap-fill` |
| `affected_canon` | list | Existing canonical files with overlap |
| `overlay_risk` | enum | `NONE`, `LOW`, `MEDIUM`, `HIGH` |
| `status` | enum | `queued`, `in_review`, `approved`, `rejected`, `superseded` |
| `reviewer` | string | Assigned reviewer or "Wolfpack" |
| `escalation_required` | boolean | True if DEC entry or Wolfpack review required |
| `created` | ISO-8601 | When entry was created |
| `updated` | ISO-8601 | Last status change |

---

## Active Queue Entries

### Batch 002 — Pending Overlay Review

| overlay_id | source_doc | canonical_target | overlay_type | overlay_risk | status | escalation_required |
|---|---|---|---|---|---|---|
| `OVL-20260524-001` | `Wolfpack_Strategic_Doctrine_Expansion_v1.pdf` | `canon/STRATEGIC_DOCTRINE_EXPANSION.md` | `expansion` | `MEDIUM` | `queued` | ⚠️ Yes — Wolfpack review |
| `OVL-20260524-002` | `WOLFPACK_AGENT_GOVERNANCE_v1.pdf` | `agents/AGENT_GOVERNANCE.md` | `contradiction-partial` | `MEDIUM` | `queued` | ⚠️ Yes — Wolfpack review |
| `OVL-20260524-003` | `Wolfpack_Operating_System_Doc_Pack_v1.pdf` | `canon/OS_DOCTRINE_OVERVIEW.md` | `contradiction` | `HIGH` | `queued` | ⚠️ Yes — DEC entry required |

---

### Overlay Review Status — Batch 002

| overlay_id | Risk | Current Status | Blocker |
|---|---|---|---|
| `OVL-20260524-001` | MEDIUM | queued | Requires Wolfpack review before extraction |
| `OVL-20260524-002` | MEDIUM | queued | Requires Wolfpack review before extraction |
| `OVL-20260524-003` | HIGH | queued | Requires DEC-00x entry before any extraction |

---

## Overlay Details

### OVL-20260524-001 — Strategic Doctrine Expansion

| Field | Value |
|---|---|
| **overlay_id** | `OVL-20260524-001` |
| **source_doc** | `Wolfpack_Strategic_Doctrine_Expansion_v1.pdf` |
| **canonical_target** | `canon/STRATEGIC_DOCTRINE_EXPANSION.md` |
| **overlay_type** | `expansion` |
| **affected_canon** | `canon/WOLFPACK_CANON.md` |
| **overlay_risk** | `MEDIUM` |
| **status** | `queued` |
| **reviewer** | Wolfpack |
| **escalation_required** | true |
| **created** | 2026-05-24 |
| **concern** | May extend `canon/WOLFPACK_CANON.md` — verify expansion vs. contradiction before merge |

---

### OVL-20260524-002 — Agent Governance

| Field | Value |
|---|---|
| **overlay_id** | `OVL-20260524-002` |
| **source_doc** | `WOLFPACK_AGENT_GOVERNANCE_v1.pdf` |
| **canonical_target** | `agents/AGENT_GOVERNANCE.md` |
| **overlay_type** | `contradiction-partial` |
| **affected_canon** | `agents/DEPLOYMENT_GOVERNOR.md`, `agents/ETERNA_COMMAND.md`, `agents/MEMORY_KEEPER.md`, `agents/OPPORTUNITY_RADAR.md`, `agents/RED_TEAM.md` |
| **overlay_risk** | `MEDIUM` |
| **status** | `queued` |
| **reviewer** | Wolfpack |
| **escalation_required** | true |
| **created** | 2026-05-24 |
| **concern** | May supplement or partially contradict existing agent role definitions — review against all 5 agent docs |

---

### OVL-20260524-003 — Operating System Doc Pack

| Field | Value |
|---|---|
| **overlay_id** | `OVL-20260524-003` |
| **source_doc** | `Wolfpack_Operating_System_Doc_Pack_v1.pdf` |
| **canonical_target** | `canon/OS_DOCTRINE_OVERVIEW.md` |
| **overlay_type** | `contradiction` |
| **affected_canon** | `canon/SYSTEM_ARCHITECTURE.md`, `canon/WOLFPACK_CANON.md` |
| **overlay_risk** | `HIGH` |
| **status** | `queued` |
| **reviewer** | Human Operator + DEC |
| **escalation_required** | true — DEC entry required |
| **created** | 2026-05-24 |
| **concern** | Broad architectural overview likely overlaps with SYSTEM_ARCHITECTURE.md and WOLFPACK_CANON.md — blocking extraction until DEC approved |

---

## Completed Overlay Reviews

*(None yet — Batch 002A docs (SRC-CANON-001, SRC-MEMORY-001) had NONE overlay risk and were auto-approved)*

---

*Queue maintained in `governance/OVERLAY_REVIEW_QUEUE.md` — append-only*