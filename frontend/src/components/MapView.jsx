import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import "leaflet/dist/leaflet.css";

const dummyLocations = [
  { id: 1, name: "College", latitude: 28.6139, longitude: 77.2090 },
  { id: 2, name: "Mall", latitude: 28.6151, longitude: 77.2132 },
  { id: 3, name: "Library", latitude: 28.6168, longitude: 77.2145 },
  { id: 4, name: "Hospital", latitude: 28.6180, longitude: 77.2164 },
  { id: 5, name: "Police Station", latitude: 28.6201, longitude: 77.2180 }
];

function MapView() {
  return (
    <MapContainer
      center={[28.6139, 77.2090]}
      zoom={15}
      style={{ height: "100vh", width: "100%" }}
    >
      <TileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        attribution="&copy; OpenStreetMap contributors"
      />
      {dummyLocations.map((loc) => (
        <Marker key={loc.id} position={[loc.latitude, loc.longitude]}>
          <Popup>{loc.name}</Popup>
        </Marker>
      ))}
    </MapContainer>
  );
}

export default MapView;