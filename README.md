# Project Documentation

## File Roles
- **`database.py`**: Handles database setup and connections.
- **`models.py`**: Defines the schema for the database.
- **`main.py`**: Implements the FastAPI application and business logic.
- **`schemas.py`**: Ensures request/response data validation.
- **`tests/`**: Contains test cases to validate the application’s functionality.


## Dependencies

Run pip install -r requirements.txt to install the correct packages to your Python enviroment

## Virtual enviromnent setup:

  activate virtual environment ---> source venv/bin/activate 
  stop the virtual environment ---> deactivate

  (venv) (base) ➜  fidoBackend ---> virtual environmnent active.
  (base) ➜  fidoBackend ---> virtual environmnent not active.


## Run the code:

uvicorn app.main:app --reload ---> to run main.py

	•	This is run from the fidoBackend: project folder. (correct path from this location)
	•	app: This is the subfolder containing the FastAPI app.
	•	main: This is the Python file where the FastAPI app is initialized (main.py).
	•	app: This is the FastAPI instance created in main.py (i.e., app = FastAPI()).

# Generating Dummy Audio:

In project root ---> python generate_audio.py 

Returns: 
  AACWUbp9KXAeL3PY7pMEgWKo9/c7S/l70HN/Nizgc5hCgLKi9u+VRLt5AXepPQXoYZ0BgGGdBeipPQF3u3mVRPbvsqJCgHOYLOB/

 # Test the Endpoint

Once the server is running, you can test the /process-audio endpoint:
	•	Open your browser and go to http://127.0.0.1:8000/docs. FastAPI automatically generates interactive API documentation with Swagger UI.
	•	Use the UI to send a POST request to /process-audio with an audio file or raw data.


## Create & Verify the DB

    1. Create DB Tables if no test.db file
     ---> python -m app.database <---

    2. Start the SQLite shell ---> sqlite3 test.db
      Show the tables in testDB ---> .tables
      Show the table structure ---> PRAGMA table_info(audio_metadata);
      # See all  the DB tables ---> SELECT * FROM audio_metadata;

## Run all tests 
  ---> pytest

## Convert an audiofile to base64 for testing:

  bash terminal decode --> base64 -i path/to/your/audio.wav
  decode and send results to a file ---> base64 -i path/to/your/audio.wav > encoded_audio.txt

    EXAMPLE = base64 -i /Users/thor/Downloads/test.wav > encoded_audio.txt

## Testing the endpoint with CURL 
  
  ### Option 1: Direct Payload

      curl -X 'POST' \
      'http://127.0.0.1:8000/process-audio' \
      -H 'Content-Type: application/json' \
      -d '{
        "session_id": "12345",
        "timestamp": "2025-01-05T16:00:00Z",
        "audio_files": [
          {
            "file_name": "test.wav",
            "encoded_audio": "PASTE_BASE64_ENCODED_STRING_HERE"
          }
        ]
      }'

  ### Option 2: JSON File Payload
  
      curl -v -X 'POST' \
      'http://127.0.0.1:8000/process-audio' \
      -H 'Content-Type: application/json' \
      -d @request_payload.json

  
## Testing the API:
    Once you’ve sent the request using one of the methods above, the FastAPI server should process the audio file, validate it, and return a response. If everything works correctly, the response should look something like this:

        {
          "status": "success",
          "processed_files": [
            {
              "file_name": "audio1.wav",
              "length_seconds": 5.0
            }
          ]
        }

    If there is an error, you’ll get an error message in the response like this:

    {
      "status": "error",
      "message": "Error processing file audio1.wav: Invalid Base64 encoding"
    }
