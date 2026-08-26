---
description: "Guided onboarding: fill in company context to activate the PM toolkit"
---

# Setup Command

You are executing the `/setup` command to guide the user through filling in company-specific context so the PM toolkit is ready to use at a new company.

## Overview

This command walks through each context file that contains `[FILL IN: ...]` placeholders and helps the user populate them with their company's real information.

Work through the sections **one at a time**, asking questions and writing the answers into the appropriate files immediately. Do not ask everything at once.

---

## Step 0: Welcome

Start with:

```
Welcome to PM Toolkit setup!

This will take about 10–15 minutes. We'll go through your company context step by step and fill in the toolkit so it's ready to use.

You can stop at any time and come back later, just run /setup again and I'll pick up where we left off (skipping anything already filled in).

Let's start with the basics.
```

---

## Step 1: Company & Product Basics

Ask:
1. What is the company name?
2. What is the product name? (same as company, or different?)
3. Write a one-sentence description of what the product does and who it's for.
4. When was the company founded?
5. What stage/funding? (Seed, Series A, Series B, bootstrapped, etc.)
6. How many customers do you have?
7. What markets/geographies do you focus on?

**After getting answers:** Update the following files:
- `PRODUCT_CONTEXT.md`, top section "What It Is"
- `config/company-context.md`, "Company Overview" section

---

## Step 2: Ideal Customer Profile

Ask:
1. Who is your perfect-fit customer? (industry, company size, key characteristics)
2. Who do you also serve but don't actively pursue?
3. Who is explicitly NOT a fit?

**After getting answers:** Update:
- `PRODUCT_CONTEXT.md`, "Ideal Customer Profile" section (perfect fit, company size, industries, also/not served). `config/company-context.md` → "Target Market" is just a pointer here, don't duplicate.

---

## Step 3: User Roles & Personas

Ask:
1. What are the user roles in the product? (e.g. "Agent, Admin, Super Admin")
2. For each role: what do they do in the product?
3. Who is the primary end user (highest usage volume)?
4. What are their top 3 pain points today?
5. What does a successful day look like for them?
6. Who is the secondary user? Same questions.
7. Is there an admin/manager role? What do they care about?

**After getting answers:** Update:
- `PRODUCT_CONTEXT.md`, "User Roles" and "User Personas" sections

---

## Step 4: Core Product Features

Ask:
1. What are the 5–8 core features of the product? (brief name + one-line description each)
2. What are the key integrations? (external tools/platforms the product connects to)
3. What are the most important limitations users should know about?

**After getting answers:** Update:
- `PRODUCT_CONTEXT.md`, "Core Features", "Key Integrations", "Key Limitations" sections

---

## Step 5: Tech Stack

Ask:
1. What is the backend tech stack? (language/framework, e.g. "Ruby on Rails + NestJS")
2. What is the frontend framework? (e.g. "React 18 + TypeScript", "Vue 3")
3. What database do you use? (e.g. "PostgreSQL")
4. What cloud provider? (e.g. "AWS", "GCP", "Azure")
5. Is there a hybrid architecture? (e.g. legacy + new services)
6. What is the deployment setup? (e.g. "Docker + ECS", "Kubernetes", "Serverless")

**After getting answers:** Update:
- `.claude/context/tech-stack.md`, full file (backend, frontend, database, infrastructure, complexity guidance). This is the canonical tech-stack source.
- `PRODUCT_CONTEXT.md`, "Tech Stack" section: only the one-line **Platform** field (e.g. "SaaS web app + mobile app"). Don't duplicate the stack detail here.

---

## Step 6: Jira & Project Management Setup

Ask:
1. What project management tool do you use? (Jira, Linear, Asana, etc.)
2. If Jira: what are your project keys? Capture them as the toolkit's three project placeholders:
   - `[PRODUCT_PROJECT]` = product / PRD / sprint-planning project (epics & stories land here)
   - `[ENG_PROJECT]` = engineering project (velocity reference for forecasts)
   - `[SUPPORT_PROJECT]` = customer-support project (CS tickets)
3. What is the ticket hierarchy? (e.g. "Epic > Story > Sub-task + Bugs")
4. How does work flow from PM to Engineering?
5. What are your user role names in Jira stories? (e.g. "Agent, Admin, Super Admin")
6. What are your typical module/feature area names for story titles?

**After getting answers:** Update:
- `PRODUCT_CONTEXT.md`, "Jira Structure" section: only **hierarchy** and **workflow** (not the project keys, those go in jira-standards, referenced by a pointer here)
- `.claude/knowledge/jira-standards.md`, the canonical project-key source: fill the "Jira Projects" table (placeholder → real key), plus role names, module examples, team assignment

---

## Step 7: Documentation Setup

Ask:
1. Where does your product documentation live? (ClickUp, Notion, Confluence, etc.)
2. What is the URL to your main product doc?
3. If ClickUp: what are the Workspace ID, Doc ID, and Page ID?
   (Find these in the URL: app.clickup.com/[workspace]/docs/[doc-id])
4. What is the top-level structure of your product documentation?
   (e.g. "Section 1: Overview, Section 2: User Roles, Section 3.1: [Module], etc.")

**After getting answers:** Update:
- `config/company-context.md`, "Documentation Approach" section
- `.claude/knowledge/team-conventions.md`, "Documentation Structure" section
- `.claude/commands/update-docs.md`, fill in documentation tool IDs
- `.claude/commands/sprint-documentation-review.md`, fill in doc section structure

---

## Step 8: Strategic Priorities

Ask:
1. What are the top 3 strategic initiatives right now? (name + status + one-line description)
2. What are the top 3 problems you're trying to solve?
3. What is the product vision, mid-term (12–18 months) and long-term?

**After getting answers:** Update:
- `PRODUCT_CONTEXT.md`, "Current Strategic Priorities" and "Product Vision" sections

---

## Step 9: Design System (Optional)

Ask:
```
Do you have access to the company's design system yet?
(This is optional, you can always come back and fill it in later)
```

If yes:
1. What component library do you use? (MUI, Ant Design, PrimeVue, custom, etc.)
2. What are the primary brand colors? (hex values if you have them)
3. What frontend framework? (React, Vue, Angular?)
4. Link to Figma file or Storybook?

**After getting answers:** Update:
- `config/design-system.md`, relevant sections

If no: Skip and move on.

---

## Step 10: Wrap Up

After all steps are complete, run a final check:

1. Scan all key files for remaining `[FILL IN:` patterns
2. Report what's fully filled in vs. what's still pending

```
✅ Setup complete!

Here's what's filled in:
- [list completed sections]

Still needs attention:
- [list any remaining [FILL IN: ...] placeholders by file]

You can come back and fill in the remaining items anytime by running /setup again, or by editing the files directly.

Your toolkit is ready to use. Try:
- /create-prd, start writing your first PRD
- /competitive-research, research competitors
- /forecast-sprint, run a sprint forecast
```

---

## Notes

- Write changes to files immediately after each step, don't batch them all at the end
- If the user says "skip" or "I don't know yet" on any question, mark it as `[FILL IN:, skipped, fill in later]` and move on
- Always read the current file content before writing to avoid losing existing data
- Be conversational, don't dump all questions at once, work through them naturally
