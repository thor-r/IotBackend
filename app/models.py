from sqlalchemy import Column, Integer, String, Float
from app.base import Base  # Import Base from base.py
from datetime import datetime

class AudioMetadata(Base):  # Ensure it inherits from Base
    __tablename__ = "audio_metadata"

    id = Column(Integer, primary_key=True, autoincrement=True) 
    session_id = Column(String, index=True)
    timestamp = Column(String)
    file_name = Column(String)
    length_seconds = Column(Float)