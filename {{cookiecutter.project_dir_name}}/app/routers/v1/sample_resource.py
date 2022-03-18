from fastapi import APIRouter, Depends
import logging

from ...db.db import get_db, AsyncIOMotorClient
from ...dao.sample_resource import create_sample_resource as \
    db_create_sample_resouce

from ...models.create_sample_resource import \
    CreateSampleResourceReq, CreateSampleResourceResp

router = APIRouter()


@router.post('/', include_in_schema=False, status_code=201)
@router.post('', response_model=CreateSampleResourceResp, status_code=201,
             responses={
                 400: {}
             }
             )
async def create_account(
    sample_resource_data: CreateSampleResourceReq,
    db: AsyncIOMotorClient = Depends(get_db)
):
    logging.info('Receive create sample resource request')

    sample_resource_db = await db_create_sample_resouce(
        db,
        sample_resource_data.name
    )

    return CreateSampleResourceResp(id=sample_resource_db.id)
