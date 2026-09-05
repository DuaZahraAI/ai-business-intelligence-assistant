from pathlib import Path

from src.data.validator import validate_file
from src.data.loader import load_data
from src.data.cleaner import clean_data
from src.analysis.analyzer import analyze_data
from src.analysis.query_processor import process_query


def process_dataset(file_path: Path) -> dict:
    """
    Complete data processing pipeline.
    """

    validate_file(file_path)

    df = load_data(file_path)

    clean_df = clean_data(df)

    report = analyze_data(clean_df)

    return report


def answer_question(
    file_path: Path,
    question: str
) -> dict:
    """
    Process a dataset and answer a user question
    using trusted facts generated from the dataset.
    """

    report = process_dataset(file_path)

    facts = report.get("facts", {})

    result = process_query(question, facts)

    return result