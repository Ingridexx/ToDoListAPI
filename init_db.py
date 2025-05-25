from models import Base
from database_config import engine

Base.metadata.create_all(bind=engine)