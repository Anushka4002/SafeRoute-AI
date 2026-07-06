from dataclasses import dataclass


@dataclass
class Road:

    source: int
    destination: int

    distance: float

    risk_score: float = 0

    travel_time: float = 0