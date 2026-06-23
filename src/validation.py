import pandas as pd


def validate_price(df):
    # Convert price to numeric (remove $ and commas)
    price_numeric = pd.to_numeric(
        df['price'].astype(str).str.replace('$', '').str.replace(',', ''),
        errors='coerce'
    )
    
    invalid = df[price_numeric < 0]

    return invalid


def validate_latitude(df):

    invalid = df[
        (df["latitude"] < -90)
        | (df["latitude"] > 90)
    ]

    return invalid


def validate_longitude(df):

    invalid = df[
        (df["longitude"] < -180)
        | (df["longitude"] > 180)
    ]

    return invalid