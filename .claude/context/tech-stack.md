# Tech Stack

This document defines the technical stack used by the product. Reference this when assessing technical feasibility, reviewing PRDs, generating user stories, or evaluating implementation complexity.

> **Setup required:** Fill in all `[FILL IN: ...]` placeholders with your company's actual tech stack.
> Run `/setup` for guided onboarding.

## Backend

### [FILL IN: Primary Backend Technology]
- **Usage:** [FILL IN: e.g. "Core application (legacy/existing features)"]
- **Version:** [FILL IN: or "Not specified"]
- **Notes:** [FILL IN: key notes about this technology in your context]

### [FILL IN: Secondary Backend Technology, if applicable]
- **Usage:** [FILL IN: e.g. "New services and microservices"]
- **Version:** [FILL IN: or "Mixed versions"]
- **Notes:** [FILL IN: key notes]

**Architecture Pattern:**
- [FILL IN: e.g. "Monolith", "Microservices", "Hybrid, core on X, new services on Y"]
- [FILL IN: decision rule for when to use which, e.g. "New features go in Y unless they extend core X functionality"]

## Frontend

### [FILL IN: Frontend Framework]
- **Framework:** [FILL IN: e.g. "React 18", "Vue 3", "Angular 17"]
- **Notes:** [FILL IN: e.g. "TypeScript throughout, hooks-based"]

## Database

### [FILL IN: Primary Database]
- **Primary Database:** [FILL IN: e.g. "PostgreSQL", "MySQL", "MongoDB"]
- **Notes:** [FILL IN: key characteristics relevant to PM/engineering work]

## Infrastructure

### [FILL IN: Cloud Provider]
- **Cloud Provider:** [FILL IN: e.g. "AWS", "GCP", "Azure"]
- **Notes:** [FILL IN: key services used, e.g. "Lambda, S3, RDS, SQS"]
- **Relevant for:** Scalability assessments, deployment considerations, infrastructure costs

## Implications for PM Toolkit Workflows

### PRD Review (Engineer Perspective)
When reviewing PRDs for technical feasibility:
- [FILL IN: key consideration 1, e.g. "Consider which service/layer this feature touches"]
- [FILL IN: key consideration 2, e.g. "Assess database modeling requirements"]
- [FILL IN: key consideration 3, e.g. "Evaluate infrastructure needs (scaling, new services, costs)"]

### User Story Generation
When creating acceptance criteria and technical notes:
- **Frontend stories:** [FILL IN: e.g. "Assume React components with TypeScript"]
- **Backend stories:** [FILL IN: e.g. "Clarify if new service or extending existing"]
- **Database stories:** [FILL IN: e.g. "Note migration complexity"]
- **Infrastructure stories:** [FILL IN: e.g. "Specify AWS service requirements"]

### Technical Complexity Assessment

**Low Complexity:**
- [FILL IN: example, e.g. "Standard CRUD in existing service"]
- [FILL IN: example, e.g. "Simple UI component with existing patterns"]

**Medium Complexity:**
- [FILL IN: example, e.g. "New microservice creation"]
- [FILL IN: example, e.g. "Database migration with existing data"]

**High Complexity:**
- [FILL IN: example, e.g. "Cross-service integration"]
- [FILL IN: example, e.g. "Major schema changes"]
- [FILL IN: example, e.g. "Real-time features (WebSockets)"]

### Common Technical Considerations

**Backend:**
- [FILL IN: e.g. "API design: RESTful / GraphQL"]
- [FILL IN: e.g. "Background jobs: [job queue technology]"]
- [FILL IN: e.g. "Authentication: JWT, OAuth"]
- [FILL IN: e.g. "Caching: Redis"]

**Frontend:**
- [FILL IN: e.g. "State management: [Zustand / Redux / Pinia]"]
- [FILL IN: e.g. "Component library: [MUI / Ant Design / PrimeVue]"]
- [FILL IN: e.g. "Build tool: Vite"]

**Database:**
- [FILL IN: e.g. "Migrations: [migration tooling]"]
- [FILL IN: e.g. "Constraints: foreign keys, indexes"]

**Infrastructure:**
- [FILL IN: e.g. "Deployment: Docker / ECS / Kubernetes"]
- [FILL IN: e.g. "Monitoring: CloudWatch / Datadog"]
- [FILL IN: e.g. "Storage: S3"]

## When to Ask for Clarification

Even with this tech stack knowledge, always ask about:
- **Specific versions**, If version matters for compatibility
- **Existing patterns**, "How is X currently implemented?" before assuming
- **Performance requirements**, Database optimization, caching strategy
- **Third-party integrations**, External APIs, services, libraries
- **Migration complexity**, If changing existing functionality
- **Testing requirements**, Unit, integration, E2E expectations

## Integration with Operating Principles

Per Operating Principles (Principle #2: Information Source Priority):
1. Check product documentation for feature constraints
2. Check Jira tickets for existing implementations
3. Reference this tech stack for general capabilities
4. **Ask the user** for implementation specifics, patterns, or unknowns

**Never assume implementation details** beyond what's documented here.

---

**Last Updated:** [FILL IN: date]
**Source:** [FILL IN: your name / role]
