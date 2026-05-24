---
title: "Source Document Registry"
document_type: "registry"
status: "active"
version: "1.0"
created: "2026-05-24"
updated: "2026-05-24"
source_type: "internal"
provenance: "wolfpack-institutional-memory"
tags:
  - "governance"
  - "registry"
  - "archive"
  - "batch-002"
related_ids:
  - "archive/SOURCE_ARCHIVE_GOVERNANCE.md"
  - "operations/STAGE_1_BATCH_002_PDF_SOURCE_INVENTORY.md"
append_only: true
---

# Source Document Registry

**Registry Version:** 1.0
**Last Updated:** 2026-05-24
**Archive Root:** `archive/source-documents/`
**Governance:** `archive/SOURCE_ARCHIVE_GOVERNANCE.md`

> **Append-only registry.** Entries are added, never modified or deleted. Superseded documents are closed with `status: superseded` and a `superseded_by` reference. See `SOURCE_ARCHIVE_GOVERNANCE.md` for retention and immutability doctrine.

---

## Registry Schema

Each entry adheres to the following schema:

| Field | Type | Description |
|---|---|---|
| `source_id` | string | Unique identifier: `SRC-<category>-<NNN>` |
| `filename` | string | Exact original filename as uploaded |
| `category` | string | Archive category subdirectory |
| `archive_path` | string | Full path within `archive/source-documents/<category>/` |
| `checksum` | string | `sha256:<hex>` — computed at ingest time |
| `ingest_date` | ISO-8601 | Date source document was archived |
| `version` | string | Version from filename or `unknown` |
| `canonical_targets` | list | Markdown paths where doctrine will be extracted |
| `overlay_risk` | enum | `NONE`, `LOW`, `MEDIUM`, `HIGH` |
| `status` | enum | `pending_upload`, `archived`, `canonical_converted`, `superseded` |
| `batch` | string | Ingestion batch ID (e.g., `STAGE_1_BATCH_002A`) |
| `notes` | string | Additional context, blockers, or risk notes |

---

## Document Entries

### Category: canonical

| source_id | filename | archive_path | checksum | status | overlay_risk | canonical_targets | batch |
|---|---|---|---|---|---|---|---|
| `SRC-CANON-001` | `01_WOLFPACK_CANONICAL_REPOSITORY_SPEC_v1.pdf` | `canonical/01_WOLFPACK_CANONICAL_REPOSITORY_SPEC_v1.pdf` | `pending_upload` | `pending_upload` | NONE | `canon/CANONICAL_REPOSITORY_SPEC.md` | `STAGE_1_BATCH_002A` |
| `SRC-CANON-002` | `Wolfpack_Strategic_Doctrine_Expansion_v1.pdf` | `canonical/Wolfpack_Strategic_Doctrine_Expansion_v1.pdf` | `pending_upload` | `pending_upload` | MEDIUM | `canon/STRATEGIC_DOCTRINE_EXPANSION.md` | `STAGE_1_BATCH_002B` |

---

### Category: memory

| source_id | filename | archive_path | checksum | status | overlay_risk | canonical_targets | batch |
|---|---|---|---|---|---|---|---|
| `SRC-MEMORY-001` | `WOLFPACK_MEMORY_ARCHITECTURE_v1.pdf` | `memory/WOLFPACK_MEMORY_ARCHITECTURE_v1.pdf` | `pending_upload` | `pending_upload` | NONE | `canon/MEMORY_ARCHITECTURE.md` | `STAGE_1_BATCH_002A` |
| `SRC-MEMORY-002` | `04_WOLFPACK_MEMORY_DATA_MODEL_v1.pdf` | `memory/04_WOLFPACK_MEMORY_DATA_MODEL_v1.pdf` | `pending_upload` | `pending_upload` | NONE | `canon/MEMORY_DATA_MODEL.md` | `STAGE_1_BATCH_002B` |

---

### Category: governance

| source_id | filename | archive_path | checksum | status | overlay_risk | canonical_targets | batch |
|---|---|---|---|---|---|---|---|
| `SRC-GOV-001` | `WOLFPACK_AGENT_GOVERNANCE_v1.pdf` | `governance/WOLFPACK_AGENT_GOVERNANCE_v1.pdf` | `pending_upload` | `pending_upload` | MEDIUM | `agents/AGENT_GOVERNANCE.md` | `STAGE_1_BATCH_002B` |
| `SRC-GOV-002` | `Wolfpack_Operating_System_Doc_Pack_v1.pdf` | `governance/Wolfpack_Operating_System_Doc_Pack_v1.pdf` | `pending_upload` | `pending_upload` | HIGH | `canon/OS_DOCTRINE_OVERVIEW.md` | `Deferred` |

---

### Category: systems

| source_id | filename | archive_path | checksum | status | overlay_risk | canonical_targets | batch |
|---|---|---|---|---|---|---|---|
| `SRC-SYSTEMS-001` | `WOLFPACK_VENDOR_ABSTRACTION_STANDARD_v1.pdf` | `systems/WOLFPACK_VENDOR_ABSTRACTION_STANDARD_v1.pdf` | `pending_upload` | `pending_upload` | NONE | `systems/VENDOR_ABSTRACTION_STANDARD.md` | `STAGE_1_BATCH_002B` |
| `SRC-SYSTEMS-002` | `03_WOLFPACK_INTERNAL_API_CONTRACTS_v1.pdf` | `systems/03_WOLFPACK_INTERNAL_API_CONTRACTS_v1.pdf` | `pending_upload` | `pending_upload` | NONE | `systems/INTERNAL_API_CONTRACTS.md` | `STAGE_1_BATCH_002B` |
| `SRC-SYSTEMS-003` | `02_WOLFPACK_EVENT_SCHEMA_SPEC_v1.pdf` | `systems/02_WOLFPACK_EVENT_SCHEMA_SPEC_v1.pdf` | `pending_upload` | `pending_upload` | NONE | `systems/EVENT_SCHEMA_SPEC.md` | `STAGE_1_BATCH_002B` |

---

### Category: runtime

| source_id | filename | archive_path | checksum | status | overlay_risk | canonical_targets | batch |
|---|---|---|---|---|---|---|---|
| `SRC-RUNTIME-001` | `05_WOLFPACK_RUNTIME_WORKER_INTERFACE_v1.pdf` | `runtime/05_WOLFPACK_RUNTIME_WORKER_INTERFACE_v1.pdf` | `pending_upload` | `pending_upload` | NONE | `runtime/RUNTIME_WORKER_INTERFACE.md` | `STAGE_1_BATCH_002B` |

---

### Category: operations

| source_id | filename | archive_path | checksum | status | overlay_risk | canonical_targets | batch |
|---|---|---|---|---|---|---|---|
| `SRC-OPS-001` | `WOLFPACK_OPERATIONAL_STATE_SPEC_v1.pdf` | `operations/WOLFPACK_OPERATIONAL_STATE_SPEC_v1.pdf` | `pending_upload` | `pending_upload` | NONE | `operations/OPERATIONAL_STATE_SPEC.md` | `STAGE_1_BATCH_002C` |

---

### Category: observability

| source_id | filename | archive_path | checksum | status | overlay_risk | canonical_targets | batch |
|---|---|---|---|---|---|---|---|
| `SRC-OBSERVE-001` | `06_WOLFPACK_OBSERVABILITY_AND_TELEMETRY_v1.pdf` | `observability/06_WOLFPACK_OBSERVABILITY_AND_TELEMETRY_v1.pdf` | `pending_upload` | `pending_upload` | NONE | `observability/TELEMETRY_SPEC.md` | `STAGE_1_BATCH_002C` |
| `SRC-OBSERVE-002` | `WOLFPACK_SYSTEM_HEALTH_SPEC_v1.pdf` | `observability/WOLFPACK_SYSTEM_HEALTH_SPEC_v1.pdf` | `pending_upload` | `pending_upload` | NONE | `observability/SYSTEM_HEALTH_SPEC.md` | `STAGE_1_BATCH_002C` |

---

### Category: deployment

| source_id | filename | archive_path | checksum | status | overlay_risk | canonical_targets | batch |
|---|---|---|---|---|---|---|---|
| `SRC-DEPLOY-001` | `09_WOLFPACK_DEPLOYMENT_EXECUTION_STANDARD_v1.pdf` | `deployment/09_WOLFPACK_DEPLOYMENT_EXECUTION_STANDARD_v1.pdf` | `pending_upload` | `pending_upload` | NONE | `deployment/DEPLOYMENT_EXECUTION_STANDARD.md` | `STAGE_1_BATCH_002C` |
| `SRC-DEPLOY-002` | `10_WOLFPACK_SYSTEM_BUILD_MASTER_SPEC_v1.pdf` | `deployment/10_WOLFPACK_SYSTEM_BUILD_MASTER_SPEC_v1.pdf` | `pending_upload` | `pending_upload` | NONE | `deployment/SYSTEM_BUILD_MASTER_SPEC.md` | `STAGE_1_BATCH_002C` |

---

### Category: automation

| source_id | filename | archive_path | checksum | status | overlay_risk | canonical_targets | batch |
|---|---|---|---|---|---|---|---|
| `SRC-AUTO-001` | `07_WOLFPACK_AUTOMATION_EXECUTION_MATRIX_v1.pdf` | `automation/07_WOLFPACK_AUTOMATION_EXECUTION_MATRIX_v1.pdf` | `pending_upload` | `pending_upload` | NONE | `automation/AUTOMATION_EXECUTION_MATRIX.md` | `STAGE_1_BATCH_002C` |
| `SRC-AUTO-002` | `08_WOLFPACK_AI_SUPPORT_RUNTIME_v1.pdf` | `automation/08_WOLFPACK_AI_SUPPORT_RUNTIME_v1.pdf` | `pending_upload` | `pending_upload` | NONE | `automation/AI_SUPPORT_RUNTIME.md` | `STAGE_1_BATCH_002C` |

---

### Category: opportunities

| source_id | filename | archive_path | checksum | status | overlay_risk | canonical_targets | batch |
|---|---|---|---|---|---|---|---|
| `SRC-OPP-001` | `WOLFPACK_OPPORTUNITY_RADAR_ENGINE_v1.pdf` | `opportunities/WOLFPACK_OPPORTUNITY_RADAR_ENGINE_v1.pdf` | `pending_upload` | `pending_upload` | NONE | `opportunities/OPPORTUNITY_RADAR_ENGINE.md` | `STAGE_1_BATCH_002C` |

---

### Category: customer_interfaces

| source_id | filename | archive_path | checksum | status | overlay_risk | canonical_targets | batch |
|---|---|---|---|---|---|---|---|
| `SRC-CUST-001` | `WOLFPACK_CUSTOMER_SYSTEM_INTERFACE_STANDARD_v1.pdf` | `customer_interfaces/WOLFPACK_CUSTOMER_SYSTEM_INTERFACE_STANDARD_v1.pdf` | `pending_upload` | `pending_upload` | NONE | `customer_interfaces/CUSTOMER_INTERFACE_STANDARD.md` | `STAGE_1_BATCH_002C` |

---

## Registry Summary

| Metric | Count |
|---|---|
| Total registered documents | 19 |
| Documents pending upload | 19 |
| Documents archived | 0 |
| Documents canonical-converted | 0 |
| Documents superseded | 0 |
| HIGH overlay risk (deferred) | 1 |
| MEDIUM overlay risk | 2 |
| LOW/NONE overlay risk | 16 |

---

## Next Ingestion Actions

| Batch | Documents | Next Action |
|---|---|---|
| `STAGE_1_BATCH_002A` (retry) | SRC-CANON-001, SRC-MEMORY-001 | Upload PDFs to cloud archive, compute checksums, update registry to `archived` |
| `STAGE_1_BATCH_002B` | SRC-CANON-002, SRC-MEMORY-002, SRC-GOV-001, SRC-SYSTEMS-001/002/003, SRC-RUNTIME-001 | Overlay review then batch upload |
| `STAGE_1_BATCH_002C` | SRC-OPS-001, SRC-OBSERVE-001/002, SRC-DEPLOY-001/002, SRC-AUTO-001/002, SRC-OPP-001, SRC-CUST-001 | Standard batch upload |

---

*Registry maintained in `archive/SOURCE_DOCUMENT_REGISTRY.md` — append-only, governed by `archive/SOURCE_ARCHIVE_GOVERNANCE.md`*