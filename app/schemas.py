from pydantic import BaseModel, Field, field_validator
from typing import List, Optional
from datetime import datetime
import base64
import numpy as np

# Schema for the individual audio file metadata
class AudioFile(BaseModel):
    file_name: str
    encoded_audio: str

    # Validator for encoded_audio to check if it's valid Base64
    @classmethod
    def validate_base64(cls, encoded_audio: str):
        try:
            base64.b64decode(encoded_audio)
            return encoded_audio
        except Exception:
            raise ValueError("Invalid Base64 encoding")

    # Validator for audio length after decoding the Base64 audio data
    @field_validator('encoded_audio')
    def validate_audio_length(cls, encoded_audio: str):
        # Decode the Base64 audio data
        decoded_audio = base64.b64decode(encoded_audio)
        # Convert the decoded audio data to a numpy array (int16 dtype)
        audio_data = np.frombuffer(decoded_audio, dtype=np.int16)
        
        # Check for length of the audio data
        if len(audio_data) == 0:
            raise ValueError("Audio file is empty or has no valid data")
        
        # minimum length of audio data required (1 second)
        min_length_samples = 4000  # 1 second at 4000 Hz sampling rate
        if len(audio_data) < min_length_samples:
            raise ValueError(f"Audio file is too short. Minimum length is {min_length_samples / 4000} seconds.")
        
        return encoded_audio

    # Custom validation for Base64 encoding
    @classmethod
    def __get_validators__(cls):
        yield cls.validate_base64
        yield cls.validate_audio_length

# Schema for request payload
class ProcessAudioRequest(BaseModel):
    session_id: str
    timestamp: datetime
    audio_files: List[AudioFile]

    class ConfigDict:
        # datetime is parsed correctly from ISO-8601 strings
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }

# Schema for response payload
class ProcessAudioResponse(BaseModel):
    status: str
    processed_files: Optional[List[dict]] = None
