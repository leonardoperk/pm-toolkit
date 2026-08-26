# Gold Labels, the answer key

Human-owned ground truth. The classifier is scored against this; it must **never** see this
file at classification time (that's why stories and labels live apart). Each label answers
one question from `../labeling-guide.md`: *could a user observe this change, or must they act
differently because of it?*

`⚠️` marks a case that's genuinely arguable, kept as a note on why the truth is what it is.

## Sprint A, CONFIRMED (human gold)

| ID | needs_docs | priority | why |
|----|-----------|----------|-----|
| RLY-201 | yes | HIGH | New WhatsApp template category a user can pick |
| RLY-202 | no |, | Virtualized render; same UI, nothing observable |
| RLY-203 | yes | MEDIUM | ⚠️ Enhancement to existing inbox filter, user-visible, docs now incomplete |
| RLY-204 | no |, | Bug fix; restores already-intended behavior |
| RLY-206 | yes | HIGH | Whole new channel with its own setup |
| RLY-207 | no |, | ⚠️ Chart lib swap; same charts/numbers, sounds user-facing but isn't |
| RLY-208 | no |, | ⚠️ Internal audit log; no user surface |
| RLY-209 | yes | MEDIUM | ⚠️ UI wording users navigate by changed; every "Flows" mention now wrong |
| RLY-211 | no |, | Runtime upgrade; invisible |
| RLY-216 | no |, | ⚠️ Better AI output quality; no new action or option to document |
| RLY-217 | yes | MEDIUM | ⚠️ Documented cap "max 3 actions" → 5; docs now wrong |
| RLY-218 | yes | MEDIUM | ⚠️ Documented "no reports on mobile" limit lifted; new capability |
| RLY-219 | yes | HIGH | AI chatbot extended to a channel that had none; availability matrix changes |
| RLY-220 | yes | LOW | ⚠️ Documented "Chrome/Edge only" limit changed; new user segment |

**Sprint A truth: 8 yes / 6 no.**

## Sprint B, CONFIRMED (human gold)

| ID | needs_docs | priority | why |
|----|-----------|----------|-----|
| RLY-301 | yes | HIGH | Conditional branching in automations, removes "no branching" limit, big new capability |
| RLY-302 | no |, | Job-queue library migration; internal |
| RLY-303 | yes | HIGH | ⚠️ Second PMS per account, removes documented "one PMS" limit |
| RLY-304 | yes | MEDIUM | ⚠️ New "reply window expiring" indicator in inbox, user-visible behavior |
| RLY-305 | no |, | ⚠️ WhatsApp Cloud API version bump (BSP side); no behavior change. FP trap |
| RLY-306 | yes | MEDIUM | ⚠️ Gmail shared-inbox support, removes documented "Gmail personal only" limit |
| RLY-307 | no |, | ⚠️ Webhook retry/backoff reliability; same contract. FP trap |
| RLY-308 | yes | HIGH | ⚠️ Subscription cancellation now self-serve, was support-only; workflow change |
| RLY-309 | no |, | Auth token storage refactor; internal security |
| RLY-310 | yes | MEDIUM | ⚠️ CSV import auto-formats phone to E.164, user-visible import behavior |
| RLY-311 | yes | MEDIUM | AI conversation summarization, new capability |
| RLY-312 | no |, | DB index for contact search; internal perf |
| RLY-313 | yes | MEDIUM | ⚠️ Merge-field preflight warning before send, new user-visible safeguard |
| RLY-314 | no |, | Emoji rendering bug fix; restores intended behavior |
| RLY-315 | no |, | Docker image size / deploy speed; internal |

**Sprint B truth: 8 yes / 7 no.**, Total gold: 29 stories, 16 yes / 13 no.
