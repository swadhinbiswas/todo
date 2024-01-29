from pydantic_settings import BaseSettings
from pydantic import AnyHttpUrl
from typing import List 
from dotenv import load_dotenv,find_dotenv
import os
load_dotenv(find_dotenv())

class Settings(BaseSettings):
    API:str= "/api/v1"
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    REFRESH_SECRET_KEY: str = os.getenv("REFRESH_SECRET_KEY")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7
    ALGORITHM: str = "HS256"
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    PROJECT_NAME: str = "ToDoApp",
    
    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"
settings = Settings()

    
   
    