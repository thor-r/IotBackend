# Steps to Test the Audio Processing API


## Clone the repo
git clone https://github.com/thor-r/IotBackend.git
cd IotBackend

## Virtual enviromnent setup:

  1. create virtual env 
      - python3 -m venv venv
  2. activate virtual environment:
      - source venv/bin/activate  # For macOS/Linux
      - venv\Scripts\activate     # For Windows
  3. stop the virtual environment ---> deactivate

  (venv) (base) ➜  fidoBackend ---> virtual environmnent active.
  (base) ➜  fidoBackend ---> virtual environmnent not active.

## Dependencies

  • Run pip install -r requirements.txt to install the correct packages to your Python enviroment



# --- Automated Testing ---

## Run main.py:

	•	uvicorn app.main:app --reload  (This is run from the fidoBackend: project folder. (correct path from this location))

## Run integrated test

  •	From the project folder run ---> pytest -v tests/test_integration.py 

#### The automated test verifies this criteria:
	- Valid payloads with correctly encoded audio data are processed successfully.
	- Metadata is stored in the SQLite database with accurate audio length calculations.
	- The API returns appropriate error messages for invalid payloads (e.g., missing fields, invalid Base64 strings).



# --- Manual Testing --- 

## Create & Verify the DB

    1. Create DB Tables if no test.db file
     ---> python -m app.database

    2. Start the SQLite shell ---> sqlite3 test.db
      Show the tables in testDB ---> .tables
      Show the table structure ---> PRAGMA table_info(audio_metadata);
      # See all  the DB tables ---> SELECT * FROM audio_metadata;

## Run main.py:

	•	uvicorn app.main:app --reload  (This is run from the fidoBackend: project folder. (correct path from this location))

## Test using FastAPI UI

  #### Once the server is running, you can test the /process-audio endpoint:
      - Open your browser and go to http://127.0.0.1:8000/docs. 
      - Use the UI to send a POST request to /process-audio.

  ##### Example JSON payload:

    {
    "session_id": "session123",
    "timestamp": "2025-01-03T10:00:00Z",
    "audio_files": [
      {
        "file_name": "audio1.wav",
        "encoded_audio": "UklGRiYAAABXQVZFZmNkZWZnaGdpaWJl..."  // Replace with valid Base64 audio data
      }
    ]
    }

## Test using curl

  #### I have setup two sample json payloads complete with the encoded audio string run either or both to test it.

  1. curl -v -X 'POST' \
      'http://127.0.0.1:8000/process-audio' \
      -H 'Content-Type: application/json' \
      -d @request_payload.json

  2.  curl -v -X 'POST' \
      'http://127.0.0.1:8000/process-audio' \
      -H 'Content-Type: application/json' \
      -d @request_payload2.json

### Expected Responses

  ##### Success Example:
    {
      "status": "success",
      "processed_files": [
        {
          "file_name": "audio1.wav",
          "length_seconds": 2.5
        }
      ]
    }

  ##### Error Example:

    {
    "status": "error",
    "message": "Invalid audio data"
    }