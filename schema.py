from pydantic import BaseModel, EmailStr

# User Authentication
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True


# Task List
class  TaskCreate(BaseModel):
    taskHead: str
    taskBody: str
    tags: str
    status: str

class TaskResponse(TaskCreate):
    id: int
    
    class Config:
        from_attributes = True