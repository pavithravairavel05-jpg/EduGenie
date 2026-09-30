import json
import re

from gemini_client import generate_text


def clean_json_block(text: str) -> str:
    text = text.strip()
    text = re.sub(r"^```(?:json)?\s*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\s*```$", "", text)
    return text.strip()


def generate_quiz(passage: str):
    if not passage.strip():
        return {"error": "Please enter a passage or topic."}

    prompt = f"""
Create exactly 3 multiple-choice questions from the passage below.

Return ONLY valid JSON in this exact structure:
{{
  "questions": [
    {{
      "question": "string",
      "options": ["option A", "option B", "option C", "option D"],
      "correct_answer": "one exact option from options",
      "explanation": "short explanation"
    }}
  ]
}}

Requirements:
- Exactly 3 questions.
- Exactly 4 options per question.
- Questions must be answerable from the supplied passage/topic.
- Distractors should be plausible.
- No Markdown fences.

Passage/topic:
{passage}
"""

    try:
        raw = clean_json_block(generate_text(prompt))
        data = json.loads(raw)

        questions = data.get("questions")
        if not isinstance(questions, list) or len(questions) != 3:
            raise ValueError("Gemini did not return exactly 3 questions.")

        for item in questions:
            if (
                not isinstance(item, dict)
                or not isinstance(item.get("options"), list)
                or len(item["options"]) != 4
                or item.get("correct_answer") not in item["options"]
            ):
                raise ValueError("Invalid quiz question structure.")

        return data
    except Exception as exc:
        return {"error": f"Quiz generation/parsing failed: {exc}"}
