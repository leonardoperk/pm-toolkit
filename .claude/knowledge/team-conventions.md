# Team Conventions & Company-Specific Practices

This file documents company-specific conventions, technical context, and team practices.

> **Setup required:** Fill in all `[FILL IN: ...]` placeholders with your company's information.
> Run `/setup` for guided onboarding.

## Technical Architecture

### Backend Stack

**[FILL IN: Primary Backend Framework/Language]**
- Usage: [FILL IN: e.g. "Core application, legacy features"]
- Status: [FILL IN: e.g. "Production-stable, established codebase"]
- When to consider: [FILL IN: e.g. "Extending existing features"]

**[FILL IN: Secondary Backend Framework/Language, if applicable]**
- Usage: [FILL IN: e.g. "New services and microservices"]
- Status: [FILL IN: e.g. "Modern framework for new feature development"]
- When to consider: [FILL IN: e.g. "Greenfield features, new services"]

**Architecture Pattern:** [FILL IN: e.g. "Monolith", "Microservices", "Hybrid monolith + new services"]

### Frontend Stack

**[FILL IN: Frontend Framework]**
- Framework: [FILL IN: e.g. "React 18", "Vue 3", "Angular"]
- Features: [FILL IN: e.g. "Hooks-based, TypeScript"]
- State management: [FILL IN: e.g. "Redux", "Zustand", "Pinia"]
- Build tool: [FILL IN: e.g. "Vite", "Webpack"]

### Database

**[FILL IN: Database]**
- Primary database: [FILL IN: e.g. "PostgreSQL", "MySQL", "MongoDB"]
- Supports: [FILL IN: key capabilities]
- Migrations: [FILL IN: e.g. "Rails migrations", "TypeORM", "Flyway"]

### Infrastructure

**[FILL IN: Cloud Provider]**
- Cloud provider: [FILL IN: e.g. "AWS", "GCP", "Azure"]
- Relevant for: Scalability assessments, deployment, infrastructure costs
- Common services: [FILL IN: key services used]

## Technical Complexity Assessment

### Low Complexity
- [FILL IN: example of low complexity work in your stack]
- [FILL IN: example 2]

### Medium Complexity
- [FILL IN: example of medium complexity work]
- [FILL IN: example 2]

### High Complexity
- [FILL IN: example of high complexity work]
- [FILL IN: example 2]

## Product Documentation Standards

### Source of Truth Priority

When answering questions about product capabilities, trust sources in this order:

1. **Product documentation** (`docs/product documentation/`)
2. **Jira tickets** (completed stories, PRDs, specifications)
3. **User-provided context** (what the user tells you directly)
4. **Logical inference** (only when above sources unavailable)

### Documentation Structure

Product documentation is organized as:
- [FILL IN: Section 1, e.g. "Product Overview"]
- [FILL IN: Section 2, e.g. "User Roles & Permissions"]
- [FILL IN: Section 3, Core Features]
  - [FILL IN: 3.1 Feature Area]
  - [FILL IN: 3.2 Feature Area]
  - [FILL IN: 3.3 Feature Area]
- [FILL IN: Section 4, Additional Products/Apps]
- [FILL IN: Section 5, Key Workflows]
- [FILL IN: Section 6, Limitations & Boundaries]

**Do not add new top-level sections** without deliberate intent, respect existing structure.

## Communication Style

### Direct and Professional
- Use active voice and clear statements
- Avoid apologizing for limitations, state what you CAN do
- No hedging with "I think maybe" or "perhaps possibly"
- Be concise, respect the user's time
- No unnecessary superlatives or praise

### Cite Sources
Always reference specific sources when stating facts:

**Format:** "According to [Section X.Y], [fact]"

### Prioritize Truth Over Validation
- Provide direct, factual information even if it contradicts user assumptions
- Disagree respectfully when necessary
- Apply rigorous standards to all ideas
- Focus on "what is" rather than "what you want to hear"

## PM Toolkit Workflows

### PRD Creation
1. Ask extensive clarifying questions first
2. Use `/create-prd` command for structured interview
3. Reference the Hybrid template (`.claude/knowledge/prd-template.md`)
4. Identify which persona(s) the feature serves
5. Include evidence and customer context

### User Story Generation
1. Use user story template (`templates/user-story-template.md`)
2. Follow naming convention: `[Module] - [Description]`
3. Include proper role, acceptance criteria, prototypes
4. Clarify implementation details in Additions
5. Add Out of Scope section when boundaries need clarity

### Sprint Documentation Review
1. Use `/sprint-documentation-review` command
2. Analyze completed work against product documentation
3. Propose documentation updates
4. Respect existing documentation structure

### CS Monthly Review
1. Use `/cs-monthly-review` command
2. Analyze tickets for patterns, bugs, feature requests
3. Update `.claude/knowledge/customer-insights.md` with findings
4. Identify product vs. documentation vs. onboarding issues

## Decision-Making Principles

### Challenge Low-Value Work
Before executing organizational/cleanup tasks, assess: "What real problem does this solve?"

**When to DO the work:**
- User is actively struggling to find things
- Multiple people are getting confused
- Current organization is causing errors or bugs
- System is being shared/onboarded to new people soon
- Technical debt is slowing actual development

**When to SKIP the work:**
- "It would be cleaner this way"
- "Best practices say we should..."
- "This might become a problem someday"
- No one has complained or struggled with current state

### Information Source Priority
Always check documentation FIRST before making assumptions:
1. Check product documentation for feature constraints
2. Check Jira tickets for existing implementations
3. Reference tech stack for general capabilities
4. Ask user for implementation specifics or unknowns

**Never assume implementation details** beyond what's documented.

### When to Ask for Clarification
Even with knowledge files, always ask about:
- Specific versions (if version matters for compatibility)
- Existing patterns ("How is X currently implemented?")
- Performance requirements (database optimization, caching)
- Third-party integrations (external APIs, services, libraries)
- Migration complexity (if changing existing functionality)
- Testing requirements (unit, integration, E2E expectations)

## Workflow Commands Reference

**PRD Workflows:**
- `/create-prd` - Interactive PRD creation
- `/review-prd` - Review PRD for completeness

**Jira Workflows:**
- `/generate-user-stories` - Generate user stories from PRD sections
- `/generate-kb-article` - Create KB article from PRD/Jira story

**Analysis Workflows:**
- `/cs-monthly-review` - Monthly CS ticket analysis
- `/sprint-documentation-review` - Analyze sprint and propose doc updates

**Forecasting Workflows:**
- `/forecast-sprint` - Monte Carlo sprint completion forecast
- `/forecast-epic` - Epic completion forecast

**Project Workflows:**
- `/requirements` - Structured requirements gathering
- `/extract-action-items` - Extract action items from meeting notes

## Knowledge Capture

After completing major workflows (PRD, user stories, sprint review, CS review), consider capturing learnings:

**Questions to ask yourself:**
- What patterns worked well?
- What caused confusion or rework?
- What edge cases emerged?
- What would you do differently next time?

**Where to capture:**
- PRD learnings → `.claude/knowledge/prd-template.md`
- Jira story learnings → `.claude/knowledge/jira-standards.md`
- Customer insights → `.claude/knowledge/customer-insights.md`
- Team practices → This file (`.claude/knowledge/team-conventions.md`)

## Related Resources

- Operating Principles: `.claude/context/operating-principles.md`
- Tech Stack: `.claude/context/tech-stack.md`
- Product Context: `PRODUCT_CONTEXT.md`
- Jira Standards: `.claude/knowledge/jira-standards.md`
- PRD Template: `.claude/knowledge/prd-template.md`
- Customer Insights: `.claude/knowledge/customer-insights.md`

---

**Last Updated:** [FILL IN: date]
**Maintainer:** [FILL IN: your name]

## Maintenance Notes

This file should be updated when:
- New team conventions are established
- Technical stack changes (new frameworks, services)
- Workflow commands are added or modified
- Common patterns emerge that should be standardized
- Mistakes are made that should be avoided in future

Keep this file focused on **company-specific** practices. General PM best practices belong in other knowledge files.
