import os

from pydantic import BaseSettings

ENV = os.getenv("ENV", default="PROD")

env_file = "envs/.env.prod"
if ENV == "DEV":
    env_file = "envs/.env.dev"


class APISettings(BaseSettings):
    MODEL_DIR: str
    # ...
    class Config:
        env_file = env_file
        env_file_encoding = "utf-8"
