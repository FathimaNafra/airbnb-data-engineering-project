from config import *
from ingest import (
    load_listings,
    load_calendar,
    load_reviews
)
import logging
import time
from datetime import datetime


with open(
    "data/metadata/last_run.txt"
) as f:

    last_run = f.read().strip()


logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
#Add Retry Function
def retry(func, retries=3):

    for attempt in range(retries):

        try:
            return func()

        except Exception as e:

            logging.warning(
                f"Attempt {attempt + 1} failed: {e}"
            )

            time.sleep(2)

    raise Exception(
        "Maximum retries exceeded"
    )

print(f"Processing city: {CITY}")

logging.info("Pipeline started")

try:

    print("Loading data")

    listings = retry(
    lambda: load_listings(
        f"{RAW_PATH}/listings.csv"
    )
)

    calendar = retry(
    lambda: load_calendar(
        f"{RAW_PATH}/calendar.csv"
    )
)

    reviews = retry(
    lambda: load_reviews(
        f"{RAW_PATH}/reviews.csv"
    )
)

    logging.info(
        "Data loaded successfully"
    )

except Exception as e:

    logging.error(
        f"Loading failed: {e}"
    )

    raise

with open(
    "data/metadata/last_run.txt",
    "w"
) as f:

    f.write(
        str(datetime.today().date())
    )