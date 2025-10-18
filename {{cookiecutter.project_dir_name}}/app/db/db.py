from motor.motor_asyncio import AsyncIOMotorClient
import logging

from ..conf.config import Config


db_client: AsyncIOMotorClient = None


async def get_db() -> AsyncIOMotorClient:
    return db_client


async def connect_and_init_db():
    logging.info('Connecting to mongo...')
    global db_client
    db_client = AsyncIOMotorClient(
        Config.app_settings.get('mongodb_url'),
        maxPoolSize=Config.app_settings.get('max_db_conn_count'),
        minPoolSize=Config.app_settings.get('min_db_conn_count')
    )
    logging.info('Connected to mongo.')


async def close_db_connect():
    logging.info('Closing connection to mongo...')
    db_client.close()
    logging.info('Mongo connection closed.')
