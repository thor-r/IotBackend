import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_process_audio():
    # Example payload for testing
    payload = {
        "session_id": "session123",
        "timestamp": "2025-01-03T10:00:00Z",
        "audio_files": [
            {
                "file_name": "audio1.wav",
                "encoded_audio": "UklGRiYAAABXQVZFZmNkZWZnaGdpaWJl... (Base64 encoded audio data)"
            }
        ]
    }
    
    response = client.post("/process-audio", json=payload)
    assert response.status_code == 200
    assert response.json() == {
        "status": "success",
        "processed_files": [
            {"file_name": "audio1.wav", "length_seconds": 2.5}
        ]
    }
