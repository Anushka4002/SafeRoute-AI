class Route:

    def __init__(

        self,
        algorithm,
        path,
        distance,
        risk=0,
        safety_percentage=100,
        coordinates=None

    ):

        self.algorithm = algorithm

        self.path = path

        self.distance = distance

        self.risk = risk

        self.safety_percentage = safety_percentage

        if coordinates is None:
            coordinates = []

        self.coordinates = coordinates

    def to_dict(self):

        return {

            "algorithm": self.algorithm,

            "path": self.path,

            "distance": self.distance,

            "risk": self.risk,

            "safety_percentage": self.safety_percentage,

            "coordinates": self.coordinates

        }