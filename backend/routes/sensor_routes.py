from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.database import SessionLocal
from backend.models import SensorData
from backend.schemas import SensorCreate

router = APIRouter(prefix="/sensors", tags=["Sensors"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def add_sensor(data: SensorCreate, db: Session = Depends(get_db)):
    record = SensorData(**data.dict())
    db.add(record)
    db.commit()
    return {"message": "Sensor data added"}


@router.get("/")
def get_all(db: Session = Depends(get_db)):
    return db.query(SensorData).all()