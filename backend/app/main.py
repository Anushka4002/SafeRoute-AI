from fastapi import FastAPI
from pydantic import BaseModel

from app.data.city_graph import graph, locations
from app.services.route_service import RouteService

app = FastAPI(
    title="SafeRoute AI",
    description="AI Powered Accident Risk Route Advisor",
    version="1.0"
)

service = RouteService(graph, locations)


class RouteRequest(BaseModel):
    source: int
    destination: int


@app.get("/")
def home():
    return {
        "message": "Welcome to SafeRoute AI"
    }


@app.get("/locations")
def get_locations():
    return locations


@app.post("/route/dijkstra")
def dijkstra(request: RouteRequest):
    return service.get_dijkstra_route(
        request.source,
        request.destination
    )


@app.post("/route/astar")
def astar(request: RouteRequest):
    return service.get_astar_route(
        request.source,
        request.destination
    )


@app.post("/route/safest")
def safest(request: RouteRequest):
    return service.get_safest_route(
        request.source,
        request.destination
    )