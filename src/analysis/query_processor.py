
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
    intent = None

    if "average" in normalized_question and "profit" in normalized_question:
        intent = "average_profit"

    elif "total" in normalized_question and "revenue" in normalized_question:
        intent = "total_revenue"

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
