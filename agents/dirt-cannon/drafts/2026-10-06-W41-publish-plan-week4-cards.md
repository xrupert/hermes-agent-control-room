# Publish plan — THREE NUMBERS, Week 4 cards (NFL W4 / CFB W5 pack)

> ⛔ **CANCELLED (owner, 2026-10-06) — "ok just cancel that."** Not approved, not pursued. Nothing was
> posted, scheduled, or spent. Do not re-raise this plan or a variant of it unless Chris asks.
> The cards, the audited pack (`evidence/2026-nfl-week-4-cfb-week-5-handoff/`), and the verified numbers
> stay on the desk — the data doesn't rot and needs no decision. Only the posting plan is cancelled.
>
> Context found while building it, recorded so nobody re-discovers it: the site's Game Predictions sit behind
> the $6/mo GridIron Oracle login, and `/pricing` says checkout is still being finalized (nothing is locked,
> but there is no live prediction page to send traffic to yet). `/remote-patrol` is free but currently shows
> "this week's issue has wrapped" with an empty streaming table. A captions→site funnel has no cake to point
> at today.

**Status: DRAFT — cancelled before approval.**
**Thrown: Tue 2026-10-06. Per `STALE-POLICY.md` this plan expires 24h after Chris is told (→ Wed 2026-10-07 09:00 ET) unless he acts on it.**
**Source of record:** `evidence/2026-nfl-week-4-cfb-week-5-handoff/` (`dirt-canon-three-numbers-nfl-week-4-cfb-week-5-2026.zip`, 12.1 MB, 74 files).
Every number below traces to that pack. Nothing invented.

---

## 1. What the pack gives us (verified this pass, not taken on faith)

| Check | Result | How verified |
|---|---|---|
| Six public cards, 1080×1350 PNG | ✅ all six | read PNG IHDR headers directly |
| Captions + alt text already written | ✅ `captions-and-alt-text.md`, `cards/captions.md` | read |
| Eligible plays / missing data | ✅ 7,789 plays; `missing_epa=0`, `missing_yards=0`, `duplicate_ids=0` | `nfl-audit.json` |
| Week-4 finals vs ESPN | ✅ 16/16 `final_match: true` | `nfl-audit.json → latest_week_score_checks` |
| Week-4 box totals vs play-by-play | ✅ 32/32 yards, 32/32 plays | `nfl-boxscore-audit.csv` |
| Games by week | ✅ 16/16/16/16 | `nfl-audit.json` |
| **New this pack: prior-published-rank deltas** | ✅ `*_prior_published_rank`, `*_rank_change` columns | `nfl-all-32-metrics.csv` |

**Data integrity is clean. The numbers are real. That is not the same as a track record** — this pack still ships zero picks,
zero spreads, zero confidence numbers. Same product gap as week 3, still open.

## 2. The six cards (season-to-date, 4 games, not opponent-adjusted)

| Team | Net EPA/play (rank) | Consistency pp (rank) | Big-play pp (rank) | Movement since last published | Next (Week 5) |
|---|---|---|---|---|---|
| San Francisco 49ers | +0.278 (1) | +9.2 (3) | +10.4 (1) | flat — r1/r3/r1 all unchanged | @ SEA, Sun 4:25pm ET |
| Baltimore Ravens | +0.215 (4) | +9.3 (2) | +4.8 (2) | up: EPA r5→r4, SUC r4→r2, EXP r4→r2 | @ ATL, **SNF 8:20pm ET** |
| Atlanta Falcons | +0.029 (13) | +11.1 (**1**) | +4.0 (5) | **up 10** on EPA (r23→r13), SUC r6→r1 | vs BAL, **SNF 8:20pm ET** |
| Arizona Cardinals | −0.096 (24) | +3.3 (9) | −7.1 (**32**) | down: EPA r19→r24, but SUC r15→r9 | vs DET, Sun 4:25pm ET |
| Green Bay Packers | −0.124 (26) | −6.1 (27) | +1.5 (10) | up: EPA r29→r26, SUC r31→r27 | vs CHI, Sun 1:00pm ET |
| Miami Dolphins | −0.240 (**32**) | −12.0 (**32**) | −1.0 (19) | flat at the bottom (r32/r32) | vs CIN, Sun 1:00pm ET |

**Week-5 slate verified from ESPN scoreboard feed** (same source family the pack uses, 15 games — matches the pack's two byes):
TNF TB@DAL Oct 8 8:15pm · London PHI/JAX Oct 11 9:30am · 1pm window (7 games incl. **CHI@GB**, **CIN@MIA**) ·
4:05 DEN@LAC · 4:25 (**SF@SEA**, **DET@ARI**) · SNF (**BAL@ATL** 8:20pm) · MNF BUF@LAR Oct 12 8:15pm.
**All six card teams play Sunday Oct 11. Zero card teams on bye.** Two card teams play *each other* in the SNF slot.

## 3. The ideas — six angles, ranked by strength

**A. THE MOVEMENT REPORT** *(strongest — brand new this pack; week 3 had no prior-rank column, so we have never shown this)*
Nothing moved at the top; everything moved underneath. ATL **+10** (r23→r13), NO **−12** (r18→r30), NYG **+9** (r28→r19),
TEN **−8** (r21→r29). Format: 32-team table graphic or a 5-slide carousel. Line: *"San Francisco didn't move. Everybody else did."*
This is the post that proves the engine does something a highlight reel can't.

**B. THE CONTRADICTION TRIO** *(the teaching angle, and it's our thesis)*
ATL is #1 in consistency but #13 in efficiency. ARI is #9 in consistency but **dead last** in big plays. GB is #10 in big
plays but #26 in efficiency. Three teams whose numbers disagree with themselves — one thread, three cards. Line: *"Winning
more snaps is not winning the most valuable ones."*

**C. THE TWO THAT AGREE** *(the clean authority post)*
SF (1/3/1) and BAL (4/2/2) are the only teams top-five in all three. Line: *"Four games make a strong opening argument, not
a lifetime warranty."* SF has held r1 in all three measures for two straight publishes — that's the receipt-flavored claim we
can actually back.

**D. MIAMI — DEAD LAST TWICE, AND NOT UNLUCKY** *(highest engagement risk; strongest voice fit)*
#32 efficiency, #32 consistency, but #19 in big plays. Line: *"Miami's problem is not the bomb it missed. It's the boring
snap it keeps losing."* This is the anti-highlight post — on-brand, and it will get replies from a fanbase.

**E. BAL @ ATL, SUNDAY NIGHT** *(the marquee — two cards, one game)*
One team is #1 in consistency. The other is top-four in everything. Line: *"Sunday night settles the record, not the argument."*
Post it **in-window**, reply into the live SNF thread.

**F. SIX CARDS, SIX POSTS** *(the baseline cadence — one card per day Tue→Sun, each with its shipped caption)*
Every card already carries `next_opponent`, which gives each post a hook and gives Sunday a payoff.

**Honest limit on F:** a card that says "watch Seattle" is still a *question*, not a call. Nothing in this plan fixes that.
The only real fix remains the open gate in `decisions/2026-10-06-fresh-items.md` (engine publishes locked calls).

## 4. Captions — the pack ships them; these are platform-shaped versions

The pack's own caption (use verbatim on X):
> First in efficiency. First in big-play balance. Four games make a strong opening argument, not a lifetime warranty.
> Through NFL Week 4, 2026. Four-game sample; not opponent-adjusted. More at TheDiRTCanon.com. #NFL #TheDiRTCanon

**Instagram / Facebook** — add the third line, then the caveat block:
> Through NFL Week 4, 2026. **+0.278 net EPA per play — NFL #1.** Big-play balance +10.4 pp — also #1. Consistency +9.2 — #3.
> Four games make a strong opening argument, not a lifetime warranty.
> Four-game sample · not opponent-adjusted · ranks are bands, not talent. Watch the number, not the replay.
> thedirtcanon.com

**The Movement Report (new copy, all figures from `epa_rank_change`):**
> Week 4 closed. Here's what actually moved.
> Atlanta: up 10 (r23 → r13). NY Giants: up 9 (r28 → r19).
> New Orleans: down 12 (r18 → r30). Tennessee: down 8 (r21 → r29).
> San Francisco: nothing. Still #1. Still #1 in big plays.
> Four-game sample, not opponent-adjusted. The engine is at thedirtcanon.com.

**Miami (voice-forward):**
> Last in the NFL in efficiency. Last in consistency. Nineteenth in big plays.
> Miami is not unlucky. Miami is losing the boring snap, over and over, and the boring snap is where the rent gets paid.
> Four-game sample, not opponent-adjusted. thedirtcanon.com

**Every caption carries the caveats. No pick, no spread, no "lock", no "guaranteed".** Responsible-play framing stays.

## 5. Schedule — built around the real slate, not generic best-guess times

**Caveat, stated plainly: we cannot verify "prime time." There is still no analytics access and no UTM tagging, so we are
inferring from convention, not from this account's data.** These times are hypotheses to be tested, not findings.

| When (ET) | Post | Why that slot |
|---|---|---|
| **Tue Oct 6, 12–1pm or 6–8pm** | **A. The Movement Report** + thread | today's news, elevated lunchtime/evening scroll |
| Wed Oct 7, 7–9am + 6–8pm | **C. The Two That Agree** (SF + BAL cards) | midweek authority post, no game competition |
| Thu Oct 8, 6–8pm | **B. The Contradiction Trio** (ATL/ARI/GB) | runs *before* TNF kickoff, not fighting it |
| Fri Oct 9, 12–1pm | **D. Miami** (reply-bait, pre-weekend) | highest-argument post lands before the slate |
| Sat Oct 10, 10am–12pm | **F.** Recaps: 6-card carousel (IG) + "everything before Sunday" (X/FB) | pre-game research peak |
| **Sun Oct 11, 1:00pm window** | GB card + MIA card, posted at kickoff, then **reply into live threads** | their games are live |
| **Sun Oct 11, 4:25pm window** | SF card + ARI card, posted at kickoff, reply into threads | SF@SEA, DET@ARI |
| **Sun Oct 11, 8:20pm SNF** | **E. BAL @ ATL** — the marquee, posted at kickoff | two cards, one game, biggest audience |
| Mon Oct 12, 10am–12pm | **The receipt**: what the numbers said vs what happened | closes the loop, feeds the Sunday eval pass |

**Platform shapes**
- **X** — card + 1–2 line caption. Note: 1080×1350 is 4:5 and X crops it in-timeline; either accept the crop or render a 16:9 variant. Replies into live threads are the growth play, not standalone posts.
- **Instagram** — 1080×1350 is native. Carousel for the Movement Report; single card otherwise.
- **Facebook** — card + the long caption; longest shelf life of the four.
- **YouTube Shorts** — **the pack contains no video.** A short must be produced (script + card motion). That's separate work, not a repost.
- **TikTok** — still **held** per the Oct-4 gate. Nothing posts there.

## 6. COLLEGE — HOLD, do not publish

The pack ships CFB Week 5 data, but it ships it *provisional* and says so itself:

- `COLLEGE HOLD`: the independent weekly schedule feeds returned only 25 events while the dataset holds 390 FBS-involving games; 250 of 250 team scores match in the retrieved 125-game subset, but **that is not a complete FBS audit**. 95 eligible plays lack EPA.
- The production renderer **hardcodes NFL rank labels** and was deliberately not modified — so college cards would carry *wrong* rank labels.
- College data reuse terms were not resolved; raw parquet is not bundled.

**Recommendation: no public CFB cards this cycle.** The AP-cohort table is useful internally (Indiana #7 AP, #1 in the cohort on efficiency; Miami #4 AP, #1 on consistency and big plays) but publishing numbers the pack itself flags as unaudited, with a renderer that would mislabel them, is exactly the credibility risk the brand's whole moat rests on. Tell me if you want otherwise and I'll say what it would take.

## 7. What I need to execute

1. **Which angles** — all six, or a subset. My pick for the week: A, B, C, D, E, with F as the rail.
2. **Publish approval** — standing rule: nothing posts without your explicit yes.
3. **How posting actually happens.** Do we have access to post as @TheDiRTCanon / @dirtcanon / the FB page / the YouTube channel — or do you post manually from a schedule I produce? I have not assumed an answer. (If it's the browser, your logged-in agent browser has the sessions; that changes the execution plan and needs your sign-off per post.)
4. **YouTube Shorts** — in or out this week, given the pack has no video?
5. **UTM tagging** — one line of effort and it's the difference between "we posted" and "we know if anyone came." Still unmeasured.