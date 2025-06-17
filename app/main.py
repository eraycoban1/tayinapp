from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.security import OAuth2PasswordBearer
from app.routes import user as user_routes
from app.routes import horse as horse_routes
from app.routes import horse_stats as horse_stats_routes
from app.routes import predict as predict_routes

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

# ✅ Swagger için JWT Authorize butonu (Burası önemli)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

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
    for path in openapi_schema["paths"]:
        for method in openapi_schema["paths"][path]:
            openapi_schema["paths"][path][method]["security"] = [{"BearerAuth": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi
