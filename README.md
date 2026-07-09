# SafeRoute AI

An AI-powered risk-aware navigation system that recommends safer travel routes by combining graph algorithms, map APIs, and machine learning.

## Features (Planned)

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


🚧 Under Development