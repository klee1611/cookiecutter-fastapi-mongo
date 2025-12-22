from uuid import UUID

from pydantic import ConfigDict

from .sample_resource_common import SampleResourceBase, to_lower_camel_case
from .mongo_model import MongoModel


class CreateSampleResourceReq(SampleResourceBase):
    model_config = ConfigDict(alias_generator=to_lower_camel_case)


class CreateSampleResourceResp(MongoModel):
    id: UUID
