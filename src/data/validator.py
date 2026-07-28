from pathlib import Path


def validate_file(file_path: Path) -> Path:
    """
    Validate an uploaded dataset before loading it.
    """

    if not file_path.exists():
        raise FileNotFoundError(
            f"File not found: {file_path}"
        )

    allowed_extensions = {".csv", ".xlsx"}

    if file_path.suffix.lower() not in allowed_extensions:
        raise ValueError(
            "Only CSV (.csv) and Excel (.xlsx) files are supported."
        )

    if file_path.stat().st_size == 0:
        raise ValueError(
            "The uploaded file is empty."
        )

    return file_path