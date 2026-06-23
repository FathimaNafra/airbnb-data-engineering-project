import duckdb
import pandas as pd
#Loading master dataset
master = pd.read_csv(
    "data/processed/listing_master.csv"
)

#create database

conn = duckdb.connect(
    "data/airbnb_warehouse.duckdb"
)

#Create Host Dimension

dim_host = master[
    [
        "host_id",
        "host_name",
        "host_since",
        "host_tenure_years"
    ]
].drop_duplicates()

print(dim_host.head())

conn.register(
    "dim_host_df",
    dim_host
)

conn.execute("""
CREATE OR REPLACE TABLE dim_host AS
SELECT *
FROM dim_host_df
""")

#Create Listing Dimension

dim_listing = master[
    [
        "id",
        "name",
        "room_type",
        "bedrooms"
    ]
].drop_duplicates()

conn.register(
    "dim_listing_df",
    dim_listing
)

conn.execute("""
CREATE OR REPLACE TABLE dim_listing AS
SELECT *
FROM dim_listing_df
""")

#Create Neighbourhood Dimension
dim_neighbourhood = master[
    [
        "neighbourhood_cleansed",
        "median_price",
        "listing_density",
        "average_rating"
    ]
].drop_duplicates()

conn.register(
    "dim_neighbourhood_df",
    dim_neighbourhood
)

conn.execute("""
CREATE OR REPLACE TABLE dim_neighbourhood AS
SELECT *
FROM dim_neighbourhood_df
""")

