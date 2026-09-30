# Phase 2: Requirement Analysis - EduGenie

## 1. Functional Requirements
- **Question & Answer Module:** Accept a learner's question/topic and return an answer.
- **Explanation Module:** Accept a topic and return a simplified explanation.
- **Quiz Module:** Accept a topic and generate quiz content.
- **Summary Module:** Accept text and return a concise summary.
- **Learning Path Module:** Provide learning recommendations.
- **API Layer:** Expose the learning functions through FastAPI endpoints.
- **Frontend Module:** Provide a browser interface for selecting a task, entering content and viewing the result.

## 2. API Requirements
- `POST /qa`
- `POST /explain`
- `POST /quiz`
- `POST /summarize`
- `POST /learn/recommendations`

## 3. Non-Functional Requirements
- **Usability:** Clean and simple browser-based interface.
- **Maintainability:** Keep Q&A, explanation, quiz, summary and learning-path logic in separate modules.
- **Security:** Keep the Gemini API key in environment configuration and do not expose the real key in GitHub.
- **Error Handling:** Return useful errors when AI configuration or service calls fail.
- **Responsive UI:** The frontend should support a clear, user-friendly layout.

## 4. Technology Stack Requirements
- **Backend:** Python, FastAPI and Uvicorn.
- **AI Engine:** Google Gemini.
- **Frontend:** HTML/CSS with a FastAPI/Jinja2 template.
- **Environment:** Python virtual environment and VS Code.
- **Version Control:** Git/GitHub.
