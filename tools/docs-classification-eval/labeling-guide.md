# Labeling Guide, the ground truth

This is the **human-owned definition** of what a shipped story needs. The eval measures
whether the `/sprint-documentation-review` classifier reproduces *these* labels. Kept
deliberately **independent** of the command's own rule list, otherwise the eval would
just check that the command agrees with itself (circular). Here we define what's *true*;
the command has to rediscover it.

## The one question that decides `needs_docs`

> **Could a user of the product observe this change, or must they act differently because
> of it?**

If yes → `needs_docs: yes`. The user's mental model of the product changed, so the docs
that describe the product must change too.

**needs_docs: YES**
- New capability a user can use
- Changed behavior a user can observe
- New or changed configuration/option
- New or removed limitation
- New integration or channel
- A workflow step that changes how a user completes a task

**needs_docs: NO**
- Backend/internal work with no user-visible surface (refactor, infra, CI, perf that
  doesn't change observable behavior)
- Bug fix that *restores* already-documented intended behavior (nothing new to describe)
- Dev-only or internal-tooling change
- Pure visual tweak with no behavior or wording change users rely on

## The trap that defines the whole eval

The costly miss is the **enhancement to an existing feature**. It's user-visible, so it's
`YES`, but classifiers that only fire on "new feature" quietly drop it. Every false
negative here is an invisible doc gap: the feature ships, the docs silently go stale, and
the human approving the review never sees it because it was never surfaced.

## Priority (only when `needs_docs: yes`)

| Priority | When |
|----------|------|
| **HIGH** | New customer-facing capability, or a breaking/behavior change users must know now |
| **MEDIUM** | Enhancement or changed option on an existing user-facing feature |
| **LOW** | Minor but genuinely user-visible (wording, small limit change) |

## How labels get set

Each story below carries a **PROPOSED** label + rationale, that's my read, not truth.
**You own the final label.** Ambiguous ones are flagged `⚠️ EDGE` so your attention goes
where it actually matters; rubber-stamping the obvious ones is fine. Your confirmed labels
become the gold standard the classifier is scored against.
