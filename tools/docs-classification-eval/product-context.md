# Reference Product, "Relay" (fictional)

> Fictional product used purely to make the eval's reference stories coherent.
> Not a real company. The domain mirrors a category-standard omnichannel
> customer-messaging SaaS (shared inbox, Meta/WhatsApp channels, automations, AI replies,
> hospitality PMS sync) so the classification edge cases are realistic. The constraints
> below are category-common patterns, Meta's messaging rules, automation caps, companion-app
> boundaries, not any one vendor's. Rename freely; the name carries no weight.

## What it is

**Relay** is an omnichannel customer-messaging platform for hospitality and e-commerce
teams. Guests reach a business across many channels; Relay unifies them into one shared
team inbox, adds rule-based automation and AI-assisted replies, syncs guest data from the
property's booking system, and reports on response performance.

**Users:** support agents (live in the inbox all day), team leads (configure automations,
watch reports), admins (channels, roles, billing). Companion **mobile app** and **browser
extension** for on-the-go and in-context use.

## Core feature areas (where stories land)

| Area | What it does |
|------|--------------|
| **Inbox** | Shared team inbox: conversations, assignment, filters, tags, notes, snooze |
| **Channels** | WhatsApp, Instagram DM, email, live-chat widget, SMS, connect & configure |
| **Automations** | Rule-based triggers & flows (e.g. "new WhatsApp message out of hours → auto-reply") |
| **AI Assistant** | Suggested replies, auto-reply drafts, conversation summarization |
| **Templates & Broadcasts** | Reusable message templates, scheduled broadcasts to segments |
| **Contacts** | Contact profiles, segments, custom fields, consent/opt-out |
| **Reports** | Response time, volume, CSAT, agent-performance dashboards |
| **PMS Integrations** | One-way guest-data sync from the property management / booking system |
| **Companion apps** | Mobile app (agent inbox on the go) + browser extension (reply in context) |
| **Settings** | Roles & permissions, business hours, notification prefs, billing |

## Known limitations (category-common; the kind users hit and ask about)

*These matter because a story that **changes** one of them is a documentation change even
though it "sounds small", the docs state the old limit and are now wrong.*

- **Automations:** max 3 actions per event trigger; max 3 webhook automations per account;
  no conditional branching.
- **PMS:** one PMS connection per account; sync is one-way (PMS → Relay), never written back.
- **WhatsApp:** 24-hour reply window after a guest's last message; initiating outside it
  requires a Meta-approved template.
- **AI chatbot:** active on WhatsApp and web chat only, not on email or Messenger.
- **Mobile app:** cannot configure automations, templates, or PMS; no access to detailed reports.
- **Browser extension:** Chrome and Edge only (no Firefox/Safari); requires an active account.
- **Phone numbers:** must be E.164 format.
- **Support-only actions:** PMS setup and subscription cancellation require Relay support.
