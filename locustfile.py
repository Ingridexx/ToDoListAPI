# Script de teste de carga com Locust

from locust import HttpUser, task, between

class APIUser(HttpUser):
    wait_time = between(1,5) # Intervalo entre requisições 
    
    @task(3) 
    def get_tasks(self):
        """Simula um user listando tarefas"""
        self.client.get("/tasks")
        
        
    @task(1)
    def create_task(self):
        """Simula um user criando uma tarefa"""
        self.client.post("/tasks", json={"title": "Load Test Task", "description": "test"})