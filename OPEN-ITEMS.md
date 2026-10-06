# OPEN ITEMS — holding file

**Owner rule (2026-10-06):** *if we have not talked about it and finished it, it sits here.* Nothing in this
file is being worked on, chased, or nudged. It is an inventory, not a to-do queue. An item moves only when
Chris says "let's do this one."

Last updated: 2026-10-06. Owner: Chris Rupert. Maintained by: Hermes.

---

## Waiting on Chris — a decision, not work

| # | Item | Venture | Status |
|---|---|---|---|
| 1 | Baseline accuracy route, now that Lovable is on hold: run the LLM/grading pass some other way, or wait? | Cybrid | **needs a call** — local parser half is done, the accuracy number is not |
| 2 | Golden test set: n=2. Needs more de-identified packets before Phase B thresholds mean anything. | Cybrid | waiting on files |
| 3 | Hetzner build-out: what role the server plays, what runs there. **Scope before code.** | Cybrid | not discussed |
| 4 | The three Dirt Cannon items (locked calls / analytics access / UTM tagging) | Dirt Cannon | deferred to the Oct 6–7 conversation, expires end of Oct 7 |
| 5 | `TEXT_MODEL_API_KEY` — blank. Only needed if TYPE_TEXT operations should run. | jev | only if wanted |

## Open, not waiting on anyone

| # | Item | Venture | Status |
|---|---|---|---|
| 6 | Report 2 `findRunSheetFirstLien` returned a 21-digit instrument (`101177611802131232`) — implausible, unverified. | Cybrid | known defect, unfixed, not urgent |
| 7 | Non-determinism: Q7 flipped FAIL↔PASS on one packet hash. Needs retry/consensus or confidence gating. | Cybrid | design not started |
| 8 | 24-page enrichment cap — controlling facts past page 24 ride on regex+RAG. Must be designed before 50k scale. | Cybrid | design not started |
| 9 | Thursday-ish: Week-4 receipts grading — no Week-4 handoff or verified box score in the pipeline. | Dirt Cannon | blocked on a source; grades when one lands, before the window closes |
| 10 | Large-PDF upload flakiness (one `fetch failed` on a 19.5MB upload, retry worked). | Cybrid | observed, harmless so far |

## Closed / done — for the record

- ✅ Local parser baseline run (2026-10-06): Report 1 current_first FOUND, Report 2 curative = 4 items. Both defects green on the real files.
- ✅ TypeSafe key loaded and verified live (422 with key vs 403 without; 31/31 tests, ruff clean).
- ✅ Mistral key loaded locally; **Lovable parked per owner.**
- ✅ Dirt Cannon stale gates cancelled under `STALE-POLICY.md`; desk backed up and pushed.
- ✅ Durable clones at `C:\Users\Chris Rupert\code\` (scratch pruning had destroyed the old ones).

## Parked / not started

- **Liensight** — Tier 2, `agents/liensight/` is empty. Not started, no goal note beyond "exploring".
- **Tier 4 escapes** (Polymarket bot, children's book, novel, Amazon how-to books) — held back by owner decision, reinvest into Cybrid Title.