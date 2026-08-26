---
description: "Monthly CS ticket analysis - patterns, bugs, feature requests, pain points"
---

# CS Monthly Review Command

You are executing the `/cs-monthly-review` command to analyze customer-support tickets from the past month and identify patterns, recurring issues, feature requests, and product gaps.

CS tickets may live in a dedicated support tool (Zendesk, Intercom, Freshdesk, Help Scout) or an issue tracker (Jira Service Management, Linear, etc.). Use whatever integration is connected to pull them, see `config/company-context.md` → "Tools We Use" for what your company uses. The queries below use Jira/JQL as a concrete example; adapt them to your tool.

## Setup

Before starting, read `.claude/knowledge/customer-insights.md` to understand existing patterns and avoid duplicating findings already captured from previous reviews.

## Workflow

### 1. Determine Review Period

Use AskUserQuestion to confirm:
- **Time period**: Last 30 days or custom date range?
- **Default**: Last 30 days from today

**Example:**
```
Which time period should I analyze?
Options:
- Last 30 days (recommended for monthly review)
- Custom date range (you specify start/end dates)
```

### 2. Fetch CS Tickets

Pull the CS tickets for the review period from your support tool, using whatever integration is connected.

**Example, if your tickets are in Jira** (via the Atlassian MCP, `searchJiraIssuesUsingJql`):
```jql
project = [SUPPORT_PROJECT] AND created >= -30d ORDER BY created DESC
```
Custom date range:
```jql
project = [SUPPORT_PROJECT] AND created >= "YYYY-MM-DD" AND created <= "YYYY-MM-DD" ORDER BY created DESC
```

**For another tool** (Zendesk, Intercom, Freshdesk, …): use its equivalent filter/query for the same period via its connected integration.

**Extract from each ticket:**
- Ticket ID / key (e.g., [SUPPORT_PROJECT]-123 in Jira, #12345 in Zendesk)
- Summary
- Description
- Type (Bug, Question, Request, etc.)
- Status
- Priority
- Labels
- Comments (for additional context)
- Reporter
- Created date

### 3. Analyze Tickets (one coherent pass)

Work through the fetched tickets **once**, in this context, sorting findings into the four dimensions below. A single pass keeps cross-cutting themes visible, a bug that drives a feature request, a pain point that signals a product gap, and avoids re-scanning the same ticket set four times. (For very high volume, see Error Handling → sampling.)

Produce entries in the given format for each dimension.

**Dimension 1, Bug Patterns:** recurring bugs (same issue 2+ times), grouped by feature/module, with frequency, severity, and customer impact.
```
### Bug Pattern: [Name]
- **Frequency:** [N] tickets
- **Tickets:** [SUPPORT_PROJECT]-XXX, [SUPPORT_PROJECT]-YYY, [SUPPORT_PROJECT]-ZZZ
- **Pattern:** [What keeps happening]
- **Affected Feature:** [Module/area]
- **Customer Impact:** [How it affects users]
- **Priority Assessment:** HIGH / MEDIUM / LOW
```

**Dimension 2, Feature Requests:** explicit and implicit requests (workarounds, "can we do X?"), grouped by theme, with frequency, unique customers, segment, and business case.
```
### Feature Request: [Name]
- **Frequency:** [N] tickets, [N] unique customers
- **Tickets:** [SUPPORT_PROJECT]-XXX, [SUPPORT_PROJECT]-YYY
- **Request:** [What customers want]
- **Customer Segment:** [Who is asking]
- **Business Case:** [Why they need it]
- **Current Workaround:** [If any]
```

**Dimension 3, Pain Points:** "How do I..." confusion, repeated questions, workflow friction, UI/UX complaints, areas needing docs/training.
```
### Pain Point: [Name]
- **Frequency:** [N] tickets
- **Tickets:** [SUPPORT_PROJECT]-XXX, [SUPPORT_PROJECT]-YYY
- **Struggle:** [What customers find difficult]
- **Impact:** [How it affects their workflow]
- **Possible Causes:** [UI confusion, missing docs, etc.]
- **Potential Solutions:** [Docs update, UI change, training, etc.]
```

**Dimension 4, Product Gaps:** missing features ("no, we don't have that"), integration requests, platform limitations, competitive comparisons.
```
### Product Gap: [Name]
- **Frequency:** [N] tickets, [N] unique customers
- **Tickets:** [SUPPORT_PROJECT]-XXX, [SUPPORT_PROJECT]-YYY
- **Missing Capability:** [What we don't have]
- **Customer Need:** [Why they need it]
- **Competitive Context:** [Do competitors have this?]
- **Impact:** [Business risk if not addressed]
```

### 4. Cross-cutting Synthesis

From the four dimensions:
1. Identify cross-cutting themes (e.g. a bug that drives a feature request, a pain point that signals a product gap)
2. Rank issues by frequency and customer impact
3. Note any gaps in the analysis


### 5. Structure Findings Report

**Group findings into clear sections:**

```markdown
# CS Monthly Review - [Month Year]

## Summary
- **Period:** [Start Date] - [End Date]
- **Total Tickets:** [N]
- **Tickets Analyzed:** [N] (excluding spam, duplicates)
- **Key Findings:** [1-2 sentence overview]

---

## 🐛 Recurring Bugs/Issues

### [Bug Name 1] - [Frequency]
- **Tickets:** [SUPPORT_PROJECT]-XXX, [SUPPORT_PROJECT]-YYY, [SUPPORT_PROJECT]-ZZZ ([N] total)
- **Pattern:** [What keeps happening]
- **Affected Feature:** [Module/area]
- **Customer Impact:** [How it affects users]
- **Priority Assessment:** HIGH / MEDIUM / LOW

### [Bug Name 2] - [Frequency]
...

---

## 💡 Feature Requests

### [Feature Name 1] - [Frequency]
- **Tickets:** [SUPPORT_PROJECT]-XXX, [SUPPORT_PROJECT]-YYY ([N] total)
- **Request:** [What customers want]
- **Customer Segment:** [Who is asking]
- **Business Case:** [Why they need it]
- **Current Workaround:** [If any]

### [Feature Name 2] - [Frequency]
...

---

## 😓 Pain Points

### [Pain Point 1] - [Frequency]
- **Tickets:** [SUPPORT_PROJECT]-XXX, [SUPPORT_PROJECT]-YYY ([N] total)
- **Struggle:** [What customers find difficult]
- **Impact:** [How it affects their workflow]
- **Possible Causes:** [UI confusion, missing docs, etc.]
- **Potential Solutions:** [Docs update, UI change, training, etc.]

### [Pain Point 2] - [Frequency]
...

---

## 🔍 Product Gaps

### [Gap 1] - [Frequency]
- **Tickets:** [SUPPORT_PROJECT]-XXX, [SUPPORT_PROJECT]-YYY ([N] total)
- **Missing Capability:** [What we don't have]
- **Customer Need:** [Why they need it]
- **Competitive Context:** [Do competitors have this?]
- **Impact:** [Business risk if not addressed]

### [Gap 2] - [Frequency]
...

---

## 📊 Overall Insights

**Top Issues by Volume:**
1. [Issue name] - [N] tickets
2. [Issue name] - [N] tickets
3. [Issue name] - [N] tickets

**Top Issues by Customer Count:**
1. [Issue name] - [N] unique customers
2. [Issue name] - [N] unique customers
3. [Issue name] - [N] unique customers

**Feature Area Breakdown:**
- [Module A]: [N] tickets
- [Module B]: [N] tickets
- [Module C]: [N] tickets
- [Module D]: [N] tickets
- Other: [N] tickets

**Trends:**
- [Observation about patterns]
- [Notable changes from last month, if known]
- [Emerging issues to watch]

---

## 📋 Data Notes

- **Analysis Date:** [Current date]
- **Tickets Excluded:** [Spam, test tickets, duplicates, etc.]
- **Methodology:** Automated analysis via `/cs-monthly-review`
```

### 6. Save Report

Save the full findings report as a markdown file:

**File path:** `reports/cs-reviews/[YYYY-MM]-cs-monthly-review.md`

Confirm the saved location to the user.

### 7. Capture Learnings

**After saving the report, prompt for learnings:**

```
📚 Learning Capture

CS monthly review is complete! Before we finish, let's capture any customer insights.

Did this review reveal any important patterns worth documenting? For example:
- Recurring customer pain points
- New feature request themes
- Customer segment behaviors
- Product-market fit signals

Options:
- Yes, I have insights to capture
- No, skip for now
```

**If user wants to capture insights:**

Use AskUserQuestion to gather:
- **Question:** "What customer insights should I capture from this CS review?"
- **Prompt:** Share any patterns, pain points, or feature requests worth documenting for future reference.

**After receiving insights, update knowledge file:**

1. Read current content from `.claude/knowledge/customer-insights.md`
2. Update relevant sections based on learnings:
   - Add new recurring pain points to "Recurring Pain Points" section
   - Add new feature requests to "Top Feature Requests" section
   - Add monthly summary to "Monthly CS Review Summaries" section:

```markdown
### [Month Year]
**Period:** [Start] - [End]
**Total Tickets:** [N]

**Top Themes:**
1. [Theme 1 from review]
2. [Theme 2 from review]
3. [Theme 3 from review]

**Key Learnings:**
[User insights about customer patterns]

**Action Items:**
- [ ] [Product improvements identified]
- [ ] [Documentation updates needed]
- [ ] [Feature requests to prioritize]

**Link to Full Report:** reports/cs-reviews/[YYYY-MM]-cs-monthly-review.md

---
```

3. Write updated content back to `.claude/knowledge/customer-insights.md`
4. Confirm to user:

```
✅ Customer insights captured in .claude/knowledge/customer-insights.md

These patterns will inform roadmap prioritization and product decisions.
```

**If user skips:**
- Continue to completion without capturing insights

### 8. Present Results

After insights are captured (or skipped):

```
✅ CS Monthly Review Complete - [Month Year]

📊 Analysis Summary:
   - Period: [Start] - [End]
   - Total tickets analyzed: [N]

   Key Findings:
   • Recurring bugs: [N] patterns identified
   • Feature requests: [N] themes
   • Pain points: [N] areas of struggle
   • Product gaps: [N] missing capabilities

📄 Report saved: reports/cs-reviews/[YYYY-MM]-cs-monthly-review.md

📋 Next Steps:
   1. Review the report
   2. Prioritize which issues to address
   3. Create follow-up stories or bug tickets as needed
   4. Update documentation for pain points
   5. Add feature requests to roadmap consideration
```

## Pattern Detection Guidelines

### Identifying Recurring Bugs

**Look for:**
- Similar keywords in summaries (e.g., "sync", "error", "failed")
- Same feature mentioned multiple times
- Same error codes or messages
- Temporal clusters (many reports in short time)

**Grouping Rules:**
- Must affect same feature/module
- Must have similar symptoms or root cause
- Different error messages can be same bug if behavior matches
- Include resolved tickets if recent (last 30 days)

### Identifying Feature Requests

**Clear Signals:**
- Summary contains "add", "support", "enable", "allow"
- Description starts with "Can we..." or "Is it possible..."
- Comparison to competitor feature
- Explicit statement: "We need X"

**Implicit Signals:**
- Customer asks for workaround (indicates missing feature)
- Questions about functionality that doesn't exist
- Request for integration with specific tool

### Identifying Pain Points

**User Confusion:**
- "How do I..." questions
- Multiple attempts to do same thing
- Requests for training or documentation
- Support agent spent significant time explaining

**Workflow Issues:**
- "It takes too many steps to..."
- "I have to do this manually..."
- Process described as "tedious" or "difficult"

**UI/UX Problems:**
- "Can't find where to..."
- "Not intuitive"
- "Unclear" or "confusing"

### Identifying Product Gaps

**Missing Features:**
- Explicit "no" answers from support
- Comparisons: "Competitor X has this"
- Workarounds involving external tools
- Customer considering switching due to gap

**Integration Requests:**
- Specific tools/platforms mentioned
- API endpoint requests
- Data sync needs

## Error Handling

**No CS tickets in period:**
- Inform user: No CS tickets found in last 30 days
- Suggest checking project access or date range
- Stop here; nothing to report

**Support tool not accessible:**
- Verify the CS tool integration is connected and you have access
- List available projects/queues
- Suggest an alternative source or date range

**Very high volume (100+ tickets):**
- Inform user: Large dataset, analysis may take time
- Focus on most frequent patterns
- Sample tickets if needed to keep analysis manageable

**API errors (when fetching tickets):**
- Report error clearly
- Verify the integration and permissions for your CS tool
- Suggest an alternative source or date range

## Quality Checks

Before saving the report:
- [ ] All categories have at least 1 finding (or marked "None identified")
- [ ] Ticket references are accurate (using your tool's ticket ID / key format)
- [ ] Frequencies are counted correctly
- [ ] Patterns are clearly described
- [ ] Summary stats match detailed findings
- [ ] Report is structured and readable

## Important Notes

- **Focus on data, not opinions** - Present what customers reported, not interpretations
- **Include ticket counts** - Shows confidence in patterns
- **Group by theme** - Don't list every individual ticket
- **Note customer segments** - Enterprise vs SMB, industry, etc.
- **Exclude noise** - Spam, test tickets, clearly duplicate tickets
- **Recurring = 2+** - Need at least 2 similar tickets to call it "recurring"

## Integration with Other Workflows

**After monthly review:**

1. **Bug Fixes**
   - Create engineering tickets in your issue tracker for recurring bugs
   - Reference CS tickets in bug description
   - Prioritize based on customer impact

2. **Feature Roadmap**
   - Add feature requests to backlog
   - Use frequency data for prioritization
   - Consider in quarterly planning

3. **Documentation**
   - Update KB articles for pain points
   - Create new articles for confusing features
   - Add FAQ items from common questions

4. **Product Strategy**
   - Use product gaps in competitive analysis
   - Consider integration priorities
   - Inform build vs buy decisions

---

**This command provides monthly insights into customer experience, helping prioritize product improvements based on actual support data.**
