from uuid import uuid4, UUID
from datetime import datetime
import logging

from ..conf.config import Config
from ..db.db import AsyncIOMotorClient
from ..models.sample_resource_common import SampleResourceDB
from ..util import uuid_masker


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


async def get_sample_resource(
    conn: AsyncIOMotorClient,
    resource_id: UUID
) -> SampleResourceDB | None:
    logging.info(f"Getting sample resource {uuid_masker(resource_id)}...")
    sample_resource = await conn[__db_name][__db_collection].find_one(
        {'_id': resource_id},
    )
    if None is sample_resource:
        logging.info(f"Resource {uuid_masker(resource_id)} is None")
    return sample_resource
