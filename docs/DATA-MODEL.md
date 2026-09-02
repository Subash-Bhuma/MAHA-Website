# MAHA Data Model

## Core Entities
- User
- Role
- Permission
- GovernmentDepartment
- Startup
- StartupDocument
- StartupCertification
- StartupSector
- Challenge
- ChallengeRequirement
- ChallengeKPI
- ChallengeDocument
- Application
- EligibilityCheck
- Evaluation
- EvaluationScore
- EvaluationComment
- Pilot
- PilotMilestone
- PilotKPI
- PilotEvidence
- PilotDocument
- ProcurementHandoff
- Recommendation
- PolicyRule
- PolicySource
- AuditEvent
- Notification
- Document
- DataSource

## Implemented Subset

### Challenge
- `id`
- `title`
- `department`
- `outcome`
- `constraints`
- `eligibility_summary`
- `status`
- `created_at`
- `updated_at`

### AuditEvent
- `id`
- `entity_type`
- `entity_id`
- `action`
- `actor_role`
- `timestamp`
- `details`

## Notes
- Production persistence target is PostgreSQL.
- Semantic matching metadata and embeddings should use pgvector-enabled structures in later modules.
