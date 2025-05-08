from models import Base, engine 

print("Tentando criar tabelas...")
Base.metadata.create_all(bind=engine)
print("Tabelas criadas com sucesso!")