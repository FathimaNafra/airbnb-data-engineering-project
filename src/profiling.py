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

def check_duplicates(df):

    duplicates = df.duplicated().sum()

    print(
        f"Duplicate Rows: {duplicates}"
    )

    return duplicates

def detect_outliers_iqr(df, column):

    q1 = df[column].quantile(0.25)

    q3 = df[column].quantile(0.75)

    iqr = q3 - q1

    lower = q1 - (1.5 * iqr)

    upper = q3 + (1.5 * iqr)

    outliers = df[
        (df[column] < lower)
        | (df[column] > upper)
    ]

    return outliers