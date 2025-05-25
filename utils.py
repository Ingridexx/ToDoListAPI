# Funções utilitarias (ex: to_dict)

def task_to_dict(task):
    """Converte um objeto Task em um dicionário serializável."""
    return {
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "completed": task.completed
    }