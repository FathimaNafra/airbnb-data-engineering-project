import pandas as pd

import os
print(os.getcwd())

from enrichment import (
    calculate_occupancy,
    revenue_estimate,
    host_tenure
)

# Load data
listings = pd.read_csv(
    "../data/raw/london/listings.csv"
)

calendar = pd.read_csv(
    "../data/raw/london/calendar.csv"
)

# Convert date
listings["host_since"] = pd.to_datetime(
    listings["host_since"],
    errors="coerce"
)

# Occupancy
occupancy = calculate_occupancy(calendar)

# Join
master = listings.merge(
    occupancy,
    left_on="id",
    right_on="listing_id",
    how="left"
)

# Features
master = revenue_estimate(master)

master = host_tenure(master)

# Save
master.to_csv(
    "../data/curated/listing_master.csv",
    index=False
)

print("Master dataset created successfully!")