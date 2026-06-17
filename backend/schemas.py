from pydantic import BaseModel
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
    
class SensorCreate(BaseModel):
    temperature: float
    humidity: float
    soil_moisture: float

class SensorOut(SensorCreate):
    id: int
    created_at: datetime