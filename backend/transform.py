from datetime import datetime  # ✅ Add this if missing
import pandas as pd

def transform_data(raw_items, region):
    rows = []
    for item in raw_items:
        published_at = item["snippet"]["publishedAt"]

        # ✅ Convert string to datetime object
        published_at = datetime.strptime(published_at, "%Y-%m-%dT%H:%M:%SZ")

        rows.append({
            "video_id": item["id"],
            "title": item["snippet"]["title"],
            "channel": item["snippet"]["channelTitle"],
            "published_at": published_at,
            "view_count": int(item["statistics"].get("viewCount", 0)),
            "like_count": int(item["statistics"].get("likeCount", 0)),
            "comment_count": int(item["statistics"].get("commentCount", 0)),
            "category_id": int(item["snippet"]["categoryId"]),
            "region": region
        })

    return pd.DataFrame(rows)
