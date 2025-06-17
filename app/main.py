from fastapi import FastAPI
from app.database import Base, engine
from app.models import user, horse, horse_stats
from app.routes import user as user_routes
from app.routes import horse as horse_routes
from app.routes import predict as predict_routes
from app.routes import horse_stats as horse_stats_routes

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Tayin",
    description="Yarış atı tahmin API'si",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "🚀 Tayin API is running!"}

app.include_router(user_routes.router, prefix="/users", tags=["Kullanıcılar"])
app.include_router(horse_routes.router, prefix="/horses", tags=["Atlar"])
app.include_router(predict_routes.router, prefix="/predict", tags=["Tahmin"])
app.include_router(horse_stats_routes.router, prefix="/horse-stats", tags=["İstatistik"])

from app.routes import horse_stats as horse_stats_routes
app.include_router(horse_stats_routes.router, prefix="/horse-stats", tags=["İstatistik"])
