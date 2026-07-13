from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.data.city_graph import graph, locations
from app.services.route_service import RouteService

app = FastAPI(
    title="SafeRoute AI",
    description="AI Powered Accident Risk Route Advisor",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

service = RouteService(graph, locations)


class RouteRequest(BaseModel):
    source: int
    destination: int


class AddressRouteRequest(BaseModel):
    source: str
    destination: str


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


@app.get("/geocode")
def geocode(query: str):
    return service.geocode_service.geocode(query)


@app.post("/route/address/{algorithm}")
def route_by_address(algorithm: str, request: AddressRouteRequest):
    return service.get_route_by_address(
        algorithm,
        request.source,
        request.destination
    )