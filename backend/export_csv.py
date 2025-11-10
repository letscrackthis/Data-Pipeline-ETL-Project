import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

engine = create_engine("sqlite:///youtube_trending.db")

def export_to_csv():
    df = pd.read_sql_table("trending_videos", con=engine)
    file_name = f"trending_videos_{datetime.now().strftime('%Y%m%d')}.csv"
    df.to_csv(file_name, index=False)
    print(f"✅ Exported data to {file_name}")

if __name__ == "__main__":
    export_to_csv()
