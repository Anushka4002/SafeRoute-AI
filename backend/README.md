# ⚙️ SafeRoute AI Backend

> **A FastAPI-powered backend for SafeRoute AI that provides intelligent route planning using graph algorithms, machine learning-based risk prediction, and REST APIs.**

---

# 📖 Overview

The SafeRoute AI backend is responsible for route computation, risk analysis, location services, machine learning integration, and communication with the frontend.

It uses graph algorithms to compute the **Shortest**, **Fastest**, and **Safest** routes while exposing REST APIs through FastAPI. The backend also integrates a Machine Learning model that dynamically predicts road risk based on environmental conditions.

The backend follows a modular, service-oriented architecture, making it easy to maintain, test, and extend.

---

# ✨ Features

## 🚗 Route Planning

Supports multiple routing strategies:

- Shortest Route (Dijkstra)
- A* Search
- Fastest Route
- Safest Route
- Route Comparison

---

## 🌍 Address Search

- Real-world address search
- OpenStreetMap Nominatim integration
- Coordinate lookup
- Nearest graph node matching

---

## 🤖 Machine Learning Risk Prediction

A trained **Random Forest Regressor** predicts a **Risk Multiplier** using:

- Time of Day
- Weather
- Speed Limit
- Historical Accident Count

The predicted multiplier is applied before computing the safest route.

---

## 📊 Route Analytics

For every generated route, the backend computes:

- Distance
- Travel Time
- Risk Score
- Safety Percentage
- Safety Status
- Route Summary
- Safety Warnings

---

## 📡 REST API

FastAPI provides:

- Route APIs
- Location APIs
- Address Search APIs
- Route Comparison APIs
- Machine Learning Prediction APIs

Interactive API documentation is automatically generated using Swagger and ReDoc.

---

# 🛠️ Technology Stack

| Technology | Purpose |
|------------|----------|
| Python | Backend Development |
| FastAPI | REST API Framework |
| Uvicorn | ASGI Server |
| Pydantic | Data Validation |
| Scikit-learn | Machine Learning |
| NumPy | Numerical Computing |
| Heapq | Priority Queue |
| JSON | Graph Dataset |
| OpenStreetMap | Geocoding |
| Google Maps | Route Navigation |

---

# 🏗️ Backend Architecture

```text
                    FastAPI Backend
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
    REST APIs         Route Services     ML Services
        │                  │                  │
        ▼                  ▼                  ▼
 Graph Algorithms   Risk Analysis     Random Forest
        │                  │                  │
        └──────────────┬───┴──────────────────┘
                       ▼
                  JSON Graph Data
```

---

# 📂 Folder Structure

```text
backend/
│
├── app/
│
│   ├── algorithms/
│   │   ├── astar.py
│   │   ├── bfs.py
│   │   ├── dfs.py
│   │   ├── dijkstra.py
│   │   ├── fastest_path.py
│   │   ├── safest_path.py
│   │   ├── graph.py
│   │   ├── heuristics.py
│   │   └── priority_queue.py
│   │
│   ├── api/
│   │   └── routes.py
│   │
│   ├── data/
│   │   ├── city_graph.json
│   │   └── graph_loader.py
│   │
│   ├── ml/
│   │   ├── generate_dataset.py
│   │   ├── train_model.py
│   │   ├── risk_model.pkl
│   │   └── synthetic_dataset.csv
│   │
│   ├── models/
│   │   ├── graph.py
│   │   ├── location.py
│   │   ├── road.py
│   │   └── route.py
│   │
│   ├── services/
│   │   ├── coordinate_service.py
│   │   ├── geocode_service.py
│   │   ├── map_service.py
│   │   ├── ml_risk_service.py
│   │   ├── nearest_node_service.py
│   │   ├── osm_service.py
│   │   ├── risk_service.py
│   │   └── route_service.py
│   │
│   ├── utils/
│   │
│   └── main.py
│
├── tests/
│
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

Navigate to the backend directory:

```bash
cd backend
```

Create a virtual environment.

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Backend

```bash
uvicorn app.main:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

---

# 📚 API Documentation

FastAPI automatically generates API documentation.

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

# 📡 API Endpoints

## Health

| Method | Endpoint |
|---------|----------|
| GET | `/` |

---

## Locations

| Method | Endpoint |
|---------|----------|
| GET | `/locations` |

---

## Address Search

| Method | Endpoint |
|---------|----------|
| GET | `/geocode?query=` |

---

## Route APIs

| Method | Endpoint |
|---------|----------|
| POST | `/route/address/dijkstra` |
| POST | `/route/address/astar` |
| POST | `/route/address/fastest` |
| POST | `/route/address/safest` |

---

## Route Comparison

| Method | Endpoint |
|---------|----------|
| POST | `/route/address/compare` |
| POST | `/route/address/compare-conditions` |

---

# 🧠 Algorithms

## Breadth First Search (BFS)

- Graph traversal
- Queue-based implementation
- Used for exploration

---

## Depth First Search (DFS)

- Graph traversal
- Recursive/Stack implementation

---

## Dijkstra's Algorithm

Optimizes:

- Shortest Distance

---

## A* Search

Uses:

- Distance
- Heuristic Function

Provides faster pathfinding in many scenarios.

---

## Fastest Path

Optimizes:

- Travel Time

---

## Safest Path

Optimizes:

- Road Risk

Custom routing algorithm for safer navigation.

---

# 🤖 Machine Learning Pipeline

```text
Synthetic Dataset
        │
        ▼
Feature Engineering
        │
        ▼
Random Forest Regressor
        │
        ▼
Risk Multiplier
        │
        ▼
Adjusted Graph
        │
        ▼
Safest Route
```

---

## Input Features

- Time of Day
- Weather
- Speed Limit
- Historical Accident Count

---

## Output

- Risk Multiplier

---

## Model

- Random Forest Regressor
- Scikit-learn Pipeline
- OneHotEncoder

---

# 🌍 Location Services

The backend provides several location-based services.

### Geocode Service

Converts user-entered addresses into geographic coordinates.

---

### Nearest Node Service

Maps geographic coordinates to the nearest graph node using the Haversine formula.

---

### Coordinate Service

Returns coordinates for route visualization.

---

### Map Service

Builds complete route responses for the frontend.

---

### OSM Service

Generates:

- Google Maps links
- OpenStreetMap links
- Route summaries

---

# 📊 Response Information

Each route response contains:

| Property | Description |
|----------|-------------|
| Path | Route nodes |
| Coordinates | Latitude & Longitude |
| Distance | Total distance |
| Travel Time | Estimated duration |
| Risk Score | Route risk |
| Safety Percentage | Route safety |
| Safety Status | Safe / Moderate / Dangerous |
| Warnings | Risk alerts |
| Route Summary | Human-readable path |
| Google Maps URL | External navigation |
| OSM URL | OpenStreetMap route |

---

# 🧪 Testing

Run all backend tests.

```bash
pytest
```

or

```bash
python -m pytest
```

Tests include:

- Graph Construction
- JSON Loader
- BFS
- DFS
- Dijkstra
- A*
- Fastest Path
- Safest Path
- Route Service
- Risk Service
- Machine Learning Integration

---

# 🚀 Future Improvements

- PostgreSQL/PostGIS integration
- Live traffic data
- Weather API integration
- Crime hotspot analysis
- Docker support
- Cloud deployment
- Authentication
- Route caching
- Multi-city support
- Real-time navigation

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository.

2. Create a feature branch.

```bash
git checkout -b feature/your-feature
```

3. Commit changes.

```bash
git commit -m "Add feature"
```

4. Push to GitHub.

```bash
git push origin feature/your-feature
```

5. Create a Pull Request.

---

# 📄 License

This project is licensed under the MIT License.

See the LICENSE file for details.

---

# 👩‍💻 Author

**Anushka Yadav**

B.Tech – Artificial Intelligence & Machine Learning

VIT Bhopal University

GitHub: https://github.com/Anushka4002

---

<div align="center">

## ⚙️ SafeRoute AI Backend

**Fast • Modular • Scalable • AI-Powered**

Built with **FastAPI**, **Python**, **Scikit-learn**, and **OpenStreetMap**.

</div>