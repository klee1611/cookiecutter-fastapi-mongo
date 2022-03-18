import pytest_asyncio
from fastapi.testclient import TestClient

from .mongo_util import MongoUtil


@pytest_asyncio.fixture()
def test_client():
    from app.server import app
    with TestClient(app) as test_client:
        yield test_client


@pytest_asyncio.fixture(autouse=True)
async def mock_data():
    print('\033[92mSetup mock db\033[0m')
    mock_db = MongoUtil()
    yield mock_db

    print('\033[92mTeardown drop db and close conn\033[0m')
    await mock_db.drop_database()
    mock_db.close_conn()
