# Slash Commands Cheat Sheet

**PM Toolkit - Custom Claude Code Commands**

Quick reference guide for all available slash commands in this project.

---

## 📋 Table of Contents

- [Development & Project Setup](#development--project-setup)
- [Requirements & Planning](#requirements--planning)
- [Sprint & Jira Management](#sprint--jira-management)
- [Documentation](#documentation)
- [Customer Support & Analysis](#customer-support--analysis)
- [Research](#research)

---

## Development & Project Setup

### `/build`

**Purpose:** Take a project from spec to working app, scaffold if new, plan, build, and iterate

**Workflow:**
```
Scaffold (new projects only, Next.js default)
                ↓
    Check REQUIREMENTS.md (or /requirements first)
                ↓
    Plan mode → plan → user approval
                ↓
    Build → verify (dev server)
                ↓
    Iterate: screenshot feedback loop until satisfied
                ↓
    Offer /deploy when ready to ship
```

**When to use:** Building a new tool or feature, from scaffolding through refinement. Shipping stays separate (`/deploy`).

---

### `/deploy`

**Purpose:** Deploy project to GitHub and Vercel

**Workflow:**
1. Check git status
2. Create/push to GitHub repository
3. Deploy to Vercel
4. Provide deployment URL

**When to use:** Ready to deploy a project to production

---

## Requirements & Planning

### `/requirements`

**Purpose:** Gather project requirements through structured interview

**Workflow:**
```
Ask about project → Gather context → Identify stakeholders
                                            ↓
                            Ask clarifying questions
                                            ↓
                            Document requirements
                                            ↓
                    Create requirements document with:
                    - Goals & objectives
                    - User stories
                    - Constraints
                    - Success metrics
```

**When to use:** Starting a new project from scratch, prototypes, quick requirements gathering

---

### `/create-prd`

**Purpose:** Create a PRD through conversational interview using the Hybrid template

**Workflow:**
```
User describes feature naturally
                ↓
    Active listening & information extraction
    (Extract: description, problem, why, success, audience)
                ↓
    Ask targeted follow-up questions
    (Fill gaps in the Core Questions)
                ↓
    Deep dive into Solution Alignment
    (Features, flows, business logic)
                ↓
    Cover Execution
    (How: experiment plan, When: milestones)
                ↓
    Validate completeness
                ↓
    Generate PRD using the Hybrid template
                ↓
    User reviews and approves
                ↓
    Create Jira Epic in [PRODUCT_PROJECT] project
    (Status: To Do, Team: Product)
```

**Key features:**
- ✅ Conversational (not rigid Q&A)
- ✅ Uses the Hybrid PRD Template
- ✅ Automatically creates Jira Epic
- ✅ Intelligent gap identification
- ✅ Handles uncertainty gracefully (TBD sections)

**When to use:** Planning new product features, features needing stakeholder buy-in, formal PRD requirements

**Output:**
- Complete PRD markdown file with all Hybrid template sections
- Jira Epic in [PRODUCT_PROJECT] project (Team: Product, Status: To Do)
- Linked PRD reference in Epic description

---

### `/review-prd`

**Purpose:** Multi-agent comprehensive PRD review

**Workflow:**
1. Read PRD document
2. Ask 3 focused clarifying questions
3. Launch 3 sub-agents in parallel via `subagent_type`:
   - `engineer`, technical feasibility & complexity
   - `executive`, business case & ROI
   - `user-researcher`, user needs & usability
4. Consolidate feedback
5. Provide structured recommendations

**When to use:** Before finalizing a PRD, need thorough review from multiple perspectives

---

## Sprint & Jira Management

### `/generate-user-stories`

**Purpose:** Generate Jira user stories from PRD sections

**Workflow:**
```
Read PRD (jira-standards.md for conventions)
                    ↓
    Derive ALL stories in one coherent pass
    (one context, no per-feature split)
                    ↓
    Consistency check (numbering, dedup, dependencies)
                    ↓
        Present to user for approval
                    ↓
        Create approved stories in Jira
```

**Key features:**
- ✅ Single coherent pass (consistent naming, no duplicate stories)
- ✅ Roles & modules from jira-standards.md
- ✅ Automatic priority suggestions
- ✅ Consistent quality across stories

**When to use:** Converting PRD into actionable Jira tickets

**Output format:**
- [PRODUCT]-compliant user stories
- User statement (As a [Role], I want...)
- Detailed acceptance criteria
- Priority suggestions with reasoning
- Technical notes and dependencies

---

### `/forecast-sprint`

**Purpose:** Monte Carlo sprint completion forecast using historical throughput

**Workflow:**
```
Load historical data → Calculate velocity statistics
                                  ↓
                    Run Monte Carlo simulation
                    (10,000 iterations)
                                  ↓
                    Generate probability distribution
                                  ↓
                Confidence levels: 50%, 70%, 85%, 95%
                                  ↓
                    Create visual chart
```

**When to use:** Sprint planning, answering "When will this be done?"

**Key outputs:**
- Probability distribution chart
- Confidence intervals
- Recommended sprint commitment

---

### `/forecast-epic`

**Purpose:** Epic completion forecast based on historical epic velocity and story count analysis

**Workflow:**
1. Analyze historical epic data
2. Calculate average story completion rate
3. Count stories in current epic
4. Run Monte Carlo simulation
5. Generate completion date forecast with confidence intervals

**When to use:** Long-term planning, epic timeline estimation

---

## Documentation

### `/update-docs`

**Purpose:** Safely update documentation with verification gate

**Workflow:**
```
User provides: what to update → Read ClickUp + local files
                                        ↓
                        Propose changes (BEFORE/AFTER)
                                        ↓
                            🛑 VERIFICATION GATE
                            User must approve
                                        ↓
                    Update BOTH ClickUp AND local files
                    (only approved sections)
                                        ↓
                        Confirmation with links
```

**Key safety features:**
- ✅ Explicit approval required
- ✅ Shows exact changes before applying
- ✅ Updates both ClickUp and local files
- ✅ Never overwrites entire documents
- ✅ Targeted edits only

**When to use:** Updating product documentation based on new information

**Files updated:**
- Local: `docs/product documentation/*.md`
- ClickUp: https://app.clickup.com/9002000435/v/dc/8c8z81k-19355

---

### `/generate-kb-article`

**Purpose:** Generate customer-facing KB article from PRD or Jira story

**Workflow:**
1. Read PRD or Jira ticket
2. Extract user-facing features
3. Generate KB article with:
   - Overview
   - How to use
   - Step-by-step instructions
   - Screenshots placeholders
   - Troubleshooting
   - FAQs

**When to use:** Feature launch, need customer documentation

---

### `/generate-release-notes`

**Purpose:** Generate customer-facing release notes from sprint work

**Workflow:**
1. Analyze completed Jira tickets from sprint
2. Group by feature type (New, Improved, Fixed)
3. Write customer-friendly descriptions
4. Format as release notes

**When to use:** End of sprint, preparing release announcement

---

### `/sprint-documentation-review`

**Purpose:** Analyze completed sprint and propose ClickUp product documentation updates

**Workflow (with parallel agents):**
```
Fetch completed sprint stories
                ↓
    Launch 2 parallel discovery agents:

Agent 1: Ticket Analysis       Agent 2: Doc Structure Analysis
        ↓                                  ↓
  Identify doc needs               Read ClickUp docs
  Assess customer impact           Map all sections
  Categorize by update type        Find insertion points

                ↓
        Synthesize and map stories to sections
                ↓
        Draft proposed content updates
                ↓
        Create [PRODUCT_PROJECT] story with proposals
                ↓
        🛑 Wait for user approval
                ↓
        Update ClickUp documentation
```

**Key features:**
- ✅ Parallel discovery (2 agents)
- ✅ Drafts actual content to add/update
- ✅ Maps to existing doc structure
- ✅ 2x faster analysis
- ✅ More comprehensive review

**When to use:** End of sprint, ensuring docs stay current

**Safety features:**
- Requires explicit approval before updating
- Shows exact proposed changes
- Updates only approved sections

---

## Customer Support & Analysis

### `/cs-monthly-review`

**Purpose:** Monthly CS ticket analysis - patterns, bugs, feature requests, pain points

**Workflow (with parallel agents):**
```
Fetch CS tickets from last 30 days
                ↓
    Launch 4 parallel analysis agents:

Agent 1: Bug Patterns    Agent 2: Feature Requests
        ↓                        ↓
  Recurring bugs          Request clustering
  Technical issues        Customer segments

Agent 3: Pain Points     Agent 4: Product Gaps
        ↓                        ↓
  User confusion          Missing features
  Workflow struggles      Integration needs

                ↓
        Synthesize results
                ↓
        Create [PRODUCT_PROJECT] story with findings
```

**Key features:**
- ✅ Parallel analysis (4 agents simultaneously)
- ✅ Automatically creates [PRODUCT_PROJECT] story
- ✅ 3-4x faster than manual analysis
- ✅ Comprehensive pattern detection

**When to use:** Monthly CS review, identifying product improvements

**Output includes:**
- Top pain points by frequency
- Feature request themes with customer segments
- Bug patterns with affected users
- Product gaps with competitive context
- Prioritized recommendations

---

### `/extract-action-items`

**Purpose:** Extract action items, decisions, and follow-ups from meeting notes

**Workflow:**
1. Read meeting notes
2. Identify:
   - Action items (with owners)
   - Decisions made
   - Open questions
   - Follow-up needed
3. Format for Raycast/task manager
4. Create follow-up timeline

**When to use:** After meetings, need to track action items

---

## Research

### `/competitive-research`

**Purpose:** Parallel competitor research and synthesis

**Workflow:**
1. User provides competitors list
2. Launch parallel research agents:
   - Agent 1: Competitor A
   - Agent 2: Competitor B
   - Agent 3: Competitor C
   - (up to 5 competitors)
3. Each agent researches:
   - Features
   - Pricing
   - Target market
   - Strengths/weaknesses
4. Synthesize findings
5. Create comparison matrix

**When to use:** Market research, competitive analysis, feature planning

**Output includes:**
- Feature comparison table
- Pricing comparison
- Strengths/weaknesses matrix
- Gaps and opportunities

---

## Quick Reference 

| Command                        | Category      | Time      | Approval Required  |
| ------------------------------ | ------------- | --------- | ------------------ |
| `/build`                       | Development   | Varies    | Yes (plan approval) |
| `/deploy`                      | Development   | 5 min     | No                 |
| `/requirements`                | Planning      | 15-30 min | No                 |
| `/create-prd`                  | Planning      | 20-40 min | Yes (before Epic)  |
| `/review-prd`                  | Planning      | 20-40 min | No                 |
| `/generate-user-stories`       | Sprint        | 10-20 min | No                 |
| `/forecast-sprint`             | Sprint        | 5 min     | No                 |
| `/forecast-epic`               | Sprint        | 5 min     | No                 |
| `/update-docs`                 | Documentation | 10-20 min | **Yes**            |
| `/generate-kb-article`         | Documentation | 15 min    | No                 |
| `/generate-release-notes`      | Documentation | 10 min    | No                 |
| `/sprint-documentation-review` | Documentation | 10-15 min | Yes                |
| `/cs-monthly-review`           | Analysis      | 10-15 min | No                 |
| `/extract-action-items`        | Analysis      | 5 min     | No                 |
| `/competitive-research`        | Research      | 30-60 min | No                 |

---

## Tips

**Commands with Verification Gates:**
- `/update-docs` - ALWAYS requires approval before updating
- `/build` - Requires plan approval before implementation
- `/sprint-documentation-review` - Requires approval before updates

**Commands that Launch Agents:**
- `/review-prd` - Multiple review agents in parallel
- `/competitive-research` - Parallel competitor research agents
- `/build` - Enters plan mode before implementation
- `/cs-monthly-review` - 4 parallel analysis agents (bug patterns, feature requests, pain points, product gaps)
- `/sprint-documentation-review` - 2 parallel discovery agents (ticket analysis, doc structure)

**Commands for Weekly/Monthly Routines:**
- **Weekly:** `/generate-release-notes`, `/sprint-documentation-review`
- **Monthly:** `/cs-monthly-review`

**Commands for Project Kickoff:**
1. `/requirements` - Gather requirements
2. `/review-prd` - Review PRD
3. `/generate-user-stories` - Create Jira tickets
4. `/forecast-epic` - Estimate timeline
5. `/build` - Scaffold and build (if needed)

---

## Command Syntax

All commands start with `/` followed by the command name:

```bash
/command-name
```

Some commands may accept arguments:

```bash
/forecast-sprint --tickets [PRODUCT_PROJECT]-1,[PRODUCT_PROJECT]-2,[PRODUCT_PROJECT]-3
```

---

## Skills & Scripts (not slash commands)

These are **not** in the `/` menu, they run automatically (doc generation) or as Python scripts. Listed here so they're not forgotten.

### Document generation (auto-triggered)

Just ask naturally, Claude writes the file using the installed libraries. No command needed.

| Ask for… | Produces | Library |
| --- | --- | --- |
| "Create an Excel dashboard for Sprint X" | `.xlsx` | openpyxl |
| "Generate a PDF KB article about …" | `.pdf` | reportlab |
| "Create a Word doc for the … PRD" | `.docx` | python-docx |
| "Make slides from this markdown" (`/pptx` skill) | `.pptx` |, |

> Excel formulas only recalc when opened in Excel/Sheets (no LibreOffice installed). Ask for hard-coded values if you need them pre-calculated.

### RICE Prioritizer

Score and rank features by RICE (Reach × Impact × Confidence / Effort).

```bash
# Generate a sample CSV to start from
python3 .claude/skills/product-manager-toolkit/scripts/rice_prioritizer.py sample

# Run on your features
python3 .claude/skills/product-manager-toolkit/scripts/rice_prioritizer.py features.csv --capacity 15
```

CSV columns: `name,reach,impact,confidence,effort`
- **impact:** minimal · low · medium · high · massive
- **confidence:** low · medium · high
- **effort:** xs · s · m · l · xl (= 0.5, 1, 3, 6, 12 person-months)

Output: ranked features with scores, quick-wins vs big-bets, suggested quarterly roadmap by capacity.

### Customer Interview Analyzer

Extract pain points, feature requests, themes, sentiment, and quotable lines from a transcript.

```bash
python3 .claude/skills/product-manager-toolkit/scripts/customer_interview_analyzer.py transcript.txt
```

Output: sentiment score, pain points (HIGH/MED/LOW), feature requests, recurring themes, quotes for PRDs, metrics & competitor mentions. Run across several interviews to surface patterns.

> Or just ask Claude to run either script for you, no need to touch the command line.

---

## Frameworks Library (manual reference)

Strategy & prioritization frameworks in `templates/frameworks/`. Not auto-loaded by any command, reach for them (or ask Claude to apply one) at the moment noted.

| Framework | What it does | Reach for it when… |
| --- | --- | --- |
| **Assumption Mapping Matrix** (`assumption-mapping-matrix.md`) | Ranks assumptions by importance × evidence → test first / build / observe / ignore | Before committing to a risky bet, decide what actually needs validating first |
| **Rumelt Strategy Kernel** (`rumelt-strategy-kernel.md`) | Diagnosis → guiding policy → coherent action; spots "bad strategy" | A strategy or plan feels like fluff / a wish list, not a real plan |
| **Gibson-Biddle DHM** (`gibson-biddle-dhm.md`) | Pressure-tests strategy: Delightful, Hard-to-copy, Margin-enhancing? | Strategy / positioning calls, is this defensible and worth doing? |
| **Impact Estimation** (`impact-estimation-framework.md`) | Sizes feature impact: Users × Action rate × Lift × Value | Prioritizing features or forecasting the value of a bet |
| **SWOT Analysis** (`swot-analysis.md`) | Strengths / Weaknesses / Opportunities / Threats grid | Competitive or market analysis, or framing a strategic position |

---

## Need Help?

- View command details: Read `.claude/commands/<command-name>.md`
- Suggest new command: Describe the workflow you need automated
- Report issues: Note what didn't work as expected

---

**Last Updated:** 2026-02-02
