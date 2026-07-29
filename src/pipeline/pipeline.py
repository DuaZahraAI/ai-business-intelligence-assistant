from src.data.validator import validate_file
from src.data.loader import load_data
from src.data.cleaner import clean_data
from src.analysis.analyzer import analyze_data


def process_dataset(file_path: str) -> dict:
    """
    Complete data processing pipeline.
    """

    validate_file(file_path)

    df = load_data(file_path)

    clean_df = clean_data(df)

    report = analyze_data(clean_df)

    return report