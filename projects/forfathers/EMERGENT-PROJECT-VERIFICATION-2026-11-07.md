# ForFathers — Project-specific Emergent support inspection
**Date:** 2026-11-07
**Project:** fathers-together
**Job ID:** b0ebcbac-9fca-4c3f-89e5-363af17c9114
**Source:** Support reply shared by user; no changes made during inspection.
**Verdict:** Conditional GO for Emergent builder with existing Supabase+Stripe architecture; NOT an operational validation, implementation authorization or production approval.
**Canonical decision status:** D035 still Lovable, pending explicit user approval; D027/D046 remain Supabase/Stripe.

## Confirmed specifically by support
- Five pages: Home, Brotherhood, Resources, Store, Cohort. Frontend content currently in a **local data file**; buy buttons, Cohort form and members-only functionality are placeholders. Client-shipped local content is visible to every visitor and is **not** private.
- Current application already includes FastAPI backend, originally MongoDB template. Supabase Auth, Postgres/RLS and private Storage can be integrated while keeping existing UI. Edge Functions are executed/deployed at Supabase rather than inside Emergent project; not necessary for architecture.
- Production API routes need `/api` prefix; example `/api/webhooks/stripe`. Stripe secret and Supabase service role key only in backend/prod secrets (never `VITE_*`/frontend). Deploy webhook URL, not preview. Add stripe Python package explicitly in `requirements.txt`.
- Current FastAPI startup expects MongoDB environment; preserve as necessary for boot until validated, while routing *application* data to Supabase. Restrict CORS origins to production domain.
- Publishing tiers listed: Starter, Launch, Grow, Scale, Elite; support states Starter 512 MB, **conflicts with public official documentation (200 MB, 0.05 vCPU, 50 credits)** at https://help.emergent.sh/deployment-plan-levels (checked 2026-11-07). Verify account-specific Resources screen before selecting tier. Launch 2GB, Grow 4GB. Minimum 50 credits to publish. Scale gradually based on actual measured memory and error rates.

## Red-team — why support's proposed example is INCOMPLETE
- Example secure download endpoint checks member Supabase login + subscription. D019–D027 require **guest digital products**, Stripe Checkout and post-payment order entitlements, including recovery via verified email token without forcing membership.
- Five-download cap **per purchased item**, concurrency-safe and atomic, not implemented by a signed URL alone. Supabase signed Storage URLs are usable repeatedly until expiry; user-defined issuance counter and support recovery needed, with explicit count/retry semantics. Source https://supabase.com/docs/guides/storage/serving/downloads.
- Supabase's current CDN docs note caches may serve signed URLs after expiration until cacheControl TTL. Therefore zero-cache or proxy and tests needed if hard five-transfer limit; do not claim signed URL alone is one-time. Source https://supabase.com/docs/guides/storage/cdn/smart-cdn.
- Stripe webhooks must verify signed events, deduplicate and withstand out-of-order deliveries; membership entitlements must reflect paid-through and verified invoice, not redirects. Differentiate subscription entitlements from guest product purchases.
- Private Resource Library must move full paid content *out of public local data*; ensure public metadata only remains, private files/tables in RLS-protected Supabase.
- Startup MongoDB dependency is a technical maintenance risk: agent must not quietly persist business data in two stores; test cold deploy after connection changes.
- Code export, runtime resource consumption, hosted DNS and recoverable backup remain launch gates. Not tested.

## Recommendation and sequencing
1. User approval for D035 amendment to Emergent as **builder only**, preserving Supabase/Stripe decisions and frontend design; record explicit rationale (working five-page visual implementation, project-specific support confirmation) and risks (hosting credit, backend template, signed URL, portability) separately.
2. On next paid trial with user authorization: export existing code to GitHub before major backend changes. Implement **only** Supabase Auth/Postgres/RLS connectivity and protected paid sample with two identities, with backend secrets and verified public/private data isolation. No Stripe or downloads in this same slice.
3. Next controlled slice: Stripe test-mode $5 subscription + verified webhook + period-end access; fail/replay tests.
4. Next controlled slice: Stripe guest $3/$5 purchase, order entitlement, private signed URLs/proxy, concurrency-safe five-use counter and emailed recovery.
5. Community, Giving Fund (legal blocked), consented Cohort interest, content and full D054 gates follow; no full Cohort marketplace.

**No code or decision register changed during this note.**
