# MAHA Product Blueprint

## Product Identity
- **Product:** MAHA (Maharashtra Startup & Innovation Procurement Portal)
- **Team:** AXIOM
- **Problem Statement:** SIH26136
- **Purpose:** Structured digital workflow connecting government challenges with startup innovation from discovery to procurement handoff.

## Positioning Guardrails
- MAHA **does not replace** GeM or existing procurement mechanisms.
- MAHA **does not bypass** procurement law, approvals, or tender rules.
- MAHA **does not autonomously select vendors**.
- AI is assistive only; final decisions remain with authorised government officials.

## Public Portal Information Architecture
1. Home
2. Government Challenges
3. Startups
4. Startup Opportunities
5. Maharashtra Startup / Innovation Programs
6. How MAHA Works
7. Resources / Policies
8. Login
9. About MAHA

## Core Workflow
Problem → Discover → Verify → Evaluate → Pilot → Measure → Evidence → Procurement Handoff → Scale

Each stage records: owner, status, timestamp, documents, comments, and audit events.

## MVP Scope (Phase 1)
1. Government login
2. Government dashboard
3. Create challenge
4. Published challenge page
5. Startup directory
6. Startup profile
7. Application submission
8. Eligibility checklist
9. Evaluation workspace
10. Pilot creation
11. Pilot milestone/KPI tracking
12. Evidence workspace
13. Procurement handoff page
14. Audit timeline

## Prototype Status in This Repository
This repository currently provides:
- Government-style **public portal prototype** (static HTML/CSS) with the required public sections.
- Backend **vertical slice** for challenge creation/publication and audit events using FastAPI.
- Documentation for architecture, security, workflows, design system, and data model.
