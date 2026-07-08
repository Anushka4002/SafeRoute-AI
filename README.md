# SafeRoute AI

An AI-powered risk-aware navigation system that recommends safer travel routes by combining graph algorithms, map APIs, and machine learning.

## Features (Planned)

- Route Optimization
- Risk Prediction
- Safe Route Recommendation
- Interactive Map
- AI-based Risk Scoring
- Real-time Route Analysis

## Tech Stack

- Python
- FastAPI
- React
- Google Maps API / OpenStreetMap
- Scikit-learn
- Pandas

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

🚧 Under Development