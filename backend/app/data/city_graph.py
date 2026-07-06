from app.algorithms.graph import Graph
from app.models.location import Location

# Create graph object
graph = Graph()

# Add roads (edges)
graph.add_edge(1, 2, 300)
graph.add_edge(1, 3, 150)
graph.add_edge(2, 4, 250)
graph.add_edge(3, 4, 350)
graph.add_edge(4, 5, 100)

# Store locations
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