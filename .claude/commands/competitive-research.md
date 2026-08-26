---
description: "Research competitors and synthesize findings into strategic insights"
---

# Competitive Research

Research competitors and synthesize findings into strategic insights relative to our product.

## Workflow

### 1. Gather Context

Before researching, understand our positioning:
- Check for existing PRDs, product docs, or strategy docs in the project
- If not available, ask the user to briefly describe our product, target market, and key differentiators

If no competitors were specified in `$ARGUMENTS`, ask which competitors to research.
If no dimensions were specified, ask which dimensions matter most.

### 2. Select Research Sources

Based on the specified dimensions, use the most relevant sources:

| Dimension | Recommended Sources |
|---|---|
| Features & product capabilities | Product websites, changelogs, G2 feature comparisons, Product Hunt |
| Pricing & packaging | Pricing pages, G2/Capterra, archived pricing via web search |
| Market positioning & messaging | Homepage, About page, LinkedIn, press releases |
| Target market & customer segments | G2 reviewer profiles, case studies, LinkedIn job postings |
| User experience & design | Product websites, G2/Capterra reviews mentioning UX |
| Customer sentiment & satisfaction | G2, Capterra, Reddit, Twitter/X mentions |
| Growth & traction | LinkedIn employee count, job postings, press/funding news |
| Integrations & ecosystem | Product docs, integration pages, marketplace listings |

Tell the user which sources you'll use before starting.

### 3. Research

Launch agents to research each competitor in parallel, focusing on the specified dimensions.

For each competitor, always include:
- Brief company overview (what they do, founding year, size if available)
- Analysis across each requested dimension
- Strengths and weaknesses relative to our product

### 4. Synthesize

Combine findings into:
- **Competitive landscape summary**, how competitors compare across the chosen dimensions
- **Strategic insights**, patterns, gaps, and opportunities spotted across the landscape
- **Positioning recommendations**, how we can differentiate based on findings
- **Whitespace opportunities**, areas no competitor is serving well

### 5. Save Output

Save the full report as a markdown file:

**File path:** `reports/competitive-research/[YYYY-MM]-[topic]-competitive-research.md`

Structure:
```markdown
# Competitive Research: [Topic], [Month Year]

## Competitors Analyzed
[List]

## Competitive Landscape
[Comparison across dimensions, use a table where possible]

## Strategic Insights
[Key patterns and takeaways]

## Positioning Recommendations
[How [COMPANY_NAME] can differentiate]

## Whitespace Opportunities
[Underserved areas across the competitive landscape]

---
**Date:** [Date]
**Dimensions analyzed:** [List]
**Sources used:** [List]
```

Confirm saved location to the user.

### 6. Capture Learnings

After saving the report, prompt for learnings:

```
📚 Learning Capture

Competitive research is complete! Did this reveal anything worth keeping for future positioning work? For example:
- A competitor's move or new capability
- A whitespace opportunity confirmed across the landscape
- A positioning angle that holds up
- A source that proved especially useful (or misleading)

Options:
- Yes, I have insights to capture
- No, skip for now
```

**If the user wants to capture insights:** Use AskUserQuestion to gather what to record, then append to `.claude/knowledge/customer-insights.md` under a "Competitive Insights" section (create it if it doesn't exist):

```markdown
## Competitive Insights

### [Month Year], [Topic]
**Competitors:** [List]

**Key takeaways:**
- [Landscape shift, capability gap, or positioning angle worth remembering]

**Whitespace / opportunities:**
- [Underserved area to revisit]

**Link to full report:** reports/competitive-research/[YYYY-MM]-[topic]-competitive-research.md

---
```

Read the file first, add the entry, write it back, and confirm to the user. **If the user skips:** finish without capturing.
