from pathlib import Path

from src.data.validator import validate_file
from src.data.loader import load_data
from src.data.cleaner import clean_data
from src.analysis.analyzer import analyze_data
from src.analysis.query_processor import process_query
from src.generation.prompt_builder import build_prompt
from src.generation.llm_generator import generate_response


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
    question: str,
    generator
) -> dict:
    """
    Process a dataset and answer a user question
    using trusted facts generated from the dataset.
    """

    report = process_dataset(file_path)

    facts = report.get("facts", {})

    result = process_query(question, facts)

    if result["status"] != "success":
        return result

    prompt = build_prompt(result)

    response = generate_response(prompt, generator)

    return {
        "status": "success",
        "question": question,
        "intent": result["intent"],
        "fact": result["fact"],
        "prompt": prompt,
        "response": response
    }