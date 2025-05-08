import redis
import json

redis_client = redis.Redis(host='localhost', port=6379, db=0)

def get_cached_tasks():
    cached = redis_client.get("tasks")
    if cached:
        return json.loads(cached)
    return None

def set_cached_tasks(tasks):
    redis_client.set("tasks", json.dumps(tasks), ex=60)  