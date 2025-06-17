from fastapi import APIRouter
from app.schemas.horse_stats_predict import HorseStatInput
from app.services.predict import predict_ranking

router = APIRouter()

@router.post("/")
def predict(data: HorseStatInput):
    return {"tahmin": predict_ranking(data)}
