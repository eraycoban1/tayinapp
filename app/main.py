from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from app.database import Base, engine
from app.models import user, horse, horse_stats
from app.routes import user as user_routes
from app.routes import horse as horse_routes
from app.routes import horse_stats as horse_stats_routes
from app.routes import predict as predict_routes

# Veritabanı tablolarını oluştur
Base.metadata.create_all(bind=engine)

# Uygulama tanımı
app = FastAPI(
    title="Tayin",
    description="Yarış atı tahmin API'si",
    version="1.0.0"
)

# Router'ları ekle
app.include_router(user_routes.router, prefix="/users", tags=["Kullanıcılar"])
app.include_router(horse_routes.router, prefix="/horses", tags=["Atlar"])
app.include_router(horse_stats_routes.router, prefix="/horse-stats", tags=["İstatistik"])
app.include_router(predict_routes.router, tags=["Tahmin"])

# Ana test endpoint
@app.get("/")
def root():
    return {"message": "🚀 AtIntel API is running!"}

# Swagger için JWT Authorize butonu
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Tayin",
        version="1.0.0",
        description="Yarış atı tahmin API'si",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method["security"] = [{"BearerAuth": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi
