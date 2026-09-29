# Cybrid Title — Agent Project File (source of truth)

> **READ THIS FIRST in every session.** This is the master record for the venture
> that is the center of gravity. If a later session contradicts this file, this
> file wins until a human updates it. Keep secrets OUT of this file — record only
> *where* they live, never the values.

## Identity
- **Venture:** Cybrid Title — OCR / title-report examination
- **Legal/ops entity (if any):** JRW Solutions
- **Owner:** Chris Rupert (xrupert)
- **One-line mission:** Accurately examine title reports (OCR + PDF) at contract scale without hallucinations, from a 5k-file/mo client up to the largest US commercial title company (~50k files/mo, ~1,000-page PDFs).
- **Primary client now signing:** ~5,000 files/month, title reports 30–150 pages each.
- **Prospect (compounding event):** largest commercial title co in the country, ~50,000 files/mo, ~1,000-page PDFs.

## Status (updated 2026-09-29)
- ✅ **FIXED Report 2's "0 curative issues" defect** (commit 62a54c4, pushed to main): added `extractCurativeItems()` — a format-agnostic parser that reads grade-sheet/QC sections (`# <Category>` + `Status: PROBLEM` + bulleted items), wired into `result.curative`. Verified on the real 3.4MB ServiceLink file: now finds **3 items including "Missing assignment into Servbank"** (was 0). **91/91 deterministic tests green.** (Refinement: UCC + divorce instrument numbers live in section bodies — capture them next.)
- ✅ **FIXED the current_first defect on real Report 1** (commit 6f40dcb, pushed to main): added a third, format-agnostic fallback to `findRunSheetFirstLien` — reads the **"Voluntary Liens / Mortgage Information"** body section when the run sheet has no enumerated exception list. Verified against the real 18.6MB file via offline harness: now finds instrument 1222264739 (loan no.), $428,041, page 2 (UWM/MERS mortgage) — was NULL before.
- **Offline harness built** (`tools/offline-parse.ts`, `check-curative.ts`, `dump-all.ts`): real PDF → Mistral OCR → real parser, no Supabase/gateway. Repeatable test bed. Deno 2.9.7 installed.
- **Root cause (proven on both real files):** the parser was built for RCS-style enumerated exception lists. Neither the Data Tree "Two Owner Informational Summary" (Report 1) nor the ServiceLink "Foreclosure Grade Sheet" (Report 2) uses that grammar. **Both now fixed with format-agnostic fallbacks.**
- **Report 2 rerun finding:** model answers are NON-DETERMINISTIC between runs (Q7 assignment flipped FAIL↔PASS on same packet hash). Even where the parser works, a single run's PASS/FAIL isn't trustworthy → needs retry/consensus or confidence-gated escalation (Jev's probabilities fit here).
- **User correction:** "Foreclosure" label on Report 1 was the USER's chosen review type, not a machine mislabel. Retracted that part of the earlier score.
- **Pipeline architecture (agreed):** Mistral OCR (reads) → LLM extraction (understands) → Jev judgments (judges, future) → deterministic code (decides). Jev does NOT replace the LLM — it sits after it, on extracted facts, feeding confidence-gated escalation. Jev accuracy on title judgments unproven → must be measured against golden packets.
- **Mistral key:** in `report-vetter-bot/.env.local` (git-ignored, never chat). Authenticates (53 models, mistral-ocr-2512 present). Note: code asks for `mistral-ocr-latest`; if that alias fails, pin the version.
- **Gateway coupling:** VERA-20 answers + embeddings route through `ai.gateway.lovable.dev` via `LOVABLE_API_KEY`. Remote has a "Replaced Gemini with Sol" commit — the answer model is being swapped. To sever Lovable fully on Hetzner, point this at any OpenAI-compatible endpoint (Mistral has one; same key can serve it).
- **Evidence-bound repair (design validation, 2026-09-29):** preprint "Evidence-Bound Factual Repair in RAG LLM Answers" (Rajendran & Singaravelu, Preprints.org 2026-09-07) independently validates the no-hallucination architecture (deterministic code decides; model points, never authors accepted facts). Distilled at `agent-control-room/references/evidence-bound-repair.md`. Two adoptable mechanisms for the examiner UI: (a) **provenance coloring** (green=verbatim evidence / amber=flagged / black=untouched + confidence tier + coverage ratio — converts whole-report review into targeted review), (b) **coverage-cascade accounting** (report resolved vs unresolved separately — never hide unrepaired claims inside a PASS; exactly the Report 1 "PASS with wrong reasons" fix). Standing rule: no free-regeneration step anywhere without deterministic re-grounding. Preprint caveat: 1 lab, n=16/27, GPT-4-only — design-direction evidence, not gospel.
- **jev/TypeSafe:** setup done, key in `jev-ultrafast/.env`, imports OK. Parked until pipeline is at a good place (user's call).
- (Baseline retained below — `BASELINE_2026-09-25.md`)

### Baseline (2026-09-25) — retained
- ✅ **MEASURED BASELINE COMPLETE** — `BASELINE_2026-09-25.md`. Real engine run on both sample files. **Neither is contract-grade; neither is sign-off-ready.** Recorded with review IDs + packet hashes.
  - Report 1 (RCS Two-Owner): ❌ wrong order type (Foreclosure vs Two-Owner), ❌ open lien count 9 vs expected 1, ❌ target lien undetermined yet **green PASS "ready for sign-off"** — the dangerous one.
  - Report 2 (ServiceLink Grade Sheet): ✅ correctly FAILs, but ❌ curative issue count 0 (packet has ≥4 stated: missing assignment into Servbank, defective legal, UCC 2018258740, divorce 2021323450), +9× over-count/open count.
  - Root causes: order-type detection (FM S), lien-family/current_first (known HANDOFF defect), curative-issue extraction from grade sheets (FM AB/AC).
- (Older status retained below)
- Pipeline: **Phase A not yet run on real engine** (needs Supabase/Mistral secrets that live in Lovable Cloud Secrets — not this chat). App proven conceptually; real measured accuracy NOT established.
- ✅ **Golden-packets v2 built for 2 real sample files** (source of truth, no secrets needed):
  - `agent-control-room/agents/cybrid-title/golden-packets/GOLDEN_PACKET_25-003916.md` — RCS Two-Owner Informational, Order 101-10729425, Polk FL
  - `agent-control-room/agents/cybrid-title/golden-packets/GOLDEN_PACKET_25-004050.md` — ServiceLink Foreclosure Grade Sheet, Order 230258724, Duval FL (**NEW LAYOUT** — not RCS)
  - **KEY FINDING:** Report 2 is a ServiceLink "Foreclosure Grade Sheet" — a layout the pipeline was never validated on. This is exactly the "next new layout" risk HANDOFF.md warned about. Test before the 5k contract.
- ✅ **4 new failure modes added** to FAILURE_MODES.md: AA (grade-sheet layout), AB (missing assignment into servicer), AC (PROBLEM items not cleared), AD (tax year/value mismatch).
- **Scale finding (corrected):** Mistral OCR reads ALL pages (~$5/1000pg). The **24-page cap is on the separate Gemini enrichment pass, and it's a LATENCY/reliability cap, not cost** (~125 gateway calls for a 1000-pg packet if unbounded). Risk at commercial scale = controlling facts past page 24 ride on regex+RAG, not deep read. Needs targeted-enrichment design before 50k contract.
- **Timing:** 60-pg ≈ 2 min, so 1000-pg ≈ 20–30 min ≈ 3× faster than a human's 1.5hr+ — win, IF evidence completeness holds on deep pages.
- Source app: Lovable, project **"remix of veratitle-audit"**, repo **xrupert/report-vetter-bot** (PRIVATE, cloned to <HERMES_HOME>\cache\scratch\report-vetter-bot). Logic is sound (deterministic grading, truth states, evidence ledger, packet SHA-256). Do NOT rebuild logic; move infra.
- Hosting: user rents **Hetzner** (project 14923417). NOT experienced — guide step by step; secrets to .env.
- **Lightpanda (browser engine, verified 2026-09-29):** installed Hermes (v0.21.5) supports `browser.engine: lightpanda` (spawns `lightpanda serve`; auto-fallback to Chrome for screenshots/vision/unsupported). **NO Windows build** (code returns explicit error) → it's a Hetzner-phase play for thin-VPS monitoring/cron (288 checks/day RAM-swap scenario). VPS setup step: install binary + set the config line; keep Chrome as visual fallback. Local Windows workstation stays Chrome. Also: gateway runs as manual spawn, NOT a service — run `hermes gateway install` once on the VPS (and optionally locally) so restarts/reboots don't strand agents with stale plugin code.
- TypeSafe: paused signups; key later → jev-ultrafast .env. NOT required for pipeline.
- Sample files (de-identified-able): `AppData/Local/hermes/attachments/25-003916 TITLE_REPORT_1.pdf` (18.6MB), `25-004050 TitleReport2.pdf` (3.4MB). Extracted text in <HERMES_HOME>\cache\scratch\pdfs\{report1,report2}.txt.

## NEXT ACTIONS (in order)
1. When user is next in Lovable: run `process-title-report` on Report1 + Report2, paste JSON results → real measured baseline.
2. Fix `current_first` (single known defect gate per HANDOFF.md) before any new golden packets.
3. Design targeted page enrichment for commercial-size packets (raise/reshape 24-page cap) before 50k scale.
4. Then port to Hetzner behind real queue (idempotency, workers, cost model, audit trail).

## Architecture decisions (locked unless amended here)
1. **Not production on Lovable.** Lovable = prototype. Production = real infra on Hetzner.
2. **Accuracy is measured, not felt.** Golden test set of de-identified sample title reports with known-correct answers → measure precision, recall, pass-through accuracy → set contract-acceptance thresholds IN WRITING before shipping.
3. **No-hallucination-by-design, not "zero hallucination" wish:** high-confidence files auto-pass; low-confidence files escalate to a human with the model's reasoning attached. Confidence thresholds + human escalation = "accurate every time" in production.
4. **Scale is a separate test axis** from accuracy (throughput, cost/file, timeout, memory on 1,000-page PDFs).
5. **Secrets never in chat/this file**: Hetzner creds, client files, TypeSafe key → `.env` / vault.

## Phases
- **A. Golden test set + baseline** (prove today's real accuracy; zero infra risk)
- **B. Thresholds set in writing** (what the pipeline must hit to ship)
- **C. Real pipeline on Hetzner** (port Lovable logic to production)
- **D. Scale + cost test** (5k then 50k)
- **E. Acceptance → sign contract**

## Credentials & secrets (LOCATIONS only)
- Hetzner: console.hetzner.com project 14923417 → API token / SSH → `.env` (help user create)
- TypeSafe key: pending arrival → placed in `.env` of jev-ultrafast
- Gmail ×5 + Chat: `<HERMES_HOME>/google_tokens/*.json` (authenticated)

## Repos / assets on disk
- Control Room (durable): `C:\Users\Chris Rupert\agent-control-room`
- jev-ultrafast: `<HERMES_HOME>\cache\scratch\jev-ultrafast` (installed, 31 tests pass; needs TypeSafe key)
- oh-my-hermes: `<HERMES_HOME>\cache\scratch\oh-my-hermes`
- council-of-high-intelligence: `<HERMES_HOME>\cache\scratch\council-of-high-intelligence` (18-persona deliberation; has council-munger)
- This file: `C:\Users\Chris Rupert\agent-control-room\agents\cybrid-title\project.md`

## The other ventures (context, not center of gravity)
- **liensight** (HUD non-loan finding, mortgage servicers) — Tier 2 real bet, not yet an asset.
- **Dirt Cannon** (sports content) — Tier 3; the automatable content engine; defensibility play.
- Tier 4 (Polymarket bot, $100→$1200 robot, children's book/Youtube, novel, Amazon "how-to" books) — held back as escape hatches; reinvest energy into Cybrid Title.
