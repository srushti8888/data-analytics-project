
import pandas as pd
import numpy as np
from pathlib import Path


# Project folders
BASE_DIR = Path(__file__).resolve().parent
DATASET_PATH = BASE_DIR / "dataset" / "netflix_titles.csv"
OUTPUT_PATH = BASE_DIR / "output" / "netflix_cleaned.csv"


def load_data():
    """Load the original Netflix CSV file."""

    if not DATASET_PATH.exists():
        raise FileNotFoundError(
            f"Dataset not found: {DATASET_PATH}"
        )

    return pd.read_csv(DATASET_PATH)


def clean_data(df):
    """Clean the Netflix dataset."""

    df = df.copy()

    # Remove unwanted spaces from column names
    df.columns = df.columns.str.strip()

    # Remove duplicate records
    df = df.drop_duplicates()

    # Handle missing categorical values
    for column in ["director", "cast", "country"]:
        df[column] = df[column].fillna("Unknown")

    # Fix rating values that actually contain duration
    wrong_rating = df["rating"].astype("string").str.fullmatch(
        r"\s*\d+\s*min\s*", na=False
    )

    missing_duration = df["duration"].isna()

    df.loc[wrong_rating & missing_duration, "duration"] = (
        df.loc[wrong_rating & missing_duration, "rating"]
    )

    df.loc[wrong_rating, "rating"] = pd.NA

    # Fill missing ratings with a label
    df["rating"] = df["rating"].fillna("Not Rated")

    # Convert duration to text before extraction
    duration_text = df["duration"].astype("string")

    # Extract movie duration in minutes
    df["duration_minutes"] = pd.to_numeric(
        duration_text.str.extract(
            r"(\d+)\s*min",
            expand=False
        ),
        errors="coerce"
    )

    # Extract TV show duration in seasons
    df["duration_seasons"] = pd.to_numeric(
        duration_text.str.extract(
            r"(\d+)\s*Seasons?",
            expand=False,
            flags=0
        ),
        errors="coerce"
    )

    # Convert date_added to datetime
    df["date_added"] = pd.to_datetime(
        df["date_added"].astype("string").str.strip(),
        errors="coerce"
    )

    # Extract year and month
    df["added_year"] = df["date_added"].dt.year
    df["added_month"] = df["date_added"].dt.month_name()

    return df


def save_cleaned_data(df):
    """Save the cleaned dataset."""

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(OUTPUT_PATH, index=False)

    return OUTPUT_PATH


def get_missing_report(df):
    """Calculate missing values and percentages."""

    report = pd.DataFrame({
        "Missing Values": df.isnull().sum(),
        "Missing Percentage": (
            df.isnull().sum() / len(df) * 100
        ).round(2)
    })

    return report.sort_values(
        "Missing Percentage",
        ascending=False
    )
