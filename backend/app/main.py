from datetime import datetime, timezone
from typing import Dict, List

from fastapi import FastAPI, HTTPException

from .schemas import AuditEvent, Challenge, ChallengeCreate, ChallengeListResponse, ChallengeStatus

app = FastAPI(title="MAHA API", version="0.1.0")

_challenge_id = 0
_audit_id = 0
_challenges: Dict[int, Challenge] = {}
_audit_events: Dict[int, List[AuditEvent]] = {}


def _now() -> datetime:
    return datetime.now(timezone.utc)


def _create_audit_event(entity_id: int, action: str, details: str) -> AuditEvent:
    global _audit_id
    _audit_id += 1
    return AuditEvent(
        id=_audit_id,
        entity_type="Challenge",
        entity_id=entity_id,
        action=action,
        actor_role="GovernmentOfficer",
        timestamp=_now(),
        details=details,
    )


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/api/challenges", response_model=Challenge, status_code=201)
def create_challenge(payload: ChallengeCreate) -> Challenge:
    global _challenge_id
    _challenge_id += 1
    timestamp = _now()
    challenge = Challenge(
        id=_challenge_id,
        title=payload.title.strip(),
        department=payload.department.strip(),
        outcome=payload.outcome.strip(),
        constraints=payload.constraints.strip(),
        eligibility_summary=payload.eligibility_summary.strip(),
        status=ChallengeStatus.DRAFT,
        created_at=timestamp,
        updated_at=timestamp,
    )
    _challenges[challenge.id] = challenge
    _audit_events[challenge.id] = [
        _create_audit_event(challenge.id, "ChallengeCreated", "Challenge created in Draft state")
    ]
    return challenge


@app.get("/api/challenges", response_model=ChallengeListResponse)
def list_challenges() -> ChallengeListResponse:
    return ChallengeListResponse(items=list(_challenges.values()))


@app.get("/api/challenges/{challenge_id}", response_model=Challenge)
def get_challenge(challenge_id: int) -> Challenge:
    challenge = _challenges.get(challenge_id)
    if challenge is None:
        raise HTTPException(status_code=404, detail="Challenge not found")
    return challenge


@app.post("/api/challenges/{challenge_id}/publish", response_model=Challenge)
def publish_challenge(challenge_id: int) -> Challenge:
    challenge = _challenges.get(challenge_id)
    if challenge is None:
        raise HTTPException(status_code=404, detail="Challenge not found")
    if challenge.status != ChallengeStatus.DRAFT:
        raise HTTPException(status_code=409, detail="Only Draft challenges can be published")

    updated = challenge.model_copy(
        update={
            "status": ChallengeStatus.PUBLISHED,
            "updated_at": _now(),
        }
    )
    _challenges[challenge_id] = updated
    _audit_events[challenge_id].append(
        _create_audit_event(challenge_id, "ChallengePublished", "Challenge moved from Draft to Published")
    )
    return updated


@app.get("/api/challenges/{challenge_id}/audit", response_model=List[AuditEvent])
def challenge_audit_timeline(challenge_id: int) -> List[AuditEvent]:
    if challenge_id not in _challenges:
        raise HTTPException(status_code=404, detail="Challenge not found")
    return _audit_events.get(challenge_id, [])
