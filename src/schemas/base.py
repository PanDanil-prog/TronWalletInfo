from pydantic import BaseModel as PydanticBaseModel

from common import json


class BaseModel(PydanticBaseModel):

    class Config:
        json_loads = json.loads