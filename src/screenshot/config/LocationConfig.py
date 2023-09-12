from dataclasses import dataclass


@dataclass
class LocationConfig:
    id: str
    lat: float
    lng: float
    zoom: int
