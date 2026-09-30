# Hermes 14-Layer Blueprint — State Audit + Morning Roadmap

Source: article reviewed 2026-09-30 ("I would rebuild Hermes in layers" — 14 areas, 8 stages).
Loaded file: `AppData\Local\hermes\composer-pastes\pasted_content_2026-09-30_02-46-14-634_61b100.txt`.

**Verdict first: this is an audit, not a rebuild.** The article's rules are largely already true here (doctrine, layered memory, project context, skills discipline). About 70% of the 14 areas are done or partially done. The gaps are concentrated: **recovery, measurement, tool-surface pruning, gateway service, automation discipline, self-audit.** Everything below was verified against `config.yaml` and live state — not assumed.

---

## State per area (verified 2026-09-30)

| # | Area | State | Evidence / gap |
|---|------|-------|----------------|
| 1 | Foundation | 🟡 | One install (v0.21.5), one main profile (`default`), known dirs, one model. **Gap: gateway is a manual spawn — `hermes gateway install` never run → every reboot re-breaks bot-forge tools.** `hermes doctor` never run. |
| 2 | Models | ✅ | Primary `deepseek/deepseek-v4.1-flash`. **Fallbacks already configured** (nous `z-ai/glm-5.2`, `deepseek-v4-flash-0731`) + MOA preset (kimi-k3). Auxiliary slots on defaults per article. |
| 3 | Memory & Context | ✅ | SOUL = operating doctrine; built-in memory 80% (1,762/2,200 — near cap, prune soon); project context = Control Room project.md/HANDOFF/docs; session_search anchors sessions; XRBrain = external durable KB. Article's placement rules already followed. |
| 4 | Agent Structure | ✅ | 1 main profile + **Kabloom** (earned durable separation: Dirt Cannon has live work) + delegation proven (Life OS build used 2 parallel subagents). Matches "temporary → delegate, durable → separate." Liensight still has no desk. |
| 5 | Tools & Permissions | ❌ | **22 toolsets enabled on CLI** (browser, clarify, code_execution, computer_use, connections, cronjob, delegation, file, image_gen, kanban, memory, mnemosyne-dashboard, session_search, skills, terminal, todo, tts, video, video_gen, vision, web, x_search). Several have no evident workflow: computer_use, video, video_gen, kanban, tts, mnemosyne-dashboard, connections. Article: "if you can't explain why a capability is enabled, question it." |
| 6 | Skills | ✅ | Just audited + merged 2026-09-29 (3 deleted, 2 absorbed → `source-to-action-items`, `life-review`+weekly reset). 6 Life OS skills created. Progressive disclosure kept; no auto-load (correct per article). |
| 7 | Plugins, MCP & Integrations | 🟡 | **8 plugins enabled**: bot-forge (used), disk-cleanup, hermes-office, hermes-resetwatch, hindsight, memory-wiki, mnemosyne-dashboard, security-guidance — usage of the 7 non-bot-forge ones unverified. **3 MCP servers enabled**: notion, railway, vercel (hugging_face + stripe disabled). Railway has no job — deployment target is Hetzner, not Railway. Notion/Vercel usage unverified. |
| 8 | Projects & Knowledge | ✅ | Control Room (project.md source of truth), XRBrain vault, report-vetter-bot repo, HANDOFF.md — "serious recurring work has a permanent home" is done. |
| 9 | Automation | 🟡 | **0 cron on main profile** (correct — nothing stable enough; the OCRe-scoring is a /goal job, not cron). Kabloom got 2 routines **on day 1** (Mon 9am calendar, Sun 5pm eval) — article rule: run a workflow manually from a fresh session BEFORE scheduling it. First-run verify both before trusting. |
| 10 | Multi-Agent Workflows | ✅ | Delegation for temporary independence; Kabloom for durable. No supervisor chains (no coordination problem yet). Human approval points wired (publish/spend/delete). |
| 11 | Cost & Token Optimization | ❌ | **Nothing measured.** `hermes prompt-size`, `/usage`, `/compress` never run. Pipeline costs known ($5/1k pp Mistral; Jev ~420 tok/call) but Hermes session baseline is unmeasured. Article: "measure first, optimize second." 22 toolsets + 8 plugins + 63 skills = real schema weight in every session. |
| 12 | Reliability & Recovery | ❌ | **Biggest gap.** `hermes backup` never run. No restore test. Backup lives in a doc (`System/backups.md`) but no off-machine copy executed — OneDrive exists and syncs; XRBrain is local-only git (no remote) → single drive failure loses the life KB. Gateway not a service (reboot trap). |
| 13 | Security & Maintenance | 🟡 | Secrets doctrine strong (.env only, never chat). `hermes security audit` never run; `hermes doctor` never run. 8 plugins un-audited. Article: "if you can't remember why a plugin is installed or where a credential came from, the system is asking for maintenance." |
| 14 | Audit Itself | ❌ | Nothing. The article's finale (read-only self-audit prompt) is exactly the operating doctrine's "final verification" — should be a skill or routine. Cheap to build, high value. |

---

## Real gaps, ranked by practical impact

1. **G1 — Backup & recovery (article 12).** Run `hermes backup` (full, incl. credentials) to a location outside the machine + OneDrive copy of XRBrain + restore test. Refuse to let this stay "later." ~30 min tomorrow.
2. **G2 — Gateway service (article 1).** `hermes gateway install` once → kills the reboot trap permanently. ~2 min.
3. **G3 — Measurement (article 11).** `hermes prompt-size` baseline + `/usage` after a normal session. One number each. ~10 min.
4. **G4 — Tool-surface prune (articles 5, 7, 13).** `hermes tools --summary` + `hermes security audit`; disable unused toolsets (computer_use/video/video_gen/kanban/tts?), disable Railway MCP (no job), audit the 7 non-bot-forge plugins. Frees schema weight every session. ~30 min.
5. **G5 — Automation discipline (article 9).** Run Kabloom's Monday-calendar pass manually first (fresh session), then let cron own it. Verify Sun eval pass likewise. ~15 min.
6. **G6 — Self-audit (article 14).** Build the read-only audit as a skill/routine: profile, model routing, prompt-size, memory placement, installed+auto-loaded skills, toolsets, plugins/MCP, cron health, logs+doctor, backup posture → facts vs recommendations, ranked, nothing changed without approval. ~45 min.
7. **G7 — Memory cap (article 3).** Built-in memory at 80% and near-cap — prune/consolidate the 5 entries (the XRBrain + doctrine + Control Room entries can compress). ~10 min.

## Deliberately NOT building now (article areas that must wait — why)

- **External memory provider** — no missing job: built-in memory + XRBrain + session_search already cover retrieval. (Article: "don't install one just to feel advanced.")
- **More profiles/bots** — Liensight has no standing work; Kabloom earned its desk (live venture). One-profile-until-it-earns-one is already the rule here.
- **Kanban/worktrees/named projects** — no coordination problem yet; the Hetzner port will earn these.
- **More plugins/MCP** — Railway is a candidate to *remove*, not add. Hetzner phase may bring Lightpanda/BrowserSkill evaluations.
- **Computer-use / video / video_gen** — no workflow today beyond Tier-4 territory; keep disabled until a job exists.
- **Skill auto-load** — article says use sparingly; progressive disclosure is right for this mixed workload.

## Morning execution order (timeboxed, ~2h total)

1. G2 gateway install (2 min) → verify `list_agents` from a fresh gateway.
2. G1 backup: `hermes backup` → restore-test the archive; copy XRBrain to OneDrive (life KB goes from single-drive to recovered).
3. G3 prompt-size + usage baseline (record both numbers in System/changelog).
4. G4 `hermes tools --summary` + `hermes security audit` + disable unused toolsets/MCP/plugins with owner approval for each.
5. G5 Kabloom manual first-run of the Monday calendar pass (this is also a Dirt Cannon task — pairs with the OneDrive shared-folder handoff already agreed).
6. G7 memory prune (batch: remove stale, consolidate).
7. G6 self-audit skill build (the article's finale prompt, adapted to this exact setup).

## Note for morning: what the article got right vs what's already here
- Right: layers are jobs, not features; one brain first; measure before deleting; automate only the stable; don't schedule what needs babysitting; backup before you need it. All match the operating doctrine.
- Already here: layered memory placement, project-context-first, delegation-before-bots, skills hygiene, secrets doctrine. Do not rebuild these — the article validates them.
