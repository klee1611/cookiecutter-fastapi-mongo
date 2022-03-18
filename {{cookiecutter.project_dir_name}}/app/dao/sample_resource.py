from uuid import uuid4
from datetime import datetime
import logging

from ..conf.config import Config
from ..db.db import AsyncIOMotorClient
from ..models.sample_resource_common import SampleResourceDB


__db_name = Config.app_settings.get('db_name')
__db_collection = 'sample_resource'


async def create_sample_resource(
    conn: AsyncIOMotorClient,
    name: str
):
    new_sample_resource = SampleResourceDB(
        id=uuid4(),
        name=name,
        create_time=datetime.utcnow(),
        update_time=datetime.utcnow()
    )
    logging.info(
        f'Inserting sample resource {name} into db...'
    )
    await conn[__db_name][__db_collection].insert_one(
        new_sample_resource.mongo()
    )
    logging.info(
        f"Sample resource {name} has inserted into db"
    )
    return new_sample_resource
