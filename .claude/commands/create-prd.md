---
description: "Create a PRD through conversational interview using the Hybrid PRD Template (seven core questions + Solution Alignment)"
---

# Create PRD Command

You are executing the `/create-prd` command to create a Product Requirements Document through natural conversation, using the Hybrid PRD Template as the structure.

## Overview

This command guides a **conversational PRD creation process**. Rather than rigid step-by-step questions, you engage in natural dialogue with the user, intelligently extracting information and mapping it to the Hybrid PRD Template sections (Core Questions, Solution Alignment, Execution).

## Workflow

### 1. Initiate Conversation

Start by asking the user to describe their feature/project naturally:

```
Tell me about the feature or project you want to create a PRD for.

Describe it however feels natural:
- What problem are you solving?
- What's the solution idea?
- Who is it for?
- Why does it matter?

Don't worry about structure - just share your thinking, and I'll ask follow-up questions to fill in the details.
```

### 2. Active Listening & Information Extraction

As the user describes their project, **actively extract and categorize** information into the Hybrid template's three parts:

**Core Questions:**
- Description (what is it, in one paragraph)
- Problem (what problem this solves, 1-2 sentences)
- Why (evidence it's real and worth solving: research, data, feedback, competitive pressure)
- Success (metrics and criteria that tell us it's solved)
- Audience (who we're building for: users, personas, segments)
- What (roughly, what this looks like in the product)
- Non-Goals (what we're explicitly not doing, and why)

**Solution Alignment:**
- Key features
- Key flows (primary user journeys)
- Key logic (business rules, algorithms, technical decisions)

**Execution:**
- How (experiment/rollout plan: beta strategy, validation)
- When (ship date and milestones)

**Track what you've captured vs. what's still needed.**

### 3. Ask Targeted Follow-Up Questions

After the user's initial description, summarize what you understood and ask clarifying questions for gaps:

**Example:**
```
Great! I'm capturing:

✅ Problem: Manual data sync between tools is error-prone
✅ Solution: Direct integrations with the top external systems
✅ Target users: Teams that rely on those external systems

Let me clarify a few things:

1. Which specific systems? (Top 5 by priority)
2. What evidence do you have about the error-prone manual process?
   (Support tickets? Customer feedback? Data?)
3. What makes this urgent now versus 6 months from now?
```

**Ask questions conversationally** - not as a checklist, but as natural follow-ups to their answers.

### 4. Deep Dive into Solution Details

Once the Core Questions are clear, explore Solution Alignment:

**Key Features:**
```
What are the main features you envision for this?

Think about the core capabilities needed to solve the problem.
```

**User Flows:**
```
Walk me through how a [user persona] would use this:
- What's the first thing they do?
- What happens next?
- What does the system do in response?
- What are the edge cases?
```

**Business Logic:**
```
Are there specific rules or constraints I should know about?

For example:
- Access control (who can do what?)
- Validation rules (what's allowed/not allowed?)
- Error handling (what if X fails?)
- Performance requirements
```

### 5. Cover Success & Audience

Make the success criteria and target audience explicit (these are easy to skip in a free-form description):

**Success (how do we know it's solved):**
```
What does success look like?

Both measurable (metrics, numbers) and qualitative (user sentiment, outcomes).
What's the one metric that matters most?
```

**Audience (who are we building for):**
```
Who is this for? Specific users, personas, or segments.
Who feels this problem most acutely?
```

### 6. Cover Execution

Ask about the rollout plan and timeline (the Hybrid "How" and "When"):

**How (experiment plan):**
```
How will we ship and validate this?

Think about:
- Beta strategy (who gets it first?)
- Rollout approach (phased? feature-flagged?)
- Validation plan (how do we confirm it's working before full launch?)
```

**When (milestones):**
```
What's your timeline vision?

Key dates or milestones:
- When do you need designs?
- When should development be done?
- When do you want to launch?

(It's okay to say "TBD" - we can refine later)
```

### 7. Confirm the Description & Non-Goals

Pin down the one-paragraph summary that opens the PRD:

```
In a paragraph a colleague could read alone: what is this feature, and what value does it deliver?
```

Then make the boundaries explicit:

```
What are you explicitly NOT doing in this project?

These non-goals clarify boundaries and prevent scope creep.
```

### 8. Validate Completeness

Before generating the PRD, review what you've captured against the Hybrid structure:

```
Let me confirm I have everything:

📋 Core Questions:
   ✅ Description: [Summary]
   ✅ Problem: [Summary]
   ✅ Why (evidence): [What you have]
   ⚠️  Success (metrics): [Need to clarify]
   ✅ Audience: [Who]
   ✅ What: [High-level solution]
   ⚠️  Non-Goals: [Need to clarify]

📋 Solution Alignment:
   ✅ Key features: [N features identified]
   ✅ Key flows: [Flows described]
   ⚠️  Key logic: [Need more detail on rules]

📋 Execution:
   ⚠️  How (experiment plan): [Need to clarify]
   ✅ When (milestones): [Dates or TBD]

Anything missing or should we fill in [sections with ⚠️]?
```

If there are gaps, ask targeted questions. If user says "I don't know yet" or "TBD", that's fine - note it in the PRD.

### 9. Generate PRD Document

Once you have sufficient information:

1. **Read the Hybrid PRD Template** from `templates/prds/Hybrid-PRD-Template.md`
2. **Read the PRD example** for style and quality reference:
   - `.claude/knowledge/prd-example-user-core.md`, User & Team Core (auth & permissions example PRD)
3. **Map collected information** to template structure
4. **Ask for file path:**
   ```
   Where should I save this PRD?

   Suggested: projects/[feature-name]/prd.md
   ```
5. **Generate complete PRD** in markdown format
6. **Save to specified location**

**PRD Structure (following the Hybrid template):**

```markdown
# [Project Name] - PRD

**Status:** Draft
**Owner:** [Product Manager name if known, else "TBD"]
**Last Updated:** [Current date]

---

## Core Questions

**Description: What is it?**
[One-paragraph summary of the feature]

**Problem: What problem is this solving?**
[The problem in 1-2 sentences - readable alone, so a colleague could communicate the value/risks from it]

**Why: How do we know this is a real problem and worth solving?**
[Evidence: user research, data, customer feedback, competitive pressure]

**Success: How do we know if we've solved this problem?**
[Metrics and success criteria - measurable and qualitative]

**Audience: Who are we building for?**
[Target users, personas, segments]

**What: Roughly, what does this look like in the product?**
[High-level description of the solution]

**Non-Goals: What are we explicitly not doing?**
[Out-of-scope items and why - keeps the boundaries clear]

---

## Solution Alignment

**Key Features**

1. **[Feature 1 name]** - [Description] - Priority: [Must have / Should have / Nice to have]
2. **[Feature 2 name]** - [Description] - Priority: [Must have / Should have / Nice to have]
3. **[Feature 3 name]** - [Description] - Priority: [Must have / Should have / Nice to have]

**Key Flows**

#### Flow 1: [Flow Name - e.g., "Setup Flow"]

**Steps:**
1. **User:** [Action]
2. **System:** [Response]

**Edge cases:**
- [Edge case]: [How to handle]

**Key Logic**

1. **[Rule Category - e.g., "Access Control"]**
   - [Specific rule]
2. **[Validation Rules]**
   - [Rule]
3. **[Non-functional Requirements]**
   - Performance / Security / Scalability: [Requirements]

---

## Execution

**How: What is the experiment plan?**
[Beta strategy, rollout approach, validation plan]

**When: When does it ship and what are the milestones?**

| Milestone | Target Date | Description |
|-----------|-------------|-------------|
| Design Complete | [Date or TBD] | Final designs approved |
| Dev Complete | [Date or TBD] | Feature complete, ready for QA |
| Beta Launch | [Date or TBD] | Limited release to beta users |
| GA Launch | [Date or TBD] | General availability |
```

### 10. Create Jira Epic in [PRODUCT_PROJECT] Project

**After generating the PRD file, ask for user validation:**

```
✅ PRD created at: [file path]

📖 Review the PRD and let me know if it looks good.

Once approved, I'll:
1. Create this as an Epic in Jira [PRODUCT_PROJECT] project
2. Set status to "To Do"
3. Link the PRD document

Should I proceed with creating the Jira Epic?
```

**Wait for user approval.** User should respond with something like:
- "Yes, create the epic"
- "Approved, go ahead"
- "Looks good, create it"

**Once approved, create the Epic:**

Use `mcp__atlassian__createJiraIssue`:

**Epic Configuration:**
- **Project:** [PRODUCT_PROJECT]
- **Issue Type:** Epic
- **Summary:** [Project name from PRD]
- **Description:**

```markdown
# [Project Name]

## Description

[One-paragraph summary from PRD]

## Problem

[1-2 sentence problem statement from PRD]

## Why

[Evidence this is real and worth solving]

## Success

[Success metrics/criteria from PRD]

## Key Features

[List of key features from PRD]

---

**📄 Full PRD:** [Link to PRD file or note location]

**Status:** Draft - Ready for refinement and story creation

---

**Created via:** `/create-prd` command
**Date:** [Current date]
```

- **Team Field:** Set to "Product" (CRITICAL - required for visibility on board)
  - Use `additional_fields`: `{"customfield_10001": {"name": "Product"}}`
- **Epic Name:** [Short project name]
- **Labels:** Add "prd-created"
- **Priority:** Medium (default, user can adjust)
- **Initial Status:** Will be created in default status, then transition to "To Do"

**After creation, transition to "To Do":**

1. Get issue key from creation response
2. Use `mcp__atlassian__getTransitionsForJiraIssue` to find available transitions
3. Find the transition to "To Do" status
4. Use `mcp__atlassian__transitionJiraIssue` to move to "To Do"

### 11. Capture Learnings

**After Epic is created, prompt for learnings to preserve institutional knowledge:**

```
📚 Learning Capture

This PRD process is complete! Before we finish, let's capture any learnings for future PRDs.

Do you have any learnings to document? For example:
- What worked well in this PRD process?
- What was unclear or caused confusion?
- What would you do differently next time?
- Any patterns or approaches worth remembering?

Options:
- Yes, I have learnings to capture
- No, skip for now
```

**If user wants to capture learnings:**

Use AskUserQuestion to gather:
- **Question:** "What learnings should I capture from this PRD process?"
- **Prompt:** Share any insights, patterns, or improvements that would be valuable for future PRD creation.

**After receiving learnings, append to knowledge file:**

1. Read current content from `.claude/knowledge/prd-template.md`
2. Append learnings to the "Learnings & Best Practices" section:

```markdown
### [Date] - [Project Name]
**From PRD:** [file path]

**What Worked Well:**
[User learnings about successful approaches]

**Challenges:**
[User learnings about difficulties]

**Improvements for Next Time:**
[User learnings about what to do differently]

---
```

3. Write updated content back to `.claude/knowledge/prd-template.md`
4. Confirm to user:

```
✅ Learnings captured in .claude/knowledge/prd-template.md

These insights will help inform future PRD creation.
```

**If user skips:**
- Continue to completion without capturing learnings

### 12. Report Completion

After learnings are captured (or skipped):

```
✅ PRD Created Successfully!

📄 PRD Document: [file path]

🎫 Jira Epic Created:
   Epic: [[PRODUCT_PROJECT]-XXX] - [Project Name]
   Status: To Do
   Team: Product
   Link: [Jira URL]

📋 Next Steps:
   1. Share PRD with team for feedback
   2. Use /review-prd for comprehensive review
   3. Use /generate-user-stories to create implementation stories
   4. Update PRD based on feedback (track in Changelog)

Would you like me to:
- Run /review-prd now for multi-agent feedback?
- Generate user stories with /generate-user-stories?
- Just leave it for now?
```

## Conversation Best Practices

### Be Adaptive
- **If user gives lots of detail:** Extract everything, ask fewer follow-ups
- **If user gives high-level:** Ask more probing questions
- **If user is uncertain:** Note "TBD" and offer to revisit later

### Stay Natural
- Don't sound like a form: ❌ "Now I need to capture your goals"
- Sound conversational: ✅ "What does success look like to you?"

### Summarize & Validate
- After each major section, summarize back: "So the core problem is X, driven by Y evidence, and we need to solve it because Z. Did I get that right?"
- Catch misunderstandings early

### Guide Without Prescribing
- Help user think through their idea
- Ask "Why?" to uncover real goals
- Challenge assumptions gently: "What if we just did X instead of the full solution?"

### Track Coverage
Mentally track the Hybrid template sections (Core Questions, Solution Alignment, Execution):
- ✅ Covered sufficiently
- ⚠️ Partial info, could use more
- ❌ Not discussed yet

Focus questions on ⚠️ and ❌ sections.

### Handle Uncertainty Gracefully
- User: "I'm not sure about the timeline yet"
- You: "No problem - I'll mark milestones as TBD. You can update them later as things solidify."

### Examples of Great Follow-Ups

**After problem description:**
- "What evidence do you have that this is a real problem? Customer tickets? Lost deals?"
- "How many customers are affected?"
- "What happens if we don't solve this?"

**After solution idea:**
- "Walk me through how a [user] would experience this. What's the first thing they do?"
- "What alternatives did you consider? Why not go with those?"
- "What's the simplest version of this that still solves the problem?"

**For goals:**
- "How will you know if this was successful?"
- "What's the one metric that matters most?"
- "What should definitely NOT change as a result of this?"

**For features:**
- "Which of these features are must-haves for launch vs. nice-to-haves?"
- "If you could only ship one feature, which would it be?"
- "What's the smallest thing we could ship to learn if this works?"

## Edge Cases & Error Handling

### User Provides Minimal Information
```
I can create a PRD with what you've shared, but it will be pretty sparse.

The PRD will have:
✅ Basic problem statement
⚠️  Limited solution detail
⚠️  No milestones or timeline
⚠️  No execution plan (How/When)

Would you like to:
- Continue and I'll create a draft PRD (you can fill in gaps later)
- Spend a few more minutes adding more detail now
- Pause and come back to this when you have more clarity
```

### File Path Already Exists
```
A PRD already exists at [path].

Options:
- Overwrite it (replace completely)
- Create a new version (save as [path]-v2.md)
- Cancel and choose a different location
```

### Epic Creation Fails
```
❌ Could not create Jira Epic: [Error message]

The PRD file was created successfully at [path].

Possible issues:
- [PRODUCT_PROJECT] project not accessible
- Team field configuration issue
- Network/API error

Would you like me to:
- Retry creating the Epic
- Save Epic details to a file for manual creation
- Skip Epic creation for now
```

### User Wants to Pause Mid-Conversation
```
No problem! I've captured:

[Summary of what's been covered]

I'll save a draft PRD with "DRAFT - IN PROGRESS" header.

When you're ready to continue, just say:
- "Continue the PRD" or
- "Finish the PRD creation"

And I'll pick up where we left off.
```

## Integration with Other Commands

**After PRD creation, suggest:**

1. **`/review-prd`** - Multi-agent comprehensive review
   - Technical feasibility
   - User experience
   - Business requirements
   - Implementation complexity

2. **`/generate-user-stories`** - Convert PRD to Jira stories
   - Creates actionable tickets
   - Uses [PRODUCT] story template
   - Breaks down features

3. **`/competitive-research`** - Research competitors
   - Validate your approach
   - Identify gaps
   - Learn from others

4. **`/forecast-epic`** - Estimate timeline
   - Based on historical velocity
   - Story count estimates
   - Confidence intervals

## Quality Checklist

Before finalizing PRD, ensure:
- [ ] Description reads well alone (one paragraph)
- [ ] Problem statement is clear (1-2 sentences)
- [ ] Evidence (Why) for the problem is documented
- [ ] Success metrics are defined
- [ ] Audience is specified
- [ ] Non-goals clarify boundaries
- [ ] Key features are listed and prioritized
- [ ] At least one key flow is documented
- [ ] Execution plan (How + When) is captured
- [ ] Team field set to "Product" in Jira Epic

## Important Notes

- **Template location:** `templates/prds/Hybrid-PRD-Template.md`
- **Always set Team field:** `{"customfield_10001": {"name": "Product"}}` - Critical for board visibility
- **Always transition to "To Do":** Don't leave Epic in Backlog
- **Conversational, not interrogative:** Make it feel like collaboration, not a form
- **Capture uncertainty:** It's okay to have TBD sections
- **Link PRD in Epic:** Always reference the PRD file location in Epic description

---

**This command creates PRDs through natural conversation, structures them using the Hybrid template, and creates Jira Epics for tracking - all while feeling collaborative rather than procedural.**
