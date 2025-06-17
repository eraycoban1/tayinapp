from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.horse import Horse
from app.schemas.horse import HorseCreate, HorseResponse

router = APIRouter()

@router.post("/horses", response_model=HorseResponse)
def create_horse(horse: HorseCreate, db: Session = Depends(get_db)):
    existing = db.query(Horse).filter(Horse.name == horse.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Bu at zaten var.")
    new_horse = Horse(**horse.dict())
    db.add(new_horse)
    db.commit()
    db.refresh(new_horse)
    return new_horse

@router.get("/horses", response_model=List[HorseResponse])
def list_horses(db: Session = Depends(get_db)):
    return db.query(Horse).all()
