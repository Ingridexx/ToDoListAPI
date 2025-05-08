from repositories import create_task, get_tasks, update_task, delete_task
from sqlalchemy.orm import Session
from cache import get_cached_tasks, set_cached_tasks  # Note o plural

def create_task_service(db: Session, title: str, description: str):
    if not title:
        raise ValueError("Title is required")
    return create_task(db, title, description)

def get_tasks_service(db: Session):
    cached_tasks = get_cached_tasks()
    if cached_tasks:
        return cached_tasks
    tasks = get_tasks(db)
    # Use to_dict para serializar as tarefas
    tasks_dict = [task.to_dict() for task in tasks]
    set_cached_tasks(tasks_dict)
    return tasks_dict

def update_task_service(db: Session, task_id: int, title: str, description: str, completed: bool):
    return update_task(db, task_id, title, description, completed)

def delete_task_service(db: Session, task_id: int):
    return delete_task(db, task_id)