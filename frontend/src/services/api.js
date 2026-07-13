import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:8000";

export async function getLocations() {
  const response = await axios.get(`${API_BASE_URL}/locations`);
  return response.data;
}

export async function getRoute(algorithm, source, destination) {
  const response = await axios.post(
    `${API_BASE_URL}/route/${algorithm}`,
    { source, destination }
  );
  return response.data;
}

export async function geocodeSearch(query) {
  const response = await axios.get(`${API_BASE_URL}/geocode`, {
    params: { query }
  });
  return response.data;
}

export async function getRouteByAddress(algorithm, source, destination) {
  const response = await axios.post(
    `${API_BASE_URL}/route/address/${algorithm}`,
    { source, destination }
  );
  return response.data;
}