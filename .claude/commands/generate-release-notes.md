---
description: "Generate customer-facing release notes from sprint work"
---

# Generate Release Notes

Generate customer-facing release notes from the work shipped in a sprint, using the release notes template.

The shipped work is pulled from wherever it lives, an issue tracker (Jira, Linear, Azure DevOps, …), or supplied directly. See `config/company-context.md` → "Tools We Use" for what your company uses. Examples below use Jira/JQL as a concrete case; adapt them to your tracker.

## Workflow

### 1. Determine the Source

Use AskUserQuestion to ask what the notes should be based on:
- **A completed sprint** (recommended), auto-fetch its shipped items from the tracker
- **Specific epic/story IDs or a PRD reference**, supplied by the user

For a sprint, also confirm the sprint name and the project/tracker.

### 2. Fetch the Shipped Work

**If a sprint**, pull the completed items via the tracker's integration.

Example, if your work is in Jira (Atlassian MCP, `searchJiraIssuesUsingJql`):
```jql
project = [ENG_PROJECT] AND sprint = "Sprint X" AND status in (Done, Closed) ORDER BY type
```
For another tracker (Linear, Azure DevOps, …): use its equivalent query for the sprint's completed items.

**If IDs / a PRD**, read those directly (fetch each ticket via the integration, or read the PRD file).

**From each item, extract:** summary, description, type, and any customer-facing labels.

### 3. Classify Each Item

Sort the shipped work into the release-notes buckets, and drop what customers don't care about:

- **New Features**, new capability that didn't exist before
- **Improvements**, enhancements to existing functionality, user-visible changes
- **Bug Fixes**, only if customer-impacting
- **Exclude**, internal refactors, infra/tooling, tech debt, dev-only changes, minor tweaks

### 4. Write the Release Notes

Use the template at `templates/release-notes-template.md` as the structure and tone guide.

Write customer-facing content that:
- Focuses on benefits, not technical implementation
- Uses a conversational, engaging tone
- Groups related changes logically
- Emphasizes "what changed" and "why it matters"
- Avoids jargon and internal terminology

### 5. Structure

- **New Features**, Major additions with detailed descriptions
- **Improvements**, Enhancements to existing functionality
- **Bug Fixes** (optional), Only if customer-impacting

### 6. Format and Save

- Use bold for feature names and key benefits
- Bullet points for feature details
- Keep it scannable and concise
- Ask the user where to save the output file
