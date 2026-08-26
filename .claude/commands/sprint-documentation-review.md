---
description: "Analyze completed sprint and propose product documentation updates"
---

# Sprint Documentation Review Command

You are executing the `/sprint-documentation-review` command to automatically analyze a completed sprint and propose updates to your product documentation.

Your sprint work lives in an issue tracker (Jira, Linear, Azure DevOps, …) and your product docs live in a documentation tool (Confluence, Notion, ClickUp, …). This command reads from both via whatever integrations are connected, see `config/company-context.md` → "Tools We Use". Examples below use Jira + ClickUp as concrete cases; adapt them to your tools.

## Workflow

### 1. Gather Sprint Information

Use AskUserQuestion to ask:
- **Sprint to review**: Which sprint should I analyze? (e.g., "Sprint 5", "Sprint 6")
- **Project**: Confirm project key (default: [ENG_PROJECT])

**Example:**
```
Which sprint should I review for documentation needs?
Options:
- Most recent completed sprint (recommended)
- Specific sprint number (you specify)
```

### 2. Fetch Sprint Stories

Fetch all completed **stories** from the sprint via your issue tracker's integration (exclude bugs, tasks, subtasks; status Done/Closed).

**Example, if your sprint work is in Jira** (Atlassian MCP, `searchJiraIssuesUsingJql`):
```jql
project = [ENG_PROJECT] AND sprint = "Sprint X" AND type = Story AND status in (Done, Closed)
```
For another tracker (Linear, Azure DevOps, …): use its equivalent query for the sprint's completed stories.

**Extract from each story:**
- Issue key (e.g., [ENG_PROJECT]-123)
- Summary
- Description
- Acceptance criteria
- Labels (if any indicate customer-facing)

### 3. Analyze Stories and Doc Structure

Do both tasks below in this context, no subagents. They read different sources (sprint stories vs. the product doc), so run them in sequence and hold both results for the synthesis in Step 4.

**Task A, Story documentation impact.** For each completed story, decide whether it needs documentation:

   NEEDS DOCUMENTATION (✅):
   - Customer-facing feature (users interact with it)
   - New functionality (capability that didn't exist)
   - User-visible changes (behavior users can observe)
   - Configuration/settings (new options to configure)
   - Integration (connects with external systems)
   - Workflow changes (modifies how users complete tasks)

   NO DOCUMENTATION NEEDED (❌):
   - Internal improvements (backend optimization, refactoring)
   - Bug fixes
   - Technical debt (infrastructure, CI/CD, tooling)
   - Minor UI tweaks (colors, spacing)
   - Developer-only features

For each story needing docs: identify affected features/modules, update type (new feature / enhancement / workflow / limitation), priority (HIGH/MEDIUM/LOW), and draft what should be documented.

Output format per story:
```
### [[ENG_PROJECT]-XXX] - [Summary]
- **Documentation Needed:** Yes / No
- **Reason:** [Why it needs or doesn't need docs]
- **Affected Areas:** [Which product areas]
- **Update Type:** New Feature / Enhancement / Workflow / Limitation
- **Priority:** HIGH / MEDIUM / LOW
- **Key Changes to Document:** [Bullet points]
```

**Task B, Documentation structure.** Read the current product documentation and map its structure so you know where updates would land.

- Documentation tool: [FILL IN: e.g. Confluence / Notion / ClickUp]
- Location / IDs: [FILL IN: page URL, or ClickUp Workspace + Doc + Page IDs]
- See `config/company-context.md` for your documentation structure

For each section, note current subsections, level of detail, formatting style, and where new content could be added. Flag any gaps or areas needing expansion.

Output format per section:
```
### Section [X.Y] - [Name]
- **Current Subsections:** [List]
- **Content Coverage:** [Brief description]
- **Documentation Style:** [Technical/reference/workflow]
- **Potential Insert Points:** [Where new content could go]
- **Gaps Identified:** [Missing topics]
```

### 4. Synthesize and Generate Proposals

**With both results (story impact + doc structure) in hand:**

1. **Match stories to documentation sections:**
   - Use Task A's story analysis
   - Use Task B's structure mapping
   - Determine exact section for each update

2. **Draft proposed content updates:**
   For each story needing documentation, draft actual content in product doc style:
   - Use technical but clear language
   - Include feature specifics, limitations, technical details
   - Follow existing documentation structure and formatting
   - Use bullet points, tables, subsections as appropriate

3. **Categorize proposals:**

### 5. Structure Findings into Proposal Categories

#### Category A: New Content to Add
```
**Story: [[ENG_PROJECT]-XXX] - [Summary]**
- Priority: HIGH/MEDIUM/LOW
- Doc Section: [e.g., "[Section X.Y] - [Feature Area]"]
- Update Type: New Feature / New Capability / New Subsection
- Proposed Content to Add:
  ```
  [Draft the actual markdown content in product doc style]

  Example:
  ### Time Zone Configuration
  [Module] supports per-action time zone settings. While the system uses
  the account's global time zone by default, you can override this for each
  action.

  **Configuration:**
  - Set default time zone in Account Settings
  - Override per-action in automation configuration
  - Supported time zones: All IANA time zone database entries
  ```
- Insert Location: [After which existing subsection]
```

#### Category B: Updates to Existing Content
```
**Story: [[ENG_PROJECT]-XXX] - [Summary]**
- Doc Section: [e.g., "[Section X.Y] - [Feature Area]"]
- Priority: HIGH/MEDIUM/LOW
- Update Type: Enhancement / Capability Change / New Information
- Existing Content Reference: [Quote relevant existing text]
- Proposed Content Update:
  ```
  [Draft the modified/additional content]

  Example - Add to existing channel list:
  - **Telegram**: Business messaging integration (NEW)
    - Supports outbound conversations
    - Attachments supported
    - AI chatbot active
  ```
```

#### Category C: No Documentation Update Needed
```
**Story: [[ENG_PROJECT]-XXX] - [Summary]**
- Reason: [Internal improvement / Minor tweak / etc.]
```

### 6. Save Report

Save the full proposal as a markdown report:

**File path:** `reports/sprint-doc-reviews/sprint-[X]-doc-review.md`

**Report Template:**
```markdown
# Sprint [X] - Product Documentation Updates

**Date:** [Current date]
**Stories Analyzed:** [N] total
**Documentation Updates Needed:** [Y] stories
  - New Content to Add: [A]
  - Existing Content Updates: [B]
**No Documentation:** [Z] stories

**Product Doc:** [FILL IN: link to your product documentation]

---

## ➕ New Content to Add

[Insert Category A findings here - proposed new sections/content]

---

## 🔄 Updates to Existing Content

[Insert Category B findings here - proposed modifications to existing sections]

---

## ✅ No Documentation Update Needed

[Insert Category C findings here]

---

## Next Steps

After reviewing:
1. Approve specific updates (e.g., "Apply updates 1, 2, and 4")
2. Claude Code will update the product documentation
3. Review the updated doc to verify changes
```

Confirm the saved file path to the user.

### 7. Capture Learnings

**After creating [PRODUCT_PROJECT] story, prompt for learnings:**

```
📚 Learning Capture

Sprint documentation review is complete! Before we finish, let's capture any learnings.

Did this sprint reveal any documentation patterns worth noting? For example:
- Features that often get missed in documentation
- Documentation approaches that worked well
- Common gaps between what shipped and what was documented
- Process improvements for future sprints

Options:
- Yes, I have learnings to capture
- No, skip for now
```

**If user wants to capture learnings:**

Use AskUserQuestion to gather:
- **Question:** "What learnings should I capture from this sprint documentation review?"
- **Prompt:** Share any insights about documentation gaps, patterns, or process improvements.

**After receiving learnings, append to knowledge file:**

1. Read current content from `.claude/knowledge/team-conventions.md`
2. Add learnings to a "Documentation Review Learnings" section (create if doesn't exist):

```markdown
## Documentation Review Learnings

### [Date] - Sprint [X]
**Stories Analyzed:** [N] stories
**Documentation Updates:** [Y] updates needed

**Documentation Patterns:**
[User learnings about what commonly needs documentation]

**Process Improvements:**
[User learnings about improving the review workflow]

**Gaps Identified:**
[User learnings about common misses or oversights]

**Link to full report:** reports/sprint-doc-reviews/sprint-[X]-doc-review.md

---
```

3. Write updated content back to `.claude/knowledge/team-conventions.md`
4. Confirm to user:

```
✅ Learnings captured in .claude/knowledge/team-conventions.md

These insights will improve future sprint documentation reviews.
```

**If user skips:**
- Continue to completion without capturing learnings

### 8. Present Results to User

After learnings are captured (or skipped):
```
✅ Sprint [X] Documentation Review Complete

📊 Analysis Summary:
   - Stories analyzed: [N]
   - Product doc updates needed: [Y]
     • New content to add: [A]
     • Existing content updates: [B]
   - No documentation: [Z]

📄 Report saved: reports/sprint-doc-reviews/sprint-[X]-doc-review.md

📋 Next Steps:
   1. Review the report
   2. Come back here and tell me which updates to apply
   3. I'll update the product documentation with approved changes

Example: "Apply updates 1, 3, and 5 to the product doc"
```

## Error Handling

**Sprint not found:**
- List available sprints in the project
- Ask user to choose from the list

**No completed stories:**
- Inform user that sprint has no completed stories
- Do not create [PRODUCT_PROJECT] story
- Suggest checking sprint status

**Issue tracker API errors:**
- Report the error clearly
- Suggest user check their tracker's permissions / integration
- Provide fallback: Generate report as markdown file instead

**[PRODUCT_PROJECT] project not accessible:**
- Verify user has access to [PRODUCT_PROJECT] project
- Suggest checking project permissions
- Provide alternative: Save proposal as markdown file

**Team field not found:**
- If "Product" team doesn't exist, list available teams
- Ask user which team to use
- Update documentation with correct team name

## Implementation Notes (Jira example)

The proposals are always saved as the markdown report (Step 6). If you also want them as a tracked ticket in your issue tracker, create one there. The steps below are the concrete recipe **for Jira**; for another tracker, use its equivalent fields (team/owner, status).

**Setting the Team Field:**
The "Team" field is a custom field in Jira with ID `customfield_10001`. When creating the story:
1. Pass via `additional_fields` parameter: `{"customfield_10001": {"name": "Product"}}`
2. The team object must include the `name` property set to "Product"
3. This ensures the story appears on the [PRODUCT_PROJECT] board (filtered by Team = Product)
4. Value is case-sensitive and must match exactly: "Product"

**Setting Status to "To Do":**
Jira issues are created in a default status (often "Backlog"). To ensure it goes to "To Do":
1. Create the issue using `mcp__atlassian__createJiraIssue`
2. Immediately after creation, fetch available transitions using `mcp__atlassian__getTransitionsForJiraIssue`
3. Find the transition that moves to "To Do" status
4. Execute the transition using `mcp__atlassian__transitionJiraIssue`
5. If "To Do" transition not available, report to user and leave in default status

**Example workflow:**
```
1. issue = createJiraIssue(project=[PRODUCT_PROJECT], ...)
2. transitions = getTransitionsForJiraIssue(issueIdOrKey=issue.key)
3. toDoTransition = find transition with name "To Do" or to.name == "To Do"
4. if toDoTransition exists:
     transitionJiraIssue(issueIdOrKey=issue.key, transition={id: toDoTransition.id})
```

## Edge Cases

**Very large sprint (20+ stories):**
- Process all stories but group by theme in proposal
- Prioritize customer-facing features
- Summarize internal improvements

**Sprint with only internal work:**
- Create [PRODUCT_PROJECT] story anyway with message: "No customer-facing documentation needed for Sprint X"
- List why each story does not need docs
- Mark as FYI only

**Unclear if documentation needed:**
- Err on the side of flagging for review
- Mark as "LOW" priority
- Add note: "Review needed - unclear if customer-facing"

## Important Notes

- **Only analyze Stories** - Skip bugs, tasks, epics, subtasks
- **Map to existing doc structure** - Always reference specific sections ([your doc section numbers])
- **Draft actual content** - Proposals should include the exact text to add, not just descriptions
- **Match documentation style** - Use technical product reference tone, not customer KB tone
- **Be specific in proposals** - Include enough detail that user can make decision
- **Default to flagging** - If unsure, include it with LOW priority for user review
- **Match your tracker's formatting** - Ensure the description renders properly (e.g. Jira ADF, or markdown)
- **Preserve doc structure** - Don't add "What's New" or changelog sections

## Documentation Update Process

After the user reviews the proposals and approves updates:

**User says:** "Apply updates 1, 2, and 4 to the product doc"

**Response:**
1. Fetch the current doc content using your documentation tool's read capability (e.g. the ClickUp MCP `clickup_get_doc_pages`)
2. For each approved update:
   - Identify the exact location in the document
   - Insert new content or modify existing content as proposed
   - Maintain existing formatting and structure
3. Update the doc using your tool's edit capability (e.g. ClickUp MCP `clickup_edit_doc_page_content`)
4. Confirm updates applied with specific section references
5. Provide link to the updated doc for review

**Doc Details:**
- Documentation tool: `[FILL IN: e.g. Confluence / Notion / ClickUp]`
- Location / IDs: `[FILL IN: page URL, or ClickUp Workspace + Doc + Page IDs]`
- Doc Name: "[FILL IN: your company] Product Documentation"

## Quality Checklist

Before creating [PRODUCT_PROJECT] story:
- [ ] All stories analyzed with clear reasoning
- [ ] Priorities assigned (HIGH/MEDIUM/LOW)
- [ ] Proposed outlines are specific and actionable
- [ ] Description is well-formatted and readable in your tracker
- [ ] Acceptance criteria are clear
- [ ] Link to the review story / report is provided to user

## Example Output

**Sprint 5 with 3 stories:**

Story 1: [ENG_PROJECT]-145 "Add webhook automation trigger"
- Analysis: Customer-facing, new functionality → NEW CONTENT (HIGH)
- Doc Section: [Section X.Y] - [Feature/Trigger Types]
- Proposed: Add new "Webhook Triggers" subsection with configuration details

Story 2: [ENG_PROJECT]-146 "Refactor database connection pool"
- Analysis: Internal improvement → NO DOCUMENTATION NEEDED

Story 3: [ENG_PROJECT]-147 "Add filter option to [module] view"
- Analysis: User-visible change to existing feature → UPDATE EXISTING (MEDIUM)
- Doc Section: 3.1 [Module] - Organization
- Proposed: Add filter capability to existing organization section

**Result:** [PRODUCT_PROJECT] story created with 1 new content proposal, 1 existing content update, 1 no-doc entry.

---

**This command automates post-sprint documentation review and ensures product documentation stays current with shipped features.**
