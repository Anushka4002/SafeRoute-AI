from app.data.city_graph import graph
from app.data.city_graph import locations

from app.services.route_service import RouteService


def main():

    service = RouteService(
        graph,
        locations
    )

    source = 1
    destination = 5

    print("\n========== SAFE ROUTE AI ==========\n")

    print(f"Source      : {locations[source].name}")
    print(f"Destination : {locations[destination].name}")

    print("\n----- Dijkstra -----\n")

    path, distance = service.shortest_route(
        source,
        destination
    )

    print("Path:")

    for node in path:
        print(f"→ {locations[node].name}")

    print(f"\nDistance : {distance} meters")

    print("\n----- A* Search -----\n")

    path, distance = service.smart_route(
        source,
        destination
    )

    print("Path:")

    for node in path:
        print(f"→ {locations[node].name}")

    print(f"\nDistance : {distance} meters")


if __name__ == "__main__":
    main()