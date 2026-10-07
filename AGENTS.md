# Control Room — Agent Rules

This is the durable home for venture orchestration. Three ventures live here:

1. **Cybrid Title** (Tier 1) — OCR title-report examination. Center of gravity. Source of truth: `agents/cybrid-title/project.md`.
2. **Dirt Cannon** (Tier 3) — viral sports/DFS content studio. Bot: Kabloom (profile: kabloom). Desk: `agents/dirt-cannon/`.
3. **Liensight** (Tier 2) — HUD non-loan product. No desk yet; waits at the gate.

## Operating doctrine

Full text: `OPERATING_DOCTRINE.md`. Governs ALL Hermes/agent work — plan before acting, source-first lookup, effort matched to stakes, self-contained delegated briefs, evidence before claims, stop conditions, final verification. Bots spawned via bot-forge get this doctrine wired into their SOUL.

## Standing rules

- **Secrets** go in `~/.hermes/.env` or the project's `.env` — never in chat, never committed.
- **Venture repos** live in `C:\Users\Chris Rupert\code\` — never in Hermes cache/scratch (pruning destroyed earlier clones).
- **Dirt Cannon desk rule** (owner-mandated 2026-10-06): any item awaiting an owner decision is CANCELLED after 24h in limbo, not carried forward and never re-asked; resurrection is explicit and per-item. Rule file: `agents/dirt-cannon/decisions/STALE-POLICY.md`.
- **Publish/spend/delete/new-account** — always needs owner approval. No exceptions, no "I figured you'd want it."
- **Numbers are never invented.** Dirt Cannon metrics come from verified handoffs (`OneDrive\Daily Fantasy\DiRT Canon Reports` + three-numbers JSON). No fabricated wins, no invented track records.
- **XRBrain** (user's private Obsidian vault at `C:\Users\Chris Rupert\code\XRBrain`) is the source of truth for personal/life context. Read `agent_rules.md` there and search the vault BEFORE answering personal questions. Venture/business truth stays here.
- **Local Qwen 3.8-27B** runs at `http://127.0.0.1:18434/v1` (llama.cpp, API-key auth via `LLAMA_API_KEY` in `.env`). Model name: `Qwen3.8-27B-UD-Q4_K_M`. Use for auxiliary tasks (skills_hub, mcp) to save cloud spend.
- **Hermes backup**: `OneDrive\hermes-backups\` — full backups before updates. `pre_update_backup: true` is on.

## Hermes setup audit

`HERMES-SETUP-AUDIT.md` — 14-layer audit run 2026-10-06. Read before changing Hermes config.
