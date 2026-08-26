# Update Documentation

Safely update documentation based on manual input with explicit verification before applying changes.

> **Setup required:** Fill in your documentation tool IDs and local paths before using this command.

**Documentation Tool:** [FILL IN: e.g. ClickUp, Notion, Confluence]
**Product Documentation URL:** [FILL IN: link to your main product documentation]
**Workspace/Space ID:** [FILL IN: your workspace or space ID]
**Doc ID:** [FILL IN: your product documentation doc ID]
**Page ID:** [FILL IN: your product documentation page ID]

**Local Documentation Path:** `docs/product documentation/`

**Local File Structure:**
- `00_index.md` - Table of Contents
- `01_product_overview.md` - Product Overview
- `02_user_roles_permissions.md` - User Roles & Permissions
- [FILL IN: add your documentation file structure here, update these files once you set up your product docs]

## Process

### 1. Input Gathering

Ask the user:
- What needs to be updated? (incorrect info, missing content, clarification needed)
- What is the correct information?
- Which section(s) are affected?

### 2. Discovery & Analysis

- Read BOTH the remote documentation AND the relevant local file(s) from `docs/product documentation/`
- Determine which local file(s) correspond to the section being updated
- Locate the specific sections that need changes in both locations
- Identify any related sections that might also need updates
- Note any discrepancies between remote and local versions

### 3. Propose Changes (Show in Response)

Present clearly formatted:

**CURRENT CONTENT:**
```
[Show exact current text with section headers/context]
```

**PROPOSED CHANGES:**
```
[Show new text with changes highlighted]
```

**IMPACT:**
- Sections affected: [list]
- Files to update: remote documentation + local file path (if applicable)
- Related sections that may need review: [list]

### 4. Verification Gate

**STOP and wait for explicit user approval.**

User must respond with:
- "yes" / "approve" / "proceed" → Continue to execution
- "change X" → Revise the proposal
- "cancel" / "no" → Abort without changes

**Do NOT proceed without explicit confirmation.**

### 5. Execution (with safeguards)

Only after approval:

**For Remote Documentation:**
- Get current full page content
- Make changes to ONLY the approved sections
- Use the documentation tool's API to update
- NEVER truncate or remove other sections

**For Local Files:**
- Update the corresponding file(s) in `docs/product documentation/`
- Use Edit tool with specific `old_string` / `new_string`
- Use targeted edits, never rewrite entire files unless explicitly approved
- If the section spans multiple files, update all relevant files

**CRITICAL SAFEGUARDS:**
- Only change what was approved
- Preserve all other content exactly as-is
- No "improvements" beyond approved changes
- Maintain exact formatting and structure

### 6. Confirmation

After execution:
- Report what was changed (brief summary)
- Provide link to updated remote documentation
- Provide local file path (if updated)
- Offer to read back the updated sections for verification

## Safety Checklist

Before execution, verify:
- [ ] User provided explicit approval ("yes"/"approve"/"proceed")
- [ ] Proposed changes shown in command window
- [ ] Both remote AND local file will be updated
- [ ] Only approved sections will be modified
- [ ] All other content will be preserved exactly

## Notes

- Always update BOTH remote documentation and local files
- Keep them synchronized
- If discrepancies exist between remote and local, flag to user
- Default documentation location: [FILL IN: your company] Product Documentation
