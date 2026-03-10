# Agentia Backend API

FastAPI backend for Agentia AI Assistant using OpenAI Agents SDK.

## Setup

1. **Install dependencies:**
   ```bash
   cd app/api/backend
   pip install uv
   uv sync
   ```

2. **Create `.env` file:**
   Create a `.env` file in the root directory with:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

3. **Run the backend server:**
   ```bash
   cd app/api/backend
   uv run python main.py
   ```
   
   Or with uvicorn directly:
   ```bash
   uv run uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

4. **Test the API:**
   - Open `http://localhost:8000` in your browser
   - Test the chat endpoint at `POST /api/backend/chat`

## API Endpoints

- `GET /` - Welcome message
- `POST /api/backend/chat` - Chat with the AI assistant

## Tools

- **Weather Tool**: Get current weather using WeatherAPI.com
