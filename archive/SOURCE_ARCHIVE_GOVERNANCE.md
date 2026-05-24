---
title: "Source Archive Governance"
document_type: "governance"
status: "active"
version: "1.0"
created: "2026-05-24"
updated: "2026-05-24"
source_type: "internal"
provenance: "wolfpack-institutional-memory"
tags:
  - "governance"
  - "archive"
  - "doctrine"
related_ids:
  - "archive/SOURCE_DOCUMENT_REGISTRY.md"
  - "operations/STAGE_1_BATCH_002_PDF_SOURCE_INVENTORY.md"
append_only: true
---

# Source Archive Governance

**Version:** 1.0
**Created:** 2026-05-24
**Status:** Active
**Location:** `archive/SOURCE_ARCHIVE_GOVERNANCE.md`
**Doctrine Basis:** STAGE_1_MEMORY_INGESTION_PLAN.md; DEC-001 Architecture Correction

---

## 1. Archival Purpose

The Wolfpack source archive (`archive/`) is the **single authoritative storage location** for all external source documents that inform canonical institutional memory. PDFs, vendor specs, and external documents enter the archive here before any conversion to markdown canon occurs.

**Core principle:** GitHub holds canonical markdown. The archive holds archival source material. They are separate layers with distinct governance.

---

## 2. Provenance Rules

| Rule | Description |
|---|---|
| **R-001** | Every archived document must be registered in `SOURCE_DOCUMENT_REGISTRY.md` before any markdown conversion begins |
| **R-002** | The archive stores the **original, unmodified source file** — never a normalized, cleaned, or reformatted version |
| **R-003** | Provenance metadata (source filename, original URL, ingest date, checksum) must be captured at ingest time and stored in the registry |
| **R-004** | Source documents from external vendors or third parties must include source attribution and any applicable license metadata |
| **R-005** | Provenance is immutable — once registered, provenance fields in the registry are **never modified**. Superseded entries are closed with a `superseded_by` reference, never overwritten |

---

## 3. Naming Standards

| Standard | Rule | Example |
|---|---|---|
| **Directory** | lowercase-hyphenated category name | `source-documents/memory/` |
| **Archive path** | `archive/source-documents/<category>/` | `archive/source-documents/memory/` |
| **PDF filename** | Original filename preserved exactly, including version suffix | `01_WOLFPACK_MEMORY_ARCHITECTURE_v1.pdf` |
| **Canonical markdown** | `canon/<NAME>.md` — matched to source but distinct path | `canon/MEMORY_ARCHITECTURE.md` |
| **Version suffix** | `_v1`, `_v2` etc. in source filename must be preserved in registry and archive path | `_v1.pdf` → `_v1` in path |

---

## 4. Checksum Policy

| Rule | Description |
|---|---|
| **C-001** | Every source document must have an SHA-256 checksum computed at ingest time and registered in `SOURCE_DOCUMENT_REGISTRY.md` |
| **C-002** | Checksum is computed on the **exact file as archived** — before any conversion or processing |
| **C-003** | Checksums are used to detect unauthorized modifications to archived source material |
| **C-004** | Any checksum mismatch on a registered document is a **governance incident** — flagged in `INCIDENT_LOG.md` |
| **C-005** | Command: `sha256sum <file>` — result stored in registry `checksum` field as `sha256:<hex>` |
| **C-006** | Checksum verification is performed at the start of any markdown conversion workflow |

---

## 5. Ingestion Rules

| Rule | Description |
|---|---|
| **I-001** | Only upload to archive via a documented wolfpack_review task or explicit human operator authorization |
| **I-002** | Each source document upload must be accompanied by a corresponding registry entry in `SOURCE_DOCUMENT_REGISTRY.md` |
| **I-003** | Source documents are grouped by category subdirectory — do not mix categories within a directory |
| **I-004** | After upload, verify the file is present and size > 0 before marking the registry entry `status: archived` |
| **I-005** | The ingestion batch ID (e.g., `STAGE_1_BATCH_002A`) is recorded in both the archive path metadata and the registry entry |
| **I-006** | No source document enters the archive without a defined canonical markdown target path (documented in the registry) |
| **I-007** | Batch tagging: all docs in a given ingestion batch share the same `batch` tag in the registry |

---

## 6. Overlay / Conflict Handling

| Rule | Description |
|---|---|
| **O-001** | Before any markdown conversion, run an **overlay check** against existing canon files — verify no doctrine conflicts or duplicate identifiers |
| **O-002** | If a source document overlaps with existing canon, create a `DEC-00x` decision entry before canonical merge — do not silently overwrite |
| **O-003** | Overlay risk levels: **NONE**, **LOW**, **MEDIUM**, **HIGH** — logged per document in the registry |
| **O-004** | HIGH risk documents are deferred to a separate batch pending DEC entry approval |
| **O-005** | MEDIUM risk documents require explicit wolfpack_review approval before canonical merge |
| **O-006** | If two source documents claim the same canonical target, that is a conflict — escalate to DEC entry, do not choose arbitrarily |
| **O-007** | All overlay decisions are logged in `decisions/` with DEC-00x IDs — never made silently |

---

## 7. Retention Policy

| Rule | Description |
|---|---|
| **RT-001** | Archived source documents are **permanent** — no deletion under any circumstances |
| **RT-002** | If a source document is superseded by a newer version (e.g., `_v2.pdf` replaces `_v1.pdf`), the old version is marked `superseded: true` in the registry but **never deleted from the archive** |
| **RT-003** | The archive is append-only — documents are added, never removed or modified |
| **RT-004** | If a document is migrated to a different archive path, the original path entry is closed with a `migrated_to` reference, and a new entry is created at the destination |
| **RT-005** | The archive survives any single point of failure — cloud archive must be backed up independently of the GitHub repo |

---

## 8. Append-Only Rules

| Rule | Description |
|---|---|
| **A-001** | The archive directory is **strictly append-only** — no edits, no overwrites, no deletes |
| **A-002** | `SOURCE_DOCUMENT_REGISTRY.md` is append-only for new entries — existing entries are never modified |
| **A-003** | `SOURCE_ARCHIVE_GOVERNANCE.md` may be updated by DEC entry, but existing rules are never weakened — new rules may only restrict further |
| **A-004** | Versioned updates to governance rules are preferred — update `version` and add a new entry block rather than modifying existing text |
| **A-005** | Any attempt to delete or modify an archived source document is a governance violation — logged in `INCIDENT_LOG.md` |

---

## 9. Source Immutability Doctrine

> **Core doctrine:** An archived source document is a **fixed point in institutional history**. It is not interpretation-dependent. It does not change based on how subsequent doctrine develops. Future canonical extractions may reveal ambiguities — those ambiguities are documented in the canonical markdown, not resolved by modifying the source.

**Corollaries:**
- The original PDF is never edited, even if canonical extraction later reveals errors in the source
- If the source contains contradictions, those are documented as unresolved conflicts in the canonical markdown
- If a later version of the source document contradicts an earlier version, both are preserved and a DEC entry is created
- No human or agent may modify an archived source document after ingest

---

## 10. Canonical Extraction Workflow

```
Step 1: Register
  └── Add entry to SOURCE_DOCUMENT_REGISTRY.md
      └── Set status: pending_upload
      └── Record source_filename, category, archive_path, canonical_targets

Step 2: Upload
  └── Upload source document to correct category subdirectory
      └── Verify file present and size > 0
      └── Update registry entry: status: archived
      └── Compute SHA-256 checksum
      └── Update registry entry: checksum, ingest_date

Step 3: Overlay Check
  └── Run overlay check against existing canon files
      └── Record overlay_risk in registry
      └── If HIGH risk → defer to DEC entry
      └── If MEDIUM risk → wolfpack_review approval required

Step 4: Extraction
  └── Extract source content (PDF → markdown)
      └── Generate canonical markdown at target path
      └── Preserve all provenance fields in YAML front matter
      └── Mark status: active in canonical markdown

Step 5: Validation
  └── Run wolfpack_review validation pass
      └── Verify YAML front matter compliance
      └── Verify cross-links resolve
      └── Verify no duplicate canon identifiers
      └── If validation passes → canonical doc is operational

Step 6: Registry Closure
  └── Update registry entry: status: canonical_converted
      └── Record canonical_target path
      └── Record conversion_commit hash
```

---

## 11. Governance File Locations

| File | Purpose |
|---|---|
| `archive/SOURCE_ARCHIVE_GOVERNANCE.md` | This file — governing rules for the archive layer |
| `archive/SOURCE_DOCUMENT_REGISTRY.md` | Registered source documents with metadata and status |
| `archive/source-documents/<category>/` | Individual source document storage directories |

---

*Governance maintained in `archive/SOURCE_ARCHIVE_GOVERNANCE.md` — governed by Wolfpack Canon and STAGE_1_MEMORY_INGESTION_PLAN.md*