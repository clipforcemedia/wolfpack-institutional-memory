# ForFathers — Lovable Build Prompt 01: Public Foundation
Status: READY TO PASTE; NOT YET EXECUTED
Reference: V0.1-IMPLEMENTATION-SPEC.md and DECISION-REGISTER.md
Scope: PUBLIC FRONTEND ONLY. NO BACKEND OR PAYMENT CONNECTIONS.

Build a polished, responsive, mobile-first public website for ForFathers.com. The brand helps fathers first while welcoming all men. Mission: "To bring men together through brotherhood, providing the support, resources, and opportunities to help one another build better lives."

DESIGN: warm, confident, welcoming, credible—not militaristic or aggressive. Deep navy and charcoal, warm cream backgrounds, restrained muted copper/bronze accents. Accessible typography and high-contrast buttons. Use a small reusable design-token system. Use real semantic HTML, accessible forms and keyboard navigation. Avoid generic fake testimonials, fabricated metrics, invented partner logos or misleading launch claims.

CREATE EXACTLY FIVE PRIMARY NAVIGATION DESTINATIONS:
1. Home: concise mission hero; prominent primary CTA "Join The Brotherhood — $5/Month"; sections previewing Brotherhood, Resource Library, Digital Store, Cohort Coming Soon, Giving Fund, and final CTA. Be explicit where features are previews/not live.
2. Brotherhood: $5/month monthly-only membership offer, benefits (practical resources + private asynchronous discussions), cancellation-anytime explanation, and nonfunctional "Join" CTA clearly marked "Coming Soon" until account/payment integration.
3. Resource Library: responsive browsing mock with five categories: Fatherhood & Family; Career & Income; Financial Stability; Mental & Physical Wellness; Life Skills & Personal Growth. Add simple client-side title/keyword search and category filters on STATIC SAMPLE DATA. Show three clearly marked free samples and other member-only preview cards. No downloads or login gating yet. Do not claim 20 resources exist.
4. Digital Store: responsive 20-card MOCK catalog grid with 10 practical and 10 creative placeholders, split between $3 and $5. Each card includes illustrative placeholder thumbnail, title, short description, price, file-format placeholder, personal-use license note, and a DISABLED "Purchase — Coming Soon" control. No payment processing, shopping cart, reviews, or product detail pages. Do not imply mock products are purchasable.
5. The Cohort: "Coming Soon" description for future men-helping-men services. Show future categories: career/employment, business/entrepreneurship, technology/digital, home maintenance/practical skills, personal development/mentorship. Render a visual-only interest form with email, intent (offer services / hire / both), and primary category; do NOT persist data or show false success. Disable submission and label "Signups opening soon" until backend and privacy/consent flow exist.

OTHER CONTENT: Giving Fund language must be labeled proposed/subject to legal review, not imply donations have already occurred. Do not assert a charity partner. Footer: placeholder support contact, Terms, Privacy, Refunds clearly labeled "Draft — not yet published" where needed. Do not invent a working support email address.

STRICT EXCLUSIONS: No Supabase project, Stripe integration, database, authentication, membership dashboard, file downloads, checkout, live community, form submission, external APIs, Cohort marketplace transactions, or customer-data collection. Do not connect external services or add dependencies without approval. Use local mock data only.

ACCEPTANCE CHECKS:
- Exactly five top-level navigation items; all navigate correctly.
- Responsive at 375px, 768px, 1440px; no horizontal overflow.
- Home CTA is visible and clear, but cannot take money.
- Resource category filtering and search work with static data.
- Store has exactly 20 mock cards, no live purchasing.
- Cohort form cannot submit or persist data.
- No false claims of live functionality, charitable transfers, verified WCAG conformance, testimonials or business metrics.
- Keyboard navigation, labels, focus states, semantic headings, contrast and tap targets are sensible.
- No secrets, database credentials or payment integration.

STOP after implementing this public frontend slice. Report routes/components changed, anything left as placeholder, and manual test results. Ask for approval before any backend, auth or payment work.
