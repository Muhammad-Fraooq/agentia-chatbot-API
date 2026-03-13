# Agentia World Backend API 🚀

FastAPI-based backend service for Agentia World, powered by OpenAI Agents SDK. This backend provides AI agent capabilities with intelligent conversation handling and is designed for deployment on Hugging Face Spaces or any cloud platform.

![FastAPI](https://img.shields.io/badge/FastAPI-0.133-green?logo=fastapi)
![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![OpenAI Agents](https://img.shields.io/badge/OpenAI_Agents-0.10.2-412991?logo=openai)
![Docker](https://img.shields.io/badge/Docker-Ready-blue?logo=docker)

## 🌟 Features

- **FastAPI Framework**: High-performance async API with automatic OpenAPI docs
- **OpenAI Agents SDK**: Advanced AI agent orchestration and execution
- **AI-Powered Assistant**: Intelligent chatbot with contextual understanding
- **CORS Enabled**: Ready for frontend integration
- **Docker Support**: Containerized deployment on any platform
- **Hugging Face Spaces**: Optimized for HF Spaces deployment
- **Environment Configuration**: Secure API key management via `.env`
- **Type Safety**: Pydantic models for request/response validation
- **Error Handling**: Comprehensive error management and logging

## 📁 Project Structure

```
backend/
├── main.py                 # FastAPI application and API routes
├── config.py               # Configuration and OpenAI client setup
├── requirements.txt        # Python dependencies
├── pyproject.toml         # Modern Python project configuration
├── uv.lock                # UV package manager lock file
├── Dockerfile             # Docker container configuration
├── .dockerignore          # Docker ignore patterns
├── .gitignore             # Git ignore patterns
├── .python-version        # Python version specification (3.13)
├── README.md              # This file
└── .env                   # Environment variables (not tracked)
```

## 🚀 Quick Start

### Prerequisites

- **Python 3.13** or higher
- **pip** or **uv** package manager
- **OpenRouter API Key** (or OpenAI API Key)
- **Docker** (optional, for containerized deployment)

### Local Development

1. **Navigate to backend directory**
   ```bash
   cd app/api/backend
   ```

2. **Create virtual environment**
   ```bash
   # Using venv
   python -m venv venv
   
   # Activate on Windows
   venv\Scripts\activate
   
   # Activate on macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   # Using pip
   pip install -r requirements.txt
   
   # Or using uv (recommended)
   uv sync
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the backend directory:
   ```env
   OPENROUTER_API_KEY=your_openrouter_api_key
   BASE_URL=https://openrouter.ai/api/v1
   OPENAI_API_KEY=sk-your-openai-key  # Optional, for tracing
   ```

5. **Run the development server**
   ```bash
   # Using uvicorn directly
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   
   # Or using Python
   python main.py
   ```

6. **Access the API**
   
   - **API Base**: [http://localhost:8000](http://localhost:8000)
   - **Interactive Docs**: [http://localhost:8000/docs](http://localhost:8000/docs)
   - **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## 📡 API Endpoints

### Health Check

```http
GET /
```

**Response:**
```json
{
  "Welcome to Agentia World Assistant API.": ""
}
```

### Chat Endpoint

```http
POST /api/backend/chat
Content-Type: application/json
```

**Request Body:**
```json
{
  "message": "Hello, tell me about Agentia World"
}
```

**Response:**
```json
{
  "response": "Agentia World is a project that explores Agentic AI..."
}
```

**Error Response:**
```json
{
  "detail": "Error message here"
}
```

## 🐳 Docker Deployment

### Build Docker Image

```bash
cd app/api/backend
docker build -t agentia-world-backend .
```

### Run Docker Container

```bash
# With environment variables
docker run -p 7860:7860 \
  -e OPENROUTER_API_KEY=your_key \
  -e BASE_URL=https://openrouter.ai/api/v1 \
  agentia-world-backend
```

### Using Docker Compose (Optional)

Create `docker-compose.yml`:
```yaml
version: '3.8'

services:
  backend:
    build: .
    ports:
      - "7860:7860"
    environment:
      - OPENROUTER_API_KEY=${OPENROUTER_API_KEY}
      - BASE_URL=${BASE_URL}
    restart: unless-stopped
```

Run:
```bash
docker-compose up -d
```

## 🚀 Deployment on Hugging Face Spaces

1. **Create a new Space** on [Hugging Face](https://huggingface.co/spaces)
2. **Select Docker** as the SDK type
3. **Upload files**:
   - `Dockerfile`
   - `requirements.txt`
   - `main.py`
   - `config.py`
   - `.dockerignore`

4. **Configure Secrets** in Space Settings:
   - `OPENROUTER_API_KEY`
   - `BASE_URL`

5. **Deploy** - Hugging Face will automatically build and deploy

### Environment Variables for HF Spaces

| Variable | Description | Default |
|----------|-------------|---------|
| `PORT` | Server port | `7860` |
| `HOST` | Server host | `0.0.0.0` |
| `OPENROUTER_API_KEY` | OpenRouter API key | *Required* |
| `BASE_URL` | API base URL | `https://openrouter.ai/api/v1` |

## 🛠️ Configuration

### Model Configuration

Edit `config.py` to change the AI model:

```python
# Current model
MODEL = "qwen/qwen-2.5-72b-instruct"

# Available models via OpenRouter:
# - "openai/gpt-4o"
# - "anthropic/claude-3.5-sonnet"
# - "google/gemini-pro-1.5"
# - "meta-llama/llama-3-70b-instruct"
```

### Agent Instructions

Modify the agent's behavior in `main.py`:

```python
assistant = Agent(
    name="Agentia World Assistant",
    instructions="""
    Your custom instructions here...
    """
)
```

## 📝 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `fastapi` | 0.133.1 | Web framework |
| `openai-agents` | 0.10.2 | AI agent orchestration |
| `python-dotenv` | 1.2.1 | Environment variable management |
| `uvicorn` | 0.41.0 | ASGI server |
| `httpx` | 0.28.1 | Async HTTP client |

## 🧪 Testing

### Manual Testing with cURL

```bash
# Health check
curl http://localhost:8000/

# Chat endpoint
curl -X POST http://localhost:8000/api/backend/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello!"}'
```

### Testing with Python

```python
import requests

response = requests.post(
    "http://localhost:8000/api/backend/chat",
    json={"message": "Tell me about Agentia World"}
)

print(response.json())
```

## 🔒 Security Best Practices

- **Never commit `.env` files** to version control
- **Use environment variables** for API keys
- **Enable CORS restrictions** in production
- **Implement rate limiting** for production use
- **Add authentication** for protected endpoints

### Production CORS Configuration

Update `main.py` for production:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://your-domain.com"],  # Specific origins
    allow_credentials=True,
    allow_methods=["POST", "GET"],
    allow_headers=["Content-Type"],
)
```

## 🐛 Troubleshooting

### Common Issues

**1. ModuleNotFoundError**
```bash
# Ensure virtual environment is activated
# Reinstall dependencies
pip install -r requirements.txt
```

**2. API Key Errors**
```bash
# Verify .env file exists and contains valid keys
cat .env
```

**3. Port Already in Use**
```bash
# Change port in Dockerfile or uvicorn command
uvicorn main:app --port 8001
```

**4. Docker Build Fails**
```bash
# Clear Docker cache
docker builder prune
# Rebuild
docker build --no-cache -t agentia-world-backend .
```

## 📊 Performance Optimization

- **Async Operations**: All endpoints use async/await
- **Connection Pooling**: HTTPX client with connection reuse
- **Caching**: Consider adding Redis for response caching
- **Load Balancing**: Use multiple workers in production:
  ```bash
  uvicorn main:app --workers 4
  ```

## 🤝 Integration with Frontend

The backend is designed to work with the Next.js frontend:

```typescript
// Example frontend integration
const response = await fetch('/api/backend/chat', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ message: 'Hello!' })
});

const data = await response.json();
console.log(data.response);
```

## 📄 License

This project is licensed under the MIT License - see the main [LICENSE](../../../LICENSE) file for details.

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) - Modern Python web framework
- [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) - AI agent framework
- [Hugging Face](https://huggingface.co/) - Deployment platform
- [OpenRouter](https://openrouter.ai/) - Unified AI API

## 📞 Support

For backend-specific issues:
- Open an issue on GitHub
- Check API logs: `docker logs <container-id>`
- Review FastAPI documentation: [http://localhost:8000/docs](http://localhost:8000/docs)

---

**Built with ⚡ using FastAPI and OpenAI Agents SDK**
