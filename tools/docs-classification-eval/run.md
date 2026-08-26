---
description: "Run the docs-classification eval: score /sprint-documentation-review's needs_docs classification against the gold labels"
---

# Run Docs-Classification Eval

Measures how well the **doc-needs classification** inside `/sprint-documentation-review`
(its "NEEDS DOCUMENTATION ✅ / NO ❌" decision, Task A) reproduces the human gold labels.
The headline metric is **recall**, every false negative is a shipped, user-visible change
that the review would silently never surface, so the human approving the review can't catch it.

## System under test

The classification criteria in `.claude/commands/sprint-documentation-review.md` → step 3,
Task A ("NEEDS DOCUMENTATION" vs "NO DOCUMENTATION NEEDED"). Improving the classifier means
editing *those rules* (or a dedicated classification prompt), bumping the version here, and
re-running. This eval is the regression test for that command's judgment.

## Inputs

- `product-context.md`, the fictional product the stories describe
- `labeling-guide.md`, the definition of `needs_docs` truth
- `reference-set/sprint-A.md`, `sprint-B.md`, stories only (the classifier input)
- `gold/labels.md`, the answer key (used only for scoring, never shown to the classifier)

## Procedure

### 1. Build the classifier input
Collect every story from `reference-set/*.md`. Pass **only** `id · title · description · type`.
Do **not** read `gold/labels.md` into the classifier context, scoring happens after, in a
separate step.

### 2. Classify (one agent, lean by design)
Run a **single** agent pass over all stories (they're one-liners; they fit one context, no
need for one-agent-per-story, which would burn tokens for no signal; see the lean-pipeline
note in the README). Give it: `product-context.md`, the classification criteria from
`sprint-documentation-review.md` Task A, and the stories. For each story it returns:

```
RLY-XXX | needs_docs: yes|no | priority: HIGH|MEDIUM|LOW|, 
```

The agent must decide from the story text alone.

### 3. Score against gold
Now load `gold/labels.md`. Treat `needs_docs = yes` as the positive class. Compute:

- **Confusion matrix:** TP / FP / FN / TN
- **Recall** = TP / (TP + FN), the headline
- **Precision** = TP / (TP + FP)
- **F1** = harmonic mean
- **Priority accuracy** on the true-positive items (secondary, only meaningful once a story
  is correctly flagged)

### 4. List every disagreement
For each mismatch: `id · gold vs predicted · one-line diagnosis` (why the classifier likely
tripped, e.g. "fired only on 'new feature', missed the enhancement"). This list is the
actual work product: it says what to fix next.

### 5. Write results
Save to `results/v{N}.md` using the template below. Increment N per run. Never overwrite a
prior version, the point is to compare versions.

## Results template

```markdown
# Eval Run v{N}, {date}

**Classifier version:** {what rule-set / prompt was tested, 1 line}
**Reference set:** {N} stories ({A} Sprint A + {B} Sprint B)

## Scores
|              | value |
|--------------|-------|
| Recall       | XX%   |  ← headline (missed doc updates)
| Precision    | XX%   |
| F1           | XX%   |
| Priority acc | XX%   |

## Confusion matrix
|              | pred YES | pred NO |
|--------------|----------|---------|
| **gold YES** | TP       | FN ←    |
| **gold NO**  | FP       | TN      |

## Disagreements
- RLY-XXX, gold YES / pred NO, {diagnosis}
- ...

## Verdict & next change
{What the errors have in common → the one rule change to try in v{N+1}}
```

## The loop

Read the disagreements → find the pattern (v1 will almost certainly miss *enhancements to
existing features*) → make the smallest rule change that would fix that class → bump to
v{N+1} → re-run → confirm recall rose and nothing regressed. Two `results/` files side by
side are the whole story: *prompt collection → system with a feedback loop.*

## Guardrails
- Never let the classifier see `gold/labels.md`.
- Keep the gold labels human-owned. If a run reveals a *label* is wrong (not the classifier),
  fix the label deliberately and note it, don't quietly tune truth to match the model.
