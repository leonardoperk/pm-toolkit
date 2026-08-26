---
name: product-manager-toolkit
description: Two PM scripts, RICE prioritization and customer-interview analysis, with how to run them. Use for scoring and ranking features, and for extracting pain points, themes, and sentiment from interview transcripts.
---

# Product Manager Toolkit

Two working scripts for the number- and text-crunching parts of prioritization and discovery. For PRDs, use the Hybrid template (see below), this skill does not carry its own.

## RICE Prioritizer, `scripts/rice_prioritizer.py`

Scores and ranks features by RICE, with portfolio analysis (quick wins vs. big bets), a suggested quarterly roadmap, and team-capacity planning.

```bash
# Create a sample CSV to start from
python scripts/rice_prioritizer.py sample

# Score your features (capacity = person-months per quarter)
python scripts/rice_prioritizer.py features.csv --capacity 15

# JSON output for further processing
python scripts/rice_prioritizer.py features.csv --output json
```

CSV columns: `name,reach,impact,confidence,effort`

Scoring the script uses:
```
Score = (Reach × Impact × Confidence) / Effort

Reach:      users affected per quarter (a number)
Impact:     massive=3 · high=2 · medium=1 · low=0.5 · minimal=0.25
Confidence: high=100% · medium=80% · low=50%
Effort:     person-months, xs=0.5 · s=1 · m=3 · l=6 · xl=12
```

Output: ranked features, portfolio balance, and a quarterly roadmap sized to your capacity.

## Customer Interview Analyzer, `scripts/customer_interview_analyzer.py`

Extracts structured insight from an interview transcript.

```bash
python scripts/customer_interview_analyzer.py transcript.txt

# JSON output for aggregating across interviews
python scripts/customer_interview_analyzer.py transcript.txt json
```

Extracts: pain points with severity, feature requests, jobs-to-be-done, sentiment, recurring themes, competitor mentions, and quotable lines. Run across several interviews to surface patterns.

## PRDs

This toolkit standardizes on the **Hybrid PRD Template**, don't use a different format here. Run `/create-prd` for the guided interview, or start from `templates/prds/Hybrid-PRD-Template.md`. The standard and its writing principles live in `.claude/knowledge/prd-template.md`.
