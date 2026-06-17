from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import SensorData


router = APIRouter(prefix="/sensors", tags=["Sensors"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/data")
def add_data(temp: float, humidity: float, soil: float, db: Session = Depends(get_db)):
    data = SensorData(temperature=temp, humidity=humidity, soil_moisture=soil)
    db.add(data)
    db.commit()
    return {"status": "data stored"}

@router.get("/data")
def get_data(db: Session = Depends(get_db)):
return db.query(SensorData).all()