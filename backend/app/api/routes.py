from fastapi import APIRouter
from pydantic import BaseModel

from app.data.city_graph import graph
from app.data.city_graph import locations

from app.services.route_service import RouteService

router = APIRouter()

service = RouteService(graph, locations)


class RouteRequest(BaseModel):

    source: int
    destination: int


@router.get("/")
def home():

    return {

        "message": "Welcome to SafeRoute AI"

    }


@router.get("/locations")
def get_locations():

    return locations


@router.post("/route/dijkstra")
def dijkstra(request: RouteRequest):

    return service.get_dijkstra_route(

        request.source,
        request.destination

    )


@router.post("/route/astar")
def astar_route(request: RouteRequest):

    return service.get_astar_route(

        request.source,
        request.destination

    )


@router.post("/route/safest")
def safest(request: RouteRequest):

    return service.get_safest_route(

        request.source,
        request.destination

    )