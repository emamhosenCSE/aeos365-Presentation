# aeos365 Viva Cheat Sheet (One Page)

## 1) 60-Second Opening Script
- **Project**: aeos365 is a modular enterprise platform designed for SMEs and growing organizations.
- **Core value**: one codebase, two deployment modes (**SaaS multi-tenant** + **standalone single-tenant**).
- **Technical edge**: package-based architecture, four-level RBAC, tenant data isolation, API-first design.
- **Current status**: MVP stage with validated core scenarios (onboarding, RBAC enforcement, tenant isolation).

## 2) Final Slide Order — What to Emphasize
- **Slides 1–2 (Cover + Abstract)**: Problem-solution framing and why this matters for SMEs.
- **Slides 3–4 (Challenges)**: Structural and operational pain points in existing ERP ecosystems.
- **Slides 5–6 (Objectives)**: Primary goals (architecture/security/deployment) and secondary goals (scalability/API/compliance).
- **Slides 7–8 (Architecture + Deployment Modes)**: Layered system design and dual deployment strategy.
- **Slides 9–12 (Pricing + Modules)**: Product model and modular business capabilities.
- **Slides 13–14 (RBAC + Multi-tenancy)**: Security and isolation foundation.
- **Slides 15–18 (Stack + Features + Method + Timeline)**: Implementation choices, engineering process, and execution plan.
- **Slide 19 (Validation & Results)**: What has been validated today.
- **Slide 20 (Outcomes & Significance)**: Academic, industry, and social impact.
- **Slide 21 (Comparison)**: Where aeos365 is differentiated.
- **Slide 22 (Risks/Limitations/Future Work)**: Realistic scope control and roadmap.
- **Slides 23–24 (Team + Thank You)**: Ownership, closure, and Q&A.

## 3) Top 10 Likely Viva Questions + Short Answers
1. **Why build aeos365 instead of using existing ERP solutions?**  
   Existing tools often force trade-offs between cost, flexibility, and deployment control. aeos365 targets that gap with modular adoption and dual deployment.

2. **What is the main innovation in your project?**  
   The combination of one codebase with dual deployment modes plus four-level RBAC and tenant isolation as first-class architecture decisions.

3. **How is your multi-tenancy secured?**  
   Tenant context is resolved at request level, data is isolated per tenant, and RBAC checks enforce least-privilege access across all UI/actions.

4. **Why four-level RBAC?**  
   It gives precise access control at module, submodule, component, and action levels, avoiding over-permission and improving auditability.

5. **What has been implemented vs planned?**  
   Implemented: core architecture, onboarding, RBAC enforcement flow, tenant isolation validation, core module prototypes. Planned: broader module completion, scale hardening, deeper integrations.

6. **How do you ensure code quality?**  
   Modular package boundaries, test coverage on critical flows, version control discipline, review workflow, and reproducible deployment runbooks.

7. **How is this scalable?**  
   Modular services, queue/caching support, tenant isolation strategy, and phased load/performance validation roadmap.

8. **What are your biggest limitations right now?**  
   Not all planned modules are feature-complete and large-scale benchmark testing is still in progress.

9. **What is your commercialization approach?**  
   Tiered standalone pricing plus SaaS plans with modular add-ons, allowing incremental adoption based on organization maturity.

10. **If given 3 more months, what would you ship next?**  
    Complete module MVP coverage, expand automated tests/observability, and run pilot deployments with real organizations.

## 4) Defensive Q&A Lines (Use When Challenged)
- **On numeric claims**: “These are proposal-stage benchmark ranges; final defense appendix includes source-backed references.”
- **On scope**: “We intentionally prioritized architecture correctness and security-critical workflows over breadth-first module completion.”
- **On AI feature maturity**: “AI is integrated with guardrails and auditability, and we treat model behavior as an evolving subsystem.”

## 5) 30-Second Closing Script
- aeos365 demonstrates a practical path to affordable enterprise capability for SMEs.
- We validated the core architecture, deployment flexibility, and access-control foundation.
- The roadmap is clear: expand module coverage, strengthen performance validation, and move to pilot deployments.
