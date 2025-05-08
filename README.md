# API de Gerenciamento de Tarefas

Uma API RESTful para gerenciar tarefas, construída com FastAPI, PostgreSQL e Redis.

## Instalação

1. Clone o repositório.
2. Instale as dependências: `pip install -r requirements.txt`
3. Inicie os serviços com Docker: `docker-compose up -d`
4. Execute a API: `uvicorn main:app --reload`

## Uso

- Criar uma tarefa: `POST /tasks` com JSON `{ "title": "Tarefa", "description": "Descrição" }`
- Listar tarefas: `GET /tasks`
- Atualizar uma tarefa: `PUT /tasks/{id}` com JSON `{ "title": "Novo título", "description": "Nova descrição", "completed": true }`
- Excluir uma tarefa: `DELETE /tasks/{id}`

## Arquitetura

- **Controladores**: Gerenciam requisições HTTP.
- **Serviços**: Contêm lógica de negócio.
- **Repositórios**: Interagem com o banco.
- **Cache**: Redis melhora a performance do `GET /tasks`.

----

Este projeto ainda não foi finalizado... pretendo adicionar:
- **Testes Automatizados**
- **Monitoramento de Performance**
- **Deploy**
