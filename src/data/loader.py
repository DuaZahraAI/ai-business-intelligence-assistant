from pathlib import Path

import pandas as pd


def load_data(file_path: Path) -> pd.DataFrame:
    """
    Load a CSV or Excel file into a Pandas DataFrame.
    """

    suffix = file_path.suffix.lower()

    try:
        if suffix == ".csv":
            return pd.read_csv(file_path)

        if suffix == ".xlsx":
            return pd.read_excel(file_path)

        raise ValueError(
            f"Unsupported file type: {suffix}. "
            "Only CSV (.csv) and Excel (.xlsx) files are supported."
        )

    except Exception as error:
        raise RuntimeError(
            f"Failed to load file '{file_path}': {error}"
        ) from error