from environs import Env
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

env = Env()
env.read_env('.env')
engine = create_engine(
    f"postgresql://{env('DB_USER')}:{env('DB_PASSWORD')}@{env('DB_HOST')}:{env('DB_PORT')}/{env('DB_NAME')}"
)

Base = declarative_base()

Session = sessionmaker()
