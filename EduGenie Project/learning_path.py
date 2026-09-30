from gemini_client import generate_text


def get_learning_recommendations(topic: str) -> str:
    if not topic.strip():
        return "Please enter a topic."

    prompt = f"""
Create a personalized learning path for the topic below.

Organize it from beginner to advanced.
For each stage, include:
1. Concepts to learn
2. Suggested timeline
3. Practice activities
4. Useful resource types such as videos, articles, or books

Keep the plan practical and adaptable for a learner.

Topic:
{topic}
"""
    try:
        return generate_text(prompt)
    except Exception as exc:
        return f"Unable to generate a learning path right now: {exc}"
