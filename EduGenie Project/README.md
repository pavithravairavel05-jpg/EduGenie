# EduGenie — Google Gemini Powered Learning Assistant

EduGenie is a FastAPI + HTML/CSS educational assistant based on the supplied project document.

## Features

- Q&A — `/qa`
- Simple concept explanation — `/explain`
- 3-question MCQ quiz generation — `/quiz`
- Text summarization — `/summarize`
- Beginner-to-advanced learning path — `/learn/recommendations`

## Project structure

```text
EduGenie/
├── main.py
├── gemini_client.py
├── explanation_module.py
├── qna.py
├── quiz_module.py
├── summary_module.py
├── learning_path.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## Requirements

- Python 3.10+
- A Gemini API key for the cloud-powered modules.
- Internet access the first time the local explanation model is downloaded.

## Windows + VS Code setup

Open the project folder in VS Code, then open Terminal.

### 1. Create a virtual environment

```powershell
python -m venv .venv
```

### 2. Activate it

```powershell
.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use Command Prompt:

```cmd
.venv\Scripts\activate
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

### 4. Configure the API key

Copy `.env.example` to `.env` and put your Gemini API key in:

```text
GEMINI_API_KEY=your_key_here
```

Do not share the `.env` file or commit it to Git.

### 5. Run the application

```powershell
uvicorn main:app --reload
```

Open:

http://127.0.0.1:8000

## Notes

The supplied document describes Gemini 1.5 Pro for Q&A, quiz, summarization and learning paths, and LaMini-Flan-T5-783M for concept explanation. The implementation keeps those module roles, while making the Gemini model configurable through `GEMINI_MODEL` because model availability can change over time.

For a lighter installation, set:

```text
USE_LOCAL_EXPLANATION=false
```

Then the explanation module uses Gemini instead of downloading the local LaMini model.

## Troubleshooting

### `GEMINI_API_KEY is missing`

Create `.env` from `.env.example` and add your API key.

### Local explanation model is slow

The LaMini model is downloaded on first use and may use significant RAM/CPU. Set `USE_LOCAL_EXPLANATION=false` to use Gemini for explanations.

### Port already in use

Run:

```powershell
uvicorn main:app --reload --port 8001
```

Then open:

http://127.0.0.1:8001
