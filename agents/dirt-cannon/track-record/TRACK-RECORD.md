# DiRT Canon — Track Record (honest ledger)

**Owner:** Kabloom (Viral Content Studio) · **Maintained by:** Sunday evaluation pass
**Rule:** only graded, sourced results appear here. Passes and holds are never counted as wins.
Every line links to the file that proves it. No number here is invented; if a source is missing,
the row says `NOT GRADEABLE` and why.

---

## 1. Metrics-engine handoff — data integrity (2026 Week 3, published 2026-09-29)

Source: `dirt-canon-three-numbers-json-handoff-2026-week-3.zip` (Downloads),
re-verified this pass from the extracted copy.

| Check | Result | Evidence |
|---|---|---|
| Week-3 final scores vs ESPN game centers | **16 / 16 match** | `audit.json` → `score_checks[]` |
| Team box totals vs play-by-play (yards + plays) | **32 / 32 match** | `nfl-week3-boxscore-audit.csv` |
| Eligible league plays with missing EPA | **0 of 5,814** | `audit.json` |
| Metric arithmetic checks | **18 / 18 passed** | `manifest.json` |

**Verdict: the engine's DATA is trustworthy for Week 3.** 100% of the audited final scores and
box totals reconcile. This is data integrity, *not* a pick result — see §3.

## 2. Metrics-engine handoff — forward calls (2026 Week 3 → Week 4)

The Week-3 handoff contains **no win/loss picks and no DFS lineups.** Its only forward-looking
content is six `next_test` "questions" (Week-4 matchups) for the six featured teams:

| Card | next_test (Week 4) | Question posed | Graded? |
|---|---|---|---|
| San Francisco 49ers | Denver Broncos | sustain efficiency edge? | NOT GRADEABLE — Week-4 game not final at pass time |
| Seattle Seahawks | LA Chargers | larger efficiency margin? | NOT GRADEABLE — Week-4 |
| Baltimore Ravens | Tennessee Titans | keep all three measures moving? | NOT GRADEABLE — Week-4 |
| Jacksonville Jaguars | Cincinnati Bengals | improve big-play exchange? | NOT GRADEABLE — Week-4 |
| Kansas City Chiefs | Las Vegas Raiders | keep winning ordinary snaps? | NOT GRADEABLE — Week-4 |
| Green Bay Packers | Tampa Bay Buccaneers | fix the ordinary snaps? | NOT GRADEABLE — Week-4 |

**Verdict: 0 gradeable picks from the handoff.** A "question" is not a pick. Nothing here can be
scored as a hit or a miss. This is a *gap in the product*, not a win: see the report's adjustments.

## 3. Oracle game picks — the only graded, published record that exists

Source: `week-02-oracle-grading-ledger.csv` (copied from the Oracle Receipts v1.0 run,
graded 2026-09-22 against NFL Week 2, Sep 17–21). Raw accountability dump:
`week-02-accountability-raw.json`.

| Category | Wins | Losses | Pass | Hold | Ungraded | **Hit rate** |
|---|---:|---:|---:|---:|---:|---:|
| Projected winner | 8 | 7 | 0 | 0 | 1 | **8/15 = 53.3%** |
| Moneyline | 9 | 7 | 0 | 0 | 0 | **9/16 = 56.2%** |
| Spread | 0 | 0 | 4 | 12 | 0 | **not gradeable** (all held/pass) |
| Total (O/U) | 5 | 4 | 7 | 0 | 0 | **5/9 = 55.6%** |

**Verdict: marginal. Winner calls at 53.3% are statistically indistinguishable from a coin flip.**
The 12 held spreads mean the site's own records disagree on the signed line — a data-hygiene
problem that must be fixed before spreads can ever be advertised.

### Honest notes on the Week-2 record
- The headline miss: **LV–LAC, an 85.4% model confidence favorite lost outright** (LAC projected
  25–14, actual LV 26–14). One miss doesn't prove miscalibration, but a >85% favorite losing is a
  case that belongs in a calibration review, not in a promo.
- **IND–KC**: moneyline won, but the low-scoring "Under 47.5" call lost badly (final 30–33, 63 pts).
- **NYG–LA** is ungraded for projected winner (no frozen immutable score); its ML and total are graded.
- Ledger self-check this pass: `8+7+1=16`, `9+7=16`, `5+4+7=16` — the CSV reconciles.

## 4. Prediction-market / Kalshi "Six Pack" (YouTube show) — self-reported

Source: the show's own episode descriptions (public YouTube), **not** an independent grader.

| Week | Ticket | Self-reported result | Status |
|---|---|---|---|
| Week 3 (Sep 27) | 6 legs, $6 → $35.39 | **missed by one leg** — Josh Allen 30+ rush yds, actual 22 | self-reported MISS |
| Week 4 (Oct 4) | Gut 6-TD ticket vs Machine 6-leg card | pending — games not final | NOT GRADEABLE |

**Verdict: Week 3 Six Pack = no cash (5/6 legs).** Treated as a miss. Week 4 not yet gradeable.

## 5. Running summary (as of 2026-10-04)

| Track | Graded picks | Record | Hit rate |
|---|---:|---|---:|
| Oracle winner | 15 | 8–7 | 53.3% |
| Oracle moneyline | 16 | 9–7 | 56.2% |
| Oracle total | 9 | 5–4 | 55.6% |
| Oracle spread | 0 | all held/pass | n/a |
| Kalshi Six Pack (parlay) | 1 | 0 cashed | 0% |

**Bottom line: there is no winning track record to advertise yet.** Roughly coin-flip on winners,
slightly better on totals and moneylines, on a sample far too small to mean anything. Credibility
is the moat — keep the receipts honest and keep grading.