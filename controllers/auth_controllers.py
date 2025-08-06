from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from .. import schema, models
from ..utils.hashing import hash_password, verify_password

def signup(request: schema.UserCreate, db: Session):
    user = db.query(models.User).filter(models.User.email == request.email).first()
    if user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    
    new_user = models.User(name=request.name, email=request.email, password=hash_password(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def login(request: schema.UserLogin, db: Session):
    user = db.query(models.User).filter(models.User.email == request.email).first()
    if not user or not verify_password(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return user

def logout(request: schema.UserResponse, db: Session):
    return { "message": "Logout successful" }