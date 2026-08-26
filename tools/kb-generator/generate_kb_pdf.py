#!/usr/bin/env python3
"""
KB Article PDF Generator
Creates professional, customer-facing knowledge base articles in PDF format
"""

import argparse
import sys
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib import colors

def create_kb_article_pdf(title, sections, output_path, author="Product Team"):
    """
    Generate a KB article PDF with professional formatting

    Args:
        title: String - Article title
        sections: List of dicts with 'heading' and 'content' (content can be list of strings)
        output_path: String - Where to save PDF
        author: String - Author name (default: "Product Team")

    Returns:
        String - Path to generated PDF
    """

    # Create PDF document
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=72
    )

    # Define styles
    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#2C3E50'),
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )

    heading1_style = ParagraphStyle(
        'CustomHeading1',
        parent=styles['Heading1'],
        fontSize=18,
        textColor=colors.HexColor('#2980B9'),
        spaceAfter=12,
        spaceBefore=12,
        fontName='Helvetica-Bold'
    )

    heading2_style = ParagraphStyle(
        'CustomHeading2',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=colors.HexColor('#2980B9'),
        spaceAfter=10,
        spaceBefore=10,
        fontName='Helvetica-Bold'
    )

    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontSize=11,
        leading=16,
        textColor=colors.HexColor('#2C3E50'),
        alignment=TA_LEFT
    )

    bullet_style = ParagraphStyle(
        'CustomBullet',
        parent=styles['Normal'],
        fontSize=11,
        leading=16,
        textColor=colors.HexColor('#2C3E50'),
        leftIndent=20,
        bulletIndent=10
    )

    # Build document
    story = []

    # Title page
    story.append(Spacer(1, 1*inch))
    story.append(Paragraph(title, title_style))
    story.append(Spacer(1, 0.3*inch))

    # Subtitle with metadata
    metadata = f"<i>Knowledge Base Article • {author}</i><br/><i>Last Updated: {datetime.now().strftime('%B %d, %Y')}</i>"
    story.append(Paragraph(metadata, ParagraphStyle(
        'Metadata',
        parent=styles['Normal'],
        fontSize=10,
        textColor=colors.HexColor('#7F8C8D'),
        alignment=TA_CENTER
    )))

    story.append(Spacer(1, 0.5*inch))
    story.append(PageBreak())

    # Content sections
    for section in sections:
        heading = section.get('heading', '')
        content = section.get('content', [])
        level = section.get('level', 1)  # 1 or 2 for heading levels

        # Add heading
        if heading:
            if level == 1:
                story.append(Paragraph(heading, heading1_style))
            else:
                story.append(Paragraph(heading, heading2_style))

        # Add content
        if isinstance(content, list):
            for item in content:
                if item.startswith('• ') or item.startswith('- '):
                    # Bullet point
                    clean_item = item[2:] if item.startswith('• ') else item[2:]
                    story.append(Paragraph(f"• {clean_item}", bullet_style))
                elif item.startswith('**') and item.endswith('**'):
                    # Bold text (subheading)
                    clean_item = item.strip('*')
                    story.append(Paragraph(f"<b>{clean_item}</b>", body_style))
                    story.append(Spacer(1, 0.1*inch))
                elif item.strip().startswith('1.') or item.strip().startswith('2.'):
                    # Numbered list
                    story.append(Paragraph(item, bullet_style))
                else:
                    # Regular paragraph
                    if item.strip():
                        story.append(Paragraph(item, body_style))
                        story.append(Spacer(1, 0.1*inch))
        elif isinstance(content, str):
            story.append(Paragraph(content, body_style))
            story.append(Spacer(1, 0.1*inch))

        story.append(Spacer(1, 0.2*inch))

    # Build PDF
    doc.build(story)

    return output_path


def main():
    parser = argparse.ArgumentParser(
        description='Generate KB article PDF from structured content'
    )
    parser.add_argument('--title', '-t', type=str, required=True,
                       help='Article title')
    parser.add_argument('--output', '-o', type=str, required=True,
                       help='Output PDF path')
    parser.add_argument('--author', '-a', type=str, default='Product Team',
                       help='Author name (default: Product Team)')

    args = parser.parse_args()

    # Example structure for testing
    sections = [
        {
            'heading': 'Overview',
            'level': 1,
            'content': [
                'This is an example KB article generated by the KB generator tool.',
                'Use the Python API to pass in your structured content.'
            ]
        },
        {
            'heading': 'How to Use This Tool',
            'level': 1,
            'content': [
                '1. Import the create_kb_article_pdf function',
                '2. Structure your content as a list of section dicts',
                '3. Call the function with title, sections, and output path',
                '4. PDF will be generated automatically'
            ]
        }
    ]

    try:
        output_path = create_kb_article_pdf(
            title=args.title,
            sections=sections,
            output_path=args.output,
            author=args.author
        )
        print(f"✅ KB article generated: {output_path}")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Error generating KB article: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
