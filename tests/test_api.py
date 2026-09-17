from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_unregister_participant_removes_email_from_activity():
    activity = "Chess Club"
    email = "newstudent@mergington.edu"

    client.post(f"/activities/{activity}/signup?email={email}")

    response = client.delete(f"/activities/{activity}/participants/{email}")

    assert response.status_code == 200
    assert email not in client.get("/activities").json()[activity]["participants"]
