from typing import Any, Generator

from sqlalchemy.util.compat import contextmanager

from .db import SessionLocal


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


db_context = contextmanager(get_db)
