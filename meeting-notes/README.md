# Meeting Notes

This folder contains meeting notes for extraction and analysis.

## Usage

1. Save your meeting notes here as markdown (.md) or text (.txt) files
2. Use recommended naming: `YYYY-MM-DD-meeting-name.md`
3. Run `/extract-action-items` to analyze notes

## File Naming Convention

**Recommended format:**
```
2026-01-26-product-sync.md
2026-01-27-sprint-planning.md
2026-01-30-customer-interview.md
```

**Benefits:**
- Easy to find by date
- Chronological sorting
- Clear purpose from filename

## Meeting Note Template

See `meeting-template.md` for a structured template that works well with action item extraction.

## What Gets Extracted

When you run `/extract-action-items`, the system extracts:

- **Action Items**: Tasks that need to be done (with owners and deadlines)
- **Decisions**: Choices that were made during the meeting
- **Discussion Topics**: Main subjects that were covered
- **Follow-up Questions**: Open questions that need answers

Output is formatted for Raycast to-do list (markdown checklist format).

## Tips for Better Extraction

**Make action items explicit:**
- ✅ "Alex will update the PRD by Friday"
- ✅ "Michael to review designs"
- ✅ "TODO: Test webhook integration"

**Avoid vague statements:**
- ❌ "We should do something about this"
- ❌ "Team will handle it"
- ❌ "Look into it later"

**Include context:**
- ✅ "Update PRD with new authentication requirements"
- ❌ "Update PRD"

**Name owners clearly:**
- ✅ "Alex will...", "@Michael to...", "Sarah needs to..."
- ❌ "Someone should...", "We need to..."

## Archive

Completed meeting notes can be moved to `meeting-notes/archive/` to keep this folder clean.
