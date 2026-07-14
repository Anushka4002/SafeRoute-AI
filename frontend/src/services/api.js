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

export async function compareRoutes(source, destination) {
  const response = await axios.post(
    `${API_BASE_URL}/route/address/compare`,
    { source, destination }
  );
  return response.data;
}

export async function compareRoutesWithConditions(source, destination, timeOfDay, weather) {
  const response = await axios.post(
    `${API_BASE_URL}/route/address/compare-conditions`,
    { source, destination, time_of_day: timeOfDay, weather }
  );
  return response.data;
}