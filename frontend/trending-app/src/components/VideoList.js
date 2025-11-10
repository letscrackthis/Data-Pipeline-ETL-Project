import React, { useEffect, useState } from "react";

const VideoList = () => {
  const [videos, setVideos] = useState([]);
  const [loading, setLoading] = useState(true);
  const [err, setErr] = useState(null);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/trending")
      .then(res => {
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        return res.json();
      })
      .then(data => { setVideos(data); setLoading(false); })
      .catch(e => { setErr(e.message); setLoading(false); });
  }, []);

  if (loading) return <p>Loading...</p>;
  if (err) return <p>Error: {err}</p>;
  if (!videos.length) return <p>No data yet.</p>;

  return (
    <div style={{padding:20}}>
      <h2>Trending Videos</h2>
      <ul>
        {videos.map((v, i) => (
          <li key={i}>
            <strong>{v.title ?? v.title}</strong><br/>
            Channel: {v.channel ?? v.channel}<br/>
            Views: {v.view_count ?? v.viewCount ?? v.views}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default VideoList;
