# THREE NUMBERS — JSON rendering handoff

Six NFL cards using the retained September 29 research snapshot, not a new data refresh. Each cards/*.json contains exact full-precision inputs and explicit display strings. six-teams.json combines them. template-spec.json defines positions in the bundled reference coordinate system and the approved overrides.

## What this does and does not provide
These are data and design specifications, not an executable card template. The approved PNG is a flattened visual reference; it is NOT a blank background to overlay with new numbers. A renderer must rebuild/clear its variable regions and supply suitable typography. Original font identities and layered source artwork are unavailable. No exact-appearance guarantee is made. Do not use the previously generated approximate renderer as proof of reference fidelity.

The actual compass and six team emblems are included. Do not stretch the compass or put words underneath it. Series is THREE NUMBERS only. Keep all numeric text typeset in code or your design application. If a rendering tool ignores coordinates or substitutes fonts, JSON cannot prevent a changed design.

## Data
NFL nflfastR/nflverse play-by-play: https://github.com/nflverse/nflverse-data/releases/tag/pbp ; model documentation https://nflfastr.com/ . Audited snapshot: 48 season games, 16 Week 3 finals, 5,814 eligible league plays, no missing eligible EPA. Week 3 final scores and team box totals checked; Weeks 1–2 box totals not independently rechecked in this run. Included audit and computation script preserve calculations. No college cards: college classification/slate audit remains provisional.

EPA means expected points added: change in expected offensive scoring value given game situation. Success is positive EPA. Explosive is completed pass gain at least 20 yards or rush gain at least 10. Denominators are eligible scrimmage plays; sacks/scrambles/overtime included, kneels/spikes/no-plays/conversions/special teams excluded. No opponent adjustment. Compare within NFL only. Round final display after full-precision subtraction. Percentage differences are percentage points.

Stamps label rank bands only (new explicit handoff convention), not established talent: ranks 1–4 TOP EIGHTH, 5–8 TOP QUARTER, 9–24 MIDDLE HALF, 25–28 BOTTOM QUARTER, 29–32 BOTTOM EIGHTH. Three-game sample. The original reference's ELITE/STRONG assertions are not inherited.

Do not reproduce the reference's old data, dates, opponent or causal verdict. This handoff does not modify GitHub or deploy a renderer. Team emblems are supplied for identification; no ownership or reuse-rights grant is implied.
