import pandas as pd


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    cleaned_df = df.copy()

    cleaned_df.columns = (
        cleaned_df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    cleaned_df = cleaned_df.drop_duplicates()
    cleaned_df = cleaned_df.dropna()

    return cleaned_df