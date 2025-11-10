// src/api/api.js
import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000", // FastAPI backend URL
});

export default api;
