# Phase 5: Development - EduGenie

## 1. Development Overview
EduGenie is implemented as a FastAPI-based learning assistant connected to Google Gemini.

## 2. Backend Development
- `main.py` defines the FastAPI application.
- Request data is accepted through structured request models.
- FastAPI routes connect browser actions to the learning modules.
- The documented API operations include Q&A, explanation, quiz, summary and learning recommendations.

## 3. AI Integration
The Gemini integration is used to generate educational responses from user-provided questions, topics and text.

## 4. Learning Modules
- `qna.py` handles question answering.
- `explanation_module.py` handles simplified explanations.
- `quiz_module.py` generates quizzes.
- `summary_module.py` summarizes text.
- `learning_path.py` provides learning recommendations.

## 5. Frontend Development
The frontend provides:
- A task-selection interface.
- An input area for the question/topic/text.
- A submit action.
- A result area for the generated response.
- CSS styling for a clean responsive presentation.

## 6. Local Execution
The project documentation specifies running the application with:
```bash
uvicorn main:app --reload
```
and opening:
```text
http://127.0.0.1:8000
```
