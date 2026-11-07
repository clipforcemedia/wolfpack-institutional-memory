# ForFathers — Emergent platform and integration due diligence

**Date:** 2026-11-07
**Status:** RESEARCH COMPLETE; BUILDER REPLACEMENT TECHNICALLY PLAUSIBLE, NOT PRODUCTION VERIFIED. No implementation authorization. D035 remains Lovable; no canonical decision changed.
**Scope:** Compare Emergent against all 60 canonical decisions in DECISION-REGISTER.md and the Lovable + Supabase + Stripe implementation specification. User reports Emergent frontend looks better; current Emergent project built with free credits, all exhausted.
**Evidence strength:** Official product/docs support capability claims; product-specific behavior must be tested independently. The user's Emergent-generated read-only audit reported a frontend-only site with mock data and no tested backend.

## Conclusion

**Emergent can probably replace Lovable as the AI builder without replacing Supabase.** Crucial discovery: Emergent officially advertises a Supabase integration supporting Auth, Postgres/RLS, private Storage, Edge Functions, schema changes and Stripe webhooks. This means the least architectural drift is **Emergent UI + Supabase Auth/Postgres/Storage/Edge Functions + Stripe (BYOK) + own Resend account**. Reuse the already generated Emergent public UI, but do not presume backend works. Test the specific project, its export, and hosting. Alternative native Emergent Auth/MongoDB+R2 is technically possible but changes D027/D046 and demands bespoke security/portability validation; do not silently choose it.

Emergent's own auth is documented and avoids handwritten password/JWT systems. It uses a hosted login at auth.emergentagent.com with unremovable Emergent branding; account portability and moving managed sessions to external hosting are not established. Supabase Auth preserves identity control and database RLS and suits the prior design.

## Types of integrations / 'plugins'

1. **Curated app-runtime integrations/playbooks** (Stripe, Resend, Emergent Auth, SendGrid, etc.): Emergent agents configure SDKs, secrets and backend wiring, sometimes with additional credits. Implementation still must be tested.
2. **Marketing integration directory** (Stripe, Supabase, Figma, Canva, GitHub, Gmail, Mailchimp, Circle, Shopify, etc.): broad capabilities, but a listing does not establish one-click runtime functionality, pricing, support or security.
3. **External API/SDK integrations:** e.g. R2/S3, alternate auth provider, monitoring. Feasible with coding, even if no curated tile.
4. **MCP connectors for builder/agents:** can query or act on external systems during authoring; not inherently features delivered to paying website customers. Limit permission scope.

Relevant: Stripe **mandatory**; Supabase **preferred**; Resend (own provider account) **recommended**; GitHub **mandatory before launch**; Namecheap DNS/custom domain **mandatory**; monitoring and backups **mandatory operational capability, vendors optional**; R2/S3 **only if Supabase private storage unsuitable**.
Defer: PayPal, Shopify, WooCommerce, Zapier, Mailchimp, Circle, Discord, Skool, Figma/Canva runtime integration, AI model/API integrations, mobile/native, Stripe Connect, analytics add-ons until actual requirements justify.
Support mailbox (support@forfathers.com) is distinct from outbound transactional email.

## Requirements mapped to 60-decision register

| Decision area | Requirement | Feasibility with Emergent | Status/gate |
|---|---|---|---|
| D001–D010 | Fathers first/all men welcome, $5 monthly Brotherhood, public samples, cancel through paid period | Frontend and Stripe subscription flow achievable | Needs test-mode billing and disclosures |
| D011–D018 | 20 written library resources (4 in 5 categories, 3 free), 2 interactive tools, paid gating, search/filter, requests | Frontend + Supabase Storage/Auth/RLS + simple forms/tools | Custom access tests; verify inventory |
| D019–D027 | 20 products, 10 practical/10 creative; $3/$5, PDF/PNG/JPG/ZIP, guest checkout, 5 downloads and recovery | Stripe Checkout + Supabase private Storage + atomic Postgres counter + secure email links | Custom fulfillment; concurrency/URL reuse/retry tests |
| D028–D034 | $1 allocation on qualifying paid $5 invoices; reversals; quarterly charity disbursement/report | Custom idempotent ledger and scheduled reconciliation | Legal/charity/consumer/tax review external; not an Emergent plugin |
| D035–D045 | Five-page public website; mobile; WCAG 2.2 AA target; joining, dashboard | Existing Emergent frontend strong; dynamic dashboard and accessible behavior implementable | Visual only; functional accessibility testing pending |
| D046–D054 | Stripe merchant account, secure webhooks, email verification, cancellation, receipts, dedicated email support, account deletion, metrics, launch gate | Stripe + Supabase Auth/functions + Resend/custom mailbox | Test-mode workflows, legal, backups, operator processes |
| D055–D060 | The Cohort coming soon, consented interest form; future 5% commission and provider payments | Interest form feasible; future Stripe Connect marketplace technically possible | **No marketplace/payout/Connect in v0.1**; 5% economics provisional |

## Digital delivery design required
- For one-time $3/$5 Checkout, accept browser selection only of server-maintained product price ID. Verify payment on backend using signed Stripe webhooks / API; never fulfill merely from success redirect.
- Store products in **private Supabase Storage** with RLS. Order and entitlement records in Postgres. Generate short-lived grants only after payment, identity/recovery and purchase-item checks.
- Atomically cap each paid line item to five authorized uses under concurrency. Define semantics before coding: one 'download' = one successful authorized issuance/transfer start (not provably 'finished' receipt). Limit link token replay; signed storage URLs may be reusable until expiry; use very short TTL, audit logs and support-assisted resets, or proxy if true one-time enforcement is mandatory. A signed URL is **not automatically single-use**.
- Guest checkout must not require an account; email recovery is controlled by an expiring, hashed, server-validated token or verified email ownership. Do not reveal order by email alone. Refunds revoke future grants subject to law.
- Test 20 concurrent downloads of one purchase (only 5 authorized); expired links, shared links, aborted connection, 100 MB ZIP, mobile.
- **Source discrepancy:** Emergent project report says Emergent Object Store has no expiring link, while official Emergent Object Store docs expressly mention pre-signed URLs; no verified object-deletion API was located. Do not treat either as validated for the specific project. Avoid the conflict by using Supabase private Storage as originally specified, subject to tests.
- Separately verify downloadable files are actual deliverables, not 20 mock product cards; store mock labels DOCX/XLSX must be corrected to PDF/PNG/JPG/ZIP.

## Membership and community requirements
- Email verification + payment verification required for member access. Active membership gates every resource/community route on server and/or Supabase RLS; default-deny to anonymous, unpaid, expired, deleted and banned users.
- $5/month automatic recurring Stripe subscriptions, test-clock renewals and failed payments, customer portal cancel preserving paid-through access. Use Stripe-owned account and own keys for portability, keep secrets only in protected environment.
- Asynchronous threads/replies, reports, rate limits, moderator hide/remove; no live chat/DM. Dashboard and self-service deletion request with identity re-verification, Stripe cancellation, personal-data cleanup and legally mandatory record retention.
- Giving ledger $1 per qualifying invoice, duplicates deduped, refund/dispute reversals, verified 501(c)(3) before quarterly transfer. Legal review must determine charitable advertising and tax treatment.

## Hosting, credits and account economics
- User's account screenshot on Monthly tab: Standard Trial **$1 for 7 days** / **100 credits**, auto-renews at **$20/mo**; Standard **$20/mo**, **100 monthly credits + 150 first-month promotional bonus**; Pro **$200/mo**, **750 monthly credits**. Free credits reportedly exhausted.
- Official fixed hosting tiers: Starter 50 cr/mo (0.05 vCPU / 200 MB, **not recommended for meaningful production**), Launch 125 (0.5 vCPU / 2GB), Grow 225 (1 vCPU / 4GB), Scale 450, Elite 1100. The hosting consumption may exceed Standard's 100 recurring credits; do not equate plan price with all-in hosting. Official legacy plan docs say topups $10 per 50 credits; confirm availability and price in user's current account before modeling.
- Illustrative recurring spend if 50-credit topup remains available and no other paid use: Standard $20 + a $10 topup can cover 125-credit Launch with 25 left; Standard $20 + $30 in topups can cover 225-credit Grow with 25 left. This is **not a quote** or usage guarantee; actual runtime, APIs and build credits additional. At meaningful load Starter may fail.
- With Supabase Pro ($25/mo) add this amount if production requires paid features. Free allows 500 MB DB, 1GB file storage and 50K MAUs but can pause after inactivity. Resend free 3,000/mo, 100/day; verify sender domain for production. Cloudflare R2 standard has 10 GB free storage and free egress; optional only.
- Stripe US standard 2.9% + $0.30 domestic card fee, plus Stripe Billing pay-as-you-go 0.7% of billing volume; confirm account and products. Gross $5 monthly membership roughly $4.52 after those fees and ~$3.52 after $1 Giving reservation, before taxes, refunds, disputes, email and hosting.
- Budget **credits**, not just dollars. Code generation, test runs, third-party tools and runtime scheduled jobs may consume credits. Keep AI runtime APIs out of v0.1.

## Portability and operational risks
- Code source can be **pushed to GitHub** on Standard+ using Save > Save to GitHub. It is not the same as Lovable's documented continuous two-way sync. Code export excludes secrets, environment values, database records and platform-managed services. No seamless production DB export/restore guaranteed.
- Emergent default shared MongoDB is isolated per app but externally inaccessible; production export not self-service per FAQ; support or migration to own DB required. Preview and production DB separate; first publish copies preview data, republish generally does not. Avoid test records migrating as real accounts.
- Emergent Auth hosted login at auth.emergentagent.com has fixed platform branding; migration of sessions/users outside platform unverified. Supabase mitigates.
- Emergent's object store portability/deletion unverified; use Supabase private storage.
- Official docs confirm routine backups but not self-serve restoration. Set and validate owned data exports/restoration. Production uptime and scheduling capabilities need tests. Published apps 24/7, previews sleep after inactivity. Use webhook retry/idempotency and reconciliation—not unreliable preview cron.
- SEO: typical Emergent React SPA may have poor per-route indexing. Its Enable SEO crawler pre-render mode exists but has redirect/404 status-code caveats and may cache outdated pages; test live deep routes or prefer app-side SSR where supported.
- Custom domain through Namecheap DNS and Emergent managed SSL documented.
- User reviews report variable quality and credit frustration; independent reviews/review aggregators are weak evidence of any individual project's reliability. Own tests trump anecdotes.
- Privacy / compliance: legal entity, privacy/terms/refund policy, charitable promotion review, moderation, retention, payment taxes and email operational setup remain outside AI builder's guarantee.

## Top blockers, ranked
1. **Production economics:** hosting tier for a real Stripe+auth+DB+download/community application; ability to fit within modest budget and reserve maintenance credits.
2. **Secure fulfillment:** real paid-only private downloads, five-use concurrent cap, recovery and product removal, no reusable public leakage.
3. **Data/control portability:** Supabase integration tested in existing Emergent project, GitHub export and independent restore/hosting; SSL/domain and transactional sender credentials.
Additional required test: identity and billing sync, webhook retries/out-of-order, moderation/account deletion, giving ledger and tax/legal.

## Recommended controlled validation (no unnecessary build credit)
1. **No-cost gate:** confirm platform's Supabase connection for *existing* project (not just new jobs) and whether full-stack app can use Supabase Auth/Storage/Edge Functions while keeping Emergent public pages. Ask support in writing whether managed MongoDB can be unused and whether project structure or build type must change; confirm actual Launch/Grow production credits on account and available topups.
2. **Decision:** Amend D035 builder to Emergent, keep Supabase as already recorded in D027/D046, only with user's explicit approval. Separate ADR for any backend substitution; do not silently change 60 decisions.
3. **Paid trial only when prepared:** Save current design to GitHub early, then implement **ONE test slice**: Supabase auth + Stripe test-mode subscription verified webhook + paid gating, with tests before additional features. Then separate store/secure delivery slice. Do not take live payments before D054 legal and functional launch gates.
4. **No production launch** until exact content inventory, security, restore, accessibility, mobile, consent, merchant, support and giving review pass.

## Source index — primary
- Emergent platform integrations catalogue: https://emergent.sh/integrations
- Emergent Supabase integration: https://emergent.sh/integrations/supabase
- Emergent integration types: https://help.emergent.sh/connect-your-tools
- Emergent curated integrations: https://help.emergent.sh/key-integrations-catalogue
- Emergent Stripe: https://help.emergent.sh/stripe
- Emergent Auth: https://help.emergent.sh/emergent-auth-built-in
- Emergent Auth alternates: https://help.emergent.sh/add-login-user-accounts
- Emergent Resend: https://help.emergent.sh/resend
- Emergent Object Store: https://help.emergent.sh/file-storage-emergent-object-store
- Emergent MongoDB / preview-prod / exports: https://help.emergent.sh/database-mongodb
- Emergent FAQ GitHub and production DB export: https://help.emergent.sh/faqs
- Emergent ownership and backups: https://help.emergent.sh/your-data-ownership
- Emergent deployment tiers: https://help.emergent.sh/deployment-plan-levels
- Emergent monthly credits/usage: https://help.emergent.sh/managing-credit-usage
- Emergent published app: https://help.emergent.sh/deploying-web
- Emergent SEO pre-rendering: https://help.emergent.sh/enable-seo-crawler-pre-rendering
- Stripe US pricing: https://stripe.com/pricing
- Stripe Billing pricing: https://stripe.com/billing/pricing
- Supabase pricing: https://supabase.com/pricing
- Supabase private storage: https://supabase.com/docs/guides/storage/serving/downloads
- Resend pricing: https://resend.com/pricing
- Cloudflare R2 pricing: https://developers.cloudflare.com/r2/pricing/

**Final verdict:** **Conditional GO for Emergent as Lovable replacement builder, especially with preserved Supabase backend; NO claim of proven end-to-end v0.1 until the tests above pass.** Builder choice is a separate explicit decision from backend architecture.

## First-party support response: received 2026-11-07 20:46 UTC
**Source:** Direct support reply in Gmail thread subject “ForFathers.com — Existing project Supabase/Stripe compatibility and hosting cost questions”. Specific project **not** inspected by support because inquiry was not sent from the email registered on Emergent account; reply from that account for project review. These are platform-general assertions, not tests.

**Supabase on the existing project:** Existing five-page UI need not be recreated. Existing project's template is fixed; only deployable backends are Python FastAPI and NextJS. Supabase Postgres/RLS and Supabase Auth supported; use SUPABASE_URL, SUPABASE_ANON_KEY, SUPABASE_SERVICE_ROLE_KEY in server-controlled environment. Supabase private Storage and Edge Functions **NOT DOCUMENTED** by support; explicit direct integration tests required. MongoDB provisioned by default even if application data are stored in Supabase; production MongoDB created upon first publish. Preview and prod environment secrets are distinct; configure prod under Manage Publishes > Secrets.

**Stripe:** Own account test/live keys, one-time Checkout, recurring subscriptions, webhooks and billing portal supported. Stripe webhook endpoint must target deployed URL, not sleeping preview. No documented hard limits to routes/webhooks, but heavy jobs advised outside app. Test signed webhook, out-of-order and duplicate event recovery and membership entitlements.

**Hosting:** 50 to 1,100 deployment credits/month, exact tier shown in deployment panel. Deployment debits the same credit balance as plan allocation. Starter and Launch can scale to zero, so in-process scheduled tasks do not run when dormant. Grow+ two always-on instances and less single-instance risk. Monthly subscription credits do not roll over; purchased credits never expire. Current top-up packages (reported): $50/250 credits, $100/500, $500/2500+, $1000/5000+, $2000/10000+, and custom amounts; checkout governs actual price. This **supersedes** earlier speculative “$10 for 50 credits” top-up availability; custom minimum unknown. Standard plan screenshot: $20/mo for 100 monthly credits, Standard Trial $1/7 days /100 credits, auto-renewal $20/mo. Launch hosting 125 credits needs 25 above monthly recurring Standard credits even without build usage; Grow 225 needs 125 extra. This is ~ $5 or $25 in *credits* at quoted 20c/credit, but topup purchase increments and available credits/cost can make paid upfront amount greater. Do not claim fixed cash hosting price without account checkout.

**Trial and cancellation:** Standard trial eligibility varies; Standard features and GitHub push permitted. Support says deployment during trial is free until end of trial, but exact future deployment charge must be confirmed in project panel. Nonrenewal reverts to Free, retains code/projects, private projects inaccessible until resubscribe, live deployments offline unless positive top-up credit balance, subscription credits zero. Warn against triggering a live launch or seven-day autorenewal without budget decision.

**GitHub/portability:** Save to GitHub (paid) is push-only, one GitHub account per project; code, configuration and package files included; secrets/env vars, node_modules and DB records excluded; >100 MB files rejected; secrets in history block push. Can externally host exported code, while owned Stripe/Supabase accounts persist. MongoDB data via mongodump and MONGO_URL, if utilized. Independent hosting and restoring secrets/routing/webhooks still require smoke tests.

**Decision impact:** D035 remains Lovable until user explicitly approves change. D027/D046 explicitly Supabase can be preserved (no need to amend for MongoDB). Strongest next test: existing Emergent project's full Supabase integration incl. private Storage + Edge Functions, without damaging frontend, and narrow no-production-payment slice. For project-specific confirmation contact Emergent support from account-registered email, or verify with an authenticated account support ticket. No paid action until trial/payment authorization.
