import os
from sqlalchemy import create_engine
from sqlalchemy.sql.schema import Table, Column, Integer, String, MetaData

class Database():
    
    driver= os.environ.get("DRIVER")
    username = os.environ.get("DATABASE_USER")
    host = os.environ.get("DATABASE_HOST")
    port  = os.environ.get("DATABASE_PORT")
    passwrod = os.environ.get("DATABASE_PASSW")
    dbname = os.environ.get("DATABASE_NAME")

    def __init__(self) -> None:
        engine = create_engine(
            f"{self.driver}://{self.username}:{self.passwrod}@{self.host}/{self.dbname}", 
            echo=True)
        meta = MetaData()
    

    # def migrate_tables(self):
    #     students = Table(
    #     'students', self.meta, 
    #     Column('id', Integer, primary_key = True), 
    #     Column('name', String), 
    #     Column('lastname', String), 
    # )