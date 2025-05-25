# Rotas FastAPI e chamadas aos serviços

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database_config import SessionLocal
from services import create_task_service, get_tasks_service, update_task_service, delete_task_service
from utils import task_to_dict

app = FastAPI()

# Modelos Pydantic para validação
class TaskCreate(BaseModel):
    title: str
    description: str

class TaskUpdate(BaseModel):
    title: str
    description: str
    completed: bool

# Dependência para obter a sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/tasks")
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    return create_task_service(db, task.title, task.description)

@app.get("/tasks")
def read_tasks(db: Session = Depends(get_db)):
    return get_tasks_service(db)

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskUpdate, db: Session = Depends(get_db)):
    updated_task = update_task_service(db, task_id, task.title, task.description, task.completed)
    if updated_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    deleted_task = delete_task_service(db, task_id)
    if deleted_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted"}