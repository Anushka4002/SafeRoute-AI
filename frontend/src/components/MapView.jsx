import { useEffect, useState } from "react";
import { MapContainer, TileLayer, Marker, Popup, Polyline } from "react-leaflet";
import "leaflet/dist/leaflet.css";

import { getLocations, getRoute } from "../services/api";

function MapView() {
  const [locations, setLocations] = useState({});
  const [source, setSource] = useState("");
  const [destination, setDestination] = useState("");
  const [algorithm, setAlgorithm] = useState("dijkstra");
  const [routeResult, setRouteResult] = useState(null);
  const [error, setError] = useState("");

  useEffect(() => {
    getLocations()
      .then((data) => setLocations(data))
      .catch(() => setError("Failed to load locations from backend."));
  }, []);

  const locationList = Object.values(locations);

  const handleFindRoute = async () => {
    setError("");
    setRouteResult(null);

    if (!source || !destination) {
      setError("Select both source and destination.");
      return;
    }

    try {
      const result = await getRoute(
        algorithm,
        Number(source),
        Number(destination)
      );
      setRouteResult(result);
    } catch (err) {
      setError("Failed to fetch route.");
    }
  };

  const polylinePositions = routeResult
    ? routeResult.coordinates.map((c) => [c.latitude, c.longitude])
    : [];

  return (
    <div style={{ display: "flex", height: "100vh", width: "100%" }}>
      <div style={{ width: "300px", padding: "16px", overflowY: "auto" }}>
        <h3>SafeRoute AI</h3>

        <label>Source</label>
        <select value={source} onChange={(e) => setSource(e.target.value)}>
          <option value="">-- Select --</option>
          {locationList.map((loc) => (
            <option key={loc.id} value={loc.id}>{loc.name}</option>
          ))}
        </select>

        <br /><br />

        <label>Destination</label>
        <select value={destination} onChange={(e) => setDestination(e.target.value)}>
          <option value="">-- Select --</option>
          {locationList.map((loc) => (
            <option key={loc.id} value={loc.id}>{loc.name}</option>
          ))}
        </select>

        <br /><br />

        <label>Algorithm</label>
        <select value={algorithm} onChange={(e) => setAlgorithm(e.target.value)}>
          <option value="dijkstra">Dijkstra</option>
          <option value="astar">A*</option>
          <option value="safest">Safest Route</option>
        </select>

        <br /><br />

        <button onClick={handleFindRoute}>Find Route</button>

        {error && <p style={{ color: "red" }}>{error}</p>}

        {routeResult && (
          <div style={{ marginTop: "16px" }}>
            <p><b>Algorithm:</b> {routeResult.algorithm}</p>
            <p><b>Route:</b> {routeResult.route_summary}</p>
            <p><b>Distance:</b> {routeResult.distance}</p>
            <p><b>Risk:</b> {routeResult.risk}</p>
            <p><b>Safety %:</b> {routeResult.safety_percentage}</p>
            <p><a href={routeResult.google_maps_url} target="_blank">Open in Google Maps</a></p>
          </div>
        )}
      </div>

      <MapContainer
        center={[28.6139, 77.2090]}
        zoom={15}
        style={{ height: "100%", flex: 1 }}
      >
        <TileLayer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          attribution="&copy; OpenStreetMap contributors"
        />

        {locationList.map((loc) => (
          <Marker key={loc.id} position={[loc.latitude, loc.longitude]}>
            <Popup>{loc.name}</Popup>
          </Marker>
        ))}

        {routeResult && (
          <Polyline positions={polylinePositions} color="blue" />
        )}
      </MapContainer>
    </div>
  );
}

export default MapView;