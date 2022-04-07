from motor.motor_asyncio import AsyncIOMotorClient
import os
from uuid import UUID
import logging


class MongoHandler():
    def __init__(self, db_name: str, collection_name: str):
        self.__db_name = db_name
        self.__collection_name = collection_name
        self.__db_client = AsyncIOMotorClient(
            os.environ.get('TEST_MONGODB_URL')
        )

    async def get_sample_resource(self, resource_id: UUID):
        return await self.__db_client[self.__db_name][self.__collection_name]\
            .find_one({'_id': UUID(resource_id)})

    async def drop_database(self):
        await self.__db_client.drop_database(self.__db_name)

    def close_conn(self):
        self.__db_client.close()


class MongoClient():
    def __init__(self, db_name: str, collection_name: str):
        self.__db_handler = MongoHandler(db_name, collection_name)

    def __enter__(self):
        return self.__db_handler

    def __exit__(self, exception_type, exception_value, exception_traceback):
        if exception_type:
            logging.error(exception_value)

        self.__db_handler.drop_database()
        self.__db_handler.close_conn()
        return False
