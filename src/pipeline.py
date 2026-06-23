from config import *
from ingest import (
    load_listings,
    load_calendar,
    load_reviews
)
from metadata import log_metadata

import logging
import time
from datetime import datetime
import pandas as pd


# Configure Logging
logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# Retry Function
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

    # Load datasets with retry logic
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

    logging.info("Data loaded successfully")

    # Metadata Tracking
    log_metadata(
        "listings",
        "success",
        len(listings)
    )

    log_metadata(
        "calendar",
        "success",
        len(calendar)
    )

    log_metadata(
        "reviews",
        "success",
        len(reviews)
    )

    # Incremental Processing
    with open(
        "data/metadata/last_run.txt"
    ) as f:

        last_run = f.read().strip()

    calendar["date"] = pd.to_datetime(
        calendar["date"]
    )

    calendar_new = calendar[
        calendar["date"] > pd.to_datetime(last_run)
    ]

    print(
        f"New calendar records: {len(calendar_new)}"
    )

    logging.info(
        f"New calendar records: {len(calendar_new)}"
    )

    # Update last run date
    with open(
        "data/metadata/last_run.txt",
        "w"
    ) as f:

        f.write(
            str(datetime.today().date())
        )

    logging.info(
        "Pipeline completed successfully"
    )

except Exception as e:

    logging.error(
        f"Pipeline failed: {e}"
    )

    raise