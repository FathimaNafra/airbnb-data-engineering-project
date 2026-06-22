import pandas as pd


def load_listings(path):
    return pd.read_csv(path)


def load_calendar(path):
    return pd.read_csv(path)


def load_reviews(path):
    return pd.read_csv(path)