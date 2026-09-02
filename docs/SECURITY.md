# MAHA Security

## Security Baseline
- Server-side role-based access control (RBAC)
- Least-privilege authorization
- Input validation and schema checks
- Protected document access by role and ownership
- Audit event logging for material state changes
- Secure session/token handling with OIDC/OAuth integration
- Encryption in transit for all traffic

## Prototype Controls in Current Vertical Slice
- Request payload validation via Pydantic models
- Enumerated status transitions for challenge publication
- Immutable audit event creation on create/publish actions
- No secrets or API keys embedded in frontend assets

## Production Controls (Planned)
- Rate limiting for public and authenticated APIs
- Secure file upload scanning and metadata checks
- Object-storage signed URL access control
- Structured security event logging and alerting
- Dependency and container vulnerability checks in CI
