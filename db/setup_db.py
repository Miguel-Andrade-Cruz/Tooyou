from sqlalchemy.orm import joinedload
from config.connection import DatabaseConfig


db = DatabaseConfig()

db.create_engine()
db.sessionMaker()