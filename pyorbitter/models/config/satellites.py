from pydantic import BaseModel
import uuid
import datetime
from typing import Union, List
from models.common.classification import Classification


class Satellite(BaseModel):
    id: Union[str, int, uuid]
    classification: Classification
    international_designator: int
    toa: datetime.datetime
    ballistic_coefficient: float
    mean_motion_second_derivative: float
    drag_term: float
    ephemeris_type: int
    element_set_number: int
    major_semi_axis: float
    inclination: float
    eccentricity: float
    catalog_number: int
    inclination: float  # degrees
    raan: float  # degrees
    eccentricity: float
    perigee_arg: float  # degrees
    mean_anomaly: float  # degrees
    mean_motion: float  # revolutions per day
    revolution_number: float  # revolutions


class SatelliteNetwork(BaseModel):
    List[Satellite]
