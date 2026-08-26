# User Story Template

## Story Title Format
`[Module/Feature Area] - [Brief Description]`

**Examples:**
- "[FILL IN: Module Name] - [FILL IN: Feature Description]"
- "[FILL IN: Module Name] - [FILL IN: Feature Description]"

> **Setup:** Replace the example module names and roles below with your company's actual modules and user roles.
> See `.claude/knowledge/jira-standards.md` for team-specific standards.

---

## User Statement

As a [Role], I want to [action/capability], in order to [outcome/benefit].

**Role Options:**
- [FILL IN: role name 1, e.g. "Agent / End User"]
- [FILL IN: role name 2, e.g. "Admin"]
- [FILL IN: role name 3, e.g. "Super Admin"]
- System

**Example:**
> As a [FILL IN: role], I want to [FILL IN: capability], in order to [FILL IN: outcome].

---

## Acceptance Criteria

Bullet list of testable criteria that define "done":

* [Criterion 1 - specific, testable condition]
* [Criterion 2 - specific, testable condition]
* [Criterion 3 - specific, testable condition]

**Guidelines:**
- Use present tense ("User can...", "System displays...", "Feature is...")
- Be specific about what happens, not how it's built
- Include edge cases where relevant
- Focus on user-facing functionality and behavior
- Keep implementation details minimal (refined during sprint planning)

---

## Prototype

Link to design and interactive prototypes:

**Format:**
```
[Clickdummy](figma-prototype-link)
[Designs](figma-design-link)
[Video Walkthrough](recording-link)
```

**What to include:**
- Figma clickable prototype
- Figma design screens
- Video demonstrations
- Product prototype screenshots

---

## Additions *(Optional)*

Supplementary information that provides context:

- Technical constraints or dependencies
- Edge case explanations
- Reference data (tables, lists, enums)
- Related ticket references
- Implementation notes for devs
- Clarifications from discussions

---

## Out of Scope *(Optional)*

Explicitly state what is NOT included in this story:

* [Feature/functionality explicitly excluded]
* [Related work saved for different ticket/epic]

---

## Reference Tables *(When Applicable)*

Use tables to clarify enums, options, or structured data:

**Example - Events Table:**
| **Event** | **Definition** | **When it fires** | **Offset** |
| --- | --- | --- | --- |
| [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |

**Example - Status Explanation:**
| **Status** | **Explanation** |
| --- | --- |
| [FILL IN] | [FILL IN] |

---

## Template Notes

**Scope:**
- Product/feature stories only
- User-facing functionality
- Cross-cutting features (involving both FE and BE)
- Clear user role and outcome
- Testable from user perspective

**Key Principles:**
1. Clear, actionable acceptance criteria
2. Visual references included via Prototype section
3. Explicit boundaries (what's in via AC, what's out via Out of Scope)
4. Context provided via Additions without cluttering main sections
5. Focus on WHAT needs to happen, not HOW it's implemented

---

## Checklist Before Submission

- [ ] Story title follows naming convention `[Module] - [Description]`
- [ ] User Statement includes role, action, and outcome
- [ ] Acceptance Criteria are testable and user-focused
- [ ] Prototype link(s) included (if designs exist)
- [ ] Out of Scope section added (if scope needs clarification)
- [ ] Additions section used for context (if needed)
- [ ] Tables included for structured data (if applicable)
