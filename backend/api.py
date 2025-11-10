from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import os

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

YOUTUBE_API_KEY = "AIzaSyCpnDYIH_jNzh1FBbxBbeynSKn6QZW4c2Y"  # Replace with your actual API key

@app.get("/")
def root():
    return {"message": "YouTube Trending API running!"}


@app.get("/videos")
def get_trending_videos():
    try:
        # API endpoint for trending videos
        url = (
            f"https://www.googleapis.com/youtube/v3/videos"
            f"?part=snippet,statistics"
            f"&chart=mostPopular"
            f"&regionCode=IN"  # You can change region (e.g., US, GB)
            f"&maxResults=10"
            f"&key={YOUTUBE_API_KEY}"
        )

        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        trending_videos = []

        for item in data.get("items", []):
            trending_videos.append({
                "title": item["snippet"]["title"],
                "channel": item["snippet"]["channelTitle"],
                "views": item["statistics"].get("viewCount", "N/A"),
                "thumbnail": item["snippet"]["thumbnails"]["medium"]["url"],
                "url": f"https://www.youtube.com/watch?v={item['id']}"
            })

        return trending_videos

    except Exception as e:
        return {"error": str(e)}
