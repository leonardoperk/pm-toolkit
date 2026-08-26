---
description: "Extract action items, decisions, and follow-ups from meeting notes"
---

# Extract Action Items Command

You are executing the `/extract-action-items` command to analyze meeting notes and extract actionable items, decisions, discussion topics, and follow-up questions in Raycast-compatible format.

## Workflow

### 1. Get Meeting Notes File

Use AskUserQuestion to ask:
- **File path**: Where are the meeting notes?

**Default location:** `meeting-notes/` folder
- Example: `meeting-notes/2026-01-26-product-sync.md`

**Validation:**
- Check file exists using Read tool
- Accept markdown (.md) or text (.txt) files
- If file not found, list available files in `meeting-notes/` folder
- If no file specified, ask for correct path

### 2. Read and Analyze Meeting Notes

**Read the entire file** and understand:
- Meeting context (participants, date, purpose)
- Discussion flow and topics
- Explicit and implicit action items
- Decisions that were made
- Open questions or follow-ups needed

### 3. Extract Action Items

**Identify action items** - statements indicating someone needs to do something:

**Explicit Action Items (easy to spot):**
- "Alex will..."
- "Michael to..."
- "TODO: ..."
- "Action item: ..."
- "Follow up on..."
- "Need to..."
- "Should..."
- "Must..."

**Implicit Action Items (require inference):**
- "We agreed to..." (implies someone does it)
- "Let's..." (implies action)
- "Next steps..." (implies actions)
- Questions that need answering (implies research action)

**For each action item, extract:**
- **Task description**: What needs to be done
- **Owner**: Who is responsible (if mentioned)
- **Context**: Why it needs to be done (if clear)
- **Deadline**: If mentioned (e.g., "by Friday", "before next sprint")

**Owner Detection Patterns:**
- "Alex will update the PRD" → Owner: Alex
- "Michael to review designs" → Owner: Michael
- "Need someone to test" → Owner: Unassigned
- "@username will..." → Owner: username
- "I'll handle..." → Owner: Meeting note taker (if identifiable)

### 4. Extract Decisions

**Identify decisions** - conclusions or choices that were made:

**Decision Indicators:**
- "We decided..."
- "Agreed to..."
- "Will go with..."
- "Final decision..."
- "Chosen approach..."
- "Not doing..."
- "Postponed..."

**For each decision, extract:**
- **What was decided**: Clear statement of the decision
- **Reasoning**: Why this decision was made (if mentioned)
- **Alternatives considered**: What was rejected (if mentioned)

### 5. Extract Discussion Topics

**Identify main topics** that were discussed:

**Topic Indicators:**
- Headings in notes (##, ###)
- "Discussed..."
- "Talked about..."
- Topic changes ("Moving on to...")
- Agenda items

**For each topic, extract:**
- **Topic name**: Brief title
- **Key points**: Main takeaways from the discussion
- **Outcome**: What resulted (decision, action, or open question)

### 6. Extract Follow-up Questions

**Identify open questions** that need answers:

**Question Indicators:**
- Explicit questions: "?", "How do we...", "What about..."
- "Need to clarify..."
- "Unclear on..."
- "To be determined..."
- "Follow up needed on..."

**For each question, extract:**
- **Question**: What needs to be answered
- **Context**: Why it matters
- **Who can answer**: If mentioned

### 7. Generate Raycast-Compatible Output

**Format for Raycast (markdown checklist format):**

```markdown
# Meeting Action Items - [Date/Meeting Name]

## 📋 Action Items

- [ ] [Task description] (@owner) [due date]
- [ ] [Task description] (@owner)
- [ ] [Task description] (Unassigned)

## ✅ Decisions Made

- **[Decision title]**: [What was decided]
  - Reason: [Why]
  - Alternatives: [What was rejected]

- **[Decision title]**: [What was decided]

## 💬 Discussion Topics

- **[Topic 1]**: [Key points and outcome]
- **[Topic 2]**: [Key points and outcome]

## ❓ Follow-up Questions

- [ ] [Question to answer] (@owner if known)
- [ ] [Question to answer]

---

**Meeting:** [Meeting title/purpose]
**Date:** [Date]
**Participants:** [List if mentioned]
**Extracted:** [Current date]
```

### 8. Present Results

Show the extracted content in Raycast format:

```
✅ Meeting Notes Analyzed

📊 Extraction Summary:
   - Action items: [N]
   - Decisions: [N]
   - Discussion topics: [N]
   - Follow-up questions: [N]

📋 Raycast-Compatible Output:
[Display the formatted markdown above]

💡 Next Steps:
   1. Copy the output above
   2. Paste into Raycast to-do list
   3. Update owners/deadlines as needed
   4. Check off items as you complete them

📄 Source: [file path]
```

## Extraction Guidelines

### Action Item Detection Rules

**Must include to be an action item:**
- Clear verb indicating action (update, review, test, send, create, fix, etc.)
- Identifiable task that can be completed
- Not a discussion topic or question alone

**Include:**
- ✅ "Alex will update the PRD with new requirements"
- ✅ "Need to test the webhook integration before launch"
- ✅ "Follow up with customer on feature request"
- ✅ "Review Figma designs by Friday"

**Exclude:**
- ❌ "We discussed the roadmap" (just discussion, no action)
- ❌ "The feature looks good" (just opinion, no action)
- ❌ "Marketing will handle launch" (too vague, no specific task)

### Owner Extraction Rules

**Clear owners:**
- Name explicitly mentioned: "Alex will..." → @Alex
- Handle mentioned: "@michael to review" → @Michael
- First person from identifiable person: "I'll update" → @[note taker]

**Unclear owners:**
- "We need to..." → Unassigned (unless context makes it clear)
- "Someone should..." → Unassigned
- "Team to handle..." → Unassigned (team action, not individual)

**Handle edge cases:**
- Multiple people: "Alex and Michael will..." → Create two action items
- Conditional: "If approved, Alex will..." → Include the condition in task description

### Decision vs Action Item

**Decision = Choice made, no action required**
- "We decided to use Approach A"
- "Agreed to postpone feature X"

**Action Item = Someone must do something**
- "Update PRD to reflect Approach A" (based on decision)
- "Inform stakeholders about postponement" (based on decision)

### Context Preservation

**Include relevant context in task description:**
- "Update PRD" → "Update PRD with new authentication requirements"
- "Review designs" → "Review Figma designs for inbox email view"
- "Test feature" → "Test webhook automation on staging before launch"

**Keep tasks specific enough to be actionable**

## Output Format Examples

### Example 1: Product Sync Meeting

**Input meeting notes:**
```
# Product Sync - Jan 26, 2026

Participants: Alex, Michael, Sarah

## [Module] Feature

Discussed launch timeline. We decided to launch Feb 15 instead of Feb 1
to allow more testing time.

Alex will update the PRD with new timeline and additional test cases.
Michael to review updated PRD by end of week.

Need to confirm with engineering if Feb 15 is feasible.

## [Module] Integration

Reviewed current bugs. Sync failure happening for [email provider] users.
We agreed this is a HIGH priority fix.

Sarah will create bug ticket and assign to eng team.

Question: Do we need to notify affected customers?

## Next Meeting

Next sync: Feb 2, 2pm
```

**Output:**
```markdown
# Meeting Action Items - Product Sync (Jan 26, 2026)

## 📋 Action Items

- [ ] Update PRD with Feb 15 timeline and additional test cases (@Alex) [by end of week]
- [ ] Review updated PRD (@Michael) [by end of week]
- [ ] Confirm Feb 15 launch feasibility with engineering (Unassigned)
- [ ] Create bug ticket for [email provider] sync failure and assign to eng (@Sarah)
- [ ] Determine if we need to notify affected customers about sync issue (Unassigned)

## ✅ Decisions Made

- **Launch Date Change**: Moved [Module] launch from Feb 1 to Feb 15
  - Reason: Allow more testing time

- **[email provider] Sync Priority**: Upgraded [email provider] sync failure to HIGH priority
  - Reason: Affecting customers

## 💬 Discussion Topics

- **[Module] Feature**: Launch timeline adjusted, testing prioritized
- **[Module] Integration**: Current [email provider] sync bug identified and prioritized

## ❓ Follow-up Questions

- [ ] Do we need to notify affected customers about [email provider] sync issue? (Unassigned)

---

**Meeting:** Product Sync
**Date:** Jan 26, 2026
**Participants:** Alex, Michael, Sarah
**Extracted:** [Current date]
```

### Example 2: Sprint Planning Notes

**Input:**
```
Sprint 6 Planning - Jan 26

Team: Alex (PM), Michael (Eng Lead), Sarah (Designer)

Capacity: 25 story points

## Stories to Include

- [ENG_PROJECT]-201: Webhook filtering (8 pts) - agreed to include
- [ENG_PROJECT]-202: Email templates (5 pts) - include
- [ENG_PROJECT]-203: Dashboard redesign (13 pts) - too big, Michael will split

Decided to prioritize webhook features over dashboard work this sprint.

## Blockers

Figma access issue for new contractor. Sarah to request access from IT.

Design review meeting not scheduled yet. Need to find time with stakeholders.

## Questions

- Can we get API access to partner system for testing? Alex to follow up.
- What's the deadline for security review? TBD
```

**Output:**
```markdown
# Meeting Action Items - Sprint 6 Planning (Jan 26, 2026)

## 📋 Action Items

- [ ] Split [ENG_PROJECT]-203 (Dashboard redesign) into smaller stories (@Michael)
- [ ] Request Figma access for new contractor from IT (@Sarah)
- [ ] Schedule design review meeting with stakeholders (Unassigned)
- [ ] Follow up on API access to partner system for testing (@Alex)
- [ ] Confirm deadline for security review (Unassigned)

## ✅ Decisions Made

- **Sprint 6 Scope**: Include [ENG_PROJECT]-201 (Webhook filtering) and [ENG_PROJECT]-202 (Email templates)
  - Total: 13 story points committed

- **Sprint Priority**: Prioritize webhook features over dashboard work
  - Reason: Dashboard story too large for this sprint

## 💬 Discussion Topics

- **Sprint Capacity**: 25 story points available
- **Story Sizing**: [ENG_PROJECT]-203 needs to be split (currently 13 pts)
- **Team Blockers**: Figma access and design review meeting

## ❓ Follow-up Questions

- [ ] Can we get API access to partner system for testing? (@Alex)
- [ ] What's the deadline for security review? (TBD)

---

**Meeting:** Sprint 6 Planning
**Date:** Jan 26, 2026
**Participants:** Alex (PM), Michael (Eng Lead), Sarah (Designer)
**Extracted:** [Current date]
```

## Edge Cases

**Very short notes:**
- Still extract what's available
- If only 1-2 action items, still format properly
- Note: "Brief meeting, limited items extracted"

**Very long notes (multiple pages):**
- Extract all action items and decisions
- Group discussion topics by section if notes have clear structure
- May result in 20+ action items (that's OK)

**Unclear or messy notes:**
- Extract what's clearly identifiable
- Use "Unassigned" for unclear owners
- Add note: "Some items may need clarification"

**No action items found:**
- Still extract decisions and discussion topics
- Inform user: "No explicit action items found in notes"
- Suggest reviewing for implicit actions

**Mixed languages or informal notes:**
- Handle informal language ("gonna", "gotta", etc.)
- Extract actions regardless of formality
- Standardize format in output

## Best Practices

**Before extraction:**
- Read entire notes to understand context
- Identify meeting purpose and participants
- Note any explicit agenda or structure

**During extraction:**
- Prefer specific over vague descriptions
- Include deadlines if mentioned
- Keep owner names consistent (use same format throughout)
- Group related actions if appropriate

**After extraction:**
- Count extracted items for summary
- Verify output is valid markdown
- Check that checklist format works for Raycast
- Ensure all sections have at least "None identified" if empty

## Important Notes

- **Raycast format** - Use markdown checklist syntax: `- [ ] Task`
- **Owners** - Use @username format for easy identification
- **Context** - Include enough detail to make task actionable
- **Source** - Always reference original meeting notes file
- **No Jira creation** - This tool only extracts and formats, doesn't create tickets
- **Manual transfer** - User copies output and pastes into Raycast

---

**This command transforms messy meeting notes into actionable, organized task lists ready for your personal productivity system.**
