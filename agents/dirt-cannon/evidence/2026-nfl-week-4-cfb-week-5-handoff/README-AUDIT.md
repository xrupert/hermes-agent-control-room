# Evidence — THREE NUMBERS, NFL Week 4 / CFB Week 5 (throw 2026-10-06)

Source zip: `C:\Users\Chris Rupert\Downloads\dirt-canon-three-numbers-nfl-week-4-cfb-week-5-2026.zip` (12.1 MB, 74 files).
Copied here for audit this pass.

**`source/` is deliberately NOT committed** (18 MB of raw feed snapshots — `nfl.csv.gz`, per-game ESPN summary JSON,
CFB week feeds). It stays on disk locally and in the zip, which is the archival copy. The pack documents each feed's
URL and hash in `source/retrieval.json` / `source/checks-retrieval.json`, so the snapshot is re-derivable.

## Verified this pass (independently re-read, not taken on the pack's word)
- `nfl-audit.json`: 7,789 eligible plays · `missing_epa=0` · `missing_yards=0` · `duplicate_ids=0` · games by week 16/16/16/16
- `latest_week_score_checks`: 16/16 `final_match: true` (Week 4 finals vs ESPN)
- `nfl-boxscore-audit.csv`: 32/32 yards match · 32/32 plays match
- Six cards: all 1080×1350 PNG (read from PNG IHDR headers)
- Week-5 slate from the ESPN scoreboard feed: 15 games, matching the pack's two byes (CAR, KC). All six card teams play Sun Oct 11.

## Not verified / flagged
- College is **PROVISIONAL with a COLLEGE HOLD** (incomplete FBS audit; 95 plays missing EPA; renderer hardcodes NFL rank
  labels). Not publishable. See `drafts/2026-10-06-W41-publish-plan-week4-cards.md` §6.
- The pack ships **no picks, no spreads, no confidence numbers** — descriptive only. Zero gradeable calls.