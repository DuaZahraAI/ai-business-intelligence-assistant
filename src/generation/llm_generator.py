def generate_response(prompt: str, generator) -> str:
    """
    Generate a natural-language response from a controlled prompt.

    The generator is responsible for communicating with the
    configured LLM provider.
    """

    if not prompt or not prompt.strip():
        raise ValueError("Cannot generate a response from an empty prompt.")

    if generator is None:
        raise ValueError("An LLM generator must be provided.")

    try:
        response = generator(prompt)
    except Exception as exc:
        raise RuntimeError("LLM generation failed.") from exc

    if not isinstance(response, str):
        raise TypeError("LLM generator must return a string.")

    if not response.strip():
        raise ValueError("LLM generator returned an empty response.")

    return response.strip()