from sqlalchemy import Column, Integer, String, Float, Date
from app.database import Base

class HorseStats(Base):
    __tablename__ = "horse_stats"
    id = Column(Integer, primary_key=True, index=True)
    horse_name = Column(String, index=True)
    race_date = Column(Date)
    race_class = Column(String)
    distance = Column(Integer)
    rank = Column(Integer)
    jockey = Column(String)
    trainer = Column(String)
    weight = Column(Float)
    track_condition = Column(String)
    handicap_point = Column(Integer)
    earnings = Column(Float)
    form_last_5 = Column(String)
    avg_rank_last_5 = Column(Float)
    speed_index = Column(Float)
    win_ratio_last_5 = Column(Float)
