---
description: "Generate customer-facing KB article from a PRD or an issue-tracker story"
---

# Generate KB Article Command

You are executing the `/generate-kb-article` command to create a professional, customer-facing knowledge base article from either a PRD markdown file or a user story in your issue tracker.

## Workflow

### 1. Determine Input Source

Use AskUserQuestion to ask:
- **Source type**: PRD file or an issue-tracker ticket?
- **Source location**: File path or ticket ID (e.g., [ENG_PROJECT]-123 in Jira)?

**Example:**
```
What should I use as source material?
- PRD markdown file (recommended for new features)
- Issue-tracker story (for implemented features)
```

### 2. Extract Source Content

**If PRD file:**
- Read the markdown file using Read tool
- Extract: feature name, problem statement, solution, key functionality, user benefits

**If an issue-tracker ticket:**
- Fetch the ticket via the connected integration (e.g. Jira via the Atlassian MCP, `getJiraIssue`)
- Extract: summary, description, acceptance criteria, comments
- Check for linked issues or parent epic for additional context

### 3. Generate KB Article Content

Create a customer-friendly KB article with these sections:

#### Structure:
```markdown
# [Feature Name]

## Overview
What is this feature? Why should customers care? (2-3 sentences)

## What You Can Do
Clear list of key capabilities:
- Capability 1
- Capability 2
- Capability 3

## How to Use It
Step-by-step instructions:
1. Go to [Location]
2. Click [Action]
3. Configure [Settings]
4. [Result happens]

## Key Features
Detailed breakdown of main features with benefits:
### Feature 1
What it does and why it matters

### Feature 2
What it does and why it matters

## Common Questions

### How do I [common task]?
Answer with clear steps

### Can I [common question]?
Yes/No with explanation

### What if [edge case]?
Solution or workaround

## Best Practices
- Tip 1
- Tip 2
- Tip 3

## Troubleshooting

### Problem: [Common issue]
**Solution:** Step-by-step fix

### Problem: [Another issue]
**Solution:** Step-by-step fix

## Need Help?
Contact support at [support email/link]
```

#### Content Guidelines:
- **Customer-focused language**: Avoid technical jargon, use "you" perspective
- **Benefit-driven**: Explain WHY, not just WHAT
- **Action-oriented**: Clear steps, numbered instructions
- **Scannable**: Short paragraphs, bullet points, headers
- **Complete**: Cover setup, usage, edge cases, troubleshooting
- **Professional tone**: Helpful, confident, not overly casual

### 4. Create PDF Using PDF Skill

Format the KB article as a professional PDF:

**Visual structure:**
- Title page with feature name
- Table of contents (if article is long)
- Clear section headers
- Consistent formatting
- Optional: Screenshots placeholders marked with [Screenshot: Description]
- Footer with page numbers and "Last updated: [date]"

**Use the PDF skill or reportlab directly:**
```python
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# Build structured PDF with proper formatting
```

### 5. Save and Present

Save to:
```
projects/kb-articles/
└── [feature-name]-kb-article.pdf
```

Show the user:
1. **PDF path**: Where it was saved
2. **Quick preview**: First 2-3 sections as markdown
3. **Stats**: Word count, sections covered
4. **Next steps**: "Review the PDF, add screenshots if needed, publish to your KB"

## Input Validation

**For PRD files:**
- Check file exists before reading
- Verify it's markdown format
- If missing key sections, ask user for clarification

**For issue-tracker tickets:**
- Verify ticket exists and is accessible
- Check ticket type (Story/Bug - both can have KB articles)
- If description is sparse, warn user and ask if they want to proceed

## Quality Checklist

Before generating PDF, ensure:
- [ ] Feature name is clear and customer-friendly
- [ ] Overview explains value, not just functionality
- [ ] How-to section has actionable steps
- [ ] At least 3 common questions answered
- [ ] Troubleshooting covers realistic issues
- [ ] No internal jargon or code references
- [ ] Consistent "you" perspective throughout

## Examples

### Example: [Module] Feature

**Input:** PRD for "[Module] - Webhook Receive Action"

**Output sections:**
- Overview: "Trigger automations when external systems send data to [PRODUCT]"
- What You Can Do: Receive webhooks, parse data, trigger actions
- How to Use: Configure webhook URL, set up trigger, test
- Key Features: Custom payloads, filtering, error handling
- Common Questions: Security, formatting, testing
- Troubleshooting: Webhook not firing, incorrect data, timeout issues

### Example: [email provider] Integration

**Input:** Issue-tracker story [ENG_PROJECT]-151 "[Module] - [email provider] self service setup"

**Output sections:**
- Overview: "Connect your [email provider] email to [PRODUCT]'s unified [Module]"
- What You Can Do: Self-service setup, sync emails, unified view
- How to Use: Authorization flow, mailbox selection, sync settings
- Key Features: OAuth security, automatic sync, conversation threading
- Common Questions: Which [email provider] accounts, permissions needed
- Troubleshooting: Connection failed, sync delays, missing emails

## Edge Cases

**Sparse input:**
- If PRD/ticket lacks detail, generate structure and mark [To be filled] sections
- Ask user if they want to provide additional context

**Technical feature:**
- Translate technical language to customer-friendly terms
- Focus on user benefits, not implementation details

**Multiple features in one PRD:**
- Ask user which specific feature to document
- Or create separate KB articles for each major feature

## Error Handling

- **File not found**: Ask for correct path
- **Ticket not found**: Check ticket ID format (e.g. PROJECT-123 in Jira)
- **Empty description**: Warn and ask if user wants to proceed with template
- **PDF generation fails**: Fall back to markdown output and explain issue

## Output Format

Always provide:
1. Generated PDF file path
2. Preview of first 2 sections in markdown
3. Confirmation message with next steps

## Key Principles

1. **Customer-first**: Write for users, not internal teams
2. **Benefit-focused**: Explain value at every step
3. **Complete**: Setup → Usage → Troubleshooting
4. **Professional**: Polished, consistent, helpful tone
5. **Actionable**: Clear steps, not vague descriptions

## Note

This command is perfect for:
- Creating KB articles for new features before launch
- Documenting implemented features from issue-tracker stories
- Building a knowledge base from scratch
- Standardizing documentation format across features

The generated article is a **starting point** - users should:
- Add screenshots/videos
- Validate technical accuracy
- Review with support team
- Test instructions with real users
