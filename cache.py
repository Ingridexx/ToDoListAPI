# Funções de cache com Redis

import redis
import json

redis_client = redis.Redis(host='localhost', port=6379, db=0)

def get_cached_tasks():
    """recupera a lista de tarefas do cache Redis"""
    cached = redis_client.get("tasks")
    if cached:
        return json.loads(cached)
    return None

def set_cached_tasks(tasks):
    """Armazena a lista de tarefas no cache Redis  com expira;'ao de 60 segundos"""
    redis_client.set("tasks", json.dumps(tasks), ex=60)  