from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# URL do banco de dados (ajuste para o seu ambiente)
DATABASE_URL = "postgresql://user:password@localhost:5432/tasks_db"

# Cria o engine de conexão
engine = create_engine(DATABASE_URL)

# Define a sessão local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)