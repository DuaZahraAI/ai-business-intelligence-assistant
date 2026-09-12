def build_prompt(result: dict) -> str:
    """
    Build a controlled LLM prompt from a successful query result.
    """

    if result.get("status") != "success":
        raise ValueError("Cannot build prompt from an unsuccessful query result.")

    if result.get("fact") is None:
        raise ValueError("Cannot build prompt without a trusted fact.")

    question = result["question"]
    intent = result["intent"]
    fact = result["fact"]

    prompt = f"""
You are a business intelligence assistant.

Answer the user's question using only the trusted business fact provided below.

User question:
{question}

Intent:
{intent}

Trusted business fact:
{fact}

Instructions:
- Use only the trusted business fact.
- Do not invent business numbers.
- Do not introduce unsupported facts.
- Give a clear and concise answer.
""".strip()

    return prompt
