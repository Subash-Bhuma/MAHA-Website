from pathlib import Path
import sys

from fastapi.testclient import TestClient

sys.path.append(str(Path(__file__).resolve().parents[1]))

from app.main import app

client = TestClient(app)


def test_create_publish_and_audit_challenge() -> None:
    payload = {
        "title": "Reduce irrigation-water loss in selected districts",
        "department": "Water Resources Department",
        "outcome": "Reduce irrigation-water loss by 15 percent in selected pilot districts.",
        "constraints": "Work within existing canal network and approved budget envelope.",
        "eligibility_summary": "DPIIT-recognized startup with relevant deployment evidence.",
    }
    create_response = client.post("/api/challenges", json=payload)
    assert create_response.status_code == 201
    created = create_response.json()
    assert created["status"] == "Draft"

    challenge_id = created["id"]
    publish_response = client.post(f"/api/challenges/{challenge_id}/publish")
    assert publish_response.status_code == 200
    assert publish_response.json()["status"] == "Published"

    audit_response = client.get(f"/api/challenges/{challenge_id}/audit")
    assert audit_response.status_code == 200
    actions = [event["action"] for event in audit_response.json()]
    assert actions == ["ChallengeCreated", "ChallengePublished"]
