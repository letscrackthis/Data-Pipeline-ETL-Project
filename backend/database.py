# DB schema and connection

from sqlalchemy import create_engine, Column, String, Integer, DateTime, MetaData, Table
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///trending_videos.db"
engine = create_engine(DATABASE_URL)
metadata = MetaData()

trending_videos = Table(
    'trending_videos', metadata,
    Column('video_id', String, primary_key=True),
    Column('title', String),
    Column('channel', String),
    Column('published_at', DateTime),
    Column('view_count', Integer),
    Column('like_count', Integer),
    Column('comment_count', Integer),
    Column('category_id', Integer),
)

metadata.create_all(engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
