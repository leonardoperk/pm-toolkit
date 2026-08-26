# PRD Template & Best Practices

This file documents [PRODUCT]'s PRD standards based on the Hybrid template, including key sections, writing guidelines, and learnings.

## Template Overview

[PRODUCT] uses the **Hybrid PRD Template** as the standard format for product requirement documents.

Full template available at: `templates/prds/Hybrid-PRD-Template.md`

## Core Structure

The Hybrid template has three parts: Core Questions, Solution Alignment, and Execution.

### Part 1: Core Questions

- **Description:** What is it? One-paragraph summary.
- **Problem:** What problem is this solving? 1-2 sentences, standalone communicable.
- **Why:** How do we know this is a real problem and worth solving? Evidence: research, data, feedback, competitive pressure.
- **Success:** How do we know if we've solved it? Measurable metrics and qualitative criteria.
- **Audience:** Who are we building for? Users, personas, segments.
- **What:** Roughly, what does this look like in the product?
- **Non-Goals:** What are we explicitly not doing, and why? Keeps boundaries clear.

### Part 2: Solution Alignment

#### Key Features
- List the features that shape the solution, ideally in priority order
- Draw the perimeter of the solution space so the team can focus on filling it in
- Challenge the size - can a smaller component ship independently?

#### Key Flows
- Show the end-to-end experience: prose, flow diagrams, screenshots, or design explorations
- Collaborate with design and engineering; expect this to sharpen over time

#### Key Logic
- Rules that guide design and development
- Cover common scenarios and edge cases
- Include non-functional requirements (performance, security, scalability)

### Part 3: Execution

- **How:** The experiment plan - beta strategy, rollout approach, validation plan
- **When:** Ship date and key milestones

## PRD Writing Principles

### 1. Problem-First Thinking
Start with the problem, not the solution. Evidence should drive urgency.

**Good:** "Support agents spend 40% of their time answering the same 10 questions repeatedly. Based on ticket analysis across 5 accounts, 'How do I reset my password?' is asked 50+ times per day. Agents report this as their #1 frustration in daily standups."

**Bad:** "We should add a chatbot feature to automate responses."

### 2. Clear Boundaries
Non-goals are as important as goals. Explicit scope prevents scope creep.

**Good:**
```
Goals:
1. Reduce repetitive questions for front-line agents by 50%

Non-goals:
1. Handling complex account changes (requires human judgment)
2. Integration with third-party billing systems (future consideration)
```

### 3. Right Level of Detail
Squint test: "Can someone squint and see the same shape?"

Too vague: "Improve automation"
Too detailed: "Button should be 44px with #3B82F6 background"
Just right: "Trigger builder with visual flow showing events → conditions → actions"

### 4. Evidence-Based Urgency
Answer "Why now?" with real data, not assumptions.

**Good:** "3 customers (representing $45K ARR) specifically requested this in Q4. 2 are evaluating competitors who have this feature."

**Bad:** "This seems important and customers probably want it."

### 5. Collaborative Iteration
PRDs change over time - that's expected. Document changes and notify stakeholders.

## Persona Alignment

When writing PRDs, explicitly identify which persona(s) the feature serves:

- Front-Line Agent
- Team Coordinator
- Operations Manager

Reference: `PRODUCT_CONTEXT.md`

## Common PRD Patterns

### New Feature PRD
Full template with all sections. Focus on Problem & Opportunity and Goals.

### Enhancement PRD
Can be lighter - focus on what's changing and why. Reference original PRD.

### Experiment PRD
Emphasize hypothesis, success metrics, and learning goals in Goals section.

## Learnings & Best Practices

### What Works Well
*[Capture learnings from successful PRDs]*

**Example entries to add here:**
- PRDs that led to smooth launches
- Approaches that prevented scope creep
- Formats that worked well for specific feature types
- Collaboration patterns that improved quality

### Common Pitfalls
*[Document mistakes to avoid]*

**Example entries to add here:**
- PRDs that were too vague and caused rework
- Missing edge cases that caused bugs
- Assumptions that proved wrong
- Scope that was too large

### Templates for Specific Feature Types
*[Build library of patterns for common feature categories]*

**Example categories:**
- Integration features
- Automation features
- UI/UX improvements
- API features

## Resources

- Full template: `templates/prds/Hybrid-PRD-Template.md`
- Product context: `PRODUCT_CONTEXT.md`

## Slash Commands

- `/create-prd` - Interactive PRD creation using this template
- `/review-prd` - Review PRD for completeness and clarity

---

**Last Updated:** 2026-02-10
**Maintainer:** Product Manager

## Notes for Future Updates

After each PRD is completed, consider capturing:
- What worked well in the process?
- What was unclear or caused confusion?
- What edge cases emerged during implementation?
- What would you do differently next time?

Use `/create-prd` to prompt for learnings capture after completion.
