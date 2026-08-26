# Product Documentation Style Guide

**For [Company] Product Documentation and AI Knowledge Bases**

**Version:** 1.0
**Last Updated:** 2026-02-06
**Author:** Product Team

---

## Table of Contents

1. [Purpose](#purpose)
2. [Document Structure](#document-structure)
3. [Heading Conventions](#heading-conventions)
4. [Text Formatting](#text-formatting)
5. [Lists](#lists)
6. [Tables](#tables)
7. [Code Blocks & Diagrams](#code-blocks--diagrams)
8. [Links](#links)
9. [Callouts & Emphasis](#callouts--emphasis)
10. [UI Elements & Status Values](#ui-elements--status-values)
11. [Sections & Separators](#sections--separators)
12. [Version Control](#version-control)

---

## Purpose

This style guide ensures LLM-readability and consistency across [Company]'s product documentation. Following these guidelines helps:

- **LLMs** parse and understand the documentation accurately
- **AI chatbots** provide correct answers to users
- **Teams** maintain consistency across multiple documents
- **Readers** navigate and comprehend information easily

---

## Document Structure

### 1. Document Header

Every document must start with:

```markdown
# [Document Title]

**Last Updated:** YYYY-MM-DD
**Version:** X.Y

## Table of Contents

[ToC content]

---
```

**Example:**
```markdown
# [Company] Product Documentation

**Last Updated:** 2026-02-06
**Version:** 1.1

## Table of Contents

### 1. Product Overview
### 2. User Roles & Permissions
...

---
```

### 2. Section Introductions

Every major section (H1) should include a brief introduction paragraph explaining what the section covers.

**Good:**
```markdown
# 2. User Roles & Permissions

[Company] supports two user roles with distinct permission levels: Users (Agents) who handle day-to-day communication, and Admins who configure the platform and manage settings.
```

**Bad:**
```markdown
# 2. User Roles & Permissions

## User (Agent)
[jumps straight to subsections]
```

### 3. Document Footer

End every document with:

```markdown
---

_This documentation describes [Company]'s product functionality for internal reference and AI chatbot knowledge bases._

_Last updated: YYYY-MM-DD_
```

---

## Heading Conventions

### Hierarchical Numbering

Use **hierarchical numbering** for major sections and subsections:

**Correct:**
```markdown
# 1. Product Overview
# 2. User Roles & Permissions
# 3. Core Modules
## 3.1 Projects
## 3.2 Members
## 3.3 Automations
# 4. Companion Applications
## 4.1 Browser Extension
## 4.2 Mobile Application
```

**Incorrect:**
```markdown
# 1. Product Overview
# 2. User Roles & Permissions
# 3.1 Projects  ← Don't skip from flat to hierarchical
# 3.2 Members
# 4. Companion Applications
```

### Heading Levels

- **H1 (`#`)**: Major sections only (numbered: 1, 2, 3...)
- **H2 (`##`)**: Subsections (numbered: 3.1, 3.2, 4.1...)
- **H3 (`###`)**: Sub-subsections (no numbers, descriptive titles)
- **H4 (`####`)**: Rarely used, only for deep nesting

**Example:**
```markdown
# 3. Core Modules
## 3.1 Projects
### Supported Channels
### Core Actions
#### Message Handling  ← Use H4 sparingly
```

### Heading Formatting

- Use **sentence case** for headings (capitalize first word only, except proper nouns)
- No trailing punctuation (no periods, no colons)
- Be descriptive and specific

**Good:**
```markdown
## What is the [Company] Mobile App
### Platform availability
```

**Bad:**
```markdown
## What Is The [Company] Mobile App:
### Platforms
```

---

## Text Formatting

### Bold Text

Use bold for:
- **Emphasis** on critical terms
- **Section labels** (e.g., "Prerequisites:", "Features:")
- **Important warnings** within callouts

**Example:**
```markdown
**Prerequisites:**
*   Active [Company] account
*   Internet connection

**IMPORTANT:** AI conversations do NOT auto-resolve.
```

### Italic Text

Use italic sparingly for:
- *Sub-labels* within sections
- *Document references* (e.g., "_See Section 3.1_")

**Example:**
```markdown
**iOS:**
*   Available on Apple App Store

_This feature is in beta._
```

### Inline Code

Use backticks for:
- Status values: `"Open"`, `"Pending"`, `"Closed"`
- UI labels: `Settings`, `Profile settings`
- Field names: `Due Date`, `Record ID`
- Technical terms: `OAuth`, `API`

**Example:**
```markdown
Navigate to `Settings` → `Account settings` and set the status to `"Open"`.
```

---

## Lists

### Bulleted Lists

Use `*` for bulleted lists (not `-` or `+`):

**Correct:**
```markdown
*   First item
*   Second item
*   Third item
```

**Incorrect:**
```markdown
- First item
+ Second item
* Third item  ← Inconsistent
```

### Nested Lists

Indent nested lists with **4 spaces**:

```markdown
*   Parent item
    *   Child item 1
    *   Child item 2
        *   Grandchild item
*   Another parent item
```

### Numbered Lists

Use numbered lists for sequential steps:

```markdown
1. First step
2. Second step
3. Third step
```

### Mixed Lists

Don't mix bullet styles unnecessarily. Only nest when hierarchically related:

**Good:**
```markdown
**Supported Channels:**

*   Email
*   Chat
*   Webchat
```

**Bad:**
```markdown
**Supported Channels:**

*   Email
    *   Gmail  ← Only nest if showing sub-types
    *   [email provider]
*   Chat
```

---

## Tables

### Table Structure

Always include:
1. **Header row** with semantic labels
2. **Separator row** with `---`
3. **Data rows**

**Example:**
```markdown
| Status | Description | Trigger |
| ---| ---| --- |
| Open | Requires attention | Agent manually opens |
| Pending | AI handling | Conversation with active AI |
| Closed | Resolved | Agent closes or auto-resolves |
```

### Table Headers

Use **clear, semantic headers** that describe the column content:

**Good:**
```markdown
| Event | Description | Timing Options |
```

**Less Clear:**
```markdown
| Name | Info | When |
```

### Descriptive Context

Add a descriptive line before complex tables:

```markdown
**Available Merge Fields:**

[Company] uses standardized merge fields guaranteed across all external integrations:

| Merge Field | Description | Example |
| ---| ---| --- |
| Due Date | Task's due date | 2026-03-15 |
```

### Table Alignment

Use default left-alignment for readability (no `:---:` center alignment needed).

---

## Code Blocks & Diagrams

### Code Fence Types

Use appropriate code fence types:

- **Plain text diagrams:** Use ` ```text `
- **Actual code:** Use language-specific fences (` ```python `, ` ```javascript `)
- **Generic content:** Use ` ```text ` or no fence (plain markdown)

**Correct:**
```markdown
    ```text
    User submits a request
            ↓
    AI chatbot receives message
            ↓
    AI responds
    ```
```

**Incorrect:**
```markdown
    ```yaml  ← Wrong! This isn't YAML
    User submits a request
            ↓
    AI chatbot receives message
    ```
```

### ASCII Diagrams

For flowcharts and diagrams:

```markdown
    ```text
    External event occurs
            ↓
    [Company] receives event
            ↓
        ┌───────────────┐
        │ Decision?     │
        └───────────────┘
               │
         Yes ──┴── No
          ↓        ↓
       Action   Other
    ```
```

### Indented Code Blocks

Alternative to fences, use 4-space indentation:

```markdown
    User submits a request
            ↓
    AI chatbot receives message
```

---

## Links

### Inline Links

Use **inline link format** consistently:

**Correct:**
```markdown
Refer to the [Integration Capability Matrix](#) and [Integration Connection Guides](https://app.clickup.com/...)
```

**Incorrect:**
```markdown
Refer to the Integration Capability Matrix (https://app.clickup.com/...)
```

**Very Incorrect:**
```markdown
[
Integration Connection Guides
https://app.clickup.com/...
]
```

### External Links

For external documentation:

```markdown
See [the chat provider's 24-hour messaging window documentation](https://developers.facebook.com/...)
```

### Internal References

For cross-references within the document:

```markdown
Refer to [Section 3.1](#31-projects) for details.
```

Or use contextual references:

```markdown
See the Integrations section for details.
```

---

## Callouts & Emphasis

### Standard Callouts

Use **standardized callout types** with consistent formatting:

**IMPORTANT:** For critical information that affects functionality

```markdown
**IMPORTANT:** AI conversations do NOT auto-resolve.
```

**NOTE:** For helpful context or clarifications

```markdown
**NOTE:** Not all external systems support all events.
```

**WARNING:** For things to avoid or potential issues

```markdown
**WARNING:** Deleting a contact also deletes all associated conversations.
```

**TIP:** For best practices or helpful suggestions

```markdown
**TIP:** Use descriptive label names for better organization.
```

### Callout Format

Always use:
- Bold for callout type
- Colon after callout type
- Space before content

**Correct:**
```markdown
**IMPORTANT:** This is the content.
```

**Incorrect:**
```markdown
**Important**: This is the content.  ← Not all caps
**IMPORTANT** This is the content.  ← Missing colon
**IMPORTANT:**This is the content.  ← Missing space
```

### Multi-Line Callouts

For longer callouts, use a bulleted list:

```markdown
**CRITICAL:** AI conversations do NOT automatically resolve.

*   AI remains in "Pending" status indefinitely
*   Manual resolution required
*   Agents must review pending conversations regularly
```

---

## UI Elements & Status Values

### Quote All UI Elements

Consistently quote:
- Status values: `"Open"`, `"Pending"`, `"Closed"`
- UI labels: `"Settings"`, `"Profile settings"`
- Button text: `"Send"`, `"Cancel"`
- Menu items: `"Account settings"`, `"Agents"`

**Correct:**
```markdown
Navigate to `Settings` → `Account settings` and change the status to `"Open"`.

When the conversation is in `"Pending"` status, agents can manually take over.
```

**Incorrect:**
```markdown
Navigate to Settings → Account settings and change the status to Open.  ← No quotes/backticks
```

### Navigation Paths

Use arrow (`→`) for navigation paths:

```markdown
`Settings` → `Account settings` → `General`
```

### Field Names

Use **bold** for field labels in descriptions, backticks in instructions:

**In descriptions:**
```markdown
**Due Date:** Task's due date
```

**In instructions:**
```markdown
Enter the value in the `Due Date` field.
```

---

## Sections & Separators

### Horizontal Rules

Use `---` (three dashes) for section separators:

**Placement:**
- After Table of Contents
- At the **end** of each major section (before next H1)
- Before document footer

**Example:**
```markdown
# 1. Product Overview

[Content]

---

# 2. User Roles & Permissions

[Content]

---
```

### Separator Style

**Correct:** `---` (three dashes)

**Incorrect:**
- `* * *` (asterisks with spaces)
- `___` (underscores)
- `-----` (five dashes)

---

## Version Control

### Version Number

Use **semantic versioning** (X.Y):
- **X**: Major changes (restructuring, new sections)
- **Y**: Minor changes (updates, corrections, additions)

**Examples:**
- `1.0` - Initial version
- `1.1` - Minor updates
- `2.0` - Major restructure

### Update Tracking

Include at both **top and bottom** of document:

**Top:**
```markdown
# Document Title

**Last Updated:** 2026-02-06
**Version:** 1.1
```

**Bottom:**
```markdown
_Last updated: 2026-02-06_
```

### Change Log

For major documents, consider maintaining a change log:

```markdown
## Change Log

**Version 1.1** (2026-02-06)
- Added section on companion applications
- Updated integration table
- Standardized callout formatting

**Version 1.0** (2026-01-15)
- Initial release
```

---

## Quick Reference

### ✅ Do's

- Use hierarchical heading numbers (1, 2, 3.1, 3.2)
- Add intro paragraphs to major sections
- Use `---` separators at end of sections
- Quote all UI elements and statuses (`"Open"`, `"Pending"`)
- Use ` ```text ` for ASCII diagrams
- Use inline link format: `[text](url)`
- Standardize callouts: **IMPORTANT:**, **NOTE:**, **WARNING:**, **TIP:**
- Include version/timestamp at top and bottom
- Use `*` for bulleted lists
- Add context before complex tables

### ❌ Don'ts

- Don't skip heading levels (H1 → H3)
- Don't mix bullet styles (`*` vs `-` vs `+`)
- Don't use language-specific code fences for diagrams (no ` ```yaml ` for flowcharts)
- Don't use block-level links with brackets
- Don't use `* * *` for separators (use `---`)
- Don't mix callout formats (always **TYPE:** format)
- Don't forget to quote status values
- Don't omit section separators

---

## Examples

### Complete Section Example

```markdown
# 3. Core Modules

[Company]'s functionality is organized into six core modules that work together to provide comprehensive work management.

## 3.1 Projects

The projects module is [Company]'s central hub for team collaboration.

### Supported Channels

The Projects module receives events from the following channels:

*   **Email**: Gmail, [email provider], IMAP/SMTP
*   **Chat**: Chat API
*   **Webchat**: Widget for customer websites

### Conversation Statuses

Every conversation has exactly **one of four statuses** at any given time:

| Status | Description |
| ---| --- |
| Open | Requires agent attention |
| Pending | AI is handling conversation |
| Closed | Conversation resolved |

**IMPORTANT:** AI conversations remain in `"Pending"` status indefinitely.

**Workflow:**

    ```text
    User submits a request
            ↓
    AI responds
            ↓
    Status: "Pending"
    ```

For more details, see the [Key Workflows](#5-key-workflows) section.

---

# 4. Companion Applications

[Next section content]
```

---

## Compliance Checklist

Use this checklist when creating or updating documentation:

- [ ] Document has version and date at top
- [ ] Table of Contents present
- [ ] All major sections (H1) have intro paragraphs
- [ ] Heading numbering is hierarchical (1, 2, 3.1, 3.2...)
- [ ] Section separators (`---`) at end of major sections
- [ ] All UI elements quoted with backticks
- [ ] All status values quoted (e.g., `"Open"`)
- [ ] Callouts use standard format: **TYPE:** content
- [ ] Links use inline format: `[text](url)`
- [ ] ASCII diagrams use ` ```text ` fences
- [ ] Bulleted lists use `*` consistently
- [ ] Tables have descriptive headers
- [ ] Complex tables have context text above
- [ ] Document footer present with update date

---

## Maintenance

This style guide should be updated when:

- New documentation patterns emerge
- LLM parsing requirements change
- Team feedback suggests improvements
- Documentation technology changes

**Maintainer:** Product Team
**Review Cycle:** Quarterly

---

_This style guide is maintained by the [Company] Product Team._

_Last updated: 2026-02-06_
