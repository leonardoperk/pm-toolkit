# Reference Set, Sprint B ("Relay")

Classifier **input**, stories only, no labels. Answer key in `../gold/labels.md`.
15 completed stories. **Phrasing: raw-Jira**, states what changed technically; user impact
must be *inferred*, not read off a label.

Fields per story: ticket text · issue type.

---

**RLY-301, Automations: conditional branching**
Add IF/ELSE condition nodes to the automation builder. Conditions evaluate contact fields
and branch the flow. · Story

**RLY-302, Migrate job queue Bull → BullMQ**
Move background jobs to BullMQ. Update workers and queue config; job payloads unchanged. · Task

**RLY-303, Allow a second PMS connection**
Remove the single-PMS-per-account constraint. Update the connections model and the settings
UI to list multiple connections. · Story

**RLY-304, WhatsApp reply-window countdown**
Add a countdown badge on WhatsApp conversations showing time left in the 24h reply window,
computed from the last inbound timestamp. · Story

**RLY-305, Upgrade WhatsApp Cloud API v18 → v20**
Bump the WhatsApp Cloud API integration to v20.0; update endpoint versions and deprecated
field handling. · Task

**RLY-306, Gmail shared-inbox connect**
Add delegated/shared-inbox OAuth scope and handling to the Gmail connect flow (currently
personal inboxes only). · Story

**RLY-307, Webhook delivery: retry + backoff**
Add exponential backoff and a retry queue for failed outbound webhooks (currently single
attempt, dropped on failure). Payload schema unchanged. · Story

**RLY-308, Billing: self-serve cancellation**
Add a "Cancel subscription" flow in Billing settings with confirmation and end-of-period
handling (currently handled manually by support). · Story

**RLY-309, Encrypt auth token storage**
Move auth tokens from the session table to an encrypted secrets store; rotate on refresh. No
API changes. · Task

**RLY-310, Contact import: normalize phone to E.164**
In CSV import, normalize phone numbers to E.164 and flag rows that can't be parsed (currently
invalid formats fail at send time). · Story

**RLY-311, AI: summarize conversation**
Add a "Summarize conversation" action that generates a summary of the current thread on
demand. · Story

**RLY-312, Index contacts for faster search**
Add a composite index on `contacts(name, email, phone)` to speed up search queries. No query
API changes. · Task

**RLY-313, Broadcast: merge-field preflight**
Before send, validate that all template merge fields resolve for the target segment; show a
warning listing unresolved fields. · Story

**RLY-314, Email subject emoji rendering**
Emojis in email subject lines render as tofu boxes for some recipients. Fix subject encoding
to UTF-8. · Bug

**RLY-315, Shrink production Docker image**
Multi-stage build and prune dev dependencies to reduce image size and speed up deploys. · Task
