from sqlalchemy import create_engine, Table, MetaData
from datetime import datetime

engine = create_engine("sqlite:///youtube_trending.db")
metadata = MetaData()

def load_data(df):
    df["run_date"] = datetime.now().date()

    df.to_sql("trending_videos", engine, if_exists="append", index=False)
