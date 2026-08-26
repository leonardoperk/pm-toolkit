# KB Article Generator

**Status:** Phase 2 Skill #2 Complete
**Command:** `/generate-kb-article`
**Output Type:** PDF documents
**Primary Use:** Generate customer-facing knowledge base articles from technical documentation

## Description

Knowledge base article generator that converts technical product requirements documents (PRDs) or Jira user stories into professionally formatted PDF documentation suitable for end-user consumption.

## Invocation

**Slash Command:**
```
/generate-kb-article
```

**Workflow Steps:**
1. System prompts for source type: PRD file or Jira ticket
2. System prompts for source location: file path or ticket ID
3. System extracts content from source
4. System generates structured KB article content
5. System creates PDF with professional formatting
6. System saves output to `projects/kb-articles/[feature-name].pdf`

## Output Specification

**File Format:** PDF (via reportlab)
**Output Location:** `projects/kb-articles/`
**Naming Convention:** `[feature-name].pdf`

**Output Metadata:**
- Page count: typically 4-8 pages
- Sections: 8 standard sections
- Title page included with author and date
- Auto-generated table structure

## Input Sources

### PRD Files
- **Format:** Markdown (.md)
- **Use Case:** Generate KB articles for features in development
- **Extraction:** Feature name, problem statement, solution overview, key functionality, user benefits
- **Location:** Any accessible file path

### Jira Tickets
- **Format:** Jira issue (Story, Bug, Task)
- **Use Case:** Document implemented features
- **Extraction:** Summary, description, acceptance criteria, comments, linked issues
- **Access Method:** Atlassian MCP via ticket ID (e.g., [ENG_PROJECT]-123)

## Content Structure

### Article Sections (Standard)
1. **Overview** - Feature definition and value proposition
2. **What You Can Do** - Capability enumeration
3. **How to Use It** - Step-by-step procedural instructions
4. **Key Features** - Detailed feature descriptions with benefit statements
5. **Common Questions** - FAQ format Q&A
6. **Best Practices** - Recommended usage patterns
7. **Troubleshooting** - Problem-solution pairs
8. **Need Help?** - Support contact information

### Content Style Rules
- Perspective: Second-person ("you")
- Focus: User benefits over technical implementation
- Tone: Customer-facing, non-technical
- Jargon: Avoided or explained
- Paragraph length: 2-3 sentences maximum
- Lists: Bullets for items, numbers for sequential steps
- Emphasis: Bold for key terms

## PDF Formatting

### Visual Specifications
- Page size: Letter (8.5" × 11")
- Margins: 72pt (1 inch) all sides
- Title font: Helvetica-Bold, 24pt, color #2C3E50
- Heading 1: Helvetica-Bold, 18pt, color #2980B9
- Heading 2: Helvetica-Bold, 14pt, color #2980B9
- Body text: Helvetica, 11pt, color #2C3E50, 16pt leading
- Title page: Includes feature name, author, last updated date

## Technical Implementation

### Dependencies
- **Python:** Version 3.x required
- **Library:** reportlab (PDF generation)
- **MCP Integration:** Atlassian MCP (for Jira access)
- **Permissions:** Write access to `projects/kb-articles/` directory

### Python API

**Function:** `create_kb_article_pdf()`

**Import Path:**
```python
sys.path.append('tools/kb-generator')
from generate_kb_pdf import create_kb_article_pdf
```

**Function Signature:**
```python
create_kb_article_pdf(
    title: str,
    sections: list[dict],
    output_path: str,
    author: str = "Product Team"
) -> str
```

**Parameters:**
- `title`: Article title string
- `sections`: List of section dictionaries (see structure below)
- `output_path`: Absolute path for PDF output
- `author`: Optional author name (default: "Product Team")

**Returns:** String path to generated PDF file

### Section Structure

**Dictionary Schema:**
```python
{
    'heading': str,          # Section heading text
    'level': int,            # 1 for H1, 2 for H2
    'content': list[str]     # List of content strings
}
```

**Content String Formats:**
- Plain paragraph: `"Regular text content"`
- Bullet point: `"• Bullet text"` or `"- Bullet text"`
- Numbered item: `"1. First item"`, `"2. Second item"`
- Bold text: `"**Bold text**"` (converted to bold in PDF)

**Example:**
```python
sections = [
    {
        'heading': 'Overview',
        'level': 1,
        'content': [
            'Feature description paragraph.',
            'Benefit statement paragraph.'
        ]
    },
    {
        'heading': 'Step 1: Setup',
        'level': 2,
        'content': [
            '1. Navigate to Settings',
            '2. Click Configure',
            '3. Save changes'
        ]
    }
]
```

## File System Structure

```
pm-toolkit/
├── .claude/commands/
│   └── generate-kb-article.md          # Slash command workflow definition
├── tools/kb-generator/
│   ├── generate_kb_pdf.py              # Python PDF generation utility
│   └── README.md                       # Technical documentation
├── templates/
│   └── kb-article-template.md          # Manual authoring template
└── projects/kb-articles/
    ├── [feature-name].pdf              # Generated KB article outputs
    └── [feature-name]-test.py          # Optional generator scripts
```

## Use Case Categories

### Pre-Launch Documentation
- **Scenario:** Feature in development, PRD exists
- **Source:** PRD markdown file
- **Timing:** During or after PRD completion
- **Purpose:** Draft documentation before feature release
- **Command:** `/generate-kb-article` → Select "PRD file" → Provide file path

### Post-Implementation Documentation
- **Scenario:** Feature implemented and deployed
- **Source:** Jira user story or task
- **Timing:** After feature completion
- **Purpose:** Final documentation based on actual implementation
- **Command:** `/generate-kb-article` → Select "Jira ticket" → Provide ticket ID

### Support Documentation
- **Article Types:** Feature setup guides, integration instructions, workflow tutorials, configuration references
- **Source:** Either PRD or Jira
- **Purpose:** Create support knowledge base
- **Users:** Support team, CSMs

### Customer Onboarding
- **Article Types:** Getting started guides, feature overviews, best practice guides
- **Source:** PRD with customer-focused content
- **Purpose:** Onboarding materials for new customers
- **Users:** Customer success, product marketing

## Direct Python Usage

### Script Invocation

**Standalone Python script:**
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
            'Feature description and value proposition.',
            'Target user personas and use cases.'
        ]
    },
    {
        'heading': 'How to Use It',
        'level': 1,
        'content': []
    },
    {
        'heading': 'Step 1: Initial Setup',
        'level': 2,
        'content': [
            '1. Navigate to Settings menu',
            '2. Select Feature Configuration',
            '3. Click Enable Feature'
        ]
    }
]

output_path = create_kb_article_pdf(
    title=title,
    sections=sections,
    output_path='projects/kb-articles/feature-name.pdf',
    author='Company Product Team'
)

print(f"PDF generated: {output_path}")
```

### Customization Options

**Branding customization in `generate_kb_pdf.py`:**
- **Colors:** Modify `HexColor()` values in custom style definitions
- **Fonts:** Change `fontName` properties (e.g., 'Helvetica-Bold')
- **Logo:** Add image to title page in document building section
- **Footer:** Edit metadata paragraph content

**File locations:**
- Style definitions: Lines 45-93 in `generate_kb_pdf.py`
- Title page generation: Lines 97-113
- Color values: `#2C3E50` (dark blue-gray), `#2980B9` (blue headers)

### Manual Template Usage

**Workflow for manual authoring:**
1. Copy template: `cp templates/kb-article-template.md projects/kb-articles/my-article.md`
2. Fill out all sections with content
3. Invoke `/generate-kb-article` or call Python function directly
4. System converts markdown structure to PDF sections

## Best Practices

### Source Material Quality
- Provide detailed PRDs with clear feature descriptions
- Ensure Jira tickets have comprehensive acceptance criteria
- Include user benefit statements in source content
- Document edge cases and error handling

### Content Review Process
1. Generate initial PDF from source
2. Review for technical accuracy
3. Add screenshots where appropriate
4. Have support team validate instructions
5. Test all procedural steps before publishing

### Maintenance
- Update articles when features change
- Add FAQ items from support ticket patterns
- Refresh troubleshooting based on customer issues
- Regenerate PDFs quarterly or after major updates

## Workflow Phases

### Phase 1: Draft During Development
1. Author PRD for new feature in `projects/[feature-name]/prd.md`
2. Execute `/generate-kb-article` with PRD as source
3. Review generated structure and content
4. Iterate and refine as feature specification evolves
5. Result: Draft KB article ready for launch

### Phase 2: Finalize After Implementation
1. Complete feature implementation in Jira
2. Execute `/generate-kb-article` with Jira ticket as source
3. Add screenshots of production UI
4. Conduct support team review for accuracy
5. Publish final PDF to knowledge base
6. Result: Production-ready customer documentation

### Phase 3: Maintenance
1. Monitor support tickets for recurring questions
2. Extract new FAQ items
3. Update troubleshooting section with new solutions
4. Regenerate PDF on quarterly schedule or after feature updates
5. Result: Current, accurate documentation

## User Roles and Applications

### Product Managers
- **Task:** Create draft KB articles from PRDs
- **Timing:** During feature specification phase
- **Source:** PRD markdown files

### Support Teams
- **Task:** Document common workflows and procedures
- **Timing:** After observing customer usage patterns
- **Source:** Combination of PRD and Jira implementation

### Customer Success Managers
- **Task:** Create onboarding guides and training materials
- **Timing:** Pre-launch or during customer ramp-up
- **Source:** PRD with customer-focused content

### Product Marketing
- **Task:** Generate feature launch documentation
- **Timing:** Pre-launch preparation
- **Source:** Marketing-focused PRD or finalized Jira stories

## Reference Implementation

**Example file:** `projects/kb-articles/webhook-automation.pdf`

**Specifications:**
- Pages: 6
- Main sections: 8
- Content blocks: 70
- Features covered: Webhook automation feature with setup, usage, troubleshooting

**Content structure:**
- Overview and value proposition
- Capability enumeration (What You Can Do)
- Step-by-step setup (4 steps)
- Feature details (3 key features with benefits)
- FAQ (4 common questions)
- Best practices (5 recommendations)
- Troubleshooting (3 problem-solution pairs)
- Support contact information

## Limitations and Constraints

### Technical Limitations
- PDF output format requires regeneration for edits
- No native support for screenshots (must be added manually)
- Content extraction quality depends on source material completeness
- Jira API access required for Jira-based generation

### Content Limitations
- Generated content is initial draft, not final publication
- Best suited for feature documentation, not general help articles
- Assumes source material contains customer-relevant information
- May require manual editing for customer-facing tone

### Process Limitations
- Requires manual review and validation before publication
- Screenshots must be added post-generation
- Updates require full PDF regeneration
- No versioning system built in

## Phase 2 Progress

**Completed Skills:**
1. ✅ Sprint Forecasting - Monte Carlo sprint completion forecasting
2. ✅ KB Article Generator - Customer-facing KB article generation from PRDs/Jira

**Pending Skills:**
3. ⏳ User Story Generator - Convert PRD sections to Jira-ready user stories
4. ⏳ CS Ticket Analyzer - Analyze support ticket patterns and extract themes

---

**Metadata:**
- Created: January 26, 2026
- Status: Phase 2 Skill #2 Complete
- Command: `/generate-kb-article`
- Integration: Atlassian MCP (Jira) + Python reportlab
- Output format: PDF
