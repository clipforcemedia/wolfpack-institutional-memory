---
title: "Doctrine Overlay Reconciliation Standard"
document_type: "governance"
status: "active"
version: "1.0"
created: "2026-05-24"
updated: "2026-05-24"
source_type: "internal"
provenance: "wolfpack-institutional-memory"
tags:
  - "governance"
  - "doctrine"
  - "overlay"
  - "reconciliation"
  - "batch-002"
related_ids:
  - "governance/OVERLAY_REVIEW_QUEUE.md"
  - "governance/OVERLAY_DECISION_LOG.md"
  - "archive/SOURCE_ARCHIVE_GOVERNANCE.md"
append_only: true
---

# Doctrine Overlay Reconciliation Standard

**Version:** 1.0
**Effective:** 2026-05-24
**Status:** Active
**Purpose:** Define the formal process for detecting, classifying, and resolving doctrine overlay between incoming source documents and existing canonical memory.

---

## 1. What Constitutes Doctrine Overlay

Doctrine overlay occurs when an incoming source document (PDF, spec, or external document) contains claims, rules, definitions, or architecture positions that intersect with existing canonical memory.

Overlay is classified into five types:

| Type | Definition | Example |
|---|---|---|
| **Contradiction** | New doc asserts the inverse of an existing canonical claim | Existing canon says OpenClaw is control plane; new doc says it is not |
| **Duplication** | New doc covers the same subject as existing canon with identical content | Two docs both defining the same memory taxonomy |
| **Expansion** | Existing canon is a strict subset of new doctrine | Existing canon has 3 memory categories; new doc has 9 |
| **Contradiction-partial** | New doc contradicts only part of existing canon | New doc aligns with canon on 7 of 10 points but contradicts 3 |
| **Gap-fill** | New doc addresses an area of doctrine that has no existing coverage | New doc covers AI support runtime — no existing canon on this |

**Overlap threshold:** Any shared subject matter, defined term, or architectural position between a source document and any existing canonical file constitutes overlay.

---

## 2. Overlay Risk Levels

| Level | Definition | Required Action |
|---|---|---|
| **NONE** | New doc covers entirely new territory; no intersection with existing canon | Auto-approve — proceed directly to extraction |
| **LOW** | Minor terminological overlap; no semantic conflict; shared vocabulary but no contradictory claims | Auto-approve — document cross-links and proceed |
| **MEDIUM** | Substantial overlap or partial contradiction; could affect existing canonical conclusions | Wolfpack review required; explicit approval gate before extraction |
| **HIGH** | Direct contradiction of existing canon OR would overwrite active canonical structure | DEC entry required; extraction blocked until DEC approved |

---

## 3. Additive vs. Conflicting Doctrine

### Additive Doctrine

A document is **additive** when:
- It extends existing canon without changing existing claims
- New doctrine supplements rather than replaces
- Existing canon remains true as-is

**Additive response:** Create a new canonical file or add to existing canon as a supplement. No overlay conflict.

### Conflicting Doctrine

A document is **conflicting** when:
- It asserts a claim that contradicts an existing canonical statement
- It would change the meaning of existing doctrine if merged
- It redefines a term already defined in canon

**Conflicting response:** Do not merge silently. Escalate to overlay review queue. Block canonical activation until conflict resolved.

---

## 4. Canonical Precedence Hierarchy

When doctrine conflicts occur, the following precedence hierarchy determines which doctrine takes priority:

| Priority | Source | Rationale |
|---|---|---|
| **1** | Active canonical memory (GitHub `canon/`, `agents/`, `decisions/`) | Represents the current authorized operational truth |
| **2** | Approved DEC entries | Represent formal decisions made through proper governance |
| **3** | Checksum-verified source documents | Authenticated archival sources with verified integrity |
| **4** | Extracted markdown from verified sources | Processed doctrine with provenance chain |
| **5** | Unreviewed uploads | Source documents not yet through overlay check |
| **6** | Chat/session context | Transient; not institutional memory |

**Rule:** Higher-priority source always governs in conflict. Lower-priority source cannot override higher-priority doctrine without explicit approval through the reconciliation workflow.

---

## 5. Reconciliation Workflow

```
Step R1: Document Identified
  └── Source document ingested into archive
  └── Registered in SOURCE_DOCUMENT_REGISTRY.md with overlay_risk: TBD

Step R2: Overlay Scan
  └── For each new source document, scan existing canon for:
      - Shared defined terms
      - Overlapping subject categories
      - Contradictory architectural positions
  └── Identify overlay type (contradiction, duplication, expansion, gap-fill)

Step R3: Risk Assessment
  └── Classify overlay risk: NONE / LOW / MEDIUM / HIGH
  └── Record in OVERLAY_REVIEW_QUEUE.md

Step R4a (NONE/LOW): Auto-approve
  └── Proceed directly to canonical extraction
  └── Document cross-links in output markdown

Step R4b (MEDIUM): Wolfpack Review
  └── Submit to Wolfpack review gate
  └── Obtain explicit approval from 4+ roles
  └── Record approval in OVERLAY_DECISION_LOG.md

Step R4c (HIGH): DEC Entry Required
  └── Create DEC-00x entry before any extraction
  └── Block canonical activation until DEC approved
  └── DEC entry must specify: which doctrine wins, rationale, affected files

Step R5: Canonical Extraction
  └── Extract content per extraction workflow
  └── Include "Unresolved Conflicts" section documenting any residual ambiguity
  └── Cross-link to relevant canon and DEC entries

Step R6: Validation
  └── Run wolfpack_review validation pass
  └── Verify no canonical contradiction remains
  └── Update OVERLAY_DECISION_LOG.md with resolution
```

---

## 6. Prohibited Silent Overwrite Behavior

The following behaviors are **categorically prohibited:**

| Prohibited | Rationale |
|---|---|
| Extracting new markdown that overwrites existing canonical files | Violates immutability of active canon |
| Merging source doctrine into existing canon without overlay check | Risks silent contradiction |
| Treating a new document as canonical before overlay review | Violates governance |
| Modifying existing canon to accommodate incoming doctrine without DEC | Silent overwrite |
| Activating a canonical file that contradicts a higher-priority source | Violates precedence hierarchy |
| Removing or deprecating canon without formal DEC entry | Autonomous deletion prohibited |
| Overwriting a DEC-00x decision with newer source doctrine | DEC entries are authoritative once approved |

---

## 7. Conflict Escalation Rules

| Conflict Type | Escalation Path |
|---|---|
| Partial contradiction (MEDIUM) | Wolfpack review; if unresolved → DEC entry |
| Full contradiction (HIGH) | DEC entry required; no extraction until approved |
| Duplicate doctrine (MEDIUM/HIGH) | Wolfpack review; choose authoritative version; mark other as `superseded` |
| Expansive overlay (LOW/MEDIUM) | Auto-approve as supplement; document relationship in both files |
| Unresolvable ambiguity | DEC entry; extract both interpretations; document as "Unresolved" |

---

## 8. DEC Entry Requirements

For HIGH overlay or unresolved MEDIUM overlay:

| Requirement | Description |
|---|---|
| **Overlay ID** | Unique ID: `OVL-<YYYYMMDD>-NNN` |
| **Conflicting sources** | List all documents in conflict |
| **Precedence decision** | Explicit statement of which doctrine wins |
| **Rationale** | Why this decision was made |
| **Affected files** | All canonical files modified as result |
| **Rollback path** | Git commit hash of pre-conflict state |
| **Approval** | Minimum Deployment Governor sign-off + Human Operator acknowledgment |
| **Documentation** | Full context logged in `decisions/` directory |

---

## 9. Supersession Rules

| Scenario | Action |
|---|---|
| New source supersedes existing canonical file | Mark existing `status: superseded`, set `superseded_by: <new_doc>`, preserve in repo |
| New DEC entry supersedes earlier DEC | Mark earlier `superseded: true`, preserve full history |
| New canonical extraction supersedes existing stub | Preserve original stub; append as new version; update `related_ids` |
| New version of archived PDF supersedes old | Mark old `status: superseded`, preserve in archive, register new version |

---

## 10. Overlay Validation Checklist

Before any canonical markdown is marked `active`, verify:

- [ ] Overlay risk level assessed and recorded in OVERLAY_REVIEW_QUEUE.md
- [ ] NONE/LOW: Auto-approved and documented
- [ ] MEDIUM: Wolfpack review approval recorded in OVERLAY_DECISION_LOG.md
- [ ] HIGH: DEC entry approved and logged
- [ ] No silent overwrites of existing canonical files
- [ ] Precedence hierarchy respected
- [ ] "Unresolved Conflicts" section populated if any residual ambiguity
- [ ] Cross-links to affected canon files added
- [ ] Registry entry updated to `active`
- [ ] Provenance chain documented (source → archive → checksum → extraction → canonical)

---

## 11. Governance Approval Requirements

| Overlay Risk | Approval Required |
|---|---|
| NONE | None — auto-approve |
| LOW | None — auto-approve with documentation |
| MEDIUM | Wolfpack review (4+ roles) |
| HIGH | DEC entry + Deployment Governor + Human Operator |

---

## 12. Rollback / Reversal Handling

| Situation | Action |
|---|---|
| Overlay approved in error | Revert to pre-overlay canonical state; log incident in INCIDENT_LOG.md; mark DEC entry `superseded: true` |
| Canonical file activated with unresolved contradiction | Revert to previous commit; restore original; mark canonical file `status: archived` |
| Source document checksum mismatch post-approval | Treat as governance incident; halt all operations; investigate before resuming |
| DEC entry reversed | Preserve original DEC in full; create new DEC entry superseding it; never delete historical DEC |

---

*Governance maintained in `governance/DOCTRINE_OVERLAY_RECONCILIATION_STANDARD.md`*