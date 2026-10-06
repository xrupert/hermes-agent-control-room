# DiRT Canon — Weekly Performance Report
**Week of Sep 29 – Oct 4, 2026 (NFL Week 4) · Prepared Sunday, 2026-10-04, by Kabloom**
Studio desk: `C:\Users\Chris Rupert\agent-control-room\agents\dirt-cannon\`

> The honest version first: **we are making content nobody is watching, and there is no winning
> track record to advertise yet.** Volume is healthy. Reach is ~zero. The one graded pick record
> that exists (Oracle, Week 2) is coin-flip on winners. Nothing in this report claims otherwise.

---

## 1. Predictions vs. actual results — did the picks hit?

### 1a. The handoff itself contains no picks
Last week's handoff (`dirt-canon-three-numbers-json-handoff-2026-week-3.zip`, published
2026-09-29) is **descriptive**, not predictive. It ships six team cards of three-game metric
profiles plus six Week-4 `next_test` *questions*. There is no win/loss call, no spread, no DFS
lineup, and no confidence number in it. **Zero gradeable picks.** You cannot score a rhetorical
question. That is a product gap, and it is the single most important finding this week.

### 1b. The handoff's data is clean
Where the handoff *can* be checked, it holds up:
- **16 / 16** Week-3 final scores match ESPN game centers (`audit.json`).
- **32 / 32** team box totals match play-by-play yards and plays (`nfl-week3-boxscore-audit.csv`).
- **0** missing EPA across 5,814 eligible plays; 18/18 arithmetic checks pass.
Data integrity: 100%. The numbers are real. They just aren't *calls*.

### 1c. The only graded published record: Oracle, Week 2
Full detail in `track-record/TRACK-RECORD.md` and `track-record/week-02-oracle-grading-ledger.csv`.

| Category | Record | Hit rate |
|---|---:|---:|
| Projected winner | 8–7 (1 ungraded) | **53.3%** |
| Moneyline | 9–7 | **56.2%** |
| Total (O/U) | 5–4 (7 pass) | **55.6%** |
| Spread | 0 graded (4 pass / 12 held) | n/a |

**Read it straight: 53.3% on winners is a coin flip.** The single worst moment was **LV–LAC**,
where an 85.4%-confidence favorite (LAC) lost outright. The 12 held spreads mean the site's own
records disagree on the signed line — a hygiene bug, not a strategy.

### 1d. Week 4 — not gradeable today
The six handoff `next_test` games (SF@DEN, SEA@LAC, BAL@TEN, JAX@CIN, KC@LV, GB@TB) are Week-4
games played **today/Monday**, not yet final. The Week-4 Kalshi "Gut vs. Machine" card (posted to
YouTube today) is likewise pending. I did **not** fabricate results for them. Grade them Tuesday
when finals exist.

---

## 2. Engagement data — what is and isn't measured

**Measured (real platform data, public surfaces):**

| Platform | Account | Period | What we see |
|---|---|---|---|
| X | @TheDiRTCanon | Sep 30 – Oct 3 | ~10 posts; **likes 0–1, reposts 0, views ~12–32** per post |
| YouTube | @thedirtcanon | last 2 eps | Wk3 ep (Sep 27, 4:14) = **6 views**; Wk4 ep (Oct 4, 5:32) = **0 views** after ~7h |
| Instagram | @dirtcanon | — | listing shows **~4 followers** (may be a secondary/placeholder account) |

**NOT measured — say it plainly:**
- **Facebook** (`facebook.com/thedirtcanon`): page exists; follower count and post metrics are behind
  a login wall — no data retrievable this pass.
- **Click-throughs to thedirtcanon.com: not measured at all.** The studio has no site-analytics
  access and no UTM/short-link tagging in use, so "did anyone click" is currently unanswerable.
- **Instagram per-post reach/saves/shares:** not retrievable without the account's analytics.
- **X follower count:** not returned by the public read.

**Implication:** the studio is flying blind on its two most important numbers — real reach and
click-through. Fixing measurement is a prerequisite for "do more of what works."

---

## 3. What worked / what didn't (numbers, not vibes)

**Worked:**
- **Shipping discipline.** Content moved every day: ~10 X posts, a 4–6 min YouTube episode, articles.
  Cadence is not the problem.
- **The YouTube show format.** "The Gut vs. The Machine" is genuinely good television for a niche
  audience — characters (Professor Who Dat, DiRTy Bird, Gio), a real narrative, a call to comment.
  It is the strongest asset in the building. It is also invisible: 6 views.
- **Accountability as a feature.** Printing the 85.4% miss on a card ("we're printing it") is exactly
  the differentiator the brand claims. That is rare and on-voice.

**Didn't work:**
- **Reach.** Best X post: **32 views, 1 like, 0 reposts.** Week-3 YouTube: **6 views.** Week-4: **0.**
  At this scale, "engagement rate" is noise. The content is not entering anyone's feed.
- **Distribution.** 0 reposts / 0 quotes / 0 visible comments across the sample = zero organic spread.
  The show's explicit CTA ("drop a comment: GUT or MACHINE") converted to nothing measurable.
- **No cashable result.** The Week-3 Six Pack missed by one leg (Josh Allen rush yds: needed 30, got 22).
  There is no win to point at this week.
- **No pick accountability from the handoff.** Week over week, the engine asks questions and moves on.

---

## 4. Adjustments proposed for next week

**Measurement (do first — everything else depends on it):**
1. Tag every outbound link to thedirtcanon.com with UTM parameters (or a short-link service) so
   click-through becomes a real number. *(needs owner OK if it means a paid tool)*
2. Get the studio read access to FB/IG/YT/X analytics so reach is measured, not guessed.

**Product / credibility:**
3. **Turn the handoff's "next_test" questions into locked, gradeable calls** — a number, a direction,
   and a confidence. Questions build no track record; calls do.
4. **Ship a graded Oracle receipts pass for Week 3 and Week 4 within 48h of finals.** The pipeline
   already exists (`oracle-receipts/` — renderer + grader + ledger). Reuse it; don't rebuild it.
5. **Fix spread signing** before any spread is ever shown again. 12/12 held is a data bug.
6. **Calibration review** on any call at ≥80% confidence before it is promoted.

**Formats & timing:**
7. Cut the Sunday YouTube episode into **3 vertical shorts** (one per best leg) for IG/TikTok/X —
   the long-form is good but only reaches 6 people.
8. **Post the receipt at result time** (Sunday night / Monday), not just the preview. Receipts are the
   brand; previews are commodity.
9. **Trade volume for reach:** fewer, better posts that reply into larger NFL/DFS/X threads, instead
   of ~10 low-reach standalone posts a day.
10. **Hold TikTok** until measurement and one repeatable format are proven. *(needs owner decision)*

---

## 5. Decisions needed from the owner (nothing was published or spent this pass)

- **Approval to publish** any of the above drafts (none were posted — drafts are free, publishing isn't).
- **Approval to instrument** site links with UTMs / short links (possible tool cost).
- **Access to platform analytics** for FB, IG, YouTube, X.
- **Decision on TikTok** (new platform) — recommend holding until reach is measurable.

## 6. Sources & method
- Handoff: `Downloads\dirt-canon-three-numbers-json-handoff-2026-week-3.zip` (extracted, re-audited).
- Oracle grading: `track-record/week-02-oracle-grading-ledger.csv` (+ raw `week-02-accountability-raw.json`).
- X engagement: xAI X Search, public posts by @TheDiRTCanon.
- YouTube: public video pages for `I8d0f13iFy0` (Wk4) and `207Z2ea9D9Q` (Wk3).
- No number in this report is estimated. Where a source was unavailable, it says so.