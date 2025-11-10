# main.py
import logging
from extract import fetch_trending_videos
from transform import transform_data
from load import load_data
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_pipeline():
    logging.info(" Starting YouTube Trending Pipeline")
    regions = ["IN", "US"]  # You can add more regions here!

    for region in regions:
        logging.info(f" Fetching trending videos for region: {region}")
        raw = fetch_trending_videos(region)
        logging.info(f" Fetched {len(raw)} videos for region: {region}")

        logging.info(" Transforming data...")
        df = transform_data(raw, region)

        logging.info(" Loading data into database...")
        load_data(df)

    logging.info(" Pipeline completed successfully!")

if __name__ == "__main__":
    run_pipeline()
