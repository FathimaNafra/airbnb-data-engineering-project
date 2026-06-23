import pandas as pd


def clean_price(df):

    df["price"] = (
        df["price"]
        .astype(str)
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False)
    )

    df["price"] = pd.to_numeric(
        df["price"],
        errors="coerce"
    )

    return df


def convert_dates(df, column):

    df[column] = pd.to_datetime(
        df[column],
        errors="coerce"
    )

    return df


def standardize_text(df, column):

    df[column] = (
        df[column]
        .astype(str)
        .str.strip()
        .str.title()
    )

    return df