import pandas as pd


def analyze_data(df: pd.DataFrame) -> dict:
    """
    Analyze the cleaned dataset and return business insights.
    """

    analysis = {
        "rows": len(df),
        "columns": len(df.columns),
        "column_names": list(df.columns),
        "data_types": df.dtypes.astype(str).to_dict(),
        "missing_values": df.isnull().sum().to_dict(),
        "statistics": df.describe(include="all").to_dict()
    }

    return analysis