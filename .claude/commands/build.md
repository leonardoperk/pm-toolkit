---
description: "Scaffold if needed, plan, build, and iterate on a project"
---

# Build

Take a project from spec to working app: scaffold it if it's new, plan the work, build it, then refine with screenshot feedback. Shipping is deliberately separate, run `/deploy` when you're ready to go live.

## Workflow

### 1. Scaffold (new projects only)

If you're not already in a set-up project, scaffold one. Default stack is Next.js + TypeScript + Tailwind:
```
npx create-next-app@latest . --typescript --tailwind --eslint --app --no-src-dir --import-alias "@/*" --yes
```
If the folder already has files, ask before proceeding. For an existing project, skip this step.

### 2. Check for Requirements

- Look for REQUIREMENTS.md, or ask the user to describe what to build
- If requirements are vague, suggest running `/requirements` first

### 3. Plan

- Use the `EnterPlanMode` tool to switch into plan mode
- Read REQUIREMENTS.md (if it exists)
- Create a detailed plan covering:
  - Files to create/modify
  - Components and their responsibilities
  - Styling approach
  - Logic implementation
  - Any APIs or external services needed
- Present the plan clearly, then use `ExitPlanMode` to surface it for user approval

### 4. Build

After approval:
- Use TodoWrite to track build steps
- Build systematically following the approved plan
- Create all necessary files and components

### 5. Verify

- Start the dev server if applicable (`npm run dev`) and open http://localhost:3000
- Verify core functionality works

### 6. Iterate (screenshot loop)

- Tell the user: take a screenshot of what to change, paste it with Ctrl+V, and describe the change, circle things, point at elements, whatever helps
- Make targeted code changes (not wholesale rewrites)
- Tell the user to refresh the browser
- Ask: "How's that? Want to change anything else?"
- Repeat until satisfied

### 7. Wrap Up

When the user is satisfied, offer to run `/deploy` to ship to GitHub + Vercel. Deploy stays a separate, deliberate step, for deployed projects, a push goes live immediately.

## Notes

- Break complex tasks into clear, trackable steps; mark todos done as you go
- Don't skip verification before iterating
- Make focused changes per iteration and test after each
- Reference specific elements from screenshots in your responses
