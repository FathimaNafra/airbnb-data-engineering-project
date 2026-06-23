import pandas as pd


def calculate_occupancy(calendar):

    occupancy = (
        calendar.groupby(
            "listing_id"
        )["available"]
        .apply(
            lambda x:
            (x == "f").sum()
            / len(x)
        )
        .reset_index()
    )

    occupancy.columns = [
        "listing_id",
        "occupancy_rate"
    ]

    return occupancy

#Revenue Estimate
def revenue_estimate(df):

    df["estimated_revenue"] = (
        df["price"]
        * 365
        * df["occupancy_rate"]
    )

    return df

#Host Tenure
def host_tenure(df):

    current_year = 2026

    df["host_tenure_years"] = (
        current_year
        - df["host_since"].dt.year
    )

    return df

#Join Data
occupancy = calculate_occupancy(
    calendar
)

master = listings.merge(
    occupancy,
    left_on="id",
    right_on="listing_id",
    how="left"
)

master = revenue_estimate(master)

master = host_tenure(master)


master.to_csv(
    "data/curated/listing_master.csv",
    index=False
)