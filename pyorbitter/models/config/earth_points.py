from pydantic import BaseModel
import uuid
from typing import Union, List
from models.common.coords import Coords


class EarthPoint(BaseModel):
    id: Union[str, int, uuid]
    coordinates: Coords


class EarthPoints(BaseModel):
    List[EarthPoint]
