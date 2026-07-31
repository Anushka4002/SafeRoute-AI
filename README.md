# 🛣️ SafeRoute AI

> **An AI-powered risk-aware navigation system that recommends the safest, fastest, and shortest travel routes using graph algorithms, machine learning, and interactive maps.**

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![React](https://img.shields.io/badge/React-Frontend-61DAFB)
![Leaflet](https://img.shields.io/badge/Leaflet-Maps-success)
![Machine Learning](https://img.shields.io/badge/ML-RandomForest-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

# 📖 Overview

SafeRoute AI is an intelligent navigation system that goes beyond traditional shortest-path navigation by considering **road safety, travel time, and accident risk** while recommending routes.

Unlike conventional navigation systems that optimize only for distance, SafeRoute AI combines **graph algorithms**, **machine learning**, and **map services** to provide users with multiple routing options based on their preferences.

The system allows users to:

- Find the **Shortest Route**
- Find the **Fastest Route**
- Find the **Safest Route**
- Compare all available routes
- Predict road risk under different weather and traffic conditions
- Visualize routes on an interactive map

The project consists of a **FastAPI backend**, a **React + Leaflet frontend**, and a **Machine Learning module** that dynamically adjusts route risk using real-world conditions.

---

# ✨ Features

## 🚗 Smart Route Planning

- Shortest Path Recommendation
- Fastest Path Recommendation
- Safest Path Recommendation
- Side-by-side route comparison

---

## 🧠 AI-Based Risk Prediction

Instead of using fixed accident risk values, SafeRoute AI predicts a dynamic **risk multiplier** using a trained **Random Forest Regression model**.

The prediction considers:

- Time of Day
- Weather Conditions
- Speed Limit
- Historical Accident Data

This enables safer and more realistic route recommendations.

---

## 🗺️ Interactive Maps

The frontend provides an interactive map interface where users can:

- Select source and destination
- Search real-world addresses
- Visualize computed routes
- Compare different routing algorithms
- View safety metrics
- Open routes directly in Google Maps

---

## 📍 Real Address Search

Users are not restricted to predefined locations.

The system supports:

- Real address search
- Geocoding using OpenStreetMap
- Automatic mapping to the nearest graph node
- Route generation from searched locations

---

## 📊 Route Analytics

For every computed route, SafeRoute AI provides:

- Total Distance
- Estimated Travel Time
- Risk Score
- Safety Percentage
- Safety Status
- Route Summary
- Google Maps Link
- OpenStreetMap Link
- Safety Warnings

---

## ⚡ REST API

FastAPI provides fully documented REST APIs for:

- Route Generation
- Route Comparison
- Address Search
- Risk Prediction
- Location Retrieval

Interactive Swagger documentation is also included.

---

# 🏗️ System Architecture

```
                     +----------------------+
                     |    React Frontend    |
                     |     (Leaflet Map)    |
                     +----------+-----------+
                                |
                                |
                         REST API Calls
                                |
                                ▼
                   +-------------------------+
                   |    FastAPI Backend      |
                   +-----------+-------------+
                               |
      +------------------------+-------------------------+
      |                        |                         |
      ▼                        ▼                         ▼
Graph Algorithms        Route Services          ML Risk Model
(BFS, DFS,              Risk Analysis        Random Forest Model
Dijkstra, A*)              Services
      |                        |                         |
      +------------------------+-------------------------+
                               |
                               ▼
                   OpenStreetMap & Google Maps
```

---

# 🚀 Key Features at a Glance

| Feature | Description |
|----------|-------------|
| 🛣️ Shortest Route | Finds the minimum-distance path using Dijkstra |
| ⚡ Fastest Route | Finds the minimum travel-time route |
| 🛡️ Safest Route | Finds the lowest-risk path |
| 🤖 ML Risk Prediction | Predicts risk based on weather and traffic conditions |
| 📍 Address Search | Search any real-world location |
| 🗺️ Interactive Maps | Visualize routes using Leaflet |
| 📊 Route Comparison | Compare shortest, fastest and safest routes |
| 🌦️ Dynamic Conditions | Weather-aware risk calculation |
| 📚 Swagger API | Interactive REST API documentation |
| 📈 Risk Analytics | Safety %, Risk Score and Warnings |

---

# 🛠️ Technology Stack

## Backend

- Python
- FastAPI
- Uvicorn
- Pydantic
- Scikit-learn
- NumPy
- JSON

---

## Frontend

- React
- Vite
- Leaflet
- React Leaflet
- JavaScript
- CSS

---

## Maps & APIs

- OpenStreetMap
- Nominatim Geocoding API
- Google Maps

---

## Machine Learning

- Random Forest Regressor
- Scikit-learn Pipeline
- OneHotEncoder

---

## Algorithms

- Breadth First Search (BFS)
- Depth First Search (DFS)
- Dijkstra's Algorithm
- A* Search
- Fastest Path (Travel-Time Optimized)
- Safest Path (Risk-Aware Routing)

---

# 📂 Project Structure

```text
SafeRoute-AI/
│
├── backend/
│   ├── app/
│   │   ├── algorithms/
│   │   ├── api/
│   │   ├── data/
│   │   ├── ml/
│   │   ├── models/
│   │   ├── services/
│   │   ├── utils/
│   │   └── main.py
│   │
│   ├── tests/
│   ├── requirements.txt
│   └── README.md
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   └── App.jsx
│   │
│   ├── package.json
│   └── README.md
│
├── datasets/
├── docs/
├── assets/
│
├── LICENSE
├── README.md
└── .gitignore
```

---

# 📦 Repository Contents

| Folder | Description |
|---------|-------------|
| `backend/` | FastAPI backend, graph algorithms, services and APIs |
| `frontend/` | React application with Leaflet map interface |
| `datasets/` | Graph datasets and ML training data |
| `docs/` | Project documentation |
| `assets/` | Images, screenshots and diagrams |
| `backend/tests/` | Unit tests for backend components |

---
# ⚙️ Installation

## Prerequisites

Before running the project, ensure the following software is installed:

- Python 3.10 or later
- Node.js 18+ and npm
- Git
- pip
- Virtual Environment (recommended)

Verify the installation:

```bash
python --version
node --version
npm --version
git --version
```

---

# 📥 Clone the Repository

```bash
git clone https://github.com/Anushka4002/SafeRoute-AI.git
```

Move into the project directory:

```bash
cd SafeRoute-AI
```

---

# 🖥️ Backend Setup

Navigate to the backend directory:

```bash
cd backend
```

---

## Step 1: Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 3: Run the Backend Server

```bash
uvicorn app.main:app --reload
```

The backend server will start at:

```
http://127.0.0.1:8000
```

---

## API Documentation

FastAPI automatically generates interactive API documentation.

### Swagger UI

```
http://127.0.0.1:8000/docs
```

### ReDoc

```
http://127.0.0.1:8000/redoc
```

---

# 🌐 Frontend Setup

Open a new terminal.

Navigate to the frontend directory:

```bash
cd frontend
```

---

## Install Dependencies

```bash
npm install
```

---

## Start the Development Server

```bash
npm run dev
```

The frontend will be available at:

```
http://localhost:5173
```

---

# ▶️ Running the Complete Application

Start the backend:

```bash
cd backend

uvicorn app.main:app --reload
```

Open another terminal and start the frontend:

```bash
cd frontend

npm run dev
```

Open your browser and visit:

```
http://localhost:5173
```

The React frontend will communicate with the FastAPI backend to compute and visualize routes.

---

# 🧭 How to Use

1. Start both the backend and frontend servers.
2. Open the application in your browser.
3. Enter a source location.
4. Enter a destination location.
5. Select one of the routing options:
   - Shortest Route
   - Fastest Route
   - Safest Route
6. View the generated route on the interactive map.
7. Explore route analytics, including:
   - Distance
   - Travel Time
   - Risk Score
   - Safety Percentage
   - Safety Status
8. Open the generated route directly in Google Maps if required.

---

# 🔄 Project Workflow

```text
User Input
     │
     ▼
React Frontend
     │
     ▼
FastAPI REST API
     │
     ▼
Address Geocoding
     │
     ▼
Nearest Graph Node
     │
     ▼
Selected Routing Algorithm
(Dijkstra / A* / Fastest / Safest)
     │
     ▼
Machine Learning Risk Prediction
     │
     ▼
Risk Analysis
     │
     ▼
Route Generation
     │
     ▼
Interactive Map Visualization
```

---

# 📌 Available Routing Options

## 🛣️ Shortest Route

- Optimizes total travel distance.
- Uses Dijkstra's Algorithm.
- Suitable when minimizing distance is the priority.

---

## ⚡ Fastest Route

- Optimizes estimated travel time.
- Uses a travel-time-aware Dijkstra variant.
- Best for reducing journey duration.

---

## 🛡️ Safest Route

- Optimizes road safety by minimizing accident risk.
- Uses a custom risk-aware routing algorithm.
- Recommended when user safety is the highest priority.

---

## 📊 Route Comparison

The comparison feature computes all routing strategies simultaneously, allowing users to evaluate:

- Shortest Route
- Fastest Route
- Safest Route

This helps users choose the route that best matches their priorities.

---

# 🧪 Machine Learning Workflow

The machine learning pipeline dynamically adjusts road risk based on environmental conditions.

### Input Features

- Time of Day
- Weather Conditions
- Speed Limit
- Historical Accident Data

↓

### Random Forest Regression Model

↓

### Predicted Risk Multiplier

↓

### Updated Road Risk

↓

### Safest Route Computation

---

# 🗺️ Maps & Location Services

SafeRoute AI integrates with OpenStreetMap services to provide real-world navigation support.

### Supported Features

- Address Search
- Geocoding
- Reverse Mapping
- Nearest Node Matching
- Interactive Map Visualization
- Google Maps Route Generation
- OpenStreetMap Route Links

---

# 📈 Route Information Returned

Each generated route includes:

| Information | Description |
|-------------|-------------|
| Route | Ordered list of locations |
| Coordinates | Latitude and longitude of each point |
| Distance | Total route distance |
| Travel Time | Estimated journey duration |
| Risk Score | Total calculated risk |
| Safety Percentage | Overall route safety score |
| Safety Status | Safe, Moderate, or Dangerous |
| Warnings | Safety alerts for risky roads |
| Route Summary | Human-readable route description |
| Google Maps URL | Open route in Google Maps |
| OpenStreetMap URL | Open route in OpenStreetMap |

---

# ✅ Testing

Run backend unit tests:

```bash
cd backend

pytest
```

or

```bash
python -m pytest
```

The tests validate:

- Graph construction
- BFS
- DFS
- Dijkstra's Algorithm
- A* Search
- Fastest Path
- Safest Path
- Route Services
- JSON Graph Loading
- Machine Learning Integration

---
# 📡 API Reference

SafeRoute AI exposes a RESTful API built with **FastAPI** for route computation, location search, risk analysis, and machine learning-based predictions.

After starting the backend, the API documentation is available at:

**Swagger UI**

```
http://127.0.0.1:8000/docs
```

**ReDoc**

```
http://127.0.0.1:8000/redoc
```

---

# 🚀 API Endpoints

## Health Check

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | Check whether the backend is running |

---

## Locations

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/locations` | Returns all available graph locations |

---

## Address Search

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/geocode?query=` | Search real-world addresses using OpenStreetMap |

Example

```text
GET /geocode?query=VIT Bhopal
```

---

## Route Generation

### Shortest Route

```http
POST /route/address/dijkstra
```

Example Request

```json
{
  "source": "VIT Bhopal",
  "destination": "DB Mall Bhopal"
}
```

---

### A* Route

```http
POST /route/address/astar
```

---

### Fastest Route

```http
POST /route/address/fastest
```

---

### Safest Route

```http
POST /route/address/safest
```

---

## Compare All Routes

```http
POST /route/address/compare
```

Returns

- Shortest Route
- Fastest Route
- Safest Route

in a single response.

---

## Compare Routes Under Conditions

```http
POST /route/address/compare-conditions
```

Example Request

```json
{
  "source": "VIT Bhopal",
  "destination": "DB Mall Bhopal",
  "time_of_day": "night",
  "weather": "foggy"
}
```

The backend predicts a dynamic **risk multiplier** using the machine learning model and computes all routes under those conditions.

---

# 📦 Sample Response

```json
{
  "algorithm": "Safest Route",
  "path": [
    "VIT Bhopal",
    "Ratibad",
    "New Market",
    "DB Mall"
  ],
  "distance": 19500,
  "travel_time": 32,
  "risk": 1.12,
  "safety_percentage": 82.5,
  "warnings": [
    "Moderate traffic near New Market"
  ],
  "google_maps_url": "...",
  "osm_url": "..."
}
```

---

# 🧠 Routing Algorithms

SafeRoute AI supports multiple routing strategies, allowing users to choose the route that best matches their priorities.

---

## Breadth First Search (BFS)

Used for graph traversal and exploration.

**Characteristics**

- Visits nodes level by level
- Uses a queue
- Guarantees shortest path only in unweighted graphs

---

## Depth First Search (DFS)

Used for graph traversal.

**Characteristics**

- Explores one path completely before backtracking
- Uses recursion or a stack
- Useful for graph exploration

---

## Dijkstra's Algorithm

Finds the shortest path between two locations.

**Optimization Metric**

- Distance

**Uses**

- GPS navigation
- Network routing
- Path planning

---

## A* Search

A heuristic-based pathfinding algorithm.

**Optimization Metric**

- Distance + heuristic estimate

**Advantages**

- Faster than Dijkstra in many cases
- Explores fewer nodes
- Produces optimal paths with an admissible heuristic

---

## Fastest Path Algorithm

A customized variation of Dijkstra's Algorithm.

Instead of minimizing distance, it minimizes:

- Estimated travel time

Suitable for:

- Traffic-aware routing
- Faster navigation

---

## Safest Path Algorithm

A custom routing algorithm developed for SafeRoute AI.

Instead of optimizing distance, it minimizes:

- Accident Risk
- Road Safety Score

The algorithm selects the safest available route while balancing overall travel efficiency.

---

# 🤖 Machine Learning Risk Prediction

Unlike traditional navigation systems that rely on static risk values, SafeRoute AI incorporates a machine learning model to dynamically adjust road risk.

---

## Model

- Random Forest Regressor

---

## Input Features

- Time of Day
- Weather Conditions
- Speed Limit
- Historical Accident Count

---

## Output

The model predicts a **Risk Multiplier**, which scales the base risk of every road segment before route computation.

This enables the routing algorithms to adapt to changing environmental conditions.

---

# 🏗️ Machine Learning Pipeline

```text
Synthetic Dataset
        │
        ▼
Feature Engineering
        │
        ▼
OneHotEncoder
        │
        ▼
Random Forest Regressor
        │
        ▼
Risk Multiplier
        │
        ▼
Adjusted Road Risk
        │
        ▼
Safest Route
```

---

# 📁 Backend Architecture

```text
app/
│
├── algorithms/
│     BFS
│     DFS
│     Dijkstra
│     A*
│     Fastest Path
│     Safest Path
│
├── api/
│     REST Endpoints
│
├── data/
│     JSON Graph Dataset
│
├── ml/
│     Dataset Generation
│     Model Training
│     Saved ML Model
│
├── models/
│     Graph
│     Road
│     Route
│     Location
│
├── services/
│     Route Service
│     Risk Service
│     ML Risk Service
│     Map Service
│     Coordinate Service
│     Geocode Service
│     Nearest Node Service
│     OSM Service
│
└── main.py
```

---

# ⭐ Project Highlights

- AI-powered route recommendation system
- Risk-aware navigation
- Multiple routing algorithms
- Interactive Leaflet maps
- FastAPI REST backend
- React frontend
- OpenStreetMap integration
- Google Maps support
- Real-world address search
- Dynamic route comparison
- Machine learning-based risk prediction
- Modular service-oriented architecture
- JSON-based graph loading
- Scalable and extensible design

---

# 🎯 Use Cases

SafeRoute AI can be extended for several real-world applications, including:

- Smart city navigation
- Emergency response route planning
- Women's safety navigation
- School and college transportation
- Ambulance route optimization
- Disaster management
- Logistics and delivery planning
- Fleet management systems
- Traffic-aware navigation
- Intelligent transportation systems

---
# 📸 Screenshots

> **Note:** Add screenshots of your application in the `assets/` folder and update the image paths below.

## 🏠 Home Page

![Home Page](assets/home.png)

---

## 🗺️ Interactive Map

![Map](assets/map.png)

---

## 📍 Route Selection

![Route Selection](assets/route-selection.png)

---

## 🛣️ Route Visualization

![Route Visualization](assets/route-visualization.png)

---

## 📊 Route Analytics

Displays:

- Distance
- Travel Time
- Risk Score
- Safety Percentage
- Safety Status
- Safety Warnings

![Analytics](assets/analytics.png)

---

## 📑 Swagger API Documentation

![Swagger](assets/swagger.png)

---

## 🤖 Machine Learning Risk Prediction

![ML](assets/ml-model.png)

---

# 🎥 Demo

A short demonstration of SafeRoute AI.

> **Demo Video:** *(Add YouTube or Google Drive link here)*

```
https://your-demo-link.com
```

---

# 🛣️ Roadmap

### ✅ Completed

- Graph Data Structure
- JSON Graph Loader
- BFS
- DFS
- Dijkstra's Algorithm
- A* Search
- Fastest Route Algorithm
- Safest Route Algorithm
- FastAPI REST API
- Swagger Documentation
- Route Comparison
- React Frontend
- Leaflet Map Integration
- OpenStreetMap Integration
- Google Maps Integration
- Real Address Search
- Nearest Node Matching
- Route Analytics
- Machine Learning Risk Prediction

---

### 🚀 Planned Improvements

- Live Traffic Data Integration
- Real-Time Weather Integration
- Crime Data Integration
- User Authentication
- Save Favorite Routes
- Route History
- Voice Navigation
- Mobile Application
- PostgreSQL/PostGIS Database
- Docker Deployment
- Cloud Deployment
- CI/CD Pipeline
- Real-Time Traffic Alerts
- Multi-City Road Networks
- Multi-Language Support

---

# 💡 Future Scope

SafeRoute AI is designed with scalability in mind and can be extended into a production-ready navigation platform.

Possible future enhancements include:

- Integration with Google Traffic APIs
- Live accident reporting
- IoT-based traffic monitoring
- Emergency vehicle routing
- Smart city infrastructure support
- AI-powered congestion prediction
- Personalized route recommendations
- Electric vehicle route optimization
- Ride-sharing integration
- Navigation for autonomous vehicles

---

# 🤝 Contributing

Contributions are welcome!

If you would like to improve SafeRoute AI:

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature/your-feature
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push to GitHub

```bash
git push origin feature/your-feature
```

5. Open a Pull Request

---

# 🧪 Project Statistics

| Category | Details |
|-----------|---------|
| Backend | FastAPI |
| Frontend | React + Leaflet |
| Machine Learning | Random Forest Regressor |
| Programming Language | Python, JavaScript |
| Routing Algorithms | 6 |
| REST APIs | Multiple Endpoints |
| Address Search | OpenStreetMap Nominatim |
| Map Provider | Leaflet + OpenStreetMap |
| Route Types | Shortest, Fastest, Safest |
| ML Prediction | Risk Multiplier |
| Documentation | Swagger + ReDoc |

---

# 📚 References

The following technologies and resources were used during development:

- FastAPI
- React
- Leaflet
- OpenStreetMap
- OpenStreetMap Nominatim API
- Google Maps
- Scikit-learn
- NumPy
- Python Documentation

---

# 📄 License

This project is licensed under the **MIT License**.

See the [LICENSE](LICENSE) file for more information.

---

# 👩‍💻 Author

**Anushka Yadav**

B.Tech – Artificial Intelligence & Machine Learning

VIT Bhopal University

GitHub: **https://github.com/Anushka4002**

---

# 🙏 Acknowledgements

Special thanks to the open-source community and the developers of:

- FastAPI
- React
- Leaflet
- OpenStreetMap
- Scikit-learn
- NumPy
- Uvicorn

whose tools and documentation made this project possible.

---

# ⭐ Support the Project

If you found this project useful:

- ⭐ Star the repository
- 🍴 Fork the project
- 🐛 Report issues
- 💡 Suggest new features
- 🤝 Contribute to the project

Your support helps improve SafeRoute AI and encourages future development.

---

<div align="center">

## 🛣️ SafeRoute AI

### **Navigate Smarter. Travel Faster. Stay Safer.**

**Built with ❤️ using FastAPI, React, Machine Learning, and OpenStreetMap.**

⭐ **If you like this project, don't forget to star the repository!**

</div>