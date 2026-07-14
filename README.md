# SafeRoute AI

An AI-powered risk-aware navigation system that recommends safer travel routes by combining graph algorithms, map APIs, and machine learning.

## Features

- Graph Based Navigation
- BFS
- DFS
- Dijkstra
- A* Search
- JSON Graph Loading
- FastAPI Backend
- Swagger Documentation
- REST API

## Folder Structure

```text
SafeRoute-AI
│
├── assets
│
├── backend
│   ├── app
│   │   ├── algorithms
│   │   ├── data
│   │   ├── models
│   │   ├── services
│   │   ├── utils
│   │   └── main.py
│   │
│   └── tests
│
├── frontend
├── datasets
├── docs
│
├── README.md
├── LICENSE
└── .gitignore
```

## Tech Stack

- Python
- FastAPI
- Uvicorn
- JSON
- Graph Algorithms
- Dijkstra
- A*
- OpenStreetMap (Upcoming)
- React (Upcoming)

## Project Status

## 📅 Project Progress

### ✅ Day 1
- Designed project structure
- Implemented Graph data structure using adjacency list
- Added weighted undirected edges
- Tested graph representation

### ✅ Day 2
- Implemented Breadth First Search (BFS)
- Implemented Depth First Search (DFS)
- Added unit tests for graph traversal

### ✅ Day 3
- Implemented Priority Queue using heapq
- Implemented Dijkstra's Algorithm
- Reconstructed shortest path
- Calculated minimum route distance

### ✅ Day 4
- Created Route model
- Added RouteService layer
- Separated business logic from graph algorithms
- Prepared backend architecture for FastAPI integration

### ✅ Day 5
- Added Location model
- Added Road model
- Introduced node IDs
- Added latitude and longitude
- Created city graph dataset

## ✅ Day 6

### Graph Refactor
The graph architecture was upgraded from storing only edge distances to storing complete road metadata.
Each road now contains:
- Distance
- Risk Score
- Travel Time
This prepares the project for:
- AI-based safest route
- Fastest route
- Google Maps integration
- OpenStreetMap integration
- Crime and weather data

### ✅ Day 7
A* Search
Route Service
Heuristic Functions
Algorithm Comparison


# Day 8 - JSON Graph Loader
## Overview
The road network is now loaded dynamically from a JSON dataset instead of being hardcoded in Python.
##New Components
- city_graph.json
- graph_loader.py
## Advantages
- Decouples data from algorithms.
- Makes the backend easier to maintain.
- Allows replacing JSON with databases or external APIs later.
- Keeps Dijkstra and A* independent of the data source.
## Workflow
city_graph.json
↓
GraphLoader
↓
Graph + Locations
↓
RouteService
↓
Algorithms (Dijkstra / A*)
## Current Features
- Graph Data Structure
- BFS
- DFS
- Priority Queue
- Dijkstra
- A* Search
- Route Service
- JSON Data Loader
- Object-Oriented Design
- Unit Tests

## Upcoming

- FastAPI REST APIs
- Interactive Map
- OpenStreetMap Integration
- PostgreSQL/PostGIS
- Risk Prediction Engine

### ✅ Day 9
- FastAPI Backend
- Swagger API
- REST Endpoints

### ✅ Day 10

#### Safest Route Algorithm

Implemented a custom safest route algorithm that finds routes with the lowest accident risk instead of only the shortest distance.

#### Risk Analysis

Added a dedicated `RiskService` to calculate:

- Total Risk
- Average Risk
- Safety Percentage
- Route Safety Status (SAFE / MODERATE / DANGEROUS)

#### New Backend Components

Added:

- `algorithms/safest_path.py`
- `services/risk_service.py`

Updated:

- `models/road.py`
- `services/route_service.py`
- `api/routes.py`

#### New API Endpoint

```
POST /route/safest
```

Example Request

```json
{
    "source": 1,
    "destination": 5
}
```

### ✅ Day 11

#### Coordinate & Map Services

Added backend services that prepare route data for frontend map visualization.

##### New Components

- CoordinateService
- MapService

##### Improvements

- Converts node IDs into geographic coordinates.
- Converts node IDs into readable location names.
- Returns structured route responses for API endpoints.
- Prepares the backend for Leaflet/OpenStreetMap integration.

##### Current Features

- Graph Data Structure
- BFS
- DFS
- Dijkstra
- A* Search
- Safest Path
- JSON Graph Loader
- FastAPI Backend
- Swagger API
- Risk Analysis
- Coordinate Service
- Map Service

## OSM & Map Integration (Day 12)

The backend now includes `OSMService` (`app/services/osm_service.py`), which generates
map-related links and summaries for any computed route.

### Features
- `build_osm_url(coordinates)` → OpenStreetMap link centered on the start location
- `build_google_maps_url(coordinates)` → Google Maps directions link across the full route
- `build_route_summary(coordinates)` → Human-readable route string (e.g. `College → Library → Hospital → Police Station`)

### Integration
`MapService.build_route_response()` now returns three additional fields on top of the
existing response shape:

```json
{
  "algorithm": "...",
  "path": [...],
  "coordinates": [...],
  "route_summary": "College → Library → Hospital → Police Station",
  "osm_url": "https://www.openstreetmap.org/?mlat=...&mlon=...#map=15/.../...",
  "google_maps_url": "https://www.google.com/maps/dir/...",
  "distance": 600,
  "risk": 1.1,
  "safety_percentage": 63.0
}
```

No existing fields, function names, or endpoints were changed.

#### Upcoming

- Leaflet.js Interactive Maps
- Live Route Visualization
- PostgreSQL/PostGIS
- Machine Learning Risk Prediction

## Frontend (Day 12)
React + Leaflet map UI. Currently displays dummy location markers (matches backend `city_graph.json`).
Backend connection happens Day 14.

## Setup
npm install
npm run dev

## Frontend (Day 13)
# SafeRoute AI — Frontend

React + Leaflet map UI connected to FastAPI backend.

## Features
- Fetches real locations from `/locations`
- Select source, destination, algorithm (Dijkstra / A* / Safest Route)
- Draws computed route as a polyline on the map
- Shows distance, risk, safety %, and Google Maps link

## Setup
npm install
npm run dev

Backend must be running at http://127.0.0.1:8000 (see backend/README.md)

## Real Address Search + Bhopal Route Network (Day 15)

Backend now supports searching real-world addresses instead of fixed dropdown locations.

### New Services
- `GeocodeService` (`app/services/geocode_service.py`) — converts address text to coordinates via OpenStreetMap Nominatim
- `NearestNodeService` (`app/services/nearest_node_service.py`) — snaps geocoded coordinates to the nearest known graph node using the Haversine formula
- `FastestPath` algorithm (`app/algorithms/fastest_path.py`) — Dijkstra variant minimizing `travel_time` instead of `distance`

### New Endpoints
- `GET /geocode?query=...` — returns address suggestions
- `POST /route/address/{algorithm}` — accepts `{ "source": "...", "destination": "..." }`, algorithm = `dijkstra` | `astar` | `fastest` | `safest`

### City Graph
Replaced dummy Delhi locations with a real Bhopal road network (8 nodes), including VIT Bhopal and DB Mall, connected via realistic waypoints (Ratibad, Bairagarh, Habibganj, New Market, MP Nagar, Bhopal Railway Station).

### Response now includes
- `travel_time`
- `warnings` (auto-generated safety alerts)
- `source_matched_location`, `destination_matched_location`
- `source_snap_distance_m`, `destination_snap_distance_m`

## Route Comparison (Day 16)

New endpoint `POST /route/address/compare` computes Shortest, Fastest, and Safest
routes in a single call and returns them together for side-by-side comparison.

Response shape:
```json
{
  "source_matched_location": "...",
  "destination_matched_location": "...",
  "routes": {
    "dijkstra": { ... },
    "fastest": { ... },
    "safest": { ... }
  }
}

## AI Risk Prediction Model (Day 17)

Added a real machine learning component: a trained `RandomForestRegressor` (scikit-learn)
predicts a **risk multiplier** based on real-world conditions, replacing static hardcoded risk.

### Pipeline
1. `app/ml/generate_dataset.py` — generates a synthetic but realistic dataset (2000 rows)
   correlating time of day, weather, speed limit, and past incidents with a risk multiplier
2. `app/ml/train_model.py` — trains a RandomForestRegressor pipeline (OneHotEncoder + regressor),
   evaluates with Mean Absolute Error, saves to `app/ml/risk_model.pkl`
3. `app/services/ml_risk_service.py` — loads the trained model and exposes
   `predict_risk_multiplier(time_of_day, weather, speed_limit, past_incidents)`

### Integration
- `Graph.clone_with_adjusted_risk(multiplier)` — produces a temporary graph where every
  edge's risk is scaled by the ML-predicted multiplier
- `RouteService.get_all_routes_with_conditions(...)` — swaps in the adjusted graph,
  computes Shortest/Fastest/Safest routes under those conditions, then restores the original

### New Endpoint
`POST /route/address/compare-conditions`
```json
{
  "source": "VIT Bhopal",
  "destination": "DB Mall Bhopal",
  "time_of_day": "night",
  "weather": "foggy"
}
```
Returns all three routes plus the applied `risk_multiplier`.

### Model Performance
Mean Absolute Error ≈ 0.08 on held-out test data (20% split), indicating reliable
multiplier predictions across the input feature space.
```


🚧 Under Development