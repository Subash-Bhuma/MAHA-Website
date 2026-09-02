from datetime import datetime
from enum import Enum
from typing import List

from pydantic import BaseModel, Field


class ChallengeStatus(str, Enum):
    DRAFT = "Draft"
    PUBLISHED = "Published"
    OPEN = "Open"
    UNDER_REVIEW = "Under Review"
    CLOSED = "Closed"
    ARCHIVED = "Archived"


class ChallengeCreate(BaseModel):
    title: str = Field(min_length=3, max_length=200)
    department: str = Field(min_length=2, max_length=150)
    outcome: str = Field(min_length=10, max_length=2000)
    constraints: str = Field(min_length=3, max_length=2000)
    eligibility_summary: str = Field(min_length=3, max_length=1000)


class Challenge(BaseModel):
    id: int
    title: str
    department: str
    outcome: str
    constraints: str
    eligibility_summary: str
    status: ChallengeStatus
    created_at: datetime
    updated_at: datetime


class AuditEvent(BaseModel):
    id: int
    entity_type: str
    entity_id: int
    action: str
    actor_role: str
    timestamp: datetime
    details: str


class ChallengeListResponse(BaseModel):
    items: List[Challenge]
