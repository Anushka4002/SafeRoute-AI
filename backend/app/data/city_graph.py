from app.algorithms.graph import Graph
from app.models.location import Location

graph = Graph()

graph.add_edge(
    1,
    2,
    distance=300,
    risk=0.15,
    travel_time=240
)

graph.add_edge(
    1,
    3,
    distance=150,
    risk=0.45,
    travel_time=120
)

graph.add_edge(
    2,
    4,
    distance=250,
    risk=0.25,
    travel_time=200
)

graph.add_edge(
    3,
    4,
    distance=350,
    risk=0.60,
    travel_time=260
)

graph.add_edge(
    4,
    5,
    distance=100,
    risk=0.05,
    travel_time=90
)

locations = {

    1: Location(
        1,
        "College",
        28.6139,
        77.2090
    ),

    2: Location(
        2,
        "Mall",
        28.6151,
        77.2132
    ),

    3: Location(
        3,
        "Library",
        28.6168,
        77.2145
    ),

    4: Location(
        4,
        "Hospital",
        28.6180,
        77.2164
    ),

    5: Location(
        5,
        "Police Station",
        28.6201,
        77.2180
    )
}