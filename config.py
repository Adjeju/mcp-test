import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    DATABASE_URL = os.getenv("DATABASE_URL")

    def __init__(self):
        print("Config initialized")


config = Config()
