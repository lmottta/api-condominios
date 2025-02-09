from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "API de Condomínios"
    DESCRIPTION: str = "API para gerenciamento de informações de condomínios"
    VERSION: str = "1.0.0"
    
    class Config:
        case_sensitive = True

settings = Settings() 