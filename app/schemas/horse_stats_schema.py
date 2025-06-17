from pydantic import BaseModel
from datetime import date

class HorseStatsCreate(BaseModel):
    horse_name: str
    race_date: date
    race_class: str
    distance: int
    rank: int
    jockey: str
    trainer: str
    weight: float
    track_condition: str
    handicap_point: int
    earnings: float
    form_last_5: str
    avg_rank_last_5: float
    speed_index: float
    win_ratio_last_5: float

class HorseStatsResponse(HorseStatsCreate):
    id: int

    class Config:
        orm_mode = True
