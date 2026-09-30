import os

from gemini_client import generate_text

_local_model = None
_local_tokenizer = None


def _load_local_model():
    global _local_model, _local_tokenizer

    if _local_model is not None:
        return _local_model, _local_tokenizer

    try:
        from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
    except ImportError as exc:
        raise RuntimeError(
            "Local explanation requires transformers, torch and sentencepiece. "
            "Install the full requirements.txt."
        ) from exc

    model_name = os.getenv("LOCAL_EXPLANATION_MODEL", "MBZUAI/LaMini-Flan-T5-783M")
    _local_tokenizer = AutoTokenizer.from_pretrained(model_name)
    _local_model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    return _local_model, _local_tokenizer


def _explain_with_local_model(topic: str) -> str:
    import torch

    model, tokenizer = _load_local_model()
    prompt = (
        "Explain the following educational topic in simple language. "
        "Use short sections and a small example when useful.\n\n"
        f"Topic: {topic}"
    )
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512)
    with torch.no_grad():
        output = model.generate(
            **inputs,
            max_new_tokens=220,
            num_beams=4,
            early_stopping=True,
        )
    return tokenizer.decode(output[0], skip_special_tokens=True).strip()


def explain_topic(topic: str) -> str:
    if not topic.strip():
        return "Please enter a topic to explain."

    # The project document specifies LaMini-Flan-T5 for explanations.
    # Set USE_LOCAL_EXPLANATION=false to use Gemini instead.
    use_local = os.getenv("USE_LOCAL_EXPLANATION", "true").lower() == "true"

    try:
        if use_local:
            return _explain_with_local_model(topic)

        return generate_text(
            f"""
Explain this educational topic in beginner-friendly language.
Break complex ideas into simple points and include one small example.

Topic:
{topic}
"""
        )
    except Exception as exc:
        return f"Unable to generate an explanation right now: {exc}"
