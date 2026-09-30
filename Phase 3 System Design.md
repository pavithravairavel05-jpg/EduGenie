# Phase 3: System Design - EduGenie

## 1. System Architecture Pattern
EduGenie follows a modular web-application architecture.

- **Client Layer:** Browser-based HTML interface.
- **Server Layer:** FastAPI application in `main.py`.
- **AI Intelligence Layer:** Gemini client/integration.
- **Learning Modules:** Q&A, explanation, quiz, summary and learning-path modules.
- **Presentation Layer:** Jinja2 template and CSS styling.

## 2. Architectural Workflow Design
1. User opens the EduGenie web interface.
2. User selects a learning task and enters a question, topic or text.
3. The frontend sends a request to the FastAPI backend.
4. FastAPI routes the request to the relevant learning module.
5. The module uses Google Gemini to generate the learning response.
6. The generated result is returned to the frontend.
7. The frontend displays the result to the learner.

## 3. Component Interaction Flow
```text
[Browser / EduGenie UI]
          |
          | POST request
          v
     [FastAPI main.py]
          |
          +--> [Q&A Module]
          +--> [Explanation Module]
          +--> [Quiz Module]
          +--> [Summary Module]
          +--> [Learning Path Module]
          |
          v
   [Google Gemini API]
          |
          v
   [Generated Learning Result]
          |
          v
      [Browser UI]
```

## 4. Project Structure
```text
EduGenie/
├── main.py
├── gemini_client.py
├── qna.py
├── explanation_module.py
├── quiz_module.py
├── summary_module.py
├── learning_path.py
├── requirements.txt
├── .env.example
├── templates/
│   └── index.html
└── static/
    └── style.css
```
