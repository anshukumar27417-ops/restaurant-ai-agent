# Restaurant AI Agent

Backend setup for the Tenacious Techies AI Automation & Agents Developer assessment.

## Tech Stack
- **Language:** Python 3.11+
- **Framework:** FastAPI
- **Server:** Uvicorn
- **Validation:** Pydantic
- **Environment Management:** python-dotenv

## Project Structure
```text
restaurant -ai -agent/
├── app/
│   ├── __init__.py
│   ├── main.py            # FastAPI entry point & endpoints
│   ├── config.py          # Configuration and environment settings
│   ├── api/               # API route handlers
│   │   ├── __init__.py
│   │   ├── chat.py
│   │   ├── orders.py
│   │   └── tickets.py
│   ├── agent/             # LLM Agent definitions, prompts, and tools
│   │   ├── __init__.py
│   │   ├── agent.py
│   │   ├── prompts.py
│   │   └── tools.py
│   ├── rag/               # Retrieval-Augmented Generation module
│   │   ├── __init__.py
│   │   ├── embeddings.py
│   │   ├── retriever.py
│   │   └── documents/
│   ├── workflows/         # Business logic & automation workflows
│   │   ├── __init__.py
│   │   └── complaint.py
│   ├── models/            # Pydantic data models
│   │   ├── __init__.py
│   │   ├── order.py
│   │   └── ticket.py
│   └── utils/             # Utilities and helpers
│       ├── __init__.py
│       ├── logger.py
│       └── validators.py
├── tests/                 # Unit & integration tests
├── .env.example           # Environment variables template
├── .env                   # Local environment variables
├── .gitignore             # Git ignore rules
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

## Setup and Installation

### 1. Create and Activate Virtual Environment
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Copy `.env.example` to `.env` if not already present:
```bash
cp .env.example .env
```

### 4. Run the Server
```bash
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

## Available Endpoints
- **Root**: `GET http://127.0.0.1:8000/` - Returns `{"message": "Restaurant AI Agent is running"}`
- **Health Check**: `GET http://127.0.0.1:8000/health` - Returns `{"status": "healthy"}`
- **Swagger Documentation**: `GET http://127.0.0.1:8000/docs` - Interactive Swagger UI
- **ReDoc Documentation**: `GET http://127.0.0.1:8000/redoc` - Alternative API documentation
