import os

import pytest
import asyncio

from fastapi.testclient import TestClient

from database import db
from main import app


@pytest.fixture(scope="session")
def client():
    return TestClient(app)


@pytest.fixture()
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()
