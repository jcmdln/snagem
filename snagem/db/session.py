from alembic import command
from alembic import config as alembic_config
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeMeta, Session, declarative_base, sessionmaker

from snagem import settings

database_args: dict = {}
engine_args: dict = {"pool_pre_ping": True}
if "sqlite" in settings.SQLALCHEMY_URL.lower():
    database_args = {"check_same_thread": False}
else:
    engine_args = {"max_overflow": 4, "pool_size": 1}

Base: DeclarativeMeta = declarative_base()

session: sessionmaker[Session] = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=create_engine(settings.SQLALCHEMY_URL, connect_args=database_args, **engine_args),
)


def upgrade() -> None:
    cfg = alembic_config.Config("alembic.ini")
    command.upgrade(cfg, revision="head")


__all__: list[str] = ["Base", "session", "upgrade"]
