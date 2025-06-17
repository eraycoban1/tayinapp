from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import user as user_model
from app.schemas import user as user_schema
from app.utils.auth import hash_password, verify_password
from app.utils.jwt import create_access_token

router = APIRouter()

@router.post("/register")
def register(request: user_schema.UserCreate, db: Session = Depends(get_db)):
    user_exists = db.query(user_model.User).filter(user_model.User.username == request.username).first()
    if user_exists:
        raise HTTPException(status_code=400, detail="Kullanıcı adı zaten var")

    password_hash = hash_password(request.password)
    new_user = user_model.User(
        username=request.username,
        email=request.email,
        password=password_hash
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "Kayıt başarılı"}

@router.post("/login")
def login(request: user_schema.UserLogin, db: Session = Depends(get_db)):
    user = db.query(user_model.User).filter(user_model.User.username == request.username).first()
    if not user or not verify_password(request.password, user.password):
        raise HTTPException(status_code=401, detail="Geçersiz kullanıcı adı veya şifre")

    token = create_access_token(data={"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}
