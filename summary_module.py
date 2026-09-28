from gemini_client import generate_text


def summarize_text(text: str) -> str:
    if not text.strip():
        return "Please enter text to summarize."

    prompt = f"""
Summarize the educational text below.
Keep the core information, remove repetition, and use clear concise language.
Prefer short paragraphs or bullet points.

Text:
{text}
"""
    try:
        return generate_text(prompt)
    except Exception as exc:
        return f"Unable to summarize right now: {exc}"
