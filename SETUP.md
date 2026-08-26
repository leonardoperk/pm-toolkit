# PM Toolkit, Setup Checklist

Use this file to track your onboarding progress at a new company. Run `/setup` for guided step-by-step setup, or fill in files directly and check off items here.

---

## Quick Start

```
/setup
```

That command walks you through everything below, one step at a time, and writes your answers into the right files immediately.

---

## Checklist

### Priority 1, Core Context (Required for most commands)

These files are checked before every context-dependent command. Fill them in first.

- [ ] **`PRODUCT_CONTEXT.md`**, What the product is, who it's for, core features, tech stack, Jira structure, strategic priorities
- [ ] **`config/company-context.md`**, Company/business layer: overview, business model, competitors, team, metrics (product facts live in `PRODUCT_CONTEXT.md`)

### Priority 2, Engineering & Technical

- [ ] **`.claude/context/tech-stack.md`**, Backend, frontend, database, cloud infrastructure, deployment setup
- [ ] **`.claude/knowledge/jira-standards.md`**, Project keys, ticket hierarchy, user role names for stories, module/feature area examples

### Priority 3, Documentation & Workflows

- [ ] **`.claude/knowledge/team-conventions.md`**, Documentation tools, writing standards, how PMs collaborate with engineering
- [ ] **`.claude/commands/update-docs.md`**, ClickUp/Confluence/Notion workspace and document IDs for the `update-docs` command
- [ ] **`.claude/commands/sprint-documentation-review.md`**, Product doc section structure for the `sprint-documentation-review` command

### Priority 4, Design System (Optional)

- [ ] **`config/design-system.md`**, Component library, brand colors, typography, spacing tokens

---

## Files with `[FILL IN: ...]` Placeholders

The following files contain placeholders. Scan them to see what's still missing:

| File | What's in it |
| --- | --- |
| `PRODUCT_CONTEXT.md` | Product description, ICP, features, tech, Jira, strategy |
| `config/company-context.md` | Company overview, team, business model, metrics |
| `config/design-system.md` | Brand colors, components, typography |
| `.claude/knowledge/jira-standards.md` | Project keys, role names, module examples |
| `.claude/knowledge/team-conventions.md` | Tech stack, doc tools, team norms |
| `.claude/commands/update-docs.md` | Doc tool IDs and workspace URLs |
| `.claude/commands/sprint-documentation-review.md` | Doc section structure and IDs |

---

## How to Verify Setup

After filling in context, ask Claude:

```
What company am I at? What product do I work on?
```

If Claude answers correctly, setup is working. If it returns placeholder text or says it doesn't know, re-run `/setup` to fill in the remaining gaps.

---

## Resuming Setup

Run `/setup` at any time. It skips sections that are already filled in and picks up from where you left off.
