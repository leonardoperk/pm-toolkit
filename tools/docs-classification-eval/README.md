# Docs-Classification Eval

An eval that measures one thing about my `/sprint-documentation-review` command: when it
decides which shipped stories need documentation, how many real ones does it miss?

## Why recall is the number that matters

The command runs every sprint, unattended, across 15–25 stories. It flags each as "needs
docs" or not, then a human approves the proposed updates. That approval looks like the safety
net. It isn't the one that counts.

You can only approve what the system puts in front of you. A story the classifier wrongly
marks "no docs" never shows up in the review, so the human can't catch it. The gate stops bad
proposals; it can't stop missing ones. So recall (the share of genuinely doc-worthy changes
the classifier catches) is what actually protects the docs. Every miss is a gap you'd
otherwise discover through a support ticket weeks later.

This eval optimizes for recall, not accuracy. A false positive is noise a human clears in a
second. A false negative is invisible.

## What I built

- A reference set of 29 stories across two sprints, describing a category-standard messaging
  product (fictional, so it's shareable).
- Hand-labeled ground truth: each story marked needs-docs yes/no against a product-truth
  definition, held in a separate answer key the classifier never sees.
- A runner that applies the command's real classification rules with a single agent, then
  scores the output, confusion matrix, precision, recall, and a diagnosis of every error.

## Results

| | v1 | v2 |
|---|----|----|
| Recall | 100% | 100% |
| Precision | 100% | 94% |

The story is in the two runs, not the final number.

v1 scored a perfect 100%. Instead of shipping that, I treated it as suspect, a perfect score
usually means the test is too easy. It was. My story descriptions leaked the answers ("same
UI", "no user-facing change"), so the classifier was reading labels rather than judging.

v2 rewrote all 29 stories in raw Jira-ticket voice, where user impact has to be inferred
("migrate to BullMQ, payloads unchanged" instead of "internal, no user change"). Recall held
at 100%. That's the result worth having: the classifier genuinely infers doc-need from a bare
ticket, it wasn't just matching tells. The harder test also exposed the real weak spot, one
false positive on a reliability change (webhook retry), which is the cheap kind of error. The
frontier is precision now.

One limit worth stating: this is a small set. 100% recall means zero misses on 16
doc-worthy stories, not a perfect classifier. By the rule of three, zero misses on 16 is
still consistent with a true recall near 80%. That's why the two-run story matters more than
the number.

Full write-ups: [results/v1.md](results/v1.md), [results/v2.md](results/v2.md).

## Design decisions

- **Recall over accuracy**, the two errors have very different costs.
- **Human-labeled ground truth**, so the yardstick is a person's product judgment, not
  another model's opinion.
- **Input and answer key in separate files**, so the classifier can't read the answers.
- **One agent over all stories** instead of one per story, same signal, a fraction of the cost.
- **The set leans on enhancements to existing features**, the exact case a naive "new
  feature only" classifier drops.

## What I deliberately left as future work

- **Stage 2, output quality.** This eval covers routing: which stories need docs. The
  command also drafts the doc text, and judging that is a separate, softer eval with no single
  right answer. Sketched, not built.
- **v3, scenario ambiguity.** v2 hardened the phrasing; the scenarios are still one clean
  change per ticket. Real sprints bring compound and vague tickets, and that's where recall
  would finally bend.

Both are noted so the map is visible. One eval done well beats three half-built.

## Run it

See [run.md](run.md). The first run sets a baseline; the point is comparing versions, not a
single score.

## Files

```
product-context.md   the fictional product the stories describe
labeling-guide.md    the needs-docs truth definition
reference-set/        the 29 stories (classifier input, no labels)
gold/labels.md        the answer key (kept away from the classifier)
run.md                the eval runner
results/              scored runs, one file per version
```
