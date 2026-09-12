INTENT_PATTERNS = {
    "average_profit": {
        "operations": ["average", "mean", "avg"],
        "metrics": ["profit"]
    },
    "total_revenue": {
        "operations": ["total", "overall"],
        "metrics": ["revenue"]
    }
}
def detect_intent(normalized_question: str) -> str | None:
    """
    Detect the user's intent from a normalized question.
    """

    for intent, patterns in INTENT_PATTERNS.items():
        operation_found = any(
            operation in normalized_question
            for operation in patterns["operations"]
        )

        metric_found = any(
            metric in normalized_question
            for metric in patterns["metrics"]
        )

        if operation_found and metric_found:
            return intent

    return None
def process_query(question: str, facts: dict) -> dict:
    """
    Process a user question and retrieve a trusted fact.
    """

    # Step 1: Validate the question
    if not question or not question.strip():
        return {
            "status": "empty_question",
            "question": question,
            "intent": None,
            "fact": None
        }

    # Step 2: Normalize the question
    normalized_question = question.strip().lower()

    # Step 3: Detect the user's intent
    intent = detect_intent(normalized_question)

    # Step 4: Handle unknown intent
    if intent is None:
        return {
            "status": "unknown_intent",
            "question": question,
            "intent": None,
            "fact": None
        }

    # Step 5: Retrieve the trusted fact
    fact = facts.get(intent)

    # Step 6: Handle missing fact
    if fact is None:
        return {
            "status": "missing_fact",
            "question": question,
            "intent": intent,
            "fact": None
        }

    # Step 7: Return successful result
    return {
        "status": "success",
        "question": question,
        "intent": intent,
        "fact": fact
    }
