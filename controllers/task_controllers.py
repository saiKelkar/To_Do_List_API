from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models import Task
from .. import schema

def get_all_tasks(db: Session):
    return db.query(Task).all()

def get_task_by_id(id: int, db: Session):
    task = db.query(Task).filter(Task.id == id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task with ID {id} not found")
    return task

def get_task_by_status(status: str, db: Session):
    task = db.query(Task).filter(Task.status == status).all()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task with status {status} not found")
    return task

def create_task(task_data: schema.TaskCreate, db: Session):
    new_task = Task(
        taskHead = task_data.taskHead,
        taskBody = task_data.taskBody,
        tags = task_data.tags,
        status = task_data.status
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def update_task(id: int, task_data: schema.TaskCreate, db: Session):
    task = db.query(Task).filter(Task.id == id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task with ID {id} not found")
    task.taskHead = task_data.taskHead
    task.taskBody = task_data.taskBody
    task.tags = task_data.tags
    task.status = task_data.status

    db.commit()
    db.refresh(task)
    return task

def delete_task(id: int, db: Session):
    task = db.query(Task).filter(Task.id == id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task with ID {id} not found")
    db.delete(task)
    db.commit()
    return { "message": f"Task with ID {id} deleted successfully" }