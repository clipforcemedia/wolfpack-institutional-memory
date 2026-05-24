---
title: "Stage 1 — Canonical Memory Ingestion Plan"
document_type: "operations"
status: "active"
version: "1.0"
created: "2026-05-24"
updated: "2026-05-24"
source_type: "internal"
provenance: "wolfpack-institutional-memory"
tags:
  - "governance"
  - "doctrine"
  - "memory"
related_ids:
  - "DEC-001"
append_only: true
---

# Stage 1 — Canonical Memory Ingestion Plan

**Plan Version:** 1.0
**Created:** 2026-05-24
**Status:** Active — Batch 001 Pending
**Doctrine Basis:** Wolfpack Canon, DEC-001 Architecture Correction

---

## 1. Objective

Establish a repeatable, auditable process for ingesting external source documents into the Wolfpack institutional memory with full provenance, version lineage, and operational fidelity.

**Guiding Doctrine:**
- GitHub is the canonical memory source of truth
- PDFs are archival source material (never edited post-ingest)
- Markdown files are the operational memory layer
- No canonical overwrite without a formal DEC-00x decision entry
- No autonomous deletion of any canonical file
- All version lineage preserved through git history

---

## 2. Source Document Inventory

Batch 001 scope — core doctrine specs:

| Document | Type | Source | Status |
|---|---|---|---|
| DEC-001 Architecture Correction | markdown | internal | ✓ Ingested |
| DEC-002 Intake Summary Webhook | markdown | internal | ✓ Ingested |
| GPT Interaction Protocol | markdown | internal | ✓ Ingested |
| System Architecture | markdown | internal | ✓ Ingested |
| Wolfpack Canon | markdown | internal | ✓ Ingested |
| Wolfpack Review Runbook | markdown | internal | ✓ Ingested |
| Milestone Log | markdown | internal | ✓ Ingested |
| Decisions Log | markdown | internal | ✓ Ingested |
| Lessons Learned | markdown | internal | ✓ Ingested |
| Incident Log | markdown | internal | ✓ Ingested |

**Batch 002+ scope (deferred):** External vendor docs, architecture diagrams, API specs, product briefs, contract summaries, and any PDF-sourced material.

---

## 3. Target Folder Structure

```
wolfpack-institutional-memory/
├── canon/                    # Core operational doctrine
│   ├── GPT_INTERACTION_PROTOCOL.md
│   ├── SYSTEM_ARCHITECTURE.md
│   └── WOLFPACK_CANON.md
├── decisions/                # DEC-00x decision entries
│   ├── DEC-001.md
│   └── DEC-002.md
├── agents/                   # Agent role definitions
│   ├── DEPLOYMENT_GOVERNOR.md
│   ├── ETERNA_COMMAND.md
│   ├── MEMORY_KEEPER.md
│   ├── OPPORTUNITY_RADAR.md
│   └── RED_TEAM.md
├── workflows/                # Operational workflows
│   └── WOLFPACK_REVIEW.md
├── operations/               # Operational docs (this plan lives here)
│   ├── STAGE_1_MEMORY_INGESTION_PLAN.md
│   ├── DECISIONS.md
│   ├── MILESTONE_LOG.md
│   ├── INCIDENT_LOG.md
│   └── LESSONS_LEARNED.md
├── tasks/                    # Task registry and results
│   ├── inbox/                # Pending tasks
│   ├── results/              # Validated task results
│   └── wolfpack_review_runner.py
├── opportunities/            # Opportunity tracking
│   ├── OPPORTUNITY_BRIEFS.md
│   └── VALIDATION_QUEUE.md
└── status/                   # Current state docs
    ├── CURRENT_STATE.md
    ├── BLOCKED_FEATURES.md
    └── NEXT_ACTIONS.md
```

**Archival PDFs** are stored outside this repo in a designated cloud archive folder and linked via provenance front matter — they are never committed to the repo.

---

## 4. Archival PDF Policy

| Rule | Description |
|---|---|
| **Storage** | PDFs stored in cloud archive (Google Drive, S3, etc.), not in repo |
| **Linking** | Each PDF-linked document contains `source_pdf` field in YAML front matter with archive URL |
| **Never commit** | No `.pdf` files in the GitHub repo |
| **Verification** | Archive URL must be accessible and stable |
| **Replacement** | If source PDF is superseded, create new version entry; never overwrite |
| **Deletion** | PDFs are never deleted from archive; mark `superseded: true` in front matter |

---

## 5. Markdown Canon Policy

| Rule | Description |
|---|---|
| **Canonical format** | All canonical memory stored as UTF-8 markdown |
| **Front matter required** | All canon files must include YAML front matter |
| **No canonical overwrite** | Updates require DEC-00x decision entry or wolfpack_review approval |
| **No autonomous deletion** | Any deletion requires a decision entry + wolfpack_review gate |
| **Version lineage** | Git history is the sole version history; no parallel changelog |
| **Path stability** | Canonical file paths never change; create new files for new versions |
| **Encoding** | No binary assets in markdown; use external references |

---

## 6. YAML Front Matter Standard

Every canonical markdown file must begin with:

```yaml
---
title: "Short descriptive title"
type: canon|decision|agent|workflow|operations|task|status|opportunity
status: draft|active|archived|superseded
version: "0.1"                          # semantic version
created: "YYYY-MM-DD"                   # ISO-8601
updated: "YYYY-MM-DD"                   # ISO-8601
provenance:                             # required for all files
  source: "original source name or document title"
  source_type: internal|external|derived
  source_url: "https://..."             # URL or archive reference
  ingested_by: "agent or human name"
  ingest_date: "YYYY-MM-DD"
  source_pdf: "archive://..."           # only if PDF source exists
superseded: false                       # true if replaced
superseded_by: "DEC-00x"                # decision ID if superseded
tags:                                   # see Section 8
  - tag1
  - tag2
---
```

**Front matter is mandatory** for all files in: `canon/`, `decisions/`, `agents/`, `workflows/`, `operations/`, `status/`, `opportunities/`.

---

## 7. Provenance Requirements

Every document must answer:
1. Where did this come from?
2. Who or what ingested it?
3. When was it ingested?
4. Is there an archival source (PDF)?
5. Has it been superseded?

**Verification:** Provenance fields are checked during wolfpack_review validation.

**Incomplete provenance = invalid canon.** Documents missing front matter or provenance fields are flagged `draft` and not considered operational until completed.

---

## 8. Tagging Taxonomy

Standard tags for cross-referencing:

| Tag Category | Values |
|---|---|
| **Domain** | `ai-agent`, `architecture`, `deployment`, `governance`, `memory`, `workflow`, `integration` |
| **Status** | `active`, `draft`, `archived`, `superseded`, `blocked` |
| **Type** | `canon`, `decision`, `agent`, `workflow`, `task`, `incident`, `lesson`, `opportunity` |
| **Product** | `voice-ai`, `openclaw`, `base44`, `twilio`, `openai` |
| **Decision** | `DEC-001`, `DEC-002`, etc. |
| **Priority** | `high`, `medium`, `low` |

Tags are lowercase hyphenated. Multiple tags allowed.

---

## 9. Cross-Linking Rules

| Rule | Example |
|---|---|
| **Decision links** | `[DEC-001](../operations/DECISIONS.md)` |
| **Canon links** | `[System Architecture](../canon/SYSTEM_ARCHITECTURE.md)` |
| **Task links** | `task_005` → `[task_005](../tasks/inbox/task_005.md)` |
| **Agent links** | `[Memory Keeper](../agents/MEMORY_KEEPER.md)` |
| **External links** | Use full URL for external references |
| **No bare URLs** | All URLs must be wrapped in descriptive anchor text |

**No circular references.** Cross-links must form a DAG, not a cycle.

---

## 10. Validation Checklist

Before any document is marked `active` in the canon:

- [ ] YAML front matter present and valid
- [ ] All required front matter fields populated
- [ ] `provenance.source` and `provenance.ingest_date` present
- [ ] `tags` array contains at least one tag
- [ ] No broken internal links (relative paths resolve)
- [ ] No bare URLs — all links have descriptive text
- [ ] No orphaned documents (no incoming links from any other canon file)
- [ ] If `superseded: true`, `superseded_by` field populated
- [ ] File path follows folder structure convention
- [ ] Title in front matter matches filename intent
- [ ] Git history shows clean commit (no binary artifacts)

---

## 11. Batch 001 Scope

**Objective:** Validate the ingestion process against the existing canon corpus.

**Ingestion targets:** All files currently in `canon/`, `decisions/`, `agents/`, `workflows/`, `operations/`, and `status/` — retroactively apply front matter where missing.

**Batch 001 tasks:**
- [ ] Audit all existing canon files for missing front matter
- [ ] Apply YAML front matter to any file missing it
- [ ] Verify all `provenance` fields are populated
- [ ] Run wolfpack_review validation pass on updated files
- [ ] Confirm all cross-links resolve correctly
- [ ] Tag all files with appropriate taxonomy
- [ ] Document Batch 001 completion in MILESTONE_LOG.md

**Owner:** Eterna / Wolfpack
**Definition of Done:** All canon files validate against checklist in Section 10.

---

## 12. Definition of Done

Stage 1 is complete when:

1. All Batch 001 documents pass the Validation Checklist (Section 10)
2. No canon file is missing YAML front matter
3. Provenance fields complete on every document
4. Cross-links verified across entire corpus
5. MILESTONE_LOG.md updated with Stage 1 completion entry
6. Wolfpack_review run confirms no regressions
7. GitHub repo shows clean state with no uncommitted ingestion artifacts

**Stage 1 does NOT complete:**
- Batch 002+ (external docs, PDFs)
- Any production deployments
- Any code changes

---

*Maintained in `operations/STAGE_1_MEMORY_INGESTION_PLAN.md` — governed by Wolfpack Canon and DEC-001*