import { useEffect, useState } from "react";
import { MapContainer, TileLayer, Marker, Popup, Polyline } from "react-leaflet";
import L from "leaflet";
import "leaflet/dist/leaflet.css";
import "./MapView.css";

import { getLocations, compareRoutesWithConditions } from "../services/api";
import AddressInput from "./AddressInput";

const ALGORITHMS = [
  { key: "fastest", label: "Fastest Route", color: "#2563eb" },
  { key: "safest", label: "Safest Route", color: "#22c55e" }
];

const startIcon = L.divIcon({
  className: "",
  html: `<div style="width:18px;height:18px;background:#22c55e;border:3px solid white;border-radius:50%;box-shadow:0 2px 6px rgba(0,0,0,0.4)"></div>`,
  iconSize: [18, 18],
  iconAnchor: [9, 9]
});

const endIcon = L.divIcon({
  className: "",
  html: `<div style="width:18px;height:18px;background:#ef4444;border:3px solid white;border-radius:50%;box-shadow:0 2px 6px rgba(0,0,0,0.4)"></div>`,
  iconSize: [18, 18],
  iconAnchor: [9, 9]
});

const waypointIcon = L.divIcon({
  className: "",
  html: `<div style="width:12px;height:12px;background:#2563eb;border:2px solid white;border-radius:50%;box-shadow:0 2px 4px rgba(0,0,0,0.3)"></div>`,
  iconSize: [12, 12],
  iconAnchor: [6, 6]
});

async function fetchRoadGeometry(coordinates) {
  const waypoints = coordinates
    .map((c) => `${c.longitude},${c.latitude}`)
    .join(";");

  const url = `https://router.project-osrm.org/route/v1/driving/${waypoints}?overview=full&geometries=geojson`;

  try {
    const response = await fetch(url);
    const data = await response.json();
    if (data.routes && data.routes.length > 0) {
      return data.routes[0].geometry.coordinates.map(([lon, lat]) => [lat, lon]);
    }
  } catch (err) {
    console.error("Failed to fetch road geometry", err);
  }

  return coordinates.map((c) => [c.latitude, c.longitude]);
}

function MapView() {
  const [locations, setLocations] = useState({});
  const [sourceAddress, setSourceAddress] = useState("");
  const [destinationAddress, setDestinationAddress] = useState("");
  const [timeOfDay, setTimeOfDay] = useState("afternoon");
  const [weather, setWeather] = useState("clear");
  const [step, setStep] = useState("input");
  const [comparison, setComparison] = useState(null);
  const [roadGeometries, setRoadGeometries] = useState({});
  const [selectedRoute, setSelectedRoute] = useState("safest");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const [geometryLoading, setGeometryLoading] = useState(false);

  useEffect(() => {
    getLocations()
      .then((data) => setLocations(data))
      .catch(() => setError("Failed to load locations from backend."));
  }, []);

  useEffect(() => {
    if (!comparison) return;

    async function loadGeometries() {
      setGeometryLoading(true);
      const geometries = {};
      for (const algo of ALGORITHMS) {
        const route = comparison.routes[algo.key];
        geometries[algo.key] = await fetchRoadGeometry(route.coordinates);
      }
      setRoadGeometries(geometries);
      setGeometryLoading(false);
    }

    loadGeometries();
  }, [comparison]);

  const locationList = Object.values(locations);

  const handleContinue = async () => {
    setError("");
    if (!sourceAddress || !destinationAddress) {
      setError("Enter both source and destination.");
      return;
    }

    setLoading(true);
    setComparison(null);
    setRoadGeometries({});

    try {
      const result = await compareRoutesWithConditions(
        sourceAddress,
        destinationAddress,
        timeOfDay,
        weather
      );
      if (result.error) {
        setError(result.error);
      } else {
        setComparison(result);
        setStep("routes");
      }
    } catch (err) {
      setError("Failed to fetch routes.");
    }

    setLoading(false);
  };

  const handleChange = () => {
    setStep("input");
    setComparison(null);
    setRoadGeometries({});
    setError("");
  };

  if (step === "input") {
    return (
      <div className="landing">
        <div className="landing-card">
          <h1 className="app-title">🛡️ SafeRoute AI</h1>
          <p className="app-subtitle">AI-Powered Accident Risk Route Advisor</p>

          <AddressInput label="Start" onSelect={setSourceAddress} />
          <AddressInput label="Destination" onSelect={setDestinationAddress} />

          <label className="field-label">Time of Day</label>
          <select className="algo-select" value={timeOfDay} onChange={(e) => setTimeOfDay(e.target.value)}>
            <option value="morning">Morning</option>
            <option value="afternoon">Afternoon</option>
            <option value="evening">Evening</option>
            <option value="night">Night</option>
          </select>

          <label className="field-label">Weather</label>
          <select className="algo-select" value={weather} onChange={(e) => setWeather(e.target.value)}>
            <option value="clear">Clear</option>
            <option value="rainy">Rainy</option>
            <option value="foggy">Foggy</option>
          </select>

          <button className="find-btn" onClick={handleContinue} disabled={loading}>
            {loading ? "Comparing Routes..." : "Show Map"}
          </button>

          {error && <p className="error-text">{error}</p>}
        </div>
      </div>
    );
  }

  const activeRoute = comparison.routes[selectedRoute];
  const activeAlgo = ALGORITHMS.find((a) => a.key === selectedRoute);

  return (
    <div className="app-container">
      <div className="sidebar">
        <h1 className="app-title">🛡️ SafeRoute AI</h1>

        <p className="route-from-to">
          {comparison.source_matched_location} <span>→</span> {comparison.destination_matched_location}
        </p>
        <button className="change-btn" onClick={handleChange}>Change locations</button>

        <p className="ml-note">
          AI Risk Multiplier ({comparison.conditions.time_of_day}, {comparison.conditions.weather}):{" "}
          <b>{comparison.risk_multiplier}×</b>
        </p>

        {error && <p className="error-text">{error}</p>}
        {geometryLoading && <p className="loading-text">Loading road paths...</p>}

        <div className="route-buttons">
          {ALGORITHMS.map((algo) => (
            <button
              key={algo.key}
              className={"route-btn" + (selectedRoute === algo.key ? " active" : "")}
              style={selectedRoute === algo.key
                ? { borderColor: algo.color, background: algo.color, color: "white" }
                : { borderColor: algo.color, color: algo.color }
              }
              onClick={() => setSelectedRoute(algo.key)}
            >
              <span className="route-btn-dot" style={{ background: algo.color }}></span>
              {algo.label}
            </button>
          ))}
        </div>

        {activeRoute && (
          <div className="result-card">
            <h3 style={{ color: activeAlgo.color }}>{activeRoute.algorithm}</h3>
            <p className="route-summary">{activeRoute.route_summary}</p>

            <div className="stat-grid">
              <div className="stat-box">
                <span className="stat-value">{activeRoute.distance}m</span>
                <span className="stat-label">Distance</span>
              </div>
              <div className="stat-box">
                <span className="stat-value">{activeRoute.travel_time}s</span>
                <span className="stat-label">Time</span>
              </div>
              <div className="stat-box">
                <span className="stat-value">{activeRoute.risk}</span>
                <span className="stat-label">Risk</span>
              </div>
              <div className="stat-box">
                <span className="stat-value">{activeRoute.safety_percentage}%</span>
                <span className="stat-label">Safety</span>
              </div>
            </div>

            {activeRoute.warnings && activeRoute.warnings.length > 0 && (
              <ul className="warnings-list">
                {activeRoute.warnings.map((w, idx) => (
                  <li key={idx}>⚠️ {w}</li>
                ))}
              </ul>
            )}

            <a
              className="maps-link"
              href={activeRoute.google_maps_url}
              target="_blank"
              rel="noreferrer"
            >
              Open in Google Maps
            </a>
          </div>
        )}
      </div>

      <MapContainer center={[23.25, 77.40]} zoom={11} className="map">
        <TileLayer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          attribution="&copy; OpenStreetMap contributors"
        />

        {locationList.map((loc) => {
          const isStart = activeRoute &&
            activeRoute.path[0] === loc.name;
          const isEnd = activeRoute &&
            activeRoute.path[activeRoute.path.length - 1] === loc.name;

          const icon = isStart ? startIcon : isEnd ? endIcon : waypointIcon;

          return (
            <Marker
              key={loc.id}
              position={[loc.latitude, loc.longitude]}
              icon={icon}
            >
              <Popup>
                <b>{loc.name}</b>
                {isStart && <span> 🟢 Start</span>}
                {isEnd && <span> 🔴 End</span>}
              </Popup>
            </Marker>
          );
        })}

        {ALGORITHMS.map((algo) => {
          if (algo.key !== selectedRoute) return null;
          const positions = roadGeometries[algo.key];
          if (!positions) return null;
          return (
            <Polyline
              key={algo.key}
              positions={positions}
              color={algo.color}
              weight={6}
              opacity={0.9}
            />
          );
        })}
      </MapContainer>
    </div>
  );
}

export default MapView;