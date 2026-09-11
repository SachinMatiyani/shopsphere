import os
from dotenv import load_dotenv
from sqlalchemy.engine import URL

load_dotenv()

class Config:
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")
    SQLALCHEMY_DATABASE_URI = URL.create(
                                            "postgresql+psycopg",
                                            username=DB_USER,
                                            password=DB_PASSWORD,
                                            host=DB_HOST,
                                            port=DB_PORT,
                                            database=DB_NAME
                                        )
    SQLALCHEMY_TRACK_MODIFICATIONS = False