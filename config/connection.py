import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DatabaseConfig:

    def __init__(self):
        database = os.getenv('DB_DATABASE')
        password = os.getenv('DB_PASSWORD')
        self.database_url = os.getenv('', f"mysql+mysqlconnector://root:{password}@localhost:5055/{database}")

    def create_engine(self):
        self.engine = create_engine(self.database_url)
    
    def sessionMaker(self):
        SessionLocal = sessionmaker(bind=self.engine)
        self.session = SessionLocal()