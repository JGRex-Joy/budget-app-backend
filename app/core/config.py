from pydantic_settings import BaseSettings

import os
from dotenv import load_dotenv
load_dotenv()

class Settings(BaseSettings):
    APP_NAME: str = "Budget App Backend"
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    
    class Config:
        env_file = ".env"
        
settings = Settings()