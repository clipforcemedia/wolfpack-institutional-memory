# ForFathers — v0.1 Decision Register

**Recorded:** 2026-11-06  
**Status:** Planning; decisions below are not implementation approvals.  
**Purpose:** Complete mental/product decisions before execution; preserve scope lock.  
**Business entity:** Ohio LLC preferred, not yet formed; Delaware LLC resolution separate.  
**Domain:** ForFathers.com owned; DNS not configured.

**Legend:** LOCKED = recorded decision; LOCKED — CONDITIONAL / PROVISIONAL = recorded direction requiring validation before implementation or public commitment; amendments are documented in the decision log. All 60 canonical decisions have recorded positions; this is not production approval.

## Business Model & Positioning

| # | Decision | Status | Current position |
|---:|---|---|---|
| 1 | Primary target audience | LOCKED | Fathers first, all men welcome |
| 2 | Core problem ForFathers solves | LOCKED | Lack of support and opportunity; brotherhood, practical resources, mutual assistance |
| 3 | Mission statement | LOCKED | To bring men together through brotherhood, providing the support, resources, and opportunities to help one another build better lives. |
| 4 | Brand positioning and tone | LOCKED | Strong brotherhood + genuine support: confident, purposeful, welcoming, nonjudgmental |
| 5 | Membership price | LOCKED | $5/month |
| 6 | Membership name | LOCKED | The Brotherhood |
| 7 | Membership benefits | LOCKED | Resource Library plus members-only discussion community; simple asynchronous format, no live chat |
| 8 | Free visitor benefits | LOCKED | Public website and Digital Store browsing plus three free sample resources; community private |
| 9 | Annual membership option | LOCKED | Monthly only at $5/month; no annual subscription for v0.1 |
| 10 | Cancellation and refund policy | LOCKED — subject to legal/provider review | Cancel anytime; access through paid period; generally no refunds except where required by law or payment-provider rules |

## Resource Library

| # | Decision | Status | Current position |
|---:|---|---|---|
| 11 | Resource categories | LOCKED | Five: Fatherhood & Family; Career & Income; Financial Stability; Mental & Physical Wellness; Life Skills & Personal Growth |
| 12 | Types of resources | LOCKED | Written guides, checklists, worksheets, templates plus 1–2 simple interactive tools; no AI apps or video production in v0.1 |
| 13 | Minimum launch inventory | LOCKED | 20 written resources (4 per category, including 3 free samples) plus 2 interactive tools = 22 total |
| 14 | Resource quality standards | LOCKED | Practical Value Standard: specific problem, actionable guidance, fact-checking, examples where useful, clarity and limitations review |
| 15 | Content creation process | LOCKED | AI-assisted research and drafting, human verification, AI formatting, owner approval before publication |
| 16 | Content update frequency | LOCKED | Four new resources per month (target one per week); internal target, not a public guarantee |
| 17 | Member content requests | LOCKED | Members submit resource suggestions through simple form; editorial team selects what to create; no fulfillment guarantee |
| 18 | Free versus paid resource access | LOCKED | Three public sample resources; remaining library members-only; active members download at no extra charge; access ends after paid period |

## Digital Store

| # | Decision | Status | Current position |
|---:|---|---|---|
| 19 | Maximum product price | LOCKED | $5 maximum |
| 20 | Initial product categories | LOCKED | Practical digital products plus inspirational and creative products: planners, templates, printable art, wallpapers, cards |
| 21 | Initial product quantity | LOCKED | 20 products at launch: 10 practical digital products and 10 inspirational/creative products |
| 22 | Individual product pricing | LOCKED | Two price points: $3 standard individual products; $5 premium products and bundles; subject to payment fee verification |
| 23 | Product file formats | LOCKED | PDF for planners/printables; PNG/JPG for artwork and wallpapers; ZIP for multi-file bundles; no editable source templates in v0.1 |
| 24 | Product licensing | LOCKED | Personal-use license only; personal downloads, prints and device wallpapers allowed; resale, redistribution, attribution claims and commercial use prohibited; clear pre-purchase disclosure |
| 25 | Brotherhood member discounts | LOCKED | No member discounts in v0.1; everyone pays the same $3 or $5 store price |
| 26 | Refund policy | LOCKED | No discretionary refunds after successful download, except where required by law or payment-provider rules; remedy defective/non-delivered products |
| 27 | Download limits | LOCKED — AMENDED | Five downloads per digital purchase, enforced by minimal server-side Supabase purchase counter with private storage and short-lived authorized download grants; support recovery |

## Charitable Commitment

| # | Decision | Status | Current position |
|---:|---|---|---|
| 28 | Amount reserved per membership payment | LOCKED | $1 per successful $5 membership payment |
| 29 | Type of charitable organization | LOCKED | Verified U.S. IRS-recognized 501(c)(3) charities only; partner not yet selected |
| 30 | Charity selection criteria | LOCKED | Verified 501(c)(3); aligned with fathers, men, families or community needs; financial transparency; verifiable operating history; legitimate donation channel |
| 31 | Donation transfer frequency | LOCKED | Quarterly transfers of accumulated Giving Fund reserves to verified selected charity; reconcile before disbursement |
| 32 | Public donation reporting | LOCKED | Publish quarterly giving reports after each transfer: eligible membership payments, amount transferred, charity/mission, transfer date and confirmation; distinguish reserved from donated |
| 33 | Refund and chargeback adjustments | LOCKED | Reverse $1 giving allocation for refunded/charged-back membership payments before quarterly transfer; post-transfer reversals reconciled in next period without clawback from charity |
| 34 | Public charitable commitment wording | LOCKED | For every qualifying $5 Brotherhood membership payment, reserve $1 for charitable giving; donate quarterly to verified 501(c)(3) charities; publish reports; legal review before publication |

## Website & User Experience

| # | Decision | Status | Current position |
|---:|---|---|---|
| 35 | Website builder | LOCKED | Lovable |
| 36 | Main navigation | LOCKED | Five core pages: Home, Brotherhood, Resource Library, Digital Store, The Cohort |
| 37 | Homepage layout | LOCKED | Complete platform overview: mission hero, Brotherhood, Resource Library, Digital Store, Cohort coming soon, Giving Fund, final signup; membership primary CTA |
| 38 | Visual identity | LOCKED | Warm Brotherhood: deep navy and charcoal, warm cream, muted copper/bronze accents, strong approachable typography, authentic father/family/brotherhood imagery |
| 39 | Primary call to action | LOCKED | Join The Brotherhood — $5/Month; dominant homepage CTA directs to membership signup; browsing remains accessible |
| 40 | Membership signup flow | LOCKED | Combined account signup and hosted $5/month subscription checkout; email verification; membership access only after verified successful payment |
| 41 | Member dashboard requirements | LOCKED | Functional dashboard: welcome, membership status, Resource Library shortcuts, recent discussions, Digital Store shortcut, account/billing settings |
| 42 | Resource Library navigation | LOCKED | Five-category browsing, basic title/keyword search, category filtering, and resource descriptions; no AI discovery in v0.1 |
| 43 | Store browsing experience | LOCKED | Simple 20-product grid with thumbnail, name, $3/$5 price and purchase button; defer categories, dedicated product pages and advanced commerce until post-v0.1 |
| 44 | Mobile design priorities | LOCKED | Mobile-first responsive website adapted for tablet and desktop; one codebase, no separate mobile app in v0.1 |
| 45 | Accessibility requirements | LOCKED | Target WCAG 2.2 Level AA; accessible components, keyboard navigation, contrast, focus, forms, screen-reader semantics and touch targets; test before any conformance claim |

## Payments & Operations

| # | Decision | Status | Current position |
|---:|---|---|---|
| 46 | Payment processor | LOCKED — CONDITIONAL | Stripe for subscriptions and digital purchases; Lovable front end and Supabase secure fulfillment; production gated on integration, legal and tax verification |
| 47 | Merchant-of-record preference | LOCKED | ForFathers is seller of record using Stripe; responsible for applicable tax registrations, collection, filings, refunds and compliance; validate before launch |
| 48 | Subscription billing rules | LOCKED | $5 charged at signup, automatic monthly renewal, no trial/intro discount, cancel anytime with access through paid period; verified billing state governs access |
| 49 | Accepted payment methods | LOCKED | Major credit/debit cards plus Apple Pay and Google Pay where supported by Stripe Checkout, device, region and subscription/payment type |
| 50 | Customer support channel | LOCKED | Dedicated ForFathers support email only for v0.1; no live chat or contact form |
| 51 | Support response target | LOCKED | Aim to respond to support emails within 24 calendar hours; internal operational target, not guaranteed SLA |
| 52 | Member account deletion process | LOCKED | Self-service deletion request in account settings, identity re-verification, coordinated Stripe subscription cancellation, access revocation and eligible data deletion/anonymization; legally required records retained |
| 53 | Basic analytics and success metrics | LOCKED | Essential aggregate business metrics: website visitors, membership signups/cancellations, active paying members, MRR, digital product sales, payment failures |
| 54 | Launch criteria | LOCKED | Controlled production launch only after functional, legal/tax, security, billing, digital delivery, support, mobile, monitoring/backup, and accessibility gates pass |

## The Cohort — Future Marketplace

| # | Decision | Status | Current position |
|---:|---|---|---|
| 55 | Marketplace purpose | LOCKED | Men helping men |
| 56 | Commission | LOCKED — PROVISIONAL RATE | Plan for 5% platform commission on completed Cohort transactions; not public or operational until payment economics and compliance validated |
| 57 | Initial service categories | LOCKED | Future Cohort: career/employment, business/entrepreneurship, technology/digital services, home maintenance/practical skills, personal development/mentorship |
| 58 | Geographic scope | LOCKED | Future Cohort marketplace launches United States only; no international marketplace transactions in initial release |
| 59 | Interest signup questions | LOCKED | Cohort Coming Soon interest form: email, intent (offer services / hire / both), primary service category; clear opt-in and privacy notice |
| 60 | Marketplace launch trigger | LOCKED | Founder discretion to initiate future Cohort development, subject to documented go/no-go review and v0.1 operational stability; no automatic milestone |

## v0.1 Scope Guardrails

- One Brotherhood tier at $5/month, billed monthly only; no annual plan, trial or introductory discount in v0.1 (D005, D009, D048).
- Resource Library: 20 written resources across five categories, including three free public samples, plus two simple interactive tools; remaining library content available to active paying members (D011–D018).
- Members-only asynchronous discussion community; no live chat, private messaging or advanced social features (D007).
- Digital Store: 20 digital-only products at $3/$5, personal-use licensing, no member discounts, guest checkout, secure delivery and five downloads per purchase using the D027 amendment; no shipping or manual fulfillment (D019–D027, D046).
- Stripe handles payments; Lovable is the web frontend; Supabase manages authenticated data, entitlements and secure digital delivery. Architecture is conditional on integration, provider and compliance verification (D046–D049).
- Giving Fund: reserve $1 per qualifying successful $5 membership payment, adjust for refunds/chargebacks, transfer quarterly to a verified U.S. 501(c)(3), and report quarterly; specific recipient not yet selected, and public wording requires legal review (D028–D034). Do not claim customer tax deductibility.
- The Cohort: Coming Soon description and consented interest signup only. **No marketplace transactions, provider onboarding, payouts or disputes in v0.1.** Future 5% fee remains provisional (D055–D060).
- Support via dedicated domain email, internal target to respond within 24 calendar hours (D050–D051).
- Do not accept payments until legal entity, Stripe onboarding, tax treatment, consumer/charity policies and end-to-end flows are verified (D054).
- Avoid feature additions without an explicit decision-log/ADR entry covering rationale, risks, cost and v0.1 impact.

## Decision Sessions

1. Identity and audience (decisions 1–4)
2. Membership and resources (5–18)
3. Digital Store (19–27)
4. Charitable commitment (28–34)
5. Website experience (35–45)
6. Payments and operations (46–54)
7. The Cohort (55–60)

## Execution Checklist

- [x] Inventory 60 decisions and record known positions
- [x] Resolve all 60 canonical decisions in sessions 1–7
- [x] Red-team decision register and record findings in V0.1-ARCHITECTURE-AUDIT.md (implementation/legal verification still outstanding)
- [x] Lock v0.1 scope and controlled-launch acceptance criteria (D054; validation still outstanding)
- [ ] Verify payment provider, taxes, charity partner, and integrations externally
- [ ] Resolve Ohio/Delaware entity matters separately
- [ ] Build and test Lovable v0.1
- [ ] Launch only after checkout, access, cancellation, digital delivery and support checks pass

## Current Execution Queue

**Decision phase complete:** All 60 canonical decisions recorded. Some choices remain conditional on verification; no production launch approval.

1. Correct documentation drift and reconcile D027 with D046 (completed 2026-11-07).
2. Define implementation specification and testable acceptance criteria without expanding scope.
3. Verify entity, Stripe onboarding, taxes, charitable-giving disclosures, product rights and consumer policies.
4. Build and test controlled v0.1; activate real payments only after D054 gates pass.

## Decision Log

- **2026-11-07 — D001: Audience.** Approved option C: *Fathers first, all men welcome*. Rationale: focus initial outreach without excluding men who are not fathers. Risk: brand name could imply father-only eligibility; countermeasure: explicitly communicate inclusive membership eligibility in homepage copy. No change to v0.1 feature scope.

- **2026-11-07 — D002: Core problem.** Approved option C: men face gaps in both support and opportunity. ForFathers will address these through brotherhood, practical resources and opportunities for mutual assistance. Risk: too broad for a credible v0.1 promise; mitigation: lead with one concrete benefit and defer transactional marketplace features to post-v0.1. No feature expansion authorized.

- **2026-11-07 — D003: Mission statement.** Approved option C verbatim: “To bring men together through brotherhood, providing the support, resources, and opportunities to help one another build better lives.” Rationale: aligns with D001 inclusive audience and D002 support plus opportunity. Risk: broad promise; mitigation: define specific v0.1 benefits and measurable launch criteria. No feature expansion authorized.

- **2026-11-07 — D004: Brand positioning and tone.** Approved option C: strong brotherhood plus genuine support. Principles: strength without arrogance; accountability without humiliation; support without judgment; brotherhood without exclusion; action over empty motivation. Risk: masculine branding may be perceived as exclusionary; mitigation: welcoming copy and clear eligibility. No feature expansion authorized.

- **2026-11-07 — D007: Membership benefits.** Approved option B: access to Resource Library plus members-only discussion community. Rationale: recurring member value beyond static downloads. Risk: moderation workload, spam, harassment, and empty-community experience; mitigation: simple asynchronous discussions, clear rules, reporting and moderation controls before launch. No live chat or advanced social features in v0.1. Community implementation and staffing remain subject to feasibility and launch criteria.

- **2026-11-07 — D008: Free visitor benefits.** Approved option B: public website, Digital Store browsing, and three free sample resources demonstrating membership value. Community discussions remain members-only. Risk: samples may not demonstrate value; mitigation: select representative, high-quality resources and track visitor-to-member conversion. No free community access authorized.

- **2026-11-07 — D009: Annual membership.** Approved option A: monthly billing only at $5/month for v0.1. Rationale: minimize billing complexity and validate retention before considering annual pricing. Tradeoff: no annual prepayment or long-term commitment. Annual plans are explicitly out of scope for v0.1.

- **2026-11-07 — D010: Membership cancellation/refunds.** Approved option A: cancel anytime; membership access continues through the paid billing period; payments generally nonrefundable. Mandatory exceptions apply where law or payment-provider rules require refunds. Must verify cancellation UX, disclosures, applicable automatic-renewal rules, and refund terms before checkout goes live. Rationale: minimal operating complexity. Risk: disputes and dissatisfaction; mitigation: conspicuous pre-purchase terms and easy self-service cancellation. No launch authorization until compliance review.

- **2026-11-07 — D011: Resource Library categories.** Approved option A: five categories — Fatherhood & Family, Career & Income, Financial Stability, Mental & Physical Wellness, Life Skills & Personal Growth. Rationale: broad enough for the inclusive audience with manageable navigation. Risk: thin launch inventory across five categories; mitigation: set a minimum content inventory and quality standard before launch. No additional categories authorized for v0.1.

- **2026-11-07 — D012: Resource formats.** Approved option B: written resources (guides, checklists, worksheets, templates) plus simple interactive tools. Limit v0.1 to one or two tools; no complex AI apps or video lesson production. Rationale: actionable member value. Risk: implementation/testing overhead; mitigation: prioritize calculators or planners that require no external API or persistent sensitive data. Tool selection remains open under inventory planning.

- **2026-11-07 — D013: Minimum launch inventory.** Approved option B: 20 written resources (four per each of five categories), plus two simple interactive tools, for 22 total assets; three free samples are included in the 20 written resources, not additional. Rationale: substantial starting value at $5/month. Risk: content production delays launch; mitigation: reusable templates and explicit quality gates. This is the approved minimum; any reduction requires a new decision.

- **2026-11-07 — D014: Resource quality.** Approved option B: each resource addresses a specific real-world problem, provides actionable steps or tools, checks consequential factual claims against reliable sources, includes examples/templates where appropriate, receives clarity/accuracy/usefulness review, and identifies limitations. Medical, legal, or individualized financial advice must not be presented as professionally validated; high-risk topics require qualified review or exclusion. Rationale: useful, credible assets without universal expert-review costs. Risk: unverified AI content; mitigation: documented source and review checklist before publication.

- **2026-11-07 — D015: Content production.** Approved option B: select a real problem; use AI for research/drafting; verify consequential claims and practical utility; use AI to format; owner approves before publication. Rationale: low-cost production with human editorial accountability. Risks: hallucinated sources and approval bottlenecks; mitigation: source verification and documented approval checklist. No content auto-publishing in v0.1.

- **2026-11-07 — D016: Resource update cadence.** Approved option B: target four new resources monthly, approximately one per week. Rationale: consistent library growth. Risks: production capacity and quality erosion; mitigation: maintain an editorial backlog, enforce D014 quality checks, and avoid public guarantees until the cadence is demonstrated. This is an internal operational target, not a subscriber entitlement.

- **2026-11-07 — D017: Member content requests.** Approved option B: members may submit resource ideas through a simple form; the project reviews and selects ideas at its discretion. No guaranteed fulfillment, voting system, or new moderation-heavy features. Rationale: demand signals with minimal implementation. Risk: unrealistic member expectations; mitigation: state clearly that suggestions are not requests with guaranteed delivery.

- **2026-11-07 — D018: Resource access.** Approved option A: three free public samples; remaining Resource Library restricted to active Brotherhood members, with no extra download charge. Cancellation leaves access through the paid billing period, then gated access ends. Digital Store remains separate. Risk: previously downloaded files cannot realistically be revoked; mitigate by describing the expiration as access to the online library, not deletion of previously downloaded copies. No per-resource purchases in v0.1.

- **2026-11-07 — D020: Digital Store categories.** Approved option C: both practical digital products (planners, organizers, budgeting, parenting and productivity templates) and inspirational/creative products (wall art, wallpapers, printable posters and digital greeting cards). Rationale: broader range of low-cost standalone purchases. Risks: duplicate value with paid Resource Library and excessive SKU sprawl; mitigation: differentiate store products from included member resources and cap launch inventory in D021. All products digital-only and $5 or less; no physical fulfillment.

- **2026-11-07 — D021: Initial Digital Store inventory.** Approved option B: 20 launch products, split evenly between 10 practical products and 10 inspirational/creative products. Rationale: credible range without extensive catalog. Risk: production delays and low-value filler; mitigation: enforce quality gates and validate checkout and delivery before launch. Any inventory reduction requires explicit scope revision.

- **2026-11-07 — D022: Digital Store pricing.** Approved option C: two price points, $3 for standard individual products and $5 for premium products/bundles. Rationale: simpler pricing and potentially healthier per-order economics than $1 downloads. Risks: processor fixed fees and taxes may still make low-value transactions unprofitable; mitigation: verify provider fees and tax treatment before checkout activation. Maximum price remains $5.

- **2026-11-07 — D023: Digital product file formats.** Approved option B: PDF, PNG/JPG, and ZIP bundles. Rationale: covers printables and image products with simple download delivery. Risks: large files, incompatible dimensions, and ZIP extraction friction; mitigation: publish file type and size before purchase, test downloads on mobile/desktop, and use appropriate export dimensions. Editable DOCX/XLSX/Canva source templates are out of scope for v0.1.

- **2026-11-07 — D024: Digital product licensing.** Approved option A: personal-use-only license for digital products. Buyers may download and personally use files, print personal copies, and apply wallpapers to their own devices. Resale, redistribution, false authorship claims and commercial use are not permitted. Rationale: clear, minimal license for v0.1. Risks: unclear terms and third-party asset rights; mitigation: disclose license before checkout, verify rights to all included assets, and obtain legal review of final terms. This license does not override mandatory consumer rights.

- **2026-11-07 — D025: Brotherhood member discounts.** Approved option B: active Brotherhood members receive a 20% discount on all Digital Store purchases ($3 standard → $2.40; $5 premium → $4.00). Rationale: tangible membership benefit while preserving most revenue. Risks: checkout complexity, discount abuse, and transaction fees; mitigation: require verified active membership, automatic application, server-side enforcement, and payment-fee validation before launch. If chosen provider cannot support this reliably, return for explicit scope/decision revision rather than silently shipping an insecure workaround.

- **2026-11-07 — D025: Brotherhood member discounts.** Approved option A: no Digital Store discounts for Brotherhood members in v0.1. Members and nonmembers pay identical $3/$5 product prices. Rationale: simplest checkout, avoids subscription-status pricing integration and preserves per-sale economics. Risk: weaker incremental membership incentive; mitigation: differentiate membership through the gated Resource Library and community. Discount experiments require a later decision.

- **2026-11-07 — D026: Digital product delivery.** Approved option A: show immediate download access after confirmed successful payment and email a secure download link; guest checkout without a required account for one-time purchases. Rationale: lower checkout friction and two access paths. Risks: forged payment-success redirects, link sharing, expired links, and email delivery failures. Mitigation: fulfillment only after server-verified payment event, provider-managed expiring download links, delivery testing, and support recovery path. Confirm actual provider features before implementation; no custom delivery infrastructure unless required by a separate decision.

- **2026-11-07 — Register correction: D026 was mislabeled in conversation.** Original canonical #26 is Digital Store refund policy, not delivery. The approved immediate-download-plus-email delivery choice is retained as **D025a (supplemental implementation constraint)**, not counted as one of the 60 decisions. #26 remains OPEN pending explicit user selection. Secure delivery must be verified against provider capabilities.

- **2026-11-07 — D026: Digital Store refunds.** Approved option A: generally no discretionary refunds after a digital product has been downloaded, subject to applicable consumer law and payment-provider rules. Rationale: discourages download-then-refund abuse on low-priced files. Risks: customer dissatisfaction, chargebacks, and unenforceable blanket exclusions. Mitigation: disclose policy before purchase; provide working-file replacement and appropriate remedies for defective, misdescribed, duplicate-charged or undelivered purchases; legal/provider review before launch. Do not imply statutory rights are waived.

- **2026-11-07 — D027: Digital Store download limits.** Approved option B: five downloads per purchase. Rationale: balances customer convenience and link-sharing exposure. Risks: legitimate customers exhaust allowance, download links forwarded, and delivery-provider feature gaps. Mitigation: offer support-assisted recovery, use secure provider-managed links, verify provider support before checkout; do not build custom download tracking for v0.1. If provider cannot enforce the cap natively, revisit this decision before launch.

- **2026-11-07 — D029: Giving Fund recipient organization type.** Approved option A: disburse Giving Fund reserves only to verified U.S. IRS-recognized 501(c)(3) charities. Rationale: simpler eligibility verification and clearer accountability. Risks: excludes informal community efforts; charity status can lapse; and reserving membership revenue does not create a tax-deductible customer donation. Mitigation: check IRS Tax Exempt Organization Search and recipient standing before disbursement; separately decide charity-selection criteria, payout cadence, disclosures and bookkeeping. No direct individual grants in v0.1.

- **2026-11-07 — D030: Charity selection criteria.** Approved option B: require verified 501(c)(3) status, mission alignment with fathers/men/families or related community needs, financial transparency, verifiable operating history, and legitimate donation channel. Rationale: defensible recipient selection without extensive audit overhead. Risks: small/new organizations excluded and published financial information may be incomplete; mitigation: document evidence and review status and donation details before disbursement. No charity selected by this decision.

- **2026-11-07 — D031: Giving Fund transfer cadence.** Approved option B: quarterly disbursement of accumulated $1-per-successful-$5-membership-payment reserves to a verified selected 501(c)(3). Rationale: fewer transactions and straightforward reconciliation. Risks: delayed impact, unremitted balances, refunds/chargebacks and cash shortfalls; mitigation: track a dedicated giving liability/reserve ledger, reconcile successful net-eligible payments and reversals, publish timing accurately, and confirm recipient eligibility and transfer records before disbursement. No claim that funds are donated until transferred.

- **2026-11-07 — D032: Public Giving Fund reporting.** Approved option B: publish a quarterly report after each disbursement stating the count of qualifying membership payments, total amount actually transferred, recipient charity and mission, transfer date and confirmation. Explicitly distinguish funds reserved from funds disbursed. Rationale: transparent reporting aligned to quarterly giving cadence without a live dashboard. Risks: erroneous totals, privacy leakage, and claims unsupported by receipts; mitigation: reconcile the ledger against payment and transfer records, avoid member-identifying data, retain receipts, and publish only verified figures.

- **2026-11-07 — D033: Giving Fund reversals.** Approved option A: if a membership payment is refunded or charged back before the quarterly charity transfer, reverse its $1 Giving Fund allocation. For reversals after funds have been donated, do not claw money back from the charity; record the adjustment in the next reconciliation, with no negative disbursement. Rationale: prevents unfunded obligations and aligns public reports to net qualifying payments. Risks: accounting errors and misleading reported totals; mitigation: transaction-level ledger, reconciliations and clear disclosure of post-transfer adjustments.

- **2026-11-07 — D034: Public charitable commitment wording.** Approved option B: “For every qualifying $5 Brotherhood membership payment, ForFathers reserves $1 for charitable giving. Funds are donated quarterly to verified 501(c)(3) organizations, with public reports showing where the money goes.” Rationale: explicit amount, cadence, recipient eligibility and transparency. Risks: charitable sales-promotion/commercial co-venture regulations may apply by jurisdiction; promises can be misleading before a charity is selected or transfers are operational. Mitigation: legal/compliance review before publication, confirm partner and procedures, clarify qualifying payments and reversals, do not imply tax deductibility or that ForFathers is a charity. Treat as approved draft copy, not authorization to publish immediately.

- **2026-11-07 — D037: Member authentication.** Approved option A: email-and-password sign-up and sign-in using a managed authentication provider. Rationale: familiar account access without depending on email for every login. Risks: credential stuffing, password-reset abuse, account takeover and password support. Mitigation: provider-managed salted password hashing, email verification, secure reset flows, rate limiting and session management; never build custom password storage. Verify provider capabilities and production email delivery before launch. Social login and magic-link-only access excluded from v0.1.

- **2026-11-07 — Register numbering correction:** The email/password choice approved during the session is preserved as **supplemental authentication decision** (not counted in original 60). Canonical D037 is homepage layout and remains OPEN. Authentication implementation: managed email/password provider with verification, resets and abuse controls; no custom password storage.

- **2026-11-07 — D037: Homepage layout.** Approved option B: full platform overview with mission hero, Brotherhood membership, Resource Library preview, Digital Store preview, Cohort coming-soon teaser, Giving Fund explanation and final membership signup section. Primary conversion goal is Join The Brotherhood — $5/month. Rationale: show the complete ForFathers offering without hiding adjacent value. Risks: excessive homepage length, competing CTAs and misleading prelaunch claims; mitigation: concise sections, one dominant CTA, explicit coming-soon label, and charity copy gated on legal/operational readiness.

- **2026-11-07 — D038: Visual identity.** Approved option B, Warm Brotherhood: deep navy/charcoal, warm cream backgrounds, muted copper/bronze accents, strong approachable typography and authentic imagery of fathers, families and men supporting one another. Rationale: conveys strength, trust and belonging without aggression. Risks: generic stock-photo aesthetic, poor contrast and inconsistent design. Mitigation: accessible contrast checks, a small tokenized palette/type scale and imagery standards; avoid expanding into a complex design system before v0.1.

- **2026-11-07 — D039: Primary homepage call to action.** Approved option A: “Join The Brotherhood — $5/Month” is the dominant homepage CTA, directing visitors toward membership registration. Rationale: clear value proposition and subscription conversion path. Risks: first-time visitors may hesitate; mitigate with concise benefits, transparent pricing, and public browsing of free samples and Digital Store. No live payment activation before legal, processor, tax, policy and integration checks are complete.

- **2026-11-07 — D040: Membership signup flow.** Approved option C: enter email and create password, complete hosted $5/month subscription checkout, verify email, then access Brotherhood. Rationale: streamlined registration while maintaining account identity. Risks: abandoned checkouts, orphan accounts, duplicate subscriptions, missed webhook events, and unauthorized access. Mitigation: managed authentication, hosted payment checkout, idempotent payment-event handling, recovery for incomplete registrations, and entitlement only after server-verified successful subscription payment and required verification. No custom card collection; payment activation remains blocked pending legal, tax, provider and policy checks.

- **2026-11-07 — D041: Member dashboard.** Approved option B: functional member dashboard with welcome message, membership status, Resource Library shortcuts, recent community discussions, Digital Store shortcut, and account/billing settings. Rationale: useful navigation hub without gamification. Risks: extra cross-component integration, stale subscription status and privacy leakage. Mitigation: reuse existing membership entitlements and discussion queries, use provider-hosted billing portal where supported, show only authorized data, and omit personalization, badges and reputation scores in v0.1.

- **2026-11-07 — D042: Resource Library navigation.** Approved option B: browse the five categories, search by resource title/keywords, filter by category, and read descriptions before accessing resources. Rationale: straightforward discovery for 22 launch assets. Risks: search quality and inadvertent exposure of members-only content; mitigation: simple indexed/metadata search with permission-enforced downloads, mobile testing, and no personalized recommendations, favorites, popularity rankings or AI search in v0.1.

- **2026-11-07 — D043: Digital Store browsing.** Approved option A with explicit upgrade-later constraint: a simple grid of 20 products displaying thumbnail, product name, $3/$5 price and purchase button. Rationale: quickest usable storefront with minimum implementation complexity. Risks: insufficient pre-purchase details (license, format, product contents), accessibility and conversion. Mitigation: show concise descriptions and required license/file-format disclosures via lightweight product detail panel or checkout disclosure, without building dedicated product pages; test guest checkout and digital fulfillment. Category browsing, individual PDPs, reviews, cart and advanced filtering are deferred until validated demand and a new decision.

- **2026-11-07 — D044: Mobile design priorities.** Approved option A: design mobile-first, then adapt one responsive site for tablet and desktop. Rationale: prioritize essential content, navigation and checkout while limiting implementation complexity. Risks: desktop layout neglect, cramped mobile controls and slow loading; mitigation: responsive breakpoint testing, accessible tap targets, mobile checkout and download tests, and desktop QA. No native mobile app or separate mobile codebase in v0.1.

- **2026-11-07 — D045: Accessibility requirements.** Approved option B: target WCAG 2.2 Level AA for the responsive ForFathers website. Rationale: measurable accessibility baseline and broader usability. Risks: untested third-party checkout/widgets, design contrast failures, keyboard traps, and misleading compliance claims. Mitigation: select accessible components, test keyboard and screen-reader flows, forms, focus states, touch targets, mobile checkout, and remediate failures; do not claim conformance without evaluation. No blanket AAA requirement in v0.1.

- **2026-11-07 — D046: Payment processor and fulfillment architecture.** Approved Stripe for $5/month Brotherhood subscriptions and $3/$5 Digital Store purchases, with Lovable as the website and Supabase as the purchase/entitlement and secure-file-delivery backend. **Conditional architecture lock, not production approval.** Rationale: unified payment provider and direct on-site digital fulfillment. Risks: custom secure download handling and five-download enforcement, webhook reliability, tax obligations, and provider/account eligibility. Mitigation: server-verified Stripe webhook events with idempotent fulfillment, private storage and expiring signed URLs, purchase-level download counters, email link recovery, subscription cancellation testing, and legal/tax/processor verification. Do not activate live checkout until all tests and compliance gates pass. Do not assume Stripe provides file hosting or delivery natively.

- **2026-11-07 — D047: Seller/merchant-of-record arrangement.** Approved option A: ForFathers acts as seller of record for Brotherhood subscriptions and Digital Store transactions processed by Stripe. Rationale: one provider and direct customer/payment control consistent with D046. Risks: sales tax and other indirect-tax nexus/registration, collection and remittance obligations, product taxability, and chargeback/refund compliance. Mitigation: determine jurisdictions and product classifications, verify business entity and Stripe eligibility, configure appropriate tax tooling where needed, obtain professional tax/legal review, and prohibit live checkout until compliance gates pass. Stripe Tax tooling does not make Stripe the merchant of record.

- **2026-11-07 — D048: Brotherhood subscription billing.** Approved option A: charge $5 at signup, renew automatically each month, no free trial or first-month promotion; allow cancellation anytime with access until the current paid period ends. Rationale: predictable billing and minimal subscription states. Risks: failed renewals, duplicate billing, webhook delays and misleading renewal disclosures. Mitigation: hosted Stripe subscription checkout, explicit recurring-charge and cancellation disclosures, idempotent webhook processing, defined failed-payment/grace policy before launch, and server-verified entitlements. No live checkout before compliance/integration gates.

- **2026-11-07 — D049: Accepted payment methods.** Approved option B: major credit/debit cards, Apple Pay and Google Pay through Stripe-hosted checkout, where available and compatible with one-time purchases and recurring subscriptions. Rationale: mobile-friendly checkout without an additional processor. Risks: wallets may not appear on all browsers/devices or for all billing scenarios; mitigation: use Stripe-supported configuration, test mobile and desktop payment paths, and always retain card checkout fallback. Do not promise universal wallet availability.

- **2026-11-07 — D050: Customer support channel.** Approved option A: a dedicated ForFathers support email address is the sole support channel for v0.1. Rationale: low operational overhead and clear ownership. Risks: delayed responses, missed messages, phishing/spam and customer frustration. Mitigation: monitor inbox, use an address on the owned domain, establish a response target in D051, and publish support contact on purchase receipts and relevant pages. No live chat or contact form in v0.1.

- **2026-11-07 — D051: Support response target.** Approved option A: aim to provide an initial human response to support emails within 24 calendar hours, including weekends. Rationale: faster resolution of digital-download, billing, and access issues. Risks: founder availability, missed messages, and unrealistic public guarantees. Mitigation: daily inbox monitoring, notifications and a fallback coverage plan; track actual response time and treat as an internal target, not a contractual SLA. Escalate urgent payment/access incidents when possible.

- **2026-11-07 — D052: Member account deletion.** Approved option B: members can initiate account deletion through authenticated account settings. Require identity re-verification and explicit confirmation; coordinate cancellation of any active Stripe subscription before deleting account credentials; revoke entitlements and sessions; delete or anonymize eligible personal data and preserve legally required transactional/accounting records under documented retention rules. Risks: accidental/unauthorized deletion, orphaned recurring charges, irreversible loss of purchases, and privacy-law noncompliance. Mitigation: test cancellation-before-deletion, retries/error handling, audit logs without unnecessary PII, and clear disclosure of consequences; failed cancellation must block final deletion and trigger support escalation. Provide a support-based fallback for users unable to access accounts without making it a second primary UI pathway.

- **2026-11-07 — D053: Basic analytics and success metrics.** Approved option A: measure website visitors, membership signups and cancellations, active paying members, monthly recurring revenue (MRR), digital product sales, and payment failures. Rationale: enough visibility to judge acquisition, revenue and checkout reliability without extensive instrumentation. Risks: inconsistent metric definitions, duplicate events, privacy exposure, and false revenue attribution. Mitigation: use verified Stripe payment/subscription records as financial source of truth, define MRR as recurring subscription revenue excluding one-off product sales, use aggregate/minimal visitor tracking with applicable privacy disclosures, and reconcile metrics. No complex attribution, behavioral tracking or cohort analytics in v0.1.

- **2026-11-07 — D054: Controlled production launch gate.** Approved option B. No real-customer checkout until: functioning site, Stripe subscription and one-time payment tests; verified business entity/payment account; applicable tax obligations addressed; published privacy/terms/refund disclosures; tested authentication, authorization and private storage; tested cancellation, failed payments and account deletion; tested digital fulfillment and five-download limit; operational email support; tested mobile checkout; basic monitoring and backups; and accessibility checks. Rationale: reduce payment, security, legal and customer-harm risks while avoiding extended beta scope. Risks: delayed launch or superficial sign-offs; mitigation: maintain evidence-based pass/fail checklist and block launch on any critical failure. Decision lock does not mean requirements have passed.

- **2026-11-07 — D056: Cohort marketplace commission.** Approved option A: use a 5% commission on completed Cohort marketplace transactions as the provisional business-model rate. Rationale: lower fee friction and simple positioning. Risks: processing fees, refunds, disputes, payout costs, tax and marketplace compliance may eliminate margins; Stripe's ordinary payment checkout does not by itself implement marketplace split payments/payouts. Mitigation: defer marketplace implementation beyond v0.1, validate marketplace payment provider capabilities, legal obligations and unit economics before publicly promising or activating the fee; revisit via ADR if not viable. Example: $100 gross transaction yields $5 gross platform fee before all costs.

- **2026-11-07 — D057: Cohort initial service categories.** Approved option B: plan future marketplace categories covering career/employment assistance, business/entrepreneurship, technology/digital services, home maintenance/practical skills, and personal development/mentorship. Rationale: balance the mission of men helping men with defined category boundaries. Risks: in-person safety, liability, regulated services, qualifications and moderation. Mitigation: Cohort remains coming soon in v0.1; before activation define prohibited services, identity/provider verification, safety standards, jurisdictional restrictions, dispute resolution and insurance/legal review. Category selection is not approval to transact or provide regulated professional advice.

- **2026-11-07 — D058: Cohort geographic scope.** Approved option A: limit initial future Cohort marketplace transactions and providers to the United States. Rationale: constrain jurisdictional, payout, tax, safety, and dispute-management complexity. Risks: U.S. still entails state-by-state rules, service licensing, marketplace tax obligations and local safety considerations; U.S.-only does not eliminate compliance. Mitigation: verify provider/customer residency and permitted service locations, assess state-specific requirements before Cohort activation, and expand internationally only through a separate decision. Does not automatically restrict Brotherhood membership or Digital Store geography. Cohort remains coming soon in v0.1.

- **2026-11-07 — D059: Cohort interest signup questions.** Approved option B: collect email address, intent (offer services, hire someone, or both), and primary service category of interest from Coming Soon visitors. Rationale: validate provider and buyer interest with minimal data collection. Risks: spam, invalid addresses, privacy/consent compliance, and mistaking signups for validated demand. Mitigation: explicit consent for updates, clear privacy disclosure, verification/anti-spam controls, unsubscribe mechanism, minimal retention, and separate reporting of provider vs buyer interest. No marketplace accounts, payments or service listings in v0.1.

- **2026-11-07 — D060: Cohort marketplace development trigger.** Approved option C: founder discretion determines when to initiate development of the future Cohort marketplace; no mandatory member-count or interest-signup threshold. Rationale: preserves strategic flexibility. Risks: premature investment, scope creep, insufficient supply/demand, and distraction from core subscriptions and Digital Store. Mitigation: Cohort stays Coming Soon and outside v0.1; before development, document a separate go/no-go ADR with rationale, budget, capacity, demand evidence and risks, confirm v0.1 operational stability, and verify marketplace legal, payment/payout, safety and unit economics requirements. This approval is not authorization to build or launch Cohort now.

- **2026-11-07 — ADR-D027-01: Download limit implementation amendment.** User approved option A following v0.1 architecture audit. Keep the existing five-download-per-purchase policy, but replace the former provider-native-only/no-custom-tracking restriction with minimal custom Supabase-backed enforcement compatible with D046 Stripe + Lovable + Supabase. Rationale: consistent fulfillment without adding a second commerce provider. Risks: concurrent requests bypassing caps, premature counting on failed transfers, shared/expired links, duplicate webhooks, support burden. Mitigation: private file storage, server-verified paid order, atomic per-purchase download reservation/counter, short-lived authorized grants, idempotent purchase fulfillment, concurrency and mobile testing, and support-assisted reset after verification. Implementation must define what counts as a download and failure recovery; no public file URLs. This is an amendment to canonical D027, not a 61st decision.

- **2026-11-07 — Administrative register cleanup.** Updated stale scope guardrails, execution checklist, decision queue and legend to match D009, D027 amendment, D029–D034, D046–D054 and D055–D060. No product decisions changed by this documentation correction.
