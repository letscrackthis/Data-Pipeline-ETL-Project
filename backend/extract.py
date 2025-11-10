import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("YOUTUBE_API_KEY")

def fetch_trending_videos(region_code="IN", max_results=50):
    url = (
        f"https://youtube.googleapis.com/youtube/v3/videos"
        f"?part=snippet,statistics"
        f"&chart=mostPopular"
        f"&regionCode={region_code}"
        f"&maxResults={max_results}"
        f"&key={API_KEY}"
    )
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raises error for bad status (400, 500, etc.)
        data = response.json()
        
        if "items" not in data:
            raise Exception("No items found in API response. Check quota or API key.")

        return data["items"]
    except requests.exceptions.Timeout:
        raise Exception("Request timed out. Try again later.")
    except requests.exceptions.RequestException as e:
        raise Exception(f"Request failed: {e}")
