# Hermes setup audit — 14 layers

**Run:** 2026-10-06 · **Method:** read-only inspection (`hermes status/doctor/prompt-size/tools/skills/cron/mcp/fallback/memory/config/security audit`, direct read of `config.yaml` and the backup archive). **Nothing was modified except the backup in §12.**
**Verdict format:** FACTS (verified this run) vs RECOMMENDATIONS (my judgment). Ranked by practical impact.

---

## 0. Foundation (layer 1)

| Fact | Value |
|---|---|
| Install | Hermes **v0.21.5 (2026.9.24)**, method **git**, `C:\Users\Chris Rupert\AppData\Local\hermes\hermes-agent` |
| Python | 3.11.15 (venv in the install dir) |
| HOME | `C:\Users\Chris Rupert\AppData\Local\hermes` |
| Working dir | `C:\Users\Chris Rupert` (terminal `cwd: .`, `backend: local`) |
| `.env` | exists; API keys present: **OpenAI** only. Auth: **Nous Portal** logged in |
| Profiles | **default** (this one) + **kabloom** (gateway running, deepseek-v4.1-flash) |
| Sessions | 5 sessions, 2,207 messages, state.db 16.9 MB |

✅ Foundation is solid and understood. One fact to keep in mind: **`terminal.backend: local`** — terminal and file tools run with
Chris's own OS-user permissions. That is not a sandbox (blueprint layer 5).

## 1. Models (layer 2)

- **Primary:** `deepseek/deepseek-v4.1-flash` via **nous** (Nous Portal, `chat_completions`).
- **Fallback chain: present, 2 entries** — `z-ai/glm-5.2` → `deepseek/deepseek-v4-flash-0731`, both via nous. ✅
- **Auxiliary slots: only two configured** — `skills_hub` and `mcp`, both on the *same* model as the primary
  (`deepseek/deepseek-v4.1-flash`). Everything else (compression, vision, titles, approvals, routing) runs on defaults.
- **MoA is ENABLED** (`moa.enabled: true`, `fanout: user_turn`) with aggregator `openrouter / anthropic/claude-opus-4.8`
  — and **neither OpenRouter nor Anthropic credentials exist** (see `hermes status`). Enabled config that cannot authenticate.

## 2. Memory & Context (layer 3)

- **Built-in memory: near-full** — MEMORY 2,764/3,000 chars (92%), USER 1,313/1,375 (95%). Every add now forces an eviction.
- **`memory.provider: supermemory` and it is ACTIVE but has no `SUPERMEMORY_API_KEY`.**
  `hermes doctor`: *"supermemory configured but not available."* This is a configured layer that does not work.
- Other memory plugins installed: hindsight, memory-wiki, mnemosyne-dashboard.
- **No project context files anywhere** — checked `agent-control-room`, `XRBrain`, `report-vetter-bot`, home: no
  `AGENTS.md` / `.hermes.md` / `HERMES.md` / `CLAUDE.md`. (The jev-ultrafast clone has one, from upstream.)
- Session history is real and searchable (state.db + FTS).

## 3. Agent structure (layer 4)

One durable specialist profile (**kabloom**) + the default agent. Correct per the rule *temporary independence gets
delegated, durable state gets separated* — Kabloom has its own memory, skills, cron and SOUL.

## 4. Tools & permissions (layer 5)

24 toolsets enabled for `cli`: browser, clarify, code_execution, **computer_use**, connections, cronjob, delegation, file,
**image_gen**, kanban, memory, **mnemosyne-dashboard**, session_search, skills, terminal, todo, **tts**, **video**,
**video_gen**, vision, web, x_search.

Bold = no established workflow for them in this setup (recommendation, not fact).
MCP servers: **notion (✓), railway (✓, 67 tools), vercel (✓, 239 tools)** enabled; hugging_face and stripe disabled.
Approvals: no `--yolo`, smart approval active (it fired correctly during this session).

## 5. Skills (layer 6)

0 hub-installed, **49 builtin, 20 local — 69 enabled, 0 disabled.** No junk-drawer bloat, but two local skills look like
near-duplicates: `hermes-bot-forge-bot` and `venture-bot-spawning`. Skills Hub directory not initialized.
Index cost is ~60–95 B per skill (progressive disclosure working as intended).

## 6. Plugins, MCP & integrations (layer 7)

Plugins enabled: bot-forge, disk-cleanup, hermes-office, hermes-resetwatch, hindsight, memory-wiki, mnemosyne-dashboard,
security-guidance. Bundled web providers present but unkeyed (tavily/keyless rotation, firecrawl active via `web.backend: nous`).

## 7. Projects & knowledge (layer 8)

`hermes project list` → **none created.** The Control Room and XRBrain act as durable workspaces by convention, not by
configuration, and neither carries a project context file. Rules currently live in memory + skills instead of next to the work.

## 8. Automation (layer 9)

Default profile: **0 cron jobs.** Kabloom profile: **2** (Sunday eval `0 17 * * 0`, Monday planning `0 9 * * 1`) — both ran
successfully, both deliver to `bot-chat:kabloom`. Automation is scoped to the one agent that needs it. ✅

## 9. Multi-agent (layer 10)

Bot Mode with Kabloom; delegation available (max 9 concurrent, 250 iterations; no kanban tasks exist). Human approval points
are in place by policy (publish/spend gates). ✅

## 10. Cost & token optimization (layer 11)

- `hermes prompt-size` baseline: memory 3.4 KB, code_execution 2.9 KB, web 1.9 KB, tts 1.8 KB, clarify 1.7 KB, vision 0.8 KB —
  small, because MCP tools are deferred rather than always-on.
- **Aux model routing not done** (aux = primary model) — the blueprint's cheapest structural win.
- Unused toolsets add schema weight (layer 5 list).
- **Memory is at its cap**, which forces eviction churn — that is the "cheapest token is the one you never spent" problem in the other direction.

## 11. Reliability & recovery (layer 12) — **this was the worst layer**

- **FACTS: there was NO backup. `AppData\Local\hermes\backups\` contained only a `config` dir. `updates.pre_update_backup: false`.**
- ⚠️ **The install is 7,822 commits behind `origin/main`** (`hermes update --check`). Updating restarts the gateway and
  kills running agents, so it is a scheduled operation, not a casual one.
- `hermes doctor`: 3 npm advisories (agent-browser 1, web workspace 6, ui-tui 5).
- **ACTION TAKEN (this run):** created and verified a full backup —
  `C:\Users\Chris Rupert\OneDrive\hermes-backups\hermes-full-2026-10-06.zip`, **70 MB, 1,368 entries, zip integrity OK**,
  contains `config.yaml`, `.env`, `auth.json`, `state.db`, `memories/MEMORY.md`, `memories/USER.md`, `SOUL.md`,
  all 744 skill entries, and the full **kabloom** profile (config, SOUL, cron/jobs.json).
  **Off-machine** (OneDrive-backed). This is the first backup this setup has ever had.

## 12. Security & maintenance (layer 13)

`hermes security audit` findings in the install venv: **PyJWT 2.13.0** (7 advisories, fixed in 2.14.0) and
**urllib3 2.7.0** (3 advisories, fixed in 2.8.0) — plus the 3 npm workspaces from doctor. These are dependency exposures,
not compromises, and the 7,822-commit update very likely resolves them.
Secrets: `.env` + `auth.json` only; no external secret store (bitwarden/1password) configured. Approvals on. Local execution.

## 13. Self-audit (layer 14)

Not yet a repeatable procedure — performed ad hoc just now. Should become a skill (read-only, produces this document).

---

## Ranked change list — FACTS vs RECOMMENDATIONS

| # | Change | Layer | Why | Risk if we don't |
|---|---|---|---|---|
| 1 | ✅ **Backup created + verified** | 12 | recovery layer was empty | one bad update = rebuilt setup |
| 2 | **Keep `updates.pre_update_backup: true`** | 12 | update is 7,822 commits; auto-backup before it | updating without a rollback point |
| 3 | **Run `hermes update`** (after backup) | 1,12,13 | 7,822 behind; likely clears PyJWT/urllib3/npm advisories | drift + known CVEs |
| 4 | **Decide `supermemory`**: add the key or revert `memory.provider` to built-in | 3 | configured-but-broken layer; doctor flags it | silent memory confusion |
| 5 | **Decide MoA**: disable, or repoint the aggregator at `nous` | 2,11 | enabled with unauthenticated aggregator | dead config that looks live |
| 6 | **Initialize Skills Hub** (`hermes skills list`) | 6 | doctor issue | can't install/maintain hub skills |
| 7 | **Consolidate memory + move procedures to skills** | 3,11 | 92%/95% full, every add forces eviction | facts get evicted to make room for trivia |
| 8 | **Add project context files** (Control Room `AGENTS.md`) | 8 | rules belong next to the work | rules re-explained every session |
| 9 | **`hermes doctor --fix`** | 13 | 3 npm advisories | drift |
| 10 | **Route aux slots (skills_hub, mcp) to a cheaper model** | 11 | aux currently = flagship | paying flagship rates for lookups |
| 11 | **Prune unused toolsets** (computer_use, video_gen, image_gen, video, tts, connections, mnemosyne-dashboard) | 5,11 | schema weight on every call | slow, expensive, noisy tool surface |
| 12 | **Audit the 20 local skills** (merge `hermes-bot-forge-bot` + `venture-bot-spawning`) | 6 | duplicate procedures | two skills that disagree |
| 13 | **Create a named project for the Control Room** | 8 | durable workspace + Desktop grouping | convention-only workspace |
| 14 | **Make this audit a skill + optional monthly cron** | 14 | repeatable self-inspection | drift goes unnoticed |

**Not recommended now** (blueprint: let real usage earn them): external memory providers, skill auto-load, more MCP
servers, more specialist profiles, deeper multi-agent coordination, isolated execution backends, event-driven automation.