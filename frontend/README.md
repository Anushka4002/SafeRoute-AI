# 🎨 SafeRoute AI Frontend

> **A React + Leaflet based interactive frontend for SafeRoute AI that enables users to search locations, compare routes, and visualize navigation results on an interactive map.**

---

# 📖 Overview

The SafeRoute AI Frontend provides an intuitive user interface for interacting with the SafeRoute AI backend.

Users can search real-world locations, choose different routing strategies, visualize routes on an interactive map, and compare the safest, fastest, and shortest routes.

The frontend communicates with the FastAPI backend through REST APIs and displays route analytics such as distance, travel time, safety score, and warnings.

---

# ✨ Features

## 🗺️ Interactive Map

- Interactive map powered by Leaflet
- OpenStreetMap tiles
- Smooth zooming and panning
- Route visualization

---

## 📍 Address Search

- Search real-world locations
- Auto-complete suggestions
- Select source and destination
- Backend geocoding integration

---

## 🚗 Route Planning

Supports multiple routing algorithms:

- Shortest Route
- Fastest Route
- Safest Route

Users can also compare all routes simultaneously.

---

## 📊 Route Analytics

Displays:

- Total Distance
- Estimated Travel Time
- Risk Score
- Safety Percentage
- Safety Status
- Safety Warnings
- Route Summary

---

## 📌 Map Features

- Custom Start Marker
- Custom Destination Marker
- Intermediate Route Markers
- Colored Route Polylines
- Google Maps Link
- OpenStreetMap Link

---

## ⚡ Fast API Communication

The frontend communicates with the FastAPI backend using REST APIs for:

- Route Generation
- Address Search
- Route Comparison
- ML Risk Prediction

---

# 🛠️ Technology Stack

| Technology | Purpose |
|------------|----------|
| React | User Interface |
| Vite | Build Tool |
| JavaScript | Application Logic |
| Leaflet | Interactive Maps |
| React Leaflet | React Map Components |
| CSS | Styling |
| Axios / Fetch API | Backend Communication |

---

# 📂 Folder Structure

```text
frontend/
│
├── public/
│
├── src/
│   ├── assets/
│   ├── components/
│   │   ├── Header.jsx
│   │   ├── MapView.jsx
│   │   ├── RouteInfo.jsx
│   │   ├── SearchBox.jsx
│   │   └── Loading.jsx
│   │
│   ├── pages/
│   │   └── Home.jsx
│   │
│   ├── services/
│   │   └── api.js
│   │
│   ├── App.jsx
│   ├── main.jsx
│   └── index.css
│
├── package.json
├── vite.config.js
└── README.md
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Anushka4002/SafeRoute-AI.git
```

Move to the frontend directory:

```bash
cd SafeRoute-AI/frontend
```

Install dependencies:

```bash
npm install
```

Run the development server:

```bash
npm run dev
```

The frontend will start at:

```
http://localhost:5173
```

---

# 🔗 Backend Connection

Before running the frontend, ensure the backend server is running.

Backend URL:

```
http://127.0.0.1:8000
```

Update the API base URL in your service file if required.

Example:

```javascript
const API_BASE_URL = "http://127.0.0.1:8000";
```

---

# 🖥️ User Workflow

```text
User Opens Application
          │
          ▼
Search Source Location
          │
          ▼
Search Destination
          │
          ▼
Select Route Type
          │
          ▼
API Request
          │
          ▼
FastAPI Backend
          │
          ▼
Receive Route Data
          │
          ▼
Display Route on Map
          │
          ▼
Show Route Analytics
```

---

# 🎯 Route Types

## 🛣️ Shortest Route

Optimizes total travel distance.

---

## ⚡ Fastest Route

Optimizes estimated travel time.

---

## 🛡️ Safest Route

Optimizes road safety using accident risk analysis.

---

## 📊 Compare Routes

Displays all routing options together for easy comparison.

---

# 🗺️ Map Visualization

The application displays:

- Source Marker
- Destination Marker
- Route Polyline
- Intermediate Stops
- Route Summary
- Interactive Popups

Different route types can be represented using different polyline colors to improve readability.

---

# 📊 Information Displayed

For every generated route, the frontend displays:

| Property | Description |
|----------|-------------|
| Distance | Total travel distance |
| Travel Time | Estimated journey duration |
| Risk Score | Overall route risk |
| Safety Percentage | Route safety score |
| Safety Status | Safe / Moderate / Dangerous |
| Warnings | Safety alerts |
| Route Summary | Human-readable path |
| Google Maps | External navigation link |
| OpenStreetMap | Route visualization link |

---

# 🌐 API Integration

The frontend communicates with the following backend endpoints:

| Endpoint | Purpose |
|----------|----------|
| `/locations` | Fetch available locations |
| `/geocode` | Search addresses |
| `/route/address/dijkstra` | Shortest route |
| `/route/address/astar` | A* route |
| `/route/address/fastest` | Fastest route |
| `/route/address/safest` | Safest route |
| `/route/address/compare` | Compare routes |
| `/route/address/compare-conditions` | ML-based route comparison |

---

# 📸 Screenshots

> Add screenshots inside the `assets/` folder.

### Home Page

```text
assets/home.png
```

---

### Interactive Map

```text
assets/map.png
```

---

### Route Comparison

```text
assets/compare.png
```

---

### Route Analytics

```text
assets/analytics.png
```

---

# 🚀 Future Improvements

- Dark Mode
- Responsive Mobile UI
- Voice Navigation
- Live Traffic Layer
- Live Weather Overlay
- Saved Routes
- User Authentication
- Route History
- Real-Time Notifications
- Progressive Web App (PWA)

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a new branch.

```bash
git checkout -b feature/your-feature
```

3. Commit your changes.

```bash
git commit -m "Add new feature"
```

4. Push the branch.

```bash
git push origin feature/your-feature
```

5. Open a Pull Request.

---

# 📄 License

This project is licensed under the MIT License.

See the LICENSE file for more information.

---

# 👩‍💻 Author

**Anushka Yadav**

B.Tech – Artificial Intelligence & Machine Learning

VIT Bhopal University

GitHub: https://github.com/Anushka4002

---

<div align="center">

## 🎨 SafeRoute AI Frontend

**Interactive • Responsive • Intelligent**

Built with **React**, **Leaflet**, and **FastAPI**.

</div>