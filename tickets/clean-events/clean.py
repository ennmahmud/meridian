import pandas as pd


def clean_events(path="data/events.csv"):
    df = pd.read_csv(path)
    df = df.drop_duplicates()
    df = df.dropna(subset=["event_type"])
    df["event_date"] = pd.to_datetime(df["event_date"])
    return df
