from fastapi import FastAPI
from backend.database import engine
from backend.models import Base
from backend.routes import auth_routes, sensor_routes

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Smart Agriculture API")

app.include_router(auth_routes.router)
app.include_router(sensor_routes.router)
@app.post("/ai/recommend")
def recommend_crop(
    temperature: float,
    humidity: float,
    soil_moisture: float
):
    if soil_moisture > 70:
        crop = "Rice"
    elif temperature > 30:
        crop = "Millet"
    elif humidity > 60:
        crop = "Maize"
    else:
        crop = "Wheat"

    return {"recommended_crop": crop}