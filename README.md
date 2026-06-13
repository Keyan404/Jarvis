# Jarvis Mobile AI Backend

This is the FastAPI backend for the Jarvis Mobile AI assistant app. It processes user chats, connects to the Groq API (using the fast `llama3-8b-8192` model), and returns async responses.

## Tech Stack
- Python 3.12+
- FastAPI
- Uvicorn
- Pydantic v2
- HTTPX

## Setup Instructions

1. **Navigate to backend folder**:
   ```bash
   cd backend
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure your API Key**:
   Create a `.env` file (or copy `.env.example`) and enter your Groq API Key:
   ```env
   GROQ_API_KEY=your-actual-groq-key-here
   ```

5. **Start the server**:
   ```bash
   uvicorn app.main:app --reload --port 8000
   ```

The API will be available at `http://localhost:8000`. You can view the interactive documentation at `http://localhost:8000/docs`.
