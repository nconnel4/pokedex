from typing import Optional

from dotenv import find_dotenv
from pydantic import AnyUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=find_dotenv(".env"), env_file_encoding="utf-8"
    )

    app_name: str = "Pokedex"
    database_url: Optional[AnyUrl]
