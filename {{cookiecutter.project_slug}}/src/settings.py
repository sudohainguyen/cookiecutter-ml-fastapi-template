import os
from dotenv import load_dotenv

from pydantic import BaseSettings

ENV = os.getenv('ENV', default='PROD')

env_file = 'envs/.env.prod'
if ENV == 'DEV':
    env_file = 'envs/.env.dev'

load_dotenv(env_file)


class APISettings(BaseSettings):
    MODEL_DIR: str = os.getenv('MODEL_DIR')
    # ...
