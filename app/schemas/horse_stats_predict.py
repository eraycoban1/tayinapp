from pydantic import BaseModel
from datetime import date

class HorseStatInput(BaseModel):
    distance: int
    rank: int
    jockey: str
    trainer: str
    weight: float
    track_condition: str
    handicap_point: int
    earnings: float
    avg_rank_last_5: float
    speed_index: float
    win_ratio_last_5: float
