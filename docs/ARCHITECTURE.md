# MAHA Architecture

## Architecture Goals
- Government-grade traceability
- Role-based secure operations
- Clear separation of public information and authenticated workflows
- Assistive AI with explainability and human control

## Target Stack
- **Frontend:** Next.js + React + TypeScript + Tailwind CSS
- **Backend:** FastAPI (Python)
- **Database:** PostgreSQL + pgvector
- **Queue/Cache:** Redis
- **Storage:** S3-compatible object storage

## Layered Design
1. **Public Portal Layer**
   - Information pages, challenge browsing, startup opportunities, policy/resources.
2. **Authenticated Workflow Layer**
   - Role-based modules for officers, startups, evaluators, administrators.
3. **Domain/API Layer**
   - Challenge lifecycle, application, evaluation, pilot, evidence, procurement handoff.
4. **Policy & Rules Layer**
   - Configurable rule registry with source and jurisdiction metadata.
5. **Audit & Observability Layer**
   - Append-only audit timeline, structured logs, metrics, health checks.

## Current Vertical Slice (Implemented)
- Create challenge (`Draft`)
- Publish challenge (`Published`)
- List challenges
- Retrieve challenge
- Retrieve challenge audit timeline

This vertical slice validates:
- explicit status model
- timestamped decision history
- auditability-first design
