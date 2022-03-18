from motor.motor_asyncio import AsyncIOMotorClient
import os


class MongoUtil():
    def __init__(self):
        self.__db_name = os.environ.get("TEST_DB_NAME")
        self.__db_client = AsyncIOMotorClient(
            os.environ.get('TEST_MONGODB_URL')
        )

    def close_conn(self):
        self.__db_client.close()

    async def drop_database(self):
        await self.__db_client.drop_database(self.__db_name)
