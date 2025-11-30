from fastapi.testclient import TestClient
import api
from database import add_note_to_db


def test_api_get_notes(db_session, monkeypatch):
    monkeypatch.setattr(api, "get_all_notes", lambda db=db_session: [add_note_to_db("x", db=db)])

    client = TestClient(api.app)
    response = client.get("/notes")

    assert response.status_code == 200