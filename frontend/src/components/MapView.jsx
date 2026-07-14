import { useEffect, useState } from "react";
import { MapContainer, TileLayer, Marker, Popup, Polyline } from "react-leaflet";
import "leaflet/dist/leaflet.css";
import "./MapView.css";

import { getLocations, compareRoutesWithConditions } from "../services/api";
import AddressInput from "./AddressInput";

const ALGORITHMS = [
  { key: "dijkstra", label: "Shortest Route", color: "#22c55e" },
  { key: "fastest", label: "Fastest Route", color: "#f59e0b" },
  { key: "safest", label: "Safest Route", color: "#2563eb" }
];

function MapView() {
  const [locations, setLocations] = useState({});
  const [sourceAddress, setSourceAddress] = useState("");
  const [destinationAddress, setDestinationAddress] = useState("");
  const [timeOfDay, setTimeOfDay] = useState("afternoon");
  const [weather, setWeather] = useState("clear");
  const [step, setStep] = useState("input");
  const [comparison, setComparison] = useState(null);
  const [visibleRoutes, setVisibleRoutes] = useState({ dijkstra: true, fastest: true, safest: true });
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    getLocations()
      .then((data) => setLocations(data))
      .catch(() => setError("Failed to load locations from backend."));
  }, []);

  const locationList = Object.values(locations);

  const handleContinue = async () => {
    setError("");
    if (!sourceAddress || !destinationAddress) {
      setError("Enter both source and destination.");
      return;
    }

    setLoading(true);
    setComparison(null);

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
    setError("");
  };

  const toggleRoute = (key) => {
    setVisibleRoutes((prev) => ({ ...prev, [key]: !prev[key] }));
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

        <table className="compare-table">
          <thead>
            <tr>
              <th></th>
              <th>Shortest</th>
              <th>Fastest</th>
              <th>Safest</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Distance</td>
              <td>{comparison.routes.dijkstra.distance}m</td>
              <td>{comparison.routes.fastest.distance}m</td>
              <td>{comparison.routes.safest.distance}m</td>
            </tr>
            <tr>
              <td>Time</td>
              <td>{comparison.routes.dijkstra.travel_time}s</td>
              <td>{comparison.routes.fastest.travel_time}s</td>
              <td>{comparison.routes.safest.travel_time}s</td>
            </tr>
            <tr>
              <td>Risk</td>
              <td>{comparison.routes.dijkstra.risk}</td>
              <td>{comparison.routes.fastest.risk}</td>
              <td>{comparison.routes.safest.risk}</td>
            </tr>
            <tr>
              <td>Safety %</td>
              <td>{comparison.routes.dijkstra.safety_percentage}%</td>
              <td>{comparison.routes.fastest.safety_percentage}%</td>
              <td>{comparison.routes.safest.safety_percentage}%</td>
            </tr>
          </tbody>
        </table>

        <div className="route-toggles">
          {ALGORITHMS.map((algo) => (
            <label key={algo.key} className="toggle-row">
              <input
                type="checkbox"
                checked={visibleRoutes[algo.key]}
                onChange={() => toggleRoute(algo.key)}
              />
              <span className="color-dot" style={{ background: algo.color }}></span>
              {algo.label}
            </label>
          ))}
        </div>

        {ALGORITHMS.map((algo) => {
          const route = comparison.routes[algo.key];
          if (!route.warnings || route.warnings.length === 0) return null;
          return (
            <div key={algo.key} className="warning-block">
              <p className="warning-title" style={{ color: algo.color }}>{algo.label} warnings:</p>
              <ul className="warnings-list">
                {route.warnings.map((w, idx) => <li key={idx}>⚠️ {w}</li>)}
              </ul>
            </div>
          );
        })}

        <a
          className="maps-link"
          href={comparison.routes.safest.google_maps_url}
          target="_blank"
          rel="noreferrer"
        >
          Open Safest Route in Google Maps
        </a>
      </div>

      <MapContainer center={[23.25, 77.40]} zoom={11} className="map">
        <TileLayer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          attribution="&copy; OpenStreetMap contributors"
        />

        {locationList.map((loc) => (
          <Marker key={loc.id} position={[loc.latitude, loc.longitude]}>
            <Popup>{loc.name}</Popup>
          </Marker>
        ))}

        {ALGORITHMS.map((algo) => {
          if (!visibleRoutes[algo.key]) return null;
          const route = comparison.routes[algo.key];
          const positions = route.coordinates.map((c) => [c.latitude, c.longitude]);
          return (
            <Polyline
              key={algo.key}
              positions={positions}
              color={algo.color}
              weight={5}
              opacity={0.8}
            />
          );
        })}
      </MapContainer>
    </div>
  );
}

export default MapView;