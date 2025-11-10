import React, { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [videos, setVideos] = useState([]);
  const [error, setError] = useState("");

  useEffect(() => {
    // Fetch trending videos from FastAPI backend
    fetch("http://localhost:8000/videos")
      .then((res) => {
        if (!res.ok) {
          throw new Error(`HTTP ${res.status}`);
        }
        return res.json();
      })
      .then((data) => {
        setVideos(data);
      })
      .catch((err) => {
        console.error("Error fetching videos:", err);
        setError(err.message);
      });
  }, []);

  return (
    <div className="App">
      <h1>YouTube Trending Dashboard</h1>

      {error && <p style={{ color: "red" }}>Error: {error}</p>}

      {!error && videos.length === 0 && <p>Loading trending videos...</p>}

      <div className="video-list">
        {videos.map((video, index) => (
          <div key={index} className="video-card">
            <h3>{video.title}</h3>
            <p>Channel: {video.channel}</p>
            <p>Views: {video.views}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
