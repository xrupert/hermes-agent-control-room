# Evidence-Bound Factual Repair — design reference

Source: Rajendran, S. & Singaravelu, D. (2026). "Evidence-Bound Factual Repair in Retrieval-Augmented LLM Answers: Separating Semantic Localization from Deterministic Realization." Preprint, Preprints.org, doi:10.20944/preprints202609.0490.v1, 2026-09-07, CC BY 4.0.

STATUS: preprint, single lab (Alphashots.ai), small discordant-pair samples (RAGTruth n=16, ExpertQA n=27), GPT-4 family only, wide CI on headline. Use as design-direction evidence, not gospel. It has NOT been peer-reviewed. Nothing here signs contracts.

## The validated mechanism

Pipeline over an existing answer (B0) + retrieved evidence, four stages:

1. **Locator (LLM, the only paid step):** identifies every externally verifiable factual proposition in the answer; returns the exact answer span + one or two evidence-sentence IDs — IDs only. The model is NOT allowed to write, paraphrase, normalize, or author replacement text. Segmentation is deterministic (complete sentences only; incomplete/ambiguous units never exposed as selectable evidence). Same prompt contract applied to both datasets.
2. **Coverage Gate (deterministic, zero model calls):** classifies each claim mapping resolved/unresolved (pointer validity, evidence-ID validity, overlap safety, length guard, replacement actually applied). Fail-closed: unresolved mappings retain original text. Every response lands in exactly one of five categories — never hides unrepaired claims inside a pass.
3. **Renderer (deterministic, zero model calls):** substitutes only resolved mappings with verbatim evidence sentences. No model calls, no re-localization. Protects factual quantities ("1 mg", "$1"), suppresses same-source duplicates, cleans seams. Strict minimality: never introduces a source sentence the Locator didn't select.
4. **Provenance Coloring (deterministic, zero cost):** tiles the final answer — green = clean-rendered verbatim evidence, amber = flagged-rendered (completeness-risk flag), black = untouched original prose (never checked, no claim about it). Plus a 4-way confidence tier (high/medium/low/no-claims) computed from counts, plus a coverage ratio (fraction of final-answer chars that are verbatim evidence). Explicitly NOT a calibrated probability: high confidence = "nothing the pipeline checked was left open," not "no error exists." High-confidence label is rare (8.10% of RAGTruth held-out) — conservative by design.

## Numbers (report as-is, with the preprint caveat)

- RAGTruth (889 held-out GPT-4-0613 QA): 14/32 hallucinated responses fully repaired; 2 adverse additions → net 12/32 = 37.50% (exact paired p = 0.0042; 95% CI [18.3%, 56.7%]).
- ExpertQA (731): 26/110 reviewed grounding failures repaired = 23.64% (p = 4.17e-7); 1 new grounding failure (fail-closed, conservatively retained).
- Coverage Gate resolved 82.036% of located claim mappings; rejected no complete response.
- Renderer: changed 622/889 responses; screened defect rate 23.51% → 2.70%.
- Completeness cost (major loss only): 2.80% RAGTruth / 2.33% ExpertQA of officially clean responses — the two datasets converge.
- Baseline A (unconstrained single-shot regeneration, matched sample): removes hallucinations at a comparable or nominally higher rate (46.88% vs 43.75%) BUT introduces new evidence-unsupported content at ~4.5x the rate (1.02% vs 0.226%). Model-authored replacement trades a predictable, auditable failure mode for a several-fold higher rate of an unpredictable one.
- Second-author rationale-blinded endpoint verification: κ = 1.000 RAGTruth (n=144), 0.977 ExpertQA (n=173).
- Cost: one locator call per response ≈ USD 0.054 (RAGTruth) / 0.071 (ExpertQA), latency ~8-9 s; every later stage ~$0 and <3 ms.

## The two negative results that shaped the design (worth remembering)

1. **Surface-form claim selection does not concentrate risk.** A heuristic flagging claims containing fragile values/negation/conditionals overlapped human hallucination spans at 4.80% selected vs 6.33% non-selected (relative risk 0.758) — the claims it skipped were hallucinated MORE often. → Check every claim the locator can identify; do not build risk-prioritization heuristics on surface form.
2. **Fluency re-polish reopens the door.** Grammar polish was preferred 66% of the time but introduced new unsupported propositions at judge-raw 15% of changed responses. → No free-regeneration/polish step in the pipeline without deterministic re-grounding.

## What we adopt (our ventures)

- **Cybrid Title OCR:** (a) the architecture already matches — deterministic code writes the verdict, model points but never authors accepted facts; this paper independently validates that choice. (b) ADOPT: provenance coloring for the examiner UI (green/amber/black per span + confidence tier + coverage ratio) — converts whole-report review into targeted review. (c) ADOPT: coverage-cascade accounting — report resolved vs unresolved separately; never hide unrepaired claims inside a PASS (this is exactly the Report 1 "PASS with wrong reasons" failure mode). (d) Standing rule: no free-regeneration step anywhere without deterministic re-grounding.
- **Grounded-citations skill:** already implements ledger-at-retrieval + cite-while-writing + mechanical Sources + verify gate + verbatim-quote evidence mode. The paper's Locator→Coverage Gate→Renderer split is the same philosophy; the skill's `verify --evidence` is our Coverage Gate.
- **Any future LLM answer pipeline (Liensight, Dirt Cannon content):** apply the same separation — model localizes and binds, deterministic code realizes the accepted facts.
