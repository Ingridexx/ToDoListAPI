# Regras de negócio

from repositories import create_task, get_tasks, update_task, delete_task
from sqlalchemy.orm import Session
from cache import get_cached_tasks, set_cached_tasks 
from utils import task_to_dict

def create_task_service(db: Session, title: str, description: str):
    """Cria uma nova tarefa validando o titulo"""
    if not title:
        raise ValueError("Title is required")
    return create_task(db, title, description)

def get_tasks_service(db: Session):
    """Retorna a lista de tarefas, usando cache se disponivel"""
    cached_tasks = get_cached_tasks()
    if cached_tasks:
        return cached_tasks
    tasks = get_tasks(db)
    tasks_dict = [task_to_dict(task) for task in tasks]
    set_cached_tasks(tasks_dict)
    return tasks_dict

def update_task_service(db: Session, task_id: int, title: str, description: str, completed: bool):
    """Atualiza uma tarefa existente"""
    return update_task(db, task_id, title, description, completed)

def delete_task_service(db: Session, task_id: int):
    """exclui uma tarefa pelo ID"""
    return delete_task(db, task_id)
