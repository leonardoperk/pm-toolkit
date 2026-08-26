# Jira Standards & Story Writing Guidelines

This file documents our standards for writing Jira stories, including templates, priority rules, and conventions.

> **Setup required:** Update the examples, role names, and module names to match your company's Jira setup.
> Run `/setup` for guided onboarding.

## Jira Projects

Commands reference projects by placeholder. Replace each with your real Jira project key (run `/setup`), or substitute at runtime.

| Placeholder | Project | Key |
|---|---|---|
| `[PRODUCT_PROJECT]` | Product / PRD / sprint planning, epics & stories land here | `[FILL IN]` |
| `[ENG_PROJECT]` | Engineering, velocity reference for forecasts | `[FILL IN]` |
| `[SUPPORT_PROJECT]` | Customer support, CS tickets | `[FILL IN]` |

## Story Title Format

`[Module/Feature Area] - [Brief Description]`

**Examples:**
- "[FILL IN: Module Name] - [FILL IN: Feature Description]"
- "[FILL IN: Module Name] - [FILL IN: Feature Description]"

## User Story Template Structure

### Required Sections

#### 1. User Statement
Format: `As a [Role], I want to [action/capability], in order to [outcome/benefit].`

**Valid Roles:**
- [FILL IN: role name 1, e.g. "Agent / End User"]
- [FILL IN: role name 2, e.g. "Admin"]
- [FILL IN: role name 3, e.g. "Super Admin"]
- System

**Example:**
> As a [FILL IN: role], I want to [FILL IN: capability], in order to [FILL IN: outcome].

#### 2. Acceptance Criteria
Bullet list of testable criteria that define "done"

**Guidelines:**
- Use present tense ("User can...", "System displays...", "Feature is...")
- Be specific about what happens, not how it's built
- Include edge cases where relevant
- Focus on user-facing functionality and behavior
- Keep implementation details minimal (refined during sprint planning)

**Example:**
```
* [FILL IN: acceptance criterion 1]
* [FILL IN: acceptance criterion 2]
* [FILL IN: acceptance criterion 3]
```

#### 3. Prototype (when applicable)
Links to design and interactive prototypes:
- Figma clickable prototype
- Figma design screens
- Video demonstrations
- Product prototype screenshots

### Optional Sections

#### 4. Additions
Supplementary information that provides context:
- Technical constraints or dependencies
- Edge case explanations
- Reference data (tables, lists, enums)
- Related ticket references
- Implementation notes for devs
- Clarifications from discussions

#### 5. Out of Scope
Explicitly state what is NOT included in this story:
```
* [Feature/functionality explicitly excluded]
* [Related work saved for different ticket/epic]
```

## Story Scope

**This template applies to:**
- Product/feature stories
- User-facing functionality
- Cross-cutting features (involving both FE and BE)
- Stories with clear user role and outcome

**This template does NOT apply to:**
- Frontend-only technical stories
- Backend-only technical stories
- Testing/QA stories
- Infrastructure/DevOps stories

## Key Principles

1. **Clear, actionable acceptance criteria** - Testable from user perspective
2. **Visual references included** - Via Prototype section when designs exist
3. **Explicit boundaries** - What's in (AC) vs. what's out (Out of Scope)
4. **Context without clutter** - Use Additions section for supplementary info
5. **Focus on WHAT, not HOW** - Describe desired outcome, not implementation

## Common Story Patterns

### [FILL IN: Feature Area 1] Stories
- Focus on [FILL IN: relevant roles]
- Include [FILL IN: what these stories typically involve]

### [FILL IN: Feature Area 2] Stories
- Focus on [FILL IN: relevant roles]
- Include [FILL IN: what these stories typically involve]

### [FILL IN: Feature Area 3] Stories
- Focus on [FILL IN: relevant roles]
- Include [FILL IN: what these stories typically involve]

## Priority Guidelines

**Priority Levels:**
1. Urgent (P1)
2. High (P2)
3. Normal (P3)
4. Low (P4)

*[Document priority rules as they emerge from team practice]*

## Team Assignment

**Valid Teams:**
- [FILL IN: team name, e.g. "Product"] (default for all stories created via this toolkit)

## Labels & Tags

**Common Labels:**
- [FILL IN: document standard labels and when to use them]

*[This section should grow as labeling conventions emerge]*

## Learnings & Best Practices

### What Works Well
*[Capture learnings from successful stories]*
-

### Common Pitfalls
*[Document mistakes to avoid]*
-

### Edge Cases to Remember
*[Build institutional knowledge about tricky scenarios]*
-

## Submission Checklist

Before creating/updating a story:

- [ ] Story title follows naming convention `[Module] - [Description]`
- [ ] User Statement includes role, action, and outcome
- [ ] Acceptance Criteria are testable and user-focused
- [ ] Prototype link(s) included (if designs exist)
- [ ] Out of Scope section added (if scope needs clarification)
- [ ] Additions section used for context (if needed)
- [ ] Tables included for structured data (if applicable)

## Resources

Full template with examples: `templates/user-story-template.md`

---

**Last Updated:** [FILL IN: date]
**Maintainer:** [FILL IN: your name]

## Notes for Future Updates

This file should evolve as you learn:
- Add priority rules after observing patterns
- Capture team assignment conventions
- Document recurring edge cases
- Record successful story examples
- Note common mistakes and how to avoid them
