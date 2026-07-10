class Road:

    def __init__(
        self,
        source,
        destination,
        distance,
        risk,
        travel_time
    ):

        self.source = source
        self.destination = destination

        self.distance = distance
        self.risk = risk
        self.travel_time = travel_time

    def __repr__(self):

        return (

            f"Road("
            f"{self.source} -> {self.destination}, "
            f"distance={self.distance}, "
            f"risk={self.risk}, "
            f"time={self.travel_time}"
            f")"

        )