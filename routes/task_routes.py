from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schema, database
from ..controllers import task_controllers

router = APIRouter(prefix="/tasks", tags=["Tasks"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schema.TaskResponse])
def getTask(db: Session = Depends(get_db)):
    return task_controllers.get_all_tasks(db)

@router.get("/{id}", response_model=schema.TaskResponse)
def getTaskById(id: int, db: Session = Depends(get_db)):
    return task_controllers.get_task_by_id(id, db)

@router.get("/status/{status}", response_model=list[schema.TaskResponse])
def getTaskByStatus(status: str, db: Session = Depends(get_db)):
    return task_controllers.get_task_by_status(status, db)

@router.post("/", response_model=schema.TaskResponse)
def createTask(task: schema.TaskCreate, db: Session = Depends(get_db)):
    return task_controllers.create_task(task, db)

@router.put("/{id}", response_model=schema.TaskResponse)
def updateTask(id: int, task: schema.TaskCreate, db: Session = Depends(get_db)):
    return task_controllers.update_task(id, task, db)

@router.delete("/{id}")
def deleteTask(id: int, db: Session = Depends(get_db)):
    return task_controllers.delete_task(id, db)