# PRD Example: User & Team Core (Authentication & Permissions)

> **This is a genericized PRD example.** Use it as a reference for structure and depth when writing your own PRDs.
> Company-specific details have been replaced with `[COMPANY_NAME]`, `[LEGACY_SYSTEM]`, etc.

> **Jira:** [[PRODUCT_PROJECT]-32](https://[JIRA_URL]/browse/[PRODUCT_PROJECT]-32)
> **Type:** Epic | **Status:** IN CONCEPT | **Assignee:** [PM_NAME]

---

# Problem Alignment

## Problem & Opportunity

[COMPANY_NAME] currently relies on [LEGACY_SYSTEM]'s core for user identity, authentication, and permissions. The functionality works, but we don't own it. Building a native User & Team Core is a deliberate architectural decision to take full ownership of this layer so we can evolve it on our terms.

**Why this matters:**
- We cannot customize authentication flows, permission logic, or user identity to match [COMPANY_NAME]'s specific needs without unreasonable effort
- Continued reliance on [LEGACY_SYSTEM]'s core limits our ability to differentiate and iterate independently

**Evidence & insights:**
- [LEGACY_SYSTEM] confirmed as blocking constraint for the [platform initiative] initiative
- Product roadmap for [AI capability] requires native user identity and real-time availability signals

**Why now:**
- [platform initiative] requires this as a foundational layer
- Continued development on [LEGACY_SYSTEM] increases migration cost over time

---

## High Level Approach

Build a native User & Team Core that owns: authentication (login, password reset, invitation), user profile management, role-based access control (RBAC), multi-organization support, and Super Admin tooling. Full replacement of [LEGACY_SYSTEM]'s user/auth layer with the same capabilities built on our own stack.

**Principles:**
- **better-auth** as authentication library (includes Owner role which cannot be deleted)
- Cumulative permission model: each role inherits all permissions from roles below it
- User profile settings: display name, email, password, UI preferences, and notifications, editable by the user; admins can additionally edit display name, role, and force a password reset
- Availability is a manual setting controlled by each user, admins cannot override
- Deactivated users retain all historical contributions in [COMPANY_NAME], displayed as "Deactivated User"

**Alternatives not pursued:**

| Option | Why Rejected |
|--------|-------------|
| Extending [LEGACY_SYSTEM] | Not viable; technical debt continues to compound |

---

## Narrative

**Today, Admin invites a new team member:**
The admin opens the user settings, adds a new user with name, role, and email. An invitation email goes out. The team member clicks the link, sets a password, and lands in [COMPANY_NAME]. It works, but the entire flow runs on [LEGACY_SYSTEM]'s logic. We can't control how invitations are structured, how permissions are enforced, or how availability is handled. When we want to change something, we're working around [LEGACY_SYSTEM] instead of building forward.

**After User Core:**
The exact same flows, but running on our own stack. We define the invitation email content, the permission rules, the password requirements, the availability model. When the AI needs to check which team members are online to route work, it queries our own system. When we want to add a new role or change how deactivation works, we change our code.

---

## Goals

1. Eliminate [LEGACY_SYSTEM] dependency for user identity, authentication, and permissions
2. Deliver role-based UI so users see only what's relevant to their permission level
3. Support multi-organization access with seamless account switching
4. Lay the technical foundation for AI-driven work handoff based on user availability

**Guardrail metrics:**
- No increase in authentication-related support tickets post-launch
- Zero incidents of users accessing features or data outside their permission scope

---

## Non-goals

| Non-goal | Reason |
|----------|--------|
| Team creation and management | Out of scope for v1; keep in mind for architecture |
| SSO / social sign-ins | Not part of v1; better-auth supports this later |
| Complex approval workflows | Role changes and invitations do not require approval flows |
| Billing/subscription management | Not tied to this epic |
| [Role X] | Out of scope for this epic |
| [Role Y] | Out of scope for this epic |

---

# Solution Alignment

## Key Features

**Plan of Record:**

1. **Authentication Flows**, Login with email + password; forgot password → reset email → set new password → redirect to [COMPANY_NAME]. Generic error messaging (no field-level specificity). Min 12 chars, 1 uppercase, 1 numeric, 1 special character., [PRODUCT_PROJECT]-279, [PRODUCT_PROJECT]-280
2. **User Invitation & Onboarding**, Admin invites by name + role + email. Invitation email sent with role context and permission overview. Invited user: clicks join link → sets password → lands in [COMPANY_NAME]. Error state if invited email already exists., [PRODUCT_PROJECT]-272, [PRODUCT_PROJECT]-275
3. **Profile Management**, Display name, email, password (requires current password + new + confirmation). UI preferences: language, AI suggest mode, AI improve mode. Notifications: email & push, browser push, browser audio. Email Signatures: create/edit/delete personal signatures, assign as default to workspaces. No profile image., [PRODUCT_PROJECT]-271
4. **Availability & Role Visibility**, Users set their own availability status manually. User role is visible to all other users within the organization at all times., [PRODUCT_PROJECT]-269, [PRODUCT_PROJECT]-270
5. **User Maintenance & Deactivation**, Admin can edit: display name, role, force password reset. Deactivation: requires confirmation; user loses access; all contributions remain as "Deactivated User"., [PRODUCT_PROJECT]-273, [PRODUCT_PROJECT]-274
6. **Role & Permission Table**, Admins view a permission table showing capabilities per role. Used when inviting or modifying users. ⚠️ In scope for v1 but not yet fully defined, story requires spec before development., [PRODUCT_PROJECT]-276
7. **Multi-Organization & Account Switching**, Account switcher accessible from: top-left nav and bottom-right profile menu. On login/re-open: user redirected to last accessed account (multi-account users only)., [PRODUCT_PROJECT]-277, [PRODUCT_PROJECT]-278
8. **Super Admin Tooling**, Create new customer accounts. Impersonate users: persistent visual indicator during session; all actions fully audit-logged. Access internal admin tools., [PRODUCT_PROJECT]-284, [PRODUCT_PROJECT]-285, [PRODUCT_PROJECT]-286, [PRODUCT_PROJECT]-287
9. **Connect External Tool Flow**, ⚠️ In scope, spec TBD., [PRODUCT_PROJECT]-281
10. **Assign User to [Module A]**, ⚠️ In scope, spec TBD., [PRODUCT_PROJECT]-282
11. **Assign User to [Module B]**, ⚠️ In scope, spec TBD., [PRODUCT_PROJECT]-283

**Future Considerations:**
1. [Role X] UX, depends on this epic's RBAC foundation
2. [Role Y], depends on this epic's RBAC foundation
3. SSO / social sign-ins, better-auth supports this when needed

---

## Key Flows

#### Flow 1: Admin Invites a New User

**Steps:**
1. **Admin:** Opens user settings, clicks "Invite User"
2. **System:** Shows invite form: display name, role, email
3. **Admin:** Fills in details, submits
4. **System:** Sends invitation email with role context and permission overview; shows error if email already exists
5. **Invited User:** Clicks link in email → lands on password setup screen
6. **Invited User:** Sets password (min 12 chars, 1 uppercase, 1 numeric, 1 special character)
7. **System:** Auto-populates profile from invite data → redirects to [COMPANY_NAME]

**Edge cases:**
- Invited email already exists: error shown, no duplicate user created
- Invitation link expired: user must request a new invite

#### Flow 2: User Deactivation

**Steps:**
1. **Admin:** Opens user list, selects user, clicks "Deactivate"
2. **System:** Shows confirmation dialog
3. **Admin:** Confirms deactivation
4. **System:** User loses access immediately; removed from user list; all historical contributions remain displayed as "Deactivated User"

#### Flow 3: Super Admin Impersonation

**Steps:**
1. **Super Admin:** Initiates impersonation session for a user
2. **System:** Enters impersonation mode; persistent visual indicator shown to Super Admin throughout session
3. **Super Admin:** Performs actions within [COMPANY_NAME] as that user
4. **System:** All actions fully audit-logged under the Super Admin's identity
5. **Super Admin:** Ends impersonation session

**Edge cases:**
- No UI feedback shown to the impersonated user, intentional by design

---

## Key Logic

**Role Hierarchy (Cumulative Permissions)**

| Role | Inherits From | Additional Capabilities |
|------|--------------|------------------------|
| Member |, | Profile (display name only), manual availability, org access, account switching |
| Admin | Service | Invite users, assign/edit roles, deactivate users, multi-org management, system-wide settings, view permission table |
| Super Admin | Platform-level | Create accounts, impersonate users (logged), internal admin tools |

**Critical Rules:**
- Role visibility: a user's role is always visible to all other users in the org
- Profile editing: email, UI preferences, email signatures, and notifications are user-editable only; display name and role can also be edited by admins; admins can force a password reset
- Availability: manual setting by user only, admins cannot override
- Deactivation: all contributions persist as "Deactivated User"; all data retained in [COMPANY_NAME]
- better-auth Owner role: cannot be deleted, protects against single-admin lockout scenario
- Permission-based UI: users encounter only UI relevant to their role; no disabled features, no out-of-scope references, no placeholders

**Authentication Rules:**
- Generic error messaging only (no field-level specificity about which credential is wrong)
- Password requirements: min 12 chars, 1 uppercase, 1 numeric, 1 special character

**Non-functional Requirements:**
- No UI feedback to the impersonated user that a Super Admin session is active, intentional by design
- AI architecture note: The availability status model established here is the foundation for future AI-driven work handoff. System must be designed so AI can check real-time user availability and route work accordingly

---

## Other

**Open Questions:**
1. **Owner role in better-auth:** Are there implications for this role? Does every account require one user with the Owner role?

**Risks:**

| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| User confusion about permission scope | Medium | Low | Role-based UI (no disabled elements) + visible permission table for Admins + permission overview in invitation email |
| Privacy concern around deactivated users | Medium | Low | Anonymizing as "Deactivated User" |
