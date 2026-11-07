# ForFathers — Emergent Final Platform Evaluation

**As of:** 2026-11-07 (America/New_York)
**Status:** Conditional **GO** to select Emergent as AI builder and retain Supabase/Stripe architecture; **NO** production launch authorization; canonical D035 remains Lovable until explicit user approval. No code changes or spending authorized by this evaluation.
**Evidence hierarchy:** (1) project-specific support inspection quoted by user; (2) current official vendor docs; (3) external review community sentiment, low confidence; (4) user visual testing. No independent running-code audit.

## Executive recommendation
**Select Emergent as builder; preserve ForFathers's existing five-page React frontend; continue with Supabase Auth + Postgres/RLS + private Supabase Storage; use the existing FastAPI backend for /api webhook/download/order-sensitive logic; connect a separately controlled Stripe account and Resend account.** Do not rebuild Lovable copy. These are candidate technical decisions requiring D035 amendment and validation, not permission to implement.

Justification: User's Emergent site was generated with free credits and is visually preferred to the Lovable comparison. Emergent support inspected the exact job, found five pages (Home, Brotherhood, Resources, Store, Cohort) and FastAPI backend, confirmed ability to add Supabase Auth/Postgres/RLS/Storage without redesign. Own-Stripe Checkout/subscriptions/webhooks/portal supported. All transactional logic remains unbuilt. Architectural continuity with already-approved D027 and D046 limits switching risk.

## How Emergent works
- A *Job* is a persistent application workspace (chat, code, preview, settings). AI agents write, install, test, preview and publish; instructions in chat may induce code edits and use credits.
- Most common full-stack template React frontend / Python FastAPI backend / managed MongoDB. Templates are fixed once created; current ForFathers is FastAPI on MongoDB template, but MongoDB can remain only as boilerplate dependency while all app data live in Supabase. Do not secretly create dual data systems. Production backend endpoints must use `/api`.
- Preview sleeps after ~30 minutes; preview and production have distinct secrets and runtime. First publish may seed managed preview MongoDB into prod; later **Re-publish** replaces code without copying preview DB contents. **Replace** swaps Jobs and requires deliberate DB choice. Never test live payments using preview webhook URL.
- Source code stored in workspace; Standard+ enables manually triggered **Save to GitHub** snapshot/push. Mid-job pull/merge unavailable according to workspace docs and project support; import GitHub at new-Job creation only. Exports exclude secrets, environment variables, DB records and node_modules; files >100 MB rejected. GitHub alone is not a complete backup. Lovable has documented automatic two-way Git sync, an actual feature advantage.
- Plugins: (1) curated integrations (Stripe, Resend, etc.), (2) general SDK/API integrations including Supabase, (3) MCP connectors that give *builder agents* tool access to third-party services; MCP availability is not proof of a customer-facing app feature. Avoid unnecessary connectors. Scope integrations by least privilege. External providers have independent billing.
- Emergent Auth and managed Object Store are optional. Emergent Auth hosted branding/user portability need assessment; project should use Supabase Auth. Object Store does not support deletion according to Emergent glossary, with 5 GB quota, and is not independently portable; use Supabase Storage. Official Object Store docs say pre-signed URLs exist, whereas project read-only agent reported otherwise. This discrepancy no longer affects candidate stack.
- Deployment/publishing has credit-priced hosting tier; agent testing, iteration and some integrations consume credits. Periodic maintenance, exports, secrets and incident response require an operator, not AI-only automation. Published logs retention is limited (7 days generally, 30 days on Pro/Enterprise per Emergent app performance docs).
- SEO risk: React SPA can render shell HTML for crawlers; official Enable SEO crawler prerender toggle mitigates for normal SEO but has caching/status-code exceptions. Test all five public pages' titles, canonical routes, indexability, redirects and 404 behavior. No SEO claim before deployed tests.

## Project-specific support inspection
- Job ID b0ebcbac-9fca-4c3f-89e5-363af17c9114; app fathers-together.
- Site exists: five frontend pages; content in client-shipped local file; purchase buttons, Cohort form, member access placeholders. **Paid content in client bundle is not private**. Must replace private content references with Supabase protected content and keep only public metadata/samples.
- FastAPI can handle signature-verified Stripe endpoint at `/api/webhooks/stripe` and secure download endpoint under `/api`; add stripe SDK in requirements.txt; restrict CORS to domain, keep Supabase secret/service key and Stripe signing key on backend.
- Supabase Edge Functions may be called but deployed separately through Supabase CLI/dashboard; not directly deployed by Emergent project (this overrides optimistic marketing claims for this particular template). No need to introduce them if FastAPI backend suffices.
- Current FastAPI startup expects MongoDB env vars; verify boot without using MongoDB as production customer data store. Production app likely still provisions managed MongoDB, even if unused.
- Hosting support cites Starter 512MB but published tier spec lists Starter 200MB/0.05vCPU. Confirm actual project Resources allocation; prohibit production Starter unless workload test passes.

## Coverage across approved decisions
| Decision range | Need | Emergent feasibility / required custom work |
|---|---|---|
| 1–10 | Identity, inclusive positioning, $5 monthly membership, cancel through paid period | Frontend built; Stripe subscription flow, signup, paid access and refund/cancellation logic require custom implementation/testing |
| 11–18 | 20 written resources (4/category; 3 free) + 2 simple interactive tools; gated library; search/filter and suggestions | 15 cards observed in early prototype; inventory discrepancy must be corrected; gated content moved out of public mock data; two tools and verified content still required |
| 19–27 | 20 products (10/10), $3/$5, PDF/PNG/JPG/ZIP, personal license, guest payment, five downloads | Frontend has 20 mock products; some invalid DOCX/XLSX labels must be corrected. Stripe one-time guest Checkout, verified order, private file delivery, email recovery, atomic five-use limit are CUSTOM and untested |
| 28–34 | $1 per qualifying paid membership payment, reversal/refund/dispute ledger, quarterly gift/report | Custom ledger technically feasible; charity-law/marketing/tax review and verified recipient needed before public claim/operation |
| 35–45 | Five pages, branding, mobile, signup and dashboard, accessibility WCAG 2.2 AA target | Existing Emergent UI visually user-approved; functional navigation/accessibility/dashboard need verification. D035 amendment **requires explicit approval** |
| 46–54 | Stripe merchant account, billing states, account deletion, support mailbox, analytics, secure launch gate | APIs supported; production webhook, reconciliation, CORS, monitoring, security, backups, account deletion and support workflow must be built and tested |
| 55–60 | Cohort Coming Soon / consented interest signup only; future marketplace deferred | Static coming-soon UI exists; any form must be genuinely disabled pending backend; future Stripe Connect/payouts NOT v0.1 |

## Financial model / limits
User screenshot from Standard monthly plan: $1 / 7-day Standard trial (eligible new subscription) with 100 credits, then automatic renewal $20/month; Standard $20/month, recurring 100 credits and first-month promotional 150 bonus reported by UI; Pro $200/month 750 recurring credits. Free credits all used.
Emergent official tier table: Starter 50 credits/month (200 MB/0.05vCPU per docs), Launch 125 (2GB/0.5vCPU), Grow 225 (4GB/1vCPU), Scale 450 (8GB/2vCPU), Elite 1100 (16GB/4vCPU). Fees are credits/month, deducted from the same pool as development runs. Trial hosting waived until end according to direct support reply; confirm UI billing before publishing. Standard 100 recurring credits alone **cannot cover** a 125-credit Launch or 225-credit Grow continuously. Top-up $50/250 credits is supported by current docs and support. Support states custom top-up amounts exist but minimum unverified. Current doc mentions older $10/50 and even $1/5 options; conflicting source. The account checkout is authoritative.
Illustrative credit economics: with Standard 100 credits and only hosting usage, Launch requires at least +25 credits/mo (~$5-worth at $0.20/credit), Grow +125 (~$25-worth). This is NOT the transaction minimum, does NOT include further agent/build credits and is NOT a cash quote. Buying 250 topup costs $50 per quoted pack and lasts until consumed (no expiry). Scale-to-zero Starter/Launch means in-app scheduled jobs may not execute; Grow+ two running instances means any in-app scheduled process also needs distributed/idempotent lock. Use independent scheduled reconciliation or verified Supabase scheduling.
Additional independent costs: Supabase Free ($0, pauses after 7 days low activity), Supabase Pro from $25/mo (no inactivity pause, backups and expanded quotas). Resend Free ($0 within 3000 emails/mo, 100/day), separate owned support inbox may have cost. Stripe 2.9% + $0.30 US card transaction, subscription Stripe Billing as low-volume paygo 0.7%; actual account fees, disputes and tax services can vary. $5 membership approx 4.52 after standard 2.9%+0.30 and billing 0.7% then 3.52 after $1 giving reserve, before tax, disputes, support/hosting.
**No fixed all-in production cost is established.** Test actual hosting memory, latency, webhook availability, credit spend and maintenance. Credit cost of implementing all features unknown.

## Security / fulfillment acceptance
1. Never put private guide bodies, files, Stripe keys, admin credentials, Supabase service keys or order data in client bundle; public metadata only. Backend uses service credentials only when authorized for exact operation; service-role bypasses RLS, so FastAPI MUST enforce entitlement explicitly before using it. Test RLS with anonymous, unpaid, active, expired, other-user, moderator accounts.
2. Stripe BYOK subscription and store Checkout: server-defined price and product, verify Stripe signature and payment state; idempotent event IDs, out-of-order handling, periodic reconciliation. Success URL must never grant membership or download access.
3. Separate subscription entitlement from **guest purchase** entitlement. Support-suggested demo endpoint checking only membership would violate guest-buy requirement. Email recovery should use expiring token + verified ownership, not public order lookup.
4. Private Supabase Storage. **Signed links are not one-time.** Supabase docs say individual signed links cannot be revoked except deleting/moving/renaming object, and CDN may serve cached signed link beyond nominal expiry (https://supabase.com/docs/guides/storage/cdn/smart-cdn). Define five-use policy as five atomic authorizations/transfer starts with short TTL and careful replay/cache behavior. If true five network transfers must be strictly enforced, use server-side one-time grants + proxy/stream, and prove performance on large files. No DRM guarantee: purchaser can copy a digital product after download.
5. Test 20 concurrent download attempts of one purchase -> max five authorized. Test failed transfer/resets, refund revocation, expired links, direct bucket access denial, browser caching, ZIP size, email recovery.
6. Membership renewals, failed cards, cancel at period end, account deletion, moderation, Giving Fund idempotent ledger and reversals, audit logs, backup and restore, mobile/a11y/SEO, legal-tax-entity-privacy and support before launch.
7. Do not assert AI-created systems are security-audited or compliant until independent manual/automated tests pass.

## Discrepancies and evidence gaps
- Supabase official marketing integration page claims Edge Function deployment; project-specific support says outside Emergent, use Supabase CLI/dashboard. Treat support response as controlling actual project capabilities.
- Emergent object store pre-signed URL support documented, while the agent's read-only report said unavailable; object delete not supported according to glossary. Avoid as paid-file source.
- Starter 512MB (support) vs 200MB (published tier table). Verify in app.
- GitHub marketing integration page implies broader collaboration, but workspace docs and support say **push-only; no mid-job pull/merge**. Do not claim bidirectional Git integration.
- Subscription $20/mo (user screenshot) vs public pricing potentially annual-billed, defer to signed-in checkout for exact account billing; first-month bonus may expire.
- Some old Emergent pricing documentation lists $10/50 credits while current supports $50/250 and custom amounts. Never promise $5 checkout or only $20/month all-in.
- There is no direct penetration test, deployment load test, privacy review, backup restore, complete functional accessibility audit, actual payment fulfillment, or legal approval.
- **External reviews** including a July 2026 TechRadar review and Trustpilot feedback note cost and inconsistent completion. They are directional anecdotal evidence; they do not override project tests or support inspection.

## Replacement comparison
Emergent wins current project on user-perceived visual quality, existing working frontend, and verified ability to integrate own Supabase/Stripe. Lovable has better documented direct Supabase workflow/Edge Function deployment and continuous two-way Git synchronization, which Emergent lacks. Emergent may consume higher-than-expected hosting and AI-building credits. Neither platform supplies custom five-use digital delivery automatically. Migration back to Lovable would rebuild UI and add cost without proven technical advantage at this stage.
**Decision:** choose Emergent builder while retaining Supabase and Stripe unchanged. Do not switch database to MongoDB, add R2, add new auth service, build full marketplace, or implement AI service integrations without separate ADR and evidence.

## Staged implementation after user authorization
**Gate 0:** Record D035 amendment (approved builder only). Write ADR rationale/risks. Save existing generated code to separate GitHub repo upon trial activation; do not use institutional-memory repository for generated app code.
**Gate 1:** On paid trial, connect **existing** app to Supabase Auth/Postgres with RLS and demonstrate a protected content item using 2 identities. Maintain five UI pages; demonstrate guest exclusion. NO Stripe code yet. Test no frontend secrets.
**Gate 2:** Stripe **test-mode** monthly $5 subscription, verified webhook, paid-through/cancellation/failed renewal. Reproduce duplicate/out-of-order event behavior.
**Gate 3:** Stripe guest one-time $3/$5 purchase, email recovery, private storage and concurrent five-download semantics.
**Gate 4:** Community/moderation, member dashboard, deletion, complete content and store assets, Cohort consent, Giving ledger after legal, monitoring, backed-up restore, accessibility/SEO.
**Gate 5:** Measure hosting and outbound email, payment dispute and failed webhook behavior on published test deployment; verify own-code external hosting option; sign D054 launch checklist. No production card charges before separate authorization.

## Critical sources
- https://help.emergent.sh/what-is-emergent
- https://help.emergent.sh/how-apps-work-here-mental-model
- https://help.emergent.sh/a-tour-of-the-workspace
- https://help.emergent.sh/what-kind-of-apps-you-can-build
- https://help.emergent.sh/stripe
- https://emergent.sh/integrations/supabase
- https://help.emergent.sh/mcps-connectors
- https://help.emergent.sh/key-integrations-catalogue
- https://help.emergent.sh/file-storage-emergent-object-store
- https://help.emergent.sh/glossary-of-emergent-terms
- https://help.emergent.sh/deployment-plan-levels
- https://help.emergent.sh/managing-credit-usage
- https://help.emergent.sh/deploying-web
- https://help.emergent.sh/preview-vs-deployed-separate
- https://help.emergent.sh/your-data-ownership
- https://help.emergent.sh/faqs
- https://help.emergent.sh/enable-seo-crawler-pre-rendering
- https://supabase.com/docs/guides/storage/serving/downloads
- https://supabase.com/docs/guides/storage/cdn/smart-cdn
- https://supabase.com/pricing
- https://stripe.com/pricing
- https://stripe.com/billing/pricing
- https://resend.com/pricing
- https://docs.lovable.dev/integrations/git-sync-overview
- https://docs.lovable.dev/integrations/supabase
- https://docs.lovable.dev/features/payments

**Owner action required:** approve D035 amendment; do not auto-write locked decisions without explicit consent.
