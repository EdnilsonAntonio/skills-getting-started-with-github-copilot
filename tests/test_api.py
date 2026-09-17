from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_successful_signup_adds_participant_to_activity():
    # Arrange
    activity = "Chess Club"
    email = "newstudent@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 200
    assert email in client.get("/activities").json()[activity]["participants"]


def test_unregister_participant_removes_email_from_activity():
    # Arrange
    activity = "Chess Club"
    email = "newstudent@mergington.edu"
    client.post(f"/activities/{activity}/signup?email={email}")

    # Act
    response = client.delete(f"/activities/{activity}/participants/{email}")

    # Assert
    assert response.status_code == 200
    assert email not in client.get("/activities").json()[activity]["participants"]
