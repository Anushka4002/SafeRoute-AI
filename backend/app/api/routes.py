from fastapi import APIRouter

from app.data.city_graph import graph
from app.data.city_graph import locations

from app.models.request_models import RouteRequest

from app.services.route_service import RouteService

router = APIRouter()

service = RouteService(
    graph,
    locations
)


@router.get("/")
def home():

    return {
        "message": "Welcome to SafeRoute AI"
    }


@router.get("/locations")
def get_locations():

    data = []

    for location in locations.values():

        data.append({

            "id": location.id,
            "name": location.name,
            "latitude": location.latitude,
            "longitude": location.longitude

        })

    return data


@router.post("/route/dijkstra")
def dijkstra_route(request: RouteRequest):

    path, distance = service.shortest_route(

        request.source,
        request.destination

    )

    names = []

    for node in path:
        names.append(locations[node].name)

    return {

        "algorithm": "Dijkstra",
        "path": names,
        "distance": distance

    }


@router.post("/route/astar")
def astar_route(request: RouteRequest):

    path, distance = service.smart_route(

        request.source,
        request.destination

    )

    names = []

    for node in path:
        names.append(locations[node].name)

    return {

        "algorithm": "A*",
        "path": names,
        "distance": distance

    }