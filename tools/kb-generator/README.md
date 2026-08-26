# KB Article Generator

Generate professional, customer-facing knowledge base articles from PRDs or Jira user stories.

## What It Does

Transforms technical product documentation into polished KB articles that customers can actually use. The generator:
- Extracts key information from PRDs or Jira tickets
- Structures content in a customer-friendly format
- Creates professional PDF documents
- Follows KB best practices automatically

## How to Use

### Via Slash Command (Recommended)

```
/generate-kb-article
```

Claude will:
1. Ask for your source (PRD file or Jira ticket)
2. Extract and structure the content
3. Generate a professional PDF KB article
4. Save to `projects/kb-articles/`

### Direct Python Usage

```python
import sys
sys.path.append('tools/kb-generator')
from generate_kb_pdf import create_kb_article_pdf

title = "Feature Name"

sections = [
    {
        'heading': 'Overview',
        'level': 1,
        'content': [
            'What the feature is and why it matters.',
            'Target users and use cases.'
        ]
    },
    {
        'heading': 'How to Use It',
        'level': 1,
        'content': []
    },
    {
        'heading': 'Step 1: Setup',
        'level': 2,
        'content': [
            '1. First action',
            '2. Second action',
            '3. Third action'
        ]
    }
    # ... more sections
]

create_kb_article_pdf(
    title=title,
    sections=sections,
    output_path='projects/kb-articles/feature-name.pdf',
    author='Product Team'
)
```

## Article Structure

Generated articles include:

1. **Title Page** - Feature name, author, date
2. **Overview** - What it is, why it matters
3. **What You Can Do** - Key capabilities
4. **How to Use It** - Step-by-step setup and usage
5. **Key Features** - Detailed feature breakdown
6. **Common Questions** - FAQ section
7. **Best Practices** - Tips for success
8. **Troubleshooting** - Common issues and solutions
9. **Need Help?** - Support contact info

## Content Guidelines

**Customer-First Writing:**
- Use "you" perspective
- Focus on benefits, not technical details
- Avoid jargon and internal terminology
- Be clear, concise, and actionable

**Structure:**
- Short paragraphs (2-3 sentences)
- Bullet points for lists
- Numbered steps for procedures
- Bold for emphasis on key terms

**Completeness:**
- Cover setup, usage, and troubleshooting
- Answer the most common questions
- Include realistic examples
- Provide clear next steps

## Input Sources

### From PRD Files

Best for new features still in development:

```
/generate-kb-article
> Source: PRD file
> Path: projects/my-feature/prd.md
```

The generator extracts:
- Feature name and overview
- Key functionality
- User benefits
- Use cases

### From Jira Tickets

Best for implemented features:

```
/generate-kb-article
> Source: Jira ticket
> Ticket ID: [ENG_PROJECT]-123
```

The generator extracts:
- Summary and description
- Acceptance criteria
- Comments with context
- Linked issues

## Output Format

**PDF with Professional Formatting:**
- Clean title page
- Consistent headers and spacing
- Readable fonts and colors
- Proper pagination
- Auto-dated

**Saved to:**
```
projects/kb-articles/
└── feature-name.pdf
```

## File Organization

```
tools/kb-generator/
├── generate_kb_pdf.py        # PDF generation utility
└── README.md                  # This file

templates/
└── kb-article-template.md     # Blank template for manual writing

projects/kb-articles/
├── webhook-automation.pdf     # Example KB article
└── webhook-automation-test.py # Example generator script
```

## Customization

### Add Your Company Branding

Edit `generate_kb_pdf.py` to customize:
- Colors (change HexColor values)
- Fonts (change fontName)
- Logo (add to title page)
- Footer text

### Adjust Structure

Modify section order or add/remove sections in the slash command or your generator script.

## Best Practices

**Before Generating:**
- Have clear source material (PRD or detailed Jira ticket)
- Know your target audience
- Identify the 3-5 most common questions

**After Generating:**
- Review for accuracy and completeness
- Add screenshots where helpful
- Test instructions yourself
- Have support team review

**Maintenance:**
- Update when features change
- Add FAQ items from support tickets
- Keep troubleshooting current
- Review quarterly

## Example Output

See `projects/kb-articles/webhook-automation.pdf` for a complete example of:
- Professional formatting
- Customer-friendly language
- Comprehensive coverage
- Actionable troubleshooting

## Dependencies

```bash
pip3 install reportlab
```

Already installed if you completed Phase 1 setup.

## Tips for Great Articles

1. **Write for customers, not engineers** - No technical jargon
2. **Show, don't tell** - Specific steps over vague descriptions
3. **Answer "why" not just "how"** - Explain benefits
4. **Test your instructions** - Follow them yourself first
5. **Update based on feedback** - Support tickets reveal gaps

## Integration with Workflow

**When to Generate:**
- After completing a PRD (draft KB article)
- After implementing a feature (finalize KB article)
- When support asks for documentation
- During beta/launch preparation

**Who Uses It:**
- **PMs**: Create draft articles from PRDs
- **Support**: Document common workflows
- **Customer Success**: Create onboarding guides
- **Product Marketing**: Feature launch materials

## Limitations

- Generated content is a starting point, not final copy
- Requires editing for screenshots and visual elements
- May need support team review for accuracy
- Best suited for feature documentation, not troubleshooting guides

## Troubleshooting

**"ModuleNotFoundError: reportlab"**
```bash
pip3 install reportlab
```

**PDF formatting issues**
- Check that content strings don't have unclosed quotes
- Avoid special characters in headings
- Use proper list formatting (bullets/numbers)

**Content too generic**
- Provide more detailed source material
- Add specific examples and use cases
- Include actual UI text and field names

---

**Created:** January 26, 2026
**Status:** ✅ Phase 2 Skill #2 Complete
**Command:** `/generate-kb-article`
**Output:** Professional PDF KB articles
