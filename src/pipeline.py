from config import *
import logging

logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

print(f"Processing city: {CITY}")

logging.info("Pipeline started")