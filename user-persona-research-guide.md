# User Persona Research Guide

**Context:** We're using a lean persona approach to understand our actual users (front-line agents, team coordinators, operations managers) vs. just the buyers (business owners/VPs). This doc contains frameworks and considerations that might be helpful as you design the research approach.

---

## Key Insight: Buyer ≠ User

In B2B, we need to distinguish between:

**Buyer Personas** (Sales/GTM focus)
- Business Owners, VPs, Department Directors
- Care about: ROI, cost savings, staff efficiency, customer satisfaction scores

**User Personas** (Product focus) ⭐ **← Our focus**
- Front-Line Agents, Team Coordinators, Operations Managers
- Care about: Daily workflow, ease of use, not looking bad in front of customers, reducing repetitive work

This research should focus on **user personas** since we need to build product they'll actually use daily.

---

## Our ICP (for context)

**Perfect Match:**
- Companies with 3-10 teams or a single mid-sized team
- 60+ active users per account
- Multiple departments collaborating
- Poor/no existing tooling for the workflow
- Manual, spreadsheet-driven process today

**Standard:**
- Teams of 20+ users
- Either a small team wanting automation OR a large team with high volume
- A compatible core system (CRM / ticketing / ERP) to integrate with

**We close but don't actively pursue:**
- Very small teams (under 5 users)
- Highly bespoke enterprise setups under 10 seats

---

## Suggested User Personas to Explore

Based on the ICP, here are the primary user types worth exploring:

### 1. The Front-Line Agent
The person actually handling customer requests all day
- Handles 80% of the daily interaction volume
- Often juggling multiple channels and tools at once
- Frequently newer/rotating staff in many teams
- Entry to mid-level experience

### 2. The Team Coordinator
Sets up workflows, manages content, owns the process strategy
- Configures automations and writes response templates
- Monitors feedback and quality
- Creates campaigns or recurring workflows
- Usually 1 person for small teams, a small team in larger orgs

### 3. The Operations Manager (Hybrid User/Buyer)
Bridges the gap - uses the tool AND influenced the purchase
- Oversees the front-line team and trains new staff
- Monitors performance/KPIs
- Escalation point for complex issues
- Has budget influence for renewal decisions

---

## Lean User Persona Template

Here's a suggested structure that keeps personas actionable and focused:

```markdown
## [Persona Name] - [One-liner description]

**Role & Context**
- Title: [Actual job title]
- Typical day: [Key responsibilities]
- Team structure: [Who they work with]
- Experience level: [Junior/Mid/Senior, tenure]

### A Day in Their Life
[Describe a typical day with pain points highlighted]

### Primary Jobs to Be Done
When using [PRODUCT], they're trying to:
1. [Job 1]
2. [Job 2]
3. [Job 3]

### Pain Points (Current State)
**Workflow Friction:**
- [What slows them down]
- [What's frustrating to do]

**Capability Gaps:**
- [What they can't do today]
- [What they wish worked differently]

**Emotional/Social:**
- [What makes them look bad]
- [What stresses them out]

### Goals & Success Metrics
- Personal win: [What makes their day easier]
- Team win: [What makes them look good to their manager]
- Avoids: [What they're trying to prevent]

### Current Behavior & Workarounds
- Tools they use: [Current stack]
- Workarounds: [How they compensate]
- Power user patterns: [What advanced users do]

### Tech Comfort & Learning Style
- Tech savvy: [High/Medium/Low]
- Training preference: [How they learn new tools]
- Support needs: [When/how they ask for help]

### Decision Influence
- Can they champion new features? [Yes/No/Limited]
- Do they influence renewals? [How]
- Can they get the tool removed? [What would cause this]

### Assumptions to Test ⚠️
- [ ] Assumption 1
- [ ] Assumption 2
- [ ] Assumption 3
```

---

## Example: Front-Line Agent Persona

Here's what a completed persona might look like:

### Sarah the Front-Line Agent
*"I just need to handle requests quickly without making mistakes"*

**Role & Context**
- Title: Support Associate / Front-Line Agent
- Typical day: Intake, resolving requests, follow-ups, coordinating with other teams
- Team: 2-4 other agents on rotation
- Experience: Often entry-level, 6 months - 2 years tenure

**A Day in Their Life**

7am: Morning shift starts, check overnight messages
8-11am: Routine questions, quick resolutions, handoffs
11am-3pm: Rush period - requests piling up, notifications firing, new intake
3-7pm: Late items, scheduling, escalations, issue resolution

Throughout: Switching between the core system, chat, email, phone, and in-person requests

Pain points emerge when:
- A customer is waiting while the phone rings and chat buzzes
- Same question asked 50 times ("How do I reset this?")
- Manager asks why she didn't respond to a message from 2 hours ago
- Can't find previous conversation history when a customer follows up

**Primary Jobs to Be Done**
1. Respond to customers quickly so they don't complain or leave bad reviews
2. Look professional so manager doesn't think she's incompetent
3. Avoid mistakes like duplicate work or wrong information
4. Get through busy periods without getting overwhelmed

**Pain Points**

*Workflow Friction:*
- Juggling 4+ channels simultaneously
- Hunting for request history across systems
- Typing same answers repeatedly
- Can't respond when away from desk

*Capability Gaps:*
- No way to automate repetitive questions
- Can't hand off items between shifts cleanly
- No templates for common scenarios
- Can't see if another team already responded

*Emotional/Social:*
- Anxiety during rush periods: "I'm going to miss something"
- Embarrassment when manager points out missed messages
- Frustration: "This should be easier"
- Guilt: Making customers wait while dealing with system limitations

**Goals & Success Metrics**
- Personal win: Leave shift on time without unresolved issues
- Team win: No complaints about slow responses
- Avoids: Manager criticism, negative reviews mentioning her name

**Current Behavior & Workarounds**
- Tools: Core system (CRM/ticketing), chat, email, phone
- Workarounds:
  - Writes common answers in a Notes app to copy-paste
  - Screenshots conversations to remember context
  - Leaves notes for the next shift about pending issues
  - Ignores certain channels when too busy

**Tech Comfort & Learning Style**
- Tech savvy: Medium (comfortable with apps, not technical)
- Training: Learns by watching others, trial and error. Hates long manuals
- Support: Asks coworkers first, only contacts support if really stuck

**Decision Influence**
- Can champion? Limited - can say "this is annoying" but not drive change
- Influences renewal? Indirectly - will complain if tool makes job harder
- Can get tool removed? Yes - if she and team refuse to use it

**Assumptions to Test ⚠️**
- [ ] Agents want automation vs. personal touch
- [ ] They check multiple channels constantly vs. prefer a single unified view
- [ ] They're frustrated by repetitive questions vs. don't mind
- [ ] They want mobile access vs. only work at desk
- [ ] Training time is a barrier vs. willing to learn if it helps
- [ ] They care about customer satisfaction metrics vs. just want to finish shift

---

## Buyer vs. User: Key Differences

Worth keeping in mind when talking to different stakeholders:

| Aspect | Buyer Persona | User Persona |
|--------|---------------|--------------|
| **Primary concern** | ROI, business outcomes | Daily workflow, ease of use |
| **Success metric** | Cost savings, efficiency gains | "My job is easier" |
| **Evaluation criteria** | Features, pricing, integration | "Can I actually use this?" |
| **Deal breaker** | No core-system integration, too expensive | Too complicated, slows me down |
| **Time horizon** | Annual contract, long-term | Today's shift, this week |
| **Research sources** | Industry reports, demos, references | Coworkers, quick tutorial |

---

## Interview Guide Considerations

Some questions/approaches that tend to work well for user research:

### User Interview Structure (suggested 45 min)

**1. Shadow Their Workflow (~15 min)**
- "Walk me through handling a request from start to finish"
- "Show me your typical morning routine with the tools"
- "What tabs/windows do you have open right now?"

*Look for: Friction points, workarounds, moments of frustration*

**2. Pain Point Deep Dive (~15 min)**
- "Tell me about a time this week when the system got in your way"
- "What part of your job feels like it shouldn't be this hard?"
- "What do you dread doing each day?"
- "What makes a 'bad day' at work?"

**3. Ideal State (~10 min)**
- "If you could change one thing about how you handle requests, what would it be?"
- "What does a 'good tool' look like to you?"
- "When do you feel most productive?"

**4. Product Feedback (~5 min)**
- "What feature do you use most? Why?"
- "What feature do you ignore? Why?"
- "What's missing that would make your job easier?"

**Key principle:** Spend time **observing** them use the tool, not just asking questions. Ask about **actual behavior** ("Tell me about the last time...") rather than hypothetical preferences ("Would you ever...").

---

## Critical Assumptions Worth Testing

These are assumptions that seem common in our internal discussions - worth validating or falsifying:

### For Front-Line Agents:
- **"They want automation to reduce repetitive work"**
  ↳ Or do they fear it makes them replaceable?

- **"They prefer a single unified view for all channels"**
  ↳ Or do they like keeping channels separate?

- **"They need mobile access for flexibility"**
  ↳ Or do they only work at a desk computer?

- **"Fast onboarding is critical (high turnover)"**
  ↳ Or do teams invest in proper training?

- **"They're overwhelmed by message volume"**
  ↳ Or is volume manageable, but context-switching is the issue?

### For Team Coordinators:
- **"They want to control automation responses themselves"**
  ↳ Or do they prefer IT/support to handle configuration?

- **"They measure success by response time/satisfaction"**
  ↳ Or by conversion (revenue, upsells)?

- **"They create campaigns frequently"**
  ↳ Or set-it-and-forget-it?

- **"They need approval workflows for content"**
  ↳ Or full autonomy?

### For Operations Managers:
- **"They monitor team performance via dashboards"**
  ↳ Or via direct observation/spot checks?

- **"They use data to coach team"**
  ↳ Or coaching happens informally?

- **"They're the internal champion keeping team using the tool"**
  ↳ Or is adoption organic?

---

## What Product Team Will Do With Personas

Just so you know how we'll use these:

1. **Roadmap prioritization:** "Which persona does this feature serve?"
2. **Design reviews:** "Would Sarah the Front-Line Agent understand this?"
3. **Onboarding optimization:** "Can we get new agents productive in <30 min?"
4. **Feature adoption:** "Why isn't the Team Coordinator using Campaign Builder?"
5. **Churn prevention:** "Are Operations Managers seeing value to justify renewal?"

The more specific and evidence-based the personas are, the easier it is for us to make product decisions with them.

---

## Questions or Feedback?

This is just a starting point - feel free to adapt, ignore, or completely redesign based on what makes sense for your process. 
, 

**Last updated:** 2026-02-03
