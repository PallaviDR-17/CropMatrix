from fastapi import APIRouter


router = APIRouter(prefix="/irrigation", tags=["Irrigation"])


@router.get("/status")
def irrigation_status(soil: float):
    if soil < 30:
        return {"irrigation": "ON"}
    return {"irrigation": "OFF"}