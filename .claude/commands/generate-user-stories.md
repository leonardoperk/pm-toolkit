---
description: "Generate Jira user stories from PRD sections"
---

# Generate User Stories Command

You are executing the `/generate-user-stories` command to convert PRD sections into Jira-ready user stories in the [PRODUCT_PROJECT] project.

## Setup

Before starting, read `.claude/knowledge/jira-standards.md` for the latest story format conventions, role names, and any captured learnings from previous sessions.

## Workflow

### 1. Get PRD File Path

Use AskUserQuestion to ask:
- **PRD file path**: Which PRD should I analyze for user stories?

**Example:**
```
Which PRD should I use to generate user stories?
(Provide the file path, e.g., projects/my-feature/prd.md)
```

**Validation:**
- Check file exists using Read tool
- Confirm it's a markdown file
- If file not found, ask for correct path

### 2. Read PRD

**Read the entire PRD** using the Read tool.

### 3. Generate User Stories (one coherent pass)

Generate **all** stories in a single pass, regardless of how many features the PRD has. Keeping the whole PRD in one context is what keeps the stories consistent, same role names, same module naming, and no duplicate or overlapping stories across feature boundaries. Do **not** fan out one agent per feature: that trades coherence and token cost for a little wall-clock speed, and the drafting is not the slow part.

Do the derivation directly in this context. Only for an unusually large PRD may you offload the drafting to a **single** `general-purpose` agent, never split by feature.

**Analyze the PRD, then for every feature section derive discrete stories:**

Story Requirements:
- Represent single, deliverable functionality
- Be independently valuable to users
- Be testable with clear acceptance criteria
- Be small enough for one sprint

What qualifies as a user story:
✅ New user-facing feature
✅ Configuration/settings page
✅ Integration with external system
✅ User workflow or flow step
✅ Data import/export capability
✅ Reporting or analytics feature
✅ Permission/access control

What does NOT become separate story:
❌ Technical implementation details (these are tasks)
❌ Non-functional requirements (these are epics or constraints)
❌ Minor UI variations (part of main story)

Story Format (per `.claude/knowledge/jira-standards.md`):

**Title:** [Module] - [Brief Description]
- Use the modules/feature areas defined in `.claude/knowledge/jira-standards.md`

**User Statement:**
As a [Role], I want to [action/capability], in order to [outcome/benefit].

**Roles:** Use the roles defined in `.claude/knowledge/jira-standards.md`.

**Acceptance Criteria:**
* [Specific, testable condition 1]
* [Specific, testable condition 2]
* [Specific, testable condition 3]
* [Edge case or validation]

**Prototype:**
tbd

**Additions:**
* [Context, background, or reasoning]
* [Technical constraints or dependencies]
* [Edge case explanations]
* [Related ticket references]
* [Implementation notes or considerations]

**Out of Scope (Optional):**
* [Feature/functionality explicitly excluded]

**Priority Suggestion:** HIGH / MEDIUM / LOW
- Reason: [Why this priority based on PRD goals]

Priority Criteria:
- HIGH: Core functionality, launch blocker, high user impact
- MEDIUM: Important enhancement, good-to-have for launch
- LOW: Nice-to-have, post-launch enhancement

Output every story across all feature sections.

### 4. Consistency Check

After drafting all stories in the single pass:
1. Ensure consistent numbering across all stories
2. Dedup: merge or split any overlapping stories at feature boundaries
3. Check for cross-feature dependencies and note them
4. Validate each story meets the quality checklist

### 5. Present Story Proposals to User

Present all generated stories using the story template:

**Story Format:**

**Title Format:** `[Module/Feature Area] - [Brief Description]`
- Use the modules/feature areas defined in `.claude/knowledge/jira-standards.md`

```
## Story N: [Module] - [Brief Description]

**User Statement:**
As a [Role], I want to [action/capability], in order to [outcome/benefit].

**Roles:** Use the roles defined in `.claude/knowledge/jira-standards.md`.

**Acceptance Criteria:**
* [Specific, testable condition 1]
* [Specific, testable condition 2]
* [Specific, testable condition 3]
* [Edge case or validation]

**Prototype:**
tbd

**Note:** Replace "tbd" with actual design links if available:
* [Clickdummy](figma-prototype-link)
* [Designs](figma-design-link)
* [Video Walkthrough](recording-link)

**Additions:**
* [Context, background, or reasoning]
* [Technical constraints or dependencies]
* [Edge case explanations]
* [Related ticket references]
* [Implementation notes or considerations]

**Out of Scope (Optional):**
* [Feature/functionality explicitly excluded]
* [Related work saved for different ticket]

**Priority Suggestion:** HIGH / MEDIUM / LOW
- Reason: [Why this priority based on PRD goals]
```

**Priority Criteria:**
- **HIGH**: Core functionality, launch blocker, high user impact
- **MEDIUM**: Important enhancement, good-to-have for launch
- **LOW**: Nice-to-have, post-launch enhancement

### 6. Get User Approval

Show all generated stories in a clear, numbered format:

```
📝 Generated [N] User Stories from PRD

---

[Story 1 details]

---

[Story 2 details]

---

[Story 3 details]

---

Which stories should I create in Jira?
Options:
- All stories
- Specific stories (tell me the numbers: 1, 3, 5)
- None (just reviewing for now)
```

Wait for user to specify which stories to create. They can say:
- "All of them"
- "Stories 1, 2, and 4"
- "Just story 3"
- "None, I'll review and come back"

Parse their response and proceed with creating only approved stories.

### 7. Create Stories in Jira

For each approved story, use `mcp__atlassian__createJiraIssue`:

**Story Configuration:**
- **Project:** [PRODUCT_PROJECT]
- **Issue Type:** Story
- **Summary:** [Short feature title from story]
- **Description:** Full story with user statement, acceptance criteria, references
- **Team:** Product (`customfield_10001` = `{"name": "Product"}`)
- **Labels:** Add "prd-generated" label
- **Priority:** Map suggestion to Jira priority (High/Medium/Low)
- **Status:** Backlog (default, no transition needed)

**Description Format (Markdown for Jira):**

```markdown
## User Statement

As a [Role], I want to [action/capability], in order to [outcome/benefit].

## Acceptance Criteria

* [Criterion 1]
* [Criterion 2]
* [Criterion 3]

## Prototype

tbd

_(Replace "tbd" with actual design links when available)_

## Additions

* [Context, background, or reasoning for this story]
* [Technical constraints, dependencies, or considerations]
* [Related ticket references or integration points]
* [Implementation notes or edge case explanations]

## Out of Scope

* [What is explicitly NOT included in this story]

---

**Generated from PRD:** [PRD file path]
**Date:** [Current date]
```

### 8. Capture Learnings

**After creating stories, prompt for learnings:**

```
📚 Learning Capture

User stories created successfully! Before we finish, let's capture any learnings.

Did you notice any patterns or insights worth documenting? For example:
- Story patterns that worked well
- Acceptance criteria templates that were effective
- Common mistakes or issues to avoid
- Approaches for specific feature types

Options:
- Yes, I have learnings to capture
- No, skip for now
```

**If user wants to capture learnings:**

Use AskUserQuestion to gather:
- **Question:** "What learnings should I capture from this user story generation?"
- **Prompt:** Share any insights about story structure, patterns, or improvements.

**After receiving learnings, append to knowledge file:**

1. Read current content from `.claude/knowledge/jira-standards.md`
2. Append learnings to the "Learnings & Best Practices" section:

```markdown
### [Date] - [Feature/PRD Name]
**Stories Created:** [N] stories from [PRD file]

**What Worked Well:**
[User learnings about successful story patterns]

**Common Pitfalls:**
[User learnings about mistakes to avoid]

**Story Patterns:**
[User learnings about templates or approaches for specific feature types]

---
```

3. Write updated content back to `.claude/knowledge/jira-standards.md`
4. Confirm to user:

```
✅ Learnings captured in .claude/knowledge/jira-standards.md

These insights will help improve future user story generation.
```

**If user skips:**
- Continue to completion without capturing learnings

### 9. Report Results

After learnings are captured (or skipped):

```
✅ Created [N] User Stories in [PRODUCT_PROJECT] Project

Stories Created:
- [[PRODUCT_PROJECT]-XXX]: [Story 1 title]
  Link: [Jira URL]

- [[PRODUCT_PROJECT]-YYY]: [Story 2 title]
  Link: [Jira URL]

- [[PRODUCT_PROJECT]-ZZZ]: [Story 3 title]
  Link: [Jira URL]

📋 Next Steps:
1. Review stories in Jira [PRODUCT_PROJECT] project (Backlog)
2. Refine acceptance criteria as needed
3. Add story points or estimates
4. Move to appropriate sprint when ready
```

## Story Extraction Guidelines

### From PRD Sections

**Typical PRD structure and how to extract stories:**

1. **Overview/Problem Statement** → Context, but usually NOT a story
2. **User Personas** → Identify who stories are for
3. **Key Features** → Each major feature = 1+ stories
4. **User Flows** → Each flow step might be a story
5. **Functionality Details** → Break into discrete stories
6. **Success Metrics** → Usually NOT stories (these are acceptance criteria)
7. **Technical Requirements** → May indicate stories (e.g., "API integration")
8. **Edge Cases** → Add to acceptance criteria, not separate stories

**Example Extraction:**

PRD Section: "Key Features"
```
- Email inbox integration with OAuth
- Message threading and conversation view
- Automated response templates
- Team assignment and routing
```

Generated Stories:
1. "[Module] OAuth Integration" - Connect email via OAuth
2. "Conversation Threading View" - Display threaded messages
3. "Response Template System" - Create and use templates
4. "Team Routing Configuration" - Assign conversations to teams

### Story Quality Checklist

Before proposing a story, ensure:
- [ ] Title is clear and concise (< 10 words)
- [ ] User statement follows "As a X, I want Y, so that Z" format
- [ ] Acceptance criteria are specific and testable
- [ ] Priority is justified based on PRD goals
- [ ] Story is independent and deliverable
- [ ] Story provides clear user value
- [ ] References to designs/prototypes are included

## Error Handling

**PRD file not found:**
- List available PRD files in projects/
- Ask user for correct path

**PRD too sparse:**
- Warn user that PRD lacks detail for good stories
- Generate what's possible
- Mark stories as "NEEDS REFINEMENT" in notes

**No clear features identified:**
- Inform user that PRD doesn't contain identifiable user stories
- Suggest reviewing PRD structure
- Offer to extract general tasks instead

**Jira creation fails:**
- Report which stories failed
- Provide fallback: Save stories as markdown file
- Suggest checking Jira permissions

**[PRODUCT_PROJECT] project not accessible:**
- Verify user has access to [PRODUCT_PROJECT] project
- Suggest alternative project ([ENG_PROJECT])
- Offer to save as markdown instead

## Edge Cases

**Very large PRD (10+ features):**
- Generate all stories
- Group by theme or section
- Let user approve in batches

**PRD with epics or phases:**
- Identify epics separately
- Generate stories under each epic
- Note epic relationships in story notes

**PRD with technical tasks:**
- Distinguish between user stories and technical tasks
- Only generate user stories (user-facing value)
- Note technical dependencies in story notes

**Existing stories in Jira:**
- Generate proposals anyway
- Note: "Check if this already exists as [[ENG_PROJECT]-XXX]"
- Let user decide on duplicates

## Integration with Other Workflows

**After generating stories:**

1. **Refine in Jira**
   - Add story points
   - Add labels or components
   - Link to epics
   - Assign to team members

2. **Sprint Planning**
   - Move from Backlog to sprint
   - Prioritize against other work
   - Break down if too large

3. **Documentation**
   - Keep PRD and stories synchronized

## Best Practices

**Before Generating:**
- Ensure PRD is complete and reviewed
- Have designs/prototypes referenced in PRD
- Identify user personas clearly
- Define success criteria

**During Generation:**
- Focus on user value, not implementation
- Keep stories small and independent
- Make acceptance criteria specific
- Include design references

**After Generation:**
- Review all stories for completeness
- Refine acceptance criteria with team
- Prioritize based on roadmap
- Link related stories

## Example Output

**Input PRD:** "[Module] Feature"

**Generated Stories:**

```
📝 Generated 4 User Stories from PRD

---

## Story 1: [Module] - Webhook URL Setup

**User Statement:**
As a Superadmin, I want to create a unique webhook URL for my account, in order to allow external systems to send data to the product automatically.

**Acceptance Criteria:**
* User can generate a new webhook URL from automation settings
* URL is unique per account and secure
* User can copy URL to clipboard
* User can regenerate URL if needed
* URL format: https://api.[FILL IN: your domain]/webhooks/{uuid}

**Prototype:**
tbd

**Additions:**
* Webhook URL should support security features (HMAC signatures for verification)
* URL regeneration must invalidate old URL to prevent unauthorized access
* This story is related to webhook receive action feature (dependency)

**Priority Suggestion:** HIGH
- Reason: Core functionality required for webhook automation

---

## Story 2: [Module] - Webhook Data Mapping

**User Statement:**
As an Admin, I want to select which fields from incoming webhooks to use in my automation, in order to personalize automated messages with external data.

**Acceptance Criteria:**
* User can send a test webhook payload
* System displays all fields in the received payload
* User can select fields via checkboxes
* Selected fields become available as variables
* Variables use format: {{webhook.field_name}}

**Prototype:**
tbd

**Additions:**
* Variables should be clearly labeled in the automation builder UI
* Must handle nested JSON objects in webhook payload (e.g., data.customer.name)
* Test webhook feature required for development and user validation

**Priority Suggestion:** HIGH
- Reason: Required for dynamic data usage

---

## Story 3: [Module] - Webhook Event Filtering

**User Statement:**
As an Admin, I want to only process webhooks that meet specific conditions, in order to avoid triggering unnecessary automations.

**Acceptance Criteria:**
* User can add filter conditions (if/then logic)
* Supports operators: equals, contains, greater than, less than
* Multiple conditions with AND/OR logic
* Test mode shows if webhook would pass filter
* Filtered webhooks are logged but not processed

**Prototype:**
tbd

**Additions:**
* Filter UI should provide clear visual feedback when conditions are met/not met
* Consider adding preset filter templates for common use cases

**Out of Scope:**
* Advanced regex pattern matching
* Complex nested condition groups

**Priority Suggestion:** MEDIUM
- Reason: Important for preventing noise, but basic automation works without it

---

## Story 4: [Module] - Webhook Error Handling

**User Statement:**
As an Admin, I want to be notified when webhooks fail to process, in order to fix issues and avoid losing data.

**Acceptance Criteria:**
* Failed webhooks auto-retry up to 3 times
* Exponential backoff: 1min, 5min, 15min
* User receives email notification after final failure
* Error log shows failure reason
* User can manually retry failed webhooks

**Prototype:**
tbd

**Additions:**
* Error log should be accessible from automation settings dashboard
* Manual retry should allow editing the payload before resending
* Email notification should include webhook URL and error details for debugging
* Consider adding Slack/webhook notification option for critical failures

**Priority Suggestion:** MEDIUM
- Reason: Important for reliability, but not blocking initial launch

---

Which stories should I create in Jira?
```

## Important Notes

- **Only generate user stories** - Not technical tasks, bugs, or infrastructure work
- **Focus on user value** - Every story should explain the benefit
- **Be specific** - Vague acceptance criteria lead to unclear stories
- **Reference designs** - Always link to Figma/prototypes if available
- **Check for duplicates** - Note if story might already exist in Jira
- **Team field required** - Must set Product team for stories to appear on board

---

**This command bridges PRD to execution by creating actionable, well-structured user stories ready for sprint planning.**
