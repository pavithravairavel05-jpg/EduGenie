from gemini_client import generate_text


def answer_question(question: str) -> str:
    if not question.strip():
        return "Please enter a question."

    prompt = f"""
You are EduGenie, an educational assistant.
Answer the student's question accurately and concisely.
Use simple language suitable for a learner.
If the question is ambiguous, state the ambiguity briefly.

Student question:
{question}
"""
    try:
        return generate_text(prompt)
    except Exception as exc:
        return f"Unable to answer right now: {exc}"
