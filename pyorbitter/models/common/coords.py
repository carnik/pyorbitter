from pydantic import BaseModel


class Coords(BaseModel):
    lat: float  # degrees
    lon: float  # degrees
    height: float  # metres
