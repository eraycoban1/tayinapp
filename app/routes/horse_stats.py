from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.horse_stats import HorseStats
from app.schemas.horse_stats_schema import HorseStatsCreate, HorseStatsResponse

router = APIRouter()

@router.post("/", response_model=HorseStatsResponse, status_code=status.HTTP_201_CREATED)
def create_horse_stats(horse_stat: HorseStatsCreate, db: Session = Depends(get_db)):
    new_stat = HorseStats(**horse_stat.dict())
    db.add(new_stat)
    db.commit()
    db.refresh(new_stat)
    return new_stat

@router.get("/", response_model=List[HorseStatsResponse])
def get_all_stats(db: Session = Depends(get_db)):
    stats = db.query(HorseStats).all()
    return stats
