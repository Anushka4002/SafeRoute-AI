import { useEffect, useState } from "react";
import { MapContainer, TileLayer, Marker, Popup, Polyline } from "react-leaflet";
import "leaflet/dist/leaflet.css";
import "./MapView.css";

import { getLocations, getRouteByAddress } from "../services/api";
import AddressInput from "./AddressInput";

const ALGORITHMS = [
  { key: "dijkstra", label: "Shortest Route" },
  { key: "fastest", label: "Fastest Route" },
  { key: "safest", label: "Safest Route" }
];

function MapView() {
  const [locations, setLocations] = useState({});
  const [sourceAddress, setSourceAddress] = useState("");
  const [destinationAddress, setDestinationAddress] = useState("");
  const [step, setStep] = useState("input");
  const [activeAlgorithm, setActiveAlgorithm] = useState("");
  const [routeResult, setRouteResult] = useState(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    getLocations()
      .then((data) => setLocations(data))
      .catch(() => setError("Failed to load locations from backend."));
  }, []);

  const locationList = Object.values(locations);

  const handleContinue = () => {
    setError("");
    if (!sourceAddress || !destinationAddress) {
      setError("Enter both source and destination.");
      return;
    }
    setStep("routes");
    setRouteResult(null);
    setActiveAlgorithm("");
  };

  const handleChange = () => {
    setStep("input");
    setRouteResult(null);
    setActiveAlgorithm("");
    setError("");
  };

  const handleSelectAlgorithm = async (algoKey) => {
    setError("");
    setActiveAlgorithm(algoKey);
    setLoading(true);
    setRouteResult(null);

    try {
      const result = await getRouteByAddress(algoKey, sourceAddress, destinationAddress);
      if (result.error) {
        setError(result.error);
      } else {
        setRouteResult(result);
      }
    } catch (err) {
      setError("Failed to fetch route.");
    }

    setLoading(false);
  };

  const polylinePositions = routeResult
    ? routeResult.coordinates.map((c) => [c.latitude, c.longitude])
    : [];

  if (step === "input") {
    return (
      <div className="landing">
        <div className="landing-card">
          <h1 className="app-title">🛡️ SafeRoute AI</h1>
          <p className="app-subtitle">AI-Powered Accident Risk Route Advisor</p>

          <AddressInput label="Start" onSelect={setSourceAddress} />
          <AddressInput label="Destination" onSelect={setDestinationAddress} />

          <button className="find-btn" onClick={handleContinue}>Show Map</button>

          {error && <p className="error-text">{error}</p>}
        </div>
      </div>
    );
  }

  return (
    <div className="app-container">
      <div className="sidebar">
        <h1 className="app-title">🛡️ SafeRoute AI</h1>

        <p className="route-from-to">
          {sourceAddress} <span>→</span> {destinationAddress}
        </p>
        <button className="change-btn" onClick={handleChange}>Change locations</button>

        <div className="route-buttons">
          {ALGORITHMS.map((algo) => (
            <button
              key={algo.key}
              className={"route-btn" + (activeAlgorithm === algo.key ? " active" : "")}
              onClick={() => handleSelectAlgorithm(algo.key)}
              disabled={loading}
            >
              {algo.label}
            </button>
          ))}
        </div>

        {loading && <p className="loading-text">Finding route...</p>}
        {error && <p className="error-text">{error}</p>}

        {routeResult && (
          <div className="result-card">
            <h3>{routeResult.algorithm}</h3>
            <p className="route-summary">{routeResult.route_summary}</p>

            <div className="stat-grid">
              <div className="stat-box">
                <span className="stat-value">{routeResult.distance}m</span>
                <span className="stat-label">Distance</span>
              </div>
              <div className="stat-box">
                <span className="stat-value">{routeResult.travel_time}s</span>
                <span className="stat-label">Time</span>
              </div>
              <div className="stat-box">
                <span className="stat-value">{routeResult.risk}</span>
                <span className="stat-label">Risk</span>
              </div>
              <div className="stat-box">
                <span className="stat-value">{routeResult.safety_percentage}%</span>
                <span className="stat-label">Safety</span>
              </div>
            </div>

            {routeResult.warnings && routeResult.warnings.length > 0 && (
              <ul className="warnings-list">
                {routeResult.warnings.map((w, idx) => (
                  <li key={idx}>⚠️ {w}</li>
                ))}
              </ul>
            )}

            <p className="snap-note">
              Matched: {routeResult.source_matched_location} → {routeResult.destination_matched_location}
            </p>

            <a className="maps-link" href={routeResult.google_maps_url} target="_blank" rel="noreferrer">
              Open in Google Maps
            </a>
          </div>
        )}
      </div>

      <MapContainer center={[28.6139, 77.2090]} zoom={15} className="map">
        <TileLayer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          attribution="&copy; OpenStreetMap contributors"
        />
        {locationList.map((loc) => (
          <Marker key={loc.id} position={[loc.latitude, loc.longitude]}>
            <Popup>{loc.name}</Popup>
          </Marker>
        ))}
        {routeResult && <Polyline positions={polylinePositions} color="#2563eb" weight={5} />}
      </MapContainer>
    </div>
  );
}

export default MapView;