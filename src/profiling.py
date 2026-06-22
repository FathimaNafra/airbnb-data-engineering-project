import pandas as pd


def profile_dataframe(df, name):

    profile = {
        "dataset": name,
        "rows": len(df),
        "columns": len(df.columns),
        "missing_values": df.isnull().sum().sum(),
        "duplicate_rows": df.duplicated().sum()
    }

    return profile