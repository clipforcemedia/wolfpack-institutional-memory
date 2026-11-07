# ForFathers — Build #01 Review Notes
Date: 2026-11-07
Builder currently used: Emergent (original D035 says Lovable; **platform switch not yet formally approved**).
Preview URL: https://fathers-together--4eon0tur.preview.emergentagent.com/
Status: partial visual review; do not generate a correction prompt until all five pages and interactions are audited.

## Homepage
- Visual direction APPROVED provisionally: navy/cream/copper palette, serif editorial typography, father-focused hero image, clear $5/month CTA, five navigation links, Resource Library/Store/Cohort previews, cautious Giving Fund language.
- Initial full-page screenshot appeared to have large blank sections; user supplied second screenshot after full load showing content. **Do not diagnose as broken based on first screenshot**; check scroll animations and reduced-motion behavior in functional QA.
- Check sticky navigation positioning during scroll and whether final large photographic CTA section displays its intended heading/button.
- Check marquee/scrolling text for accessible overflow and reduced motion.
- Mobile and click behavior unverified.

## Brotherhood page
- Visual direction APPROVED provisionally: headline “Five dollars. A brotherhood behind you.”; $5/month pricing, monthly only, cancellation through paid period, resource library and asynchronous private community, all-men-welcome message, Coming Soon disabled signup, FAQ and footer.
- FAQ accordion clicks not tested.
- Mobile layout not tested.
- When enabling live checkout in later phase, add conspicuous recurring-payment and cancellation disclosures; do not activate checkout in Build #01.
- No redesign or correction prompt warranted on screenshot evidence.

## Resource Library page
- Visual direction APPROVED provisionally: consistent cream/navy/copper, clear hero, category chips, search, card grid, three free preview labels, members-only badges and $5/month membership CTA.
- **Confirmed mock-inventory discrepancy:** page says 15 resources and shows three cards per category, while D013 locks 20 written resources (four per category), plus two interactive tools for eventual launch. For Build #01, add five more mock cards (one per category) without pretending they are published content; tools can remain future-stage placeholders.
- Search and category filter behavior not tested; verify interaction and empty states.
- Verify three Read Preview controls open actual static sample content or explicitly state previews are unavailable; no false functionality.
- Mobile layout, resource access protection and download behavior not tested; no backend should exist yet.
- Preserve current visual styling; consolidate corrections after remaining pages audited.

## Digital Store page
- Visual direction APPROVED provisionally: cohesive grid, mock product covers, $3/$5 pricing, 20 cards split 10 practical / 10 creative, descriptions, license notices, and Coming Soon controls.
- **Confirmed specification conflict:** some product metadata displays DOCX/XLSX editable formats, contrary to D023 PDF/PNG/JPG/ZIP only. Correct mock format labels and later actual files; do not introduce editable templates.
- Extra client-side All/Practical/Creative filters appear despite D043 minimal grid. Retain only if already functional with zero backend/dependency overhead; otherwise remove. Do not expand functionality.
- Test filters, disabled purchase buttons, mobile layout, and sticky navigation. Screenshot alone cannot verify behavior.
- Preserve visual styling; consolidate corrections after Cohort and interaction audits.

## Pending inspection
- Resource Library full-page screenshot and static search/filter behavior.
- Digital Store functional filter/disabled purchase verification (visual screenshot reviewed).
- Cohort full-page screenshot; interest form disabled, no data collection.
- Desktop navigation, 375/768/1440 responsive tests, keyboard, contrast, focus, no horizontal overflow.
- Confirm no backend, auth, Stripe, Supabase or external data collection introduced.

## Scope and workflow
- Do not issue another builder prompt until full review is complete.
- Compile confirmed defects into **one** narrowly scoped correction prompt; preserve approved aesthetics.
- Update D035 through explicit user approval if Emergent replaces Lovable as canonical builder.
- Source of truth: DECISION-REGISTER.md, V0.1-IMPLEMENTATION-SPEC.md and LOVABLE-BUILD-PROMPT-01.md (prompt content was used/adapted for Emergent).
