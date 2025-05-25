# Operações CRUD no banco de dados

from sqlalchemy.orm import Session
from models import Task

def create_task(db: Session, title: str, description: str):
    """Cria uma nova tarefa no banco de dados"""
    task = Task(title=title, description=description)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def get_tasks(db: Session):
    """Retorna todas as tarefas do banco de dados"""
    return db.query(Task).all()

def update_task(db: Session, task_id: int, title: str, description: str, completed: bool):
    """Atualiza uma tarefa existente"""
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        task.title = title
        task.description = description
        task.completed = completed
        db.commit()
        db.refresh(task)
    return task

def delete_task(db: Session, task_id: int):
    """Exclui uma tarefa pelo ID"""
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
    return task