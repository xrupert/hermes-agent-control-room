# Team Ops — Bot Team Maintenance Contract

Source: user-provided guide (2026-09-29, "Profiles are the feature. Boundaries are the moat",
credited to @neoaiforecast + operator-layer additions). Adapted from the generic 4-role model
(Hermes/Alan/Mira/Turing) to THIS user's venture-shaped org chart. Roles dissolve into ventures;
the operator layer survives intact.

## Roster (venture-shaped; this chat = orchestrator)

- **this chat (orchestrator)** — plans, decomposes, routes, approves, synthesizes. The OCR engine
  room. Only surface that approves: contract gate, spending, permission widening, merge to main.
- **cybrid-ops bot (Turing's job)** — owns report-vetter-bot deterministic tests, golden-packet
  scoring, Hetzner port scaffolding. Evidence: 91/91 green, scored real files. [not yet spawned]
- **liensight bot (Alan's job)** — source-first, skeptical, uncertainty-tagged research into HUD
  non-loan liens; builds the Tier-2 asset. [not yet spawned]
- **dirt-cannon bot (Mira's job)** — audience-aware sports content from validated material.
  [not yet spawned]

Rule: a bot gets created only when its venture is approved AND the OCR pipeline is at the
contract gate (Tier 4 stays caged). No generic role clones.

## Handoff contracts — the only new machinery

Every handoff between bots (or bot → orchestrator) gets ONE file per pair under
`agent-control-room/handoffs/<from>-to-<to>.md` with exactly four fields:

1. **Input shape** — what the receiver expects (e.g. liensight → orchestrator: ranked claims
   with source URLs + confidence tags, NOT raw transcripts)
2. **Output shape** — what the receiver returns (e.g. orchestrator → dirt-cannon: approved
   angle + source packet, NOT "a finished article")
3. **Failure action** — block / require-human-review / retry-with-adjusted-prompt
4. **Verification gate** — one assertion that must hold before the handoff completes (e.g.
   "every claim carries a source URL"; "every fix has a passing test")

A contract that cannot block is decoration. If input fails the declared shape, the handoff
FAILS and routes to the orchestrator. This is the anti-rot mechanism — it makes specialization
durable past day 30.

## Memory hygiene per bot

Memory rots inside each profile the same way a wiki rots past 100 pages. Weekly per-bot audit:
`hermes -p <bot> memory-kpi --json` (or check the memory file directly). Watch `stale_notes`;
past ~15% of total notes, run a resolve pass before the bot starts quoting obsolete context.
Same rule as the doctrine's memory discipline: durable facts in, task logs out.

## SOUL stability (anti-drift)

- Cap each SOUL.md at ~400 words. Identity lives in SOUL; project context lives in
  agent-control-room/agents/<venture>/project.md (or AGENTS.md). Never the reverse.
- **No SOUL.md edit without a logged reason.** Diff each SOUL weekly against its day-one
  version; any new responsibility gets an approval entry or it gets reverted. This is the
  specific defense against "Mira is slowly becoming Turing."

## Cron discipline

One shared schedule file: `agent-control-room/team/cron.md` listing every scheduled task across
every bot — exact time, duration, dependency. Check the file BEFORE adding any cron; stagger
collisions. (Currently: zero scheduled tasks. The only candidate is a future
golden-packet-scoring routine — coordinate before enabling.)

## Policy ceilings (narrowest permission, per doctrine)

- Research bot: read web/repo, write to its own venture folder only. No shell outside sandbox.
- Content bot: read research outputs, write drafts only. No secrets, no code execution.
- Engineering bot: read repo, sandboxed tests, feature branch. Merge to main = orchestrator only.
- Orchestrator (this chat): only surface that merges, widens permissions, or spends above budget.
- **No bot gets more permission than its role needs; only the orchestrator widens scope.**

Encoded per bot in its SOUL.md `Never` section + approvals list at creation. (Defaults:
sending/publishing, spending money, deleting data all require approval — keep them.)

## Guardrails (quote directly)

- No SOUL edit without a logged reason
- No handoff accepted without the declared input shape
- No role widened without orchestrator approval
- No cron added without checking the shared schedule
- Keep roster + contracts + schedule under source control (this repo); every edit is a commit
