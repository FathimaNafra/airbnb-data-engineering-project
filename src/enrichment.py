import pandas as pd


def load_data():

    listings = pd.read_csv(
        "../data/processed/listings_clean.csv"
    )

    calendar = pd.read_csv(
        "../data/processed/calendar_clean.csv"
    )

    reviews = pd.read_csv(
        "../data/processed/reviews_clean.csv"
    )

    return listings, calendar, reviews

def calculate_occupancy(calendar):

    calendar["booked"] = (
        calendar["available"]
        .map(
            {
                "f": 1,
                "t": 0
            }
        )
    )

    occupancy = (
        calendar
        .groupby("listing_id")
        ["booked"]
        .mean()
        .reset_index()
    )

    occupancy.rename(
        columns={
            "booked":
            "occupancy_rate"
        },
        inplace=True
    )

    return occupancy