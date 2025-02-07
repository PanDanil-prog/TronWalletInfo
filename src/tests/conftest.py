import os

import pytest
import asyncio

from fastapi.testclient import TestClient

from database import db
from main import app


DB_DSN = os.getenv("DB_DSN", "postgresql+asyncpg://tron_user:tron_pass@db:5432/tron_db")


@pytest.fixture(scope="function")
async def test_db_session():

    async with db.begin() as conn:
        yield conn


@pytest.fixture(scope="session")
def client():
    return TestClient(app)


@pytest.fixture()
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()
