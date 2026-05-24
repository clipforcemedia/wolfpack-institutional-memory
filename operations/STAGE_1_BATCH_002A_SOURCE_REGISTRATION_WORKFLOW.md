---
title: "Stage 1 Batch 002A — Source Registration Workflow"
document_type: "operations"
status: "active"
version: "1.0"
created: "2026-05-24"
updated: "2026-05-24"
source_type: "internal"
provenance: "wolfpack-institutional-memory"
tags:
  - "governance"
  - "workflow"
  - "batch-002"
  - "batch-002a"
  - "archive"
related_ids:
  - "archive/SOURCE_ARCHIVE_GOVERNANCE.md"
  - "archive/SOURCE_DOCUMENT_REGISTRY.md"
  - "operations/STAGE_1_BATCH_002A_INGESTION_REPORT.md"
append_only: true
---

# Stage 1 Batch 002A — Source Registration Workflow

**Version:** 1.0
**Created:** 2026-05-24
**Batch:** STAGE_1_BATCH_002A
**Status:** Active
**Governance:** `archive/SOURCE_ARCHIVE_GOVERNANCE.md`

---

## 1. Scope and Purpose

This workflow governs the upload, checksum, and registry lifecycle for Batch 002A source documents. It applies to all PDFs listed in `archive/SOURCE_DOCUMENT_REGISTRY.md` with `batch: STAGE_1_BATCH_002A`.

**Batch 002A documents:**
- `SRC-CANON-001` — `01_WOLFPACK_CANONICAL_REPOSITORY_SPEC_v1.pdf` → `canonical/`
- `SRC-MEMORY-001` — `WOLFPACK_MEMORY_ARCHITECTURE_v1.pdf` → `memory/`

**Governance principles:**
- No source overwrite — archived documents are immutable
- No checksum bypass — SHA-256 required before any status transition
- No canonical activation before overlay review
- No source deletion — append-only forever
- Append-only registry updates only

---

## 2. Approved Archive Locations

| Category | Archive Directory | Batch 002A Documents |
|---|---|---|
| `canonical` | `archive/source-documents/canonical/` | `01_WOLFPACK_CANONICAL_REPOSITORY_SPEC_v1.pdf` |
| `memory` | `archive/source-documents/memory/` | `WOLFPACK_MEMORY_ARCHITECTURE_v1.pdf` |

**Upload destination formula:**
```
archive/source-documents/<category>/<original_filename>
```

**Examples:**
```
archive/source-documents/canonical/01_WOLFPACK_CANONICAL_REPOSITORY_SPEC_v1.pdf
archive/source-documents/memory/WOLFPACK_MEMORY_ARCHITECTURE_v1.pdf
```

---

## 3. Upload Procedure

**Pre-upload checklist:**
- [ ] Source document verified present on upload system
- [ ] Target archive directory exists
- [ ] Registry entry exists in `SOURCE_DOCUMENT_REGISTRY.md` with `status: pending_upload`
- [ ] No document with same `source_id` already archived (no overwrite)

**Upload steps:**

```
Step U1: Confirm source file
  └── Verify file exists locally
  └── Record file size in bytes
  └── Record original filename exactly (preserve version suffix)

Step U2: Transfer to archive location
  └── Use approved transfer mechanism (git-LFS, cloud storage upload, or human-assisted)
  └── Target path: archive/source-documents/<category>/<original_filename>
  └── Preserve exact filename — do not rename during upload

Step U3: Verify upload integrity
  └── Confirm file present at destination
  └── Confirm file size matches source ≥ 1 byte
  └── Confirm filename matches original exactly

Step U4: Update registry entry
  └── Set status: archived
  └── Record ingest_date (ISO-8601 UTC)
  └── Record archive_path
  └── Record batch: STAGE_1_BATCH_002A
  └── Append new entry block (do not modify existing fields)
```

---

## 4. Checksum Generation Procedure

**Tool:** `sha256sum` (or equivalent SHA-256 utility)

**Command:**
```bash
sha256sum /path/to/archive/source-documents/<category>/<filename>.pdf
```

**Output format:**
```
<hex_digest>  <filename>
```

**Example:**
```
sha256sum archive/source-documents/canonical/01_WOLFPACK_CANONICAL_REPOSITORY_SPEC_v1.pdf
# Output: a3f7c2...  01_WOLFPACK_CANONICAL_REPOSITORY_SPEC_v1.pdf
```

**Registry storage format:** `sha256:<hex_digest>` (prepend `sha256:` prefix)

**Checksum recording:**
```yaml
checksum: "sha256:a3f7c2d9e1b4..."
```

---

## 5. Checksum Validation Procedure

**When to validate:**
- Before any canonical extraction workflow begins
- After any archive access or file retrieval
- On demand (manual verification step)
- After any suspected archive access incident

**Validation steps:**

```
Step CV1: Retrieve archived file
  └── Locate file at registered archive_path

Step CV2: Compute live checksum
  └── Run: sha256sum <archive_path>
  └── Capture hex digest

Step CV3: Compare to registry
  └── Read stored checksum from SOURCE_DOCUMENT_REGISTRY.md
  └── Strip sha256: prefix from both
  └── Compare hex digests bit-for-bit

Step CV4: Act on result
  └── MATCH → Record validation_date; proceed
  └── MISMATCH → Trigger governance incident; do not proceed
      └── Log to INCIDENT_LOG.md
      └── Set registry status: checksum_failed
      └── Notify via alert channel
      └── HALT canonical extraction until resolved
```

---

## 6. Registry Update Procedure

**Principle:** Append-only. Existing entries are never modified — new status information is appended as a new entry block.

**Status transition recording:**

For each status change, append a new block to the entry:

```yaml
## Status Log — SRC-CANON-001

### Transition: pending_upload → archived
**Date:** 2026-05-24T00:00:00Z
**Action:** Uploaded to canonical/
**Checksum:** sha256:<hex>
**Verified_by:** <operator>

### Transition: archived → checksum_verified
**Date:** 2026-05-24T00:00:00Z
**Action:** SHA-256 verified
**Checksum:** sha256:<hex>
**Verified_by:** <operator>
```

**Fields updated on status transition:**
- `status` — current operational status
- `checksum` — SHA-256 digest (set when transitioning to `archived` or `checksum_verified`)
- `ingest_date` — set once on `archived`
- `validation_date` — set on `checksum_verified`

---

## 7. Source Status Lifecycle

Each source document passes through the following statuses **in order:**

```
pending_upload
    ↓ upload
archived
    ↓ checksum_computed
checksum_verified
    ↓ overlay_check
overlay_review  [only if overlay_risk MEDIUM or HIGH]
    ↓ [if NONE/LOW → auto-approve] [if MEDIUM/HIGH → DEC entry required]
extraction_pending
    ↓ pdf_extraction
canonicalized
    ↓ wolfpack_review_validation
active  ← canonical markdown is now operational
    ↓ [if superseded by newer version]
superseded
```

### Status Definitions

| Status | Definition |
|---|---|
| `pending_upload` | Document registered; not yet in archive |
| `archived` | Document uploaded to correct archive path; not yet checksum-verified |
| `checksum_verified` | SHA-256 computed and recorded; matches registry |
| `overlay_review` | Awaiting overlay check against existing canon |
| `extraction_pending` | Checksum verified; cleared for canonical extraction |
| `canonicalized` | Markdown conversion complete; not yet validated |
| `active` | Canonical markdown validated and operational |
| `superseded` | Replaced by newer version; archive preserved; markdown marked `superseded: true` |

### Batch 002A Status Transitions

| source_id | Current Status | Next Required Status | Gate |
|---|---|---|---|
| `SRC-CANON-001` | `pending_upload` | `archived` | Upload to canonical/ |
| `SRC-MEMORY-001` | `pending_upload` | `archived` | Upload to memory/ |

---

## 8. Ingestion Batch Tracking

**Batch tag:** `STAGE_1_BATCH_002A`

**Tracking mechanism:**
1. Each document's `batch` field in the registry entry is set at registration
2. A batch summary is maintained at the top of `SOURCE_DOCUMENT_REGISTRY.md`
3. Batch completion is logged in `MILESTONE_LOG.md` when all docs reach `active`

**Batch 002A completion criteria:**
- All 2 documents: `status: active`
- All 2 canonical markdown files: validated against Section 10 checklist
- Milestone 010 updated with completion entry
- `status/NEXT_ACTIONS.md` updated with Batch 002A complete

**Batch 002A tracking table:**

| source_id | Status | Checksum | Archive Path | Canonical Target |
|---|---|---|---|---|
| `SRC-CANON-001` | pending_upload | pending_upload | canonical/01_WOLFPACK_CANONICAL_REPOSITORY_SPEC_v1.pdf | canon/CANONICAL_REPOSITORY_SPEC.md |
| `SRC-MEMORY-001` | pending_upload | pending_upload | memory/WOLFPACK_MEMORY_ARCHITECTURE_v1.pdf | canon/MEMORY_ARCHITECTURE.md |

---

## 9. Overlay Verification Gate

**Trigger:** When a document reaches `extraction_pending`

**Purpose:** Verify the source document's doctrine does not contradict or duplicate existing canonical memory before conversion.

**Overlay check steps:**

```
Step OV1: Identify overlay risk
  └── Read overlay_risk from registry entry
  └── NONE/LOW → Auto-approve; skip to Step OV5
  └── MEDIUM → Proceed to wolfpack_review
  └── HIGH → Escalate to DEC entry

Step OV2: Content review
  └── Access archived PDF at registered archive_path
  └── Identify doctrine claims (architectural, governance, operational)
  └── Cross-reference against existing canon files

Step OV3: Conflict detection
  └── Document any:
      - Contradictions (same claim, different truth value)
      - Duplications (same subject, identical content)
      - Expansions (existing canon is subset of new)
      - Gaps (new doc fills known gap)

Step OV4: Resolution
  └── NONE/LOW conflict → Proceed to extraction
  └── MEDIUM conflict → wolfpack_review approval required
  └── HIGH conflict → DEC entry required before extraction
      └── Document conflict in DEC-00x entry
      └── Do not proceed without DEC approval

Step OV5: Record result
  └── Log overlay check result in registry entry
  └── If conflicts found → document in canonical markdown's "Unresolved Conflicts" section
  └── Set status: extraction_pending
```

---

## 10. Canonical Extraction Gate

**Trigger:** When a document passes the overlay verification gate

**Gate criteria before markdown creation:**

- [ ] `status: extraction_pending` in registry
- [ ] `checksum: sha256:<hex>` recorded and verified
- [ ] Overlay check complete (or auto-approved for LOW/NONE)
- [ ] No unresolved HIGH overlay risk
- [ ] Target canonical markdown path defined and verified unique
- [ ] No existing `active` canonical markdown at target path

**Extraction output requirements:**

Each canonical markdown file must include:
- [ ] YAML front matter with all provenance fields
- [ ] `source_pdf` pointing to `archive://wolfpack/batch_002/<category>/<filename>.pdf`
- [ ] `batch: STAGE_1_BATCH_002A`
- [ ] `status: active` (set only after wolfpack_review validation)
- [ ] All doctrine sections extracted, not reinterpreted
- [ ] "Unresolved Conflicts" section for any areas of ambiguity
- [ ] References section with source archive path

---

## 11. Rollback / Recovery Procedure

| Incident | Response |
|---|---|
| **Checksum mismatch** | HALT all workflows; log INCIDENT; investigate; do not delete/move archive file; resolve before continuing |
| **Wrong file uploaded** | Re-upload correct file to same path; recompute checksum; update registry entry; log as incident |
| **Duplicate upload** | Do not overwrite; upload to a `_v<timestamp>` suffixed path; create new registry entry; flag for review |
| **Canonical markdown created in error** | Do not delete; mark `status: superseded`; create new entry for correct version; log in INCIDENT_LOG |
| **Registry entry incorrect** | Append correction as new entry block; do not modify existing entry; document the correction |
| **Source document corrupted** | Do not attempt repair on archived file; archive is immutable; create incident entry; treat as data loss event |

**Recovery command reference:**

```bash
# Verify checksum of archived file
sha256sum archive/source-documents/<category>/<filename>.pdf

# Check registry status
grep "SRC-CANON-001" archive/SOURCE_DOCUMENT_REGISTRY.md
```

---

## 12. Source Immutability Enforcement

**Rule:** No person or system may modify, overwrite, or delete an archived source document after ingest.

**Immutability guarantees:**
- Archive path is append-only (enforced by policy, not filesystem — GitHub is the control plane)
- Modifications to archived files are prevented by this governance document
- Any modification attempt is a governance violation → `INCIDENT_LOG.md`
- Registry entries are never modified — only appended

**If source needs correction:**
1. Do not modify the archived file
2. Upload a corrected version as a new file with `_v2` suffix
3. Create a new registry entry with new `source_id`
4. Mark the original entry `status: superseded`
5. Document the correction rationale in the new registry entry

---

## 13. Validation Checklist

Before any document in Batch 002A is marked `active`, all of the following must pass:

- [ ] Upload to correct archive path verified (file present, size > 0)
- [ ] SHA-256 checksum computed and recorded in registry
- [ ] Checksum validation passed (live vs. registry match)
- [ ] Registry entry updated to `status: archived`
- [ ] Overlay check completed (or auto-approved for LOW/NONE)
- [ ] No unresolved HIGH overlay risk
- [ ] Canonical markdown created at target path
- [ ] YAML front matter valid (title, provenance, source_pdf, batch, status, append_only)
- [ ] Cross-links from existing canon verified
- [ ] No duplicate canon identifiers detected
- [ ] "Unresolved Conflicts" section populated if any conflicts found
- [ ] Wolfpack_review validation passed on canonical markdown
- [ ] Registry entry updated to `status: active`
- [ ] Milestone log updated

---

## 14. Next Immediate Action

**Upload Batch 002A source PDFs and compute SHA-256 checksums:**

```
1. Upload 01_WOLFPACK_CANONICAL_REPOSITORY_SPEC_v1.pdf
   → archive/source-documents/canonical/

2. Upload WOLFPACK_MEMORY_ARCHITECTURE_v1.pdf
   → archive/source-documents/memory/

3. Compute SHA-256 for each file:
   sha256sum archive/source-documents/canonical/01_WOLFPACK_CANONICAL_REPOSITORY_SPEC_v1.pdf
   sha256sum archive/source-documents/memory/WOLFPACK_MEMORY_ARCHITECTURE_v1.pdf

4. Update SOURCE_DOCUMENT_REGISTRY.md entries:
   - Set status: archived
   - Record checksum: sha256:<hex>
   - Record ingest_date

5. Verify checksum:
   sha256sum <archived_file> → confirm match
```

---

*Workflow maintained in `operations/STAGE_1_BATCH_002A_SOURCE_REGISTRATION_WORKFLOW.md`*