# PM Toolkit

A working product manager's command suite for Claude Code. It turns the recurring parts of the PM job, writing PRDs, cutting user stories, forecasting sprints, reading support tickets, tracking competitors, into commands I run instead of tasks I grind through by hand.

I built it for my own work and kept sharpening it. This repo is the generic version: no company data, ready to drop into a new job.

## What you can build with it

Each command is a full workflow, not a prompt. The main ones:

| Command                        | What it does                                                                                                          |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------- |
| `/create-prd`                  | A conversational PRD interview using a problem-first template, then writes the doc and opens the epic in your tracker |
| `/generate-user-stories`       | Turns a PRD into tracker-ready stories in one coherent pass, with consistent roles and acceptance criteria            |
| `/review-prd`                  | Reviews a PRD from four angles at once, engineer, executive, user researcher, product analyst, as separate agents   |
| `/forecast-sprint`             | Monte Carlo sprint forecast from your real historical throughput, with a completion probability and distribution      |
| `/forecast-epic`               | Epic timeline forecast from historical epic velocity and story count, in four scenarios                               |
| `/cs-monthly-review`           | Reads a month of support tickets and returns ranked bugs, feature requests, pain points, and gaps                     |
| `/competitive-research`        | Researches competitors in parallel and synthesizes landscape, positioning, and whitespace                             |
| `/generate-release-notes`      | Pulls a sprint's shipped tickets and writes customer-facing notes                                                     |
| `/sprint-documentation-review` | Checks what shipped against the product docs and drafts the updates                                                   |

Plus scripts (RICE prioritization, interview analysis), document generation (xlsx/pdf/docx/pptx), and a strategy-framework library. Full reference: [docs/slash-commands-cheat-sheet.md](docs/slash-commands-cheat-sheet.md).

## Why it beats doing this without AI

Not "AI is faster." The specific gains, honestly:

| Task | Without the toolkit | With it |
|---|---|---|
| PRD | Fill a static template, hope you asked the right questions | An interview that adapts to your answers and flags the gaps |
| Sprint estimate | Gut feel, or a velocity average that hides variance | A probability from thousands of simulations on your real throughput |
| PRD review | Schedule three stakeholders, wait days | Four role-specific reviews in one run, before you spend anyone's time |
| Support triage | Read hundreds of tickets, lose the patterns | One pass that ranks the recurring themes with ticket counts |
| Release notes | Reconstruct what shipped from memory | Pulled straight from the sprint's done tickets |

The point is judgment leverage: the toolkit does the reading, drafting, and arithmetic so the PM spends time on the decisions.

## Outcomes

### What you can build with it

Concrete things you walk away with, not features:

- A PRD that's been pressure-tested from four angles before it reaches a single stakeholder.
- A sprint commitment backed by a completion probability you can defend in planning, instead of a number you hope holds.
- A month of support tickets turned into a ranked, evidence-backed list of what to fix next.
- A competitive landscape and whitespace map you can bring straight into a roadmap review.
- Customer-facing release notes and KB articles ready the day a feature ships, drawn from the actual tickets.
- A backlog scored by RICE, prioritized by evidence rather than by whoever argues loudest.

### From my own use

- Drafting a PRD went from the better part of a day to an hour at most. The interview does the structuring I used to do by hand.
- An epic forecast projected 14 sprints for work that had been scheduled for 5. Far enough off that it forced a strategic rethink, not just a reschedule.
- Building my own tools became routine, this toolkit is one of them.
- I prototyped a new automation with this workflow; it was later built out properly and shipped as a product feature.

## How it's built

- **Commands** (`.claude/commands/`), each an end-to-end workflow.
- **Agents** (`.claude/agents/`), engineer / executive / user-researcher / product-analyst, called for independent, parallel review.
- **Knowledge & context** (`.claude/knowledge/`, `.claude/context/`), company facts the commands read at runtime, filled once via `/setup`.
- **Single source per fact**, product context, tech stack, and tracker structure each live in one place; nothing is duplicated across files.

The toolkit is deliberately tool-neutral: it works with whatever issue tracker, docs tool, and support system you connect, with Jira / ClickUp / Zendesk named only as examples.

```
pm-toolkit/
├── .claude/            # commands, agents, skills, knowledge, context
├── config/             # company/business context
├── templates/          # PRD, frameworks, project templates
├── tools/              # forecasting, kb-generator scripts
├── docs/               # cheat sheet + guides
├── projects/           # your work folders
└── PRODUCT_CONTEXT.md  # always-on product context
```

## Honest limitations

- It doesn't replace judgment. The forecasts assume stable teams; the reviews are a first pass, not sign-off; the PRD is a draft you still own.
- It needs real data to be useful, an empty `/setup` produces empty output.
- The forecasting uses ticket counts, not story points, and assumes comparable work across sprints.
- It's built around my way of working. Adopting it means adopting some of those conventions or changing them.

## Getting started

1. Run `/setup`, a guided interview that fills in your company context (product, tech stack, tracker keys, personas). About 10–15 minutes. See [SETUP.md](SETUP.md) for the checklist.
2. Try a command: `/create-prd` to draft a PRD, or `/forecast-sprint` once you have a few sprints of history.
3. Full command reference: [docs/slash-commands-cheat-sheet.md](docs/slash-commands-cheat-sheet.md).

**Needs:** Node.js, Git, GitHub CLI (`gh`), and Python 3 (for the scripts). A tracker/docs/support integration connected in Claude Code for the commands that read them.
