from config import *
from ingest import (
    load_listings,
    load_calendar,
    load_reviews
)
import logging

logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

print(f"Processing city: {CITY}")

logging.info("Pipeline started")

try:

    print("Loading data")

    listings = load_listings(
        f"{RAW_PATH}/listings.csv"
    )

    calendar = load_calendar(
        f"{RAW_PATH}/calendar.csv"
    )

    reviews = load_reviews(
        f"{RAW_PATH}/reviews.csv"
    )

    logging.info(
        "Data loaded successfully"
    )

except Exception as e:

    logging.error(
        f"Loading failed: {e}"
    )

    raise