---
description: "Review PRD from engineer, executive, user researcher, and product analyst perspectives"
---

# Review PRD

Review the current PRD from multiple perspectives (engineer, executive, user researcher, product analyst).

## Workflow

### 1. Read the PRD

Read the PRD provided or linked by the user. If none is provided, ask for it.

### 2. Ask 3 Focused Clarifying Questions

Use AskUserQuestion to ask (max 3 questions, can be asked together):

1. **Context**, What triggered this PRD? (customer request, strategic initiative, competitive pressure, other)
2. **Constraints**, Are there dependencies, hard deadlines, or technical constraints I should factor into the review?
3. **Focus**, Is there a specific angle or concern you most want the review to address?

Proceed immediately after receiving answers. Do not ask follow-up clarifying questions.

### 3. Multi-Agent Review

Launch four sub-agents in parallel using the Task tool, one per perspective. Use the project's custom agents so each persona stays defined in one place (`.claude/agents/`), not duplicated here:

- `subagent_type: engineer`
- `subagent_type: executive`
- `subagent_type: user-researcher`
- `subagent_type: product-analyst`

Send all four in a **single message** (parallel). Give each agent a prompt containing:
- The full PRD text (or its file path)
- The answers from the clarifying questions (context, constraints, focus)
- The perspective-specific angles to assess (below)

**Engineer, assess:**
- Read `.claude/context/tech-stack.md` first for accurate stack context
- Technical feasibility and implementation complexity given the stack
- Technical risks and mitigation strategies
- Dependencies on systems/services
- Which service/layer this touches, and build-vs-extend considerations
- Estimate of engineering effort

**Executive, assess:**
- Business case alignment with stated goals
- ROI potential based on success metrics
- Resource requirements vs. business value
- Strategic alignment with product roadmap

**User Researcher, assess:**
- User needs validation
- Usability concerns and friction points
- Gaps between user goals and proposed solution
- Assumptions about user behavior that need validation

**Product Analyst, assess:**
- Are the success metrics measurable, and are they the right ones?
- Baseline data and how impact will be tracked post-launch
- Leading vs. lagging indicators for this feature
- Whether the stated goals can actually be evaluated once shipped

### 4. Consolidate Feedback

Combine findings into a structured report:

```markdown
# PRD Review: [Feature Name]

## Executive Summary
- Overall assessment: [Strong / Good / Needs Work / Incomplete]
- Key strengths: [2-3 bullet points]
- Critical gaps: [2-3 bullet points]
- Recommendation: [Proceed / Revise / More Research Needed]

---

## Engineer Perspective

### Technical Feasibility
[Assessment of technical viability]

### Implementation Complexity
[High / Medium / Low with rationale]

### Technical Risks
- Risk 1: [Description + mitigation]
- Risk 2: [Description + mitigation]

### Action Items
- [ ] [Specific technical clarification needed]

---

## Executive Perspective

### Business Case
[Alignment with business goals]

### ROI Assessment
[Expected value vs. investment]

### Strategic Fit
[How this aligns with product strategy]

### Action Items
- [ ] [Business metric clarification needed]

---

## User Researcher Perspective

### User Needs Validation
[How well the PRD addresses identified user problems]

### Usability Concerns
[Potential friction points for users]

### Gaps & Questions
[What's missing from user perspective]

### Action Items
- [ ] [User research needed]

---

## Product Analyst Perspective

### Success Metrics
[Are the metrics measurable and the right ones?]

### Measurement Plan
[Baseline, tracking, leading vs. lagging indicators]

### Gaps & Questions
[What can't yet be evaluated post-launch]

### Action Items
- [ ] [Metric or instrumentation clarification needed]

---

## Consolidated Action Items

### Critical (Must Address Before Development)
- [ ] [Critical item 1]

### Important (Address During Development)
- [ ] [Important item 1]

### Nice to Have
- [ ] [Enhancement 1]

---

## Overall Recommendation

[Clear recommendation: Proceed / Revise PRD / Conduct more research]
```

## Notes

- If the PRD is incomplete, note specific missing sections and recommend revision before development
- If agents return conflicting feedback, highlight the conflict and explain the trade-off
- Document any unanswered questions as open risks
