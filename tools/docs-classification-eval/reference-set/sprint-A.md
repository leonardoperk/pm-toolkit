# Reference Set, Sprint A ("Relay")

Classifier **input**, stories only, no labels. Answer key in `../gold/labels.md`.
14 completed stories. **Phrasing: raw-Jira**, states what changed technically; user impact
must be *inferred*, not read off a label. (v1 used legible phrasing that telegraphed the
answers; see `../results/v1.md` for why that was hardened.)

Fields per story: ticket text · issue type.

---

**RLY-201, WhatsApp template builder: add Utility category**
The template builder's category selector offers Marketing and Authentication. Add "Utility"
and map it to the Cloud API `category` field on submit. · Story

**RLY-202, Virtualize inbox message list**
Replace the conversation message list with a react-window virtualized renderer to fix scroll
jank on long threads. · Task

**RLY-203, Inbox filter: add "Unassigned"**
Add an "Unassigned" option to the inbox filter dropdown; filters conversations where
`assignee` is null. · Story

**RLY-204, Inbox crashes on very long threads**
White screen when opening conversations with 500+ messages; stack overflow in render
recursion. Fix. · Bug

**RLY-206, Add Instagram DM channel**
OAuth connect flow, webhook subscription, and inbound/outbound message mapping for Instagram
Direct Messages into the unified inbox. · Story

**RLY-207, Reports: migrate Chart.js → Recharts**
Replace chart components on the reports dashboards with Recharts. Keep existing datasets and
endpoints. · Task

**RLY-208, Audit log for admin config changes**
Persist who/what/when for admin configuration changes to a new `audit_log` table. Consumed by
the internal compliance export script. · Story

**RLY-209, Rename "Flows" → "Automations"**
Update all UI strings, nav labels, and settings copy from "Flows" to "Automations". No logic
changes. · Task

**RLY-211, Upgrade Node 18 → 20**
Bump backend runtime to Node 20; update CI images and the `engines` field. · Task

**RLY-216, Suggested replies: new model checkpoint**
Point the suggested-reply service at the new fine-tuned checkpoint; update the inference
endpoint and prompt template. Improves reply relevance. · Story

**RLY-217, Raise automation action cap 3 → 5**
Raise the per-event automation action limit from 3 to 5. Update validation and the config
UI max. · Story

**RLY-218, Reports in the mobile app**
Add the reports routes and views to the mobile app navigation (currently web-only). · Story

**RLY-219, AI chatbot on email channel**
Wire the email channel inbound into the bot pipeline that currently serves WhatsApp and
webchat. · Story

**RLY-220, Extension: add Firefox target**
Port the Chrome/Edge extension manifest to Firefox (MV2/MV3), add to build targets, publish
to AMO. · Story
