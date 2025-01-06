import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def read_base64_from_file(file_path):
    with open(file_path, 'r') as f:
        return f.read().strip()  # extra whitespace removed

def test_process_audio():
    # Read the Base64 string from the file
    base64_audio = read_base64_from_file("encoded_audio2.txt")
    
    # Test payload
    payload = {
        "session_id": "session123",
        "timestamp": "2025-01-03T10:00:00Z",
        "audio_files": [
            {
                "file_name": "audio1.wav",
                "encoded_audio": base64_audio
            }
        ]
    }
    
    response = client.post("/process-audio", json=payload)

    print(response.json()) 
    
    # Assert the response - must know the expected time of test audio
    assert response.status_code == 200
    assert response.json().items() == {
        "status": "success",
        "processed_files": [
            {"file_name": "audio1.wav", "length_seconds": 16.543} 
        ]
    }.items()