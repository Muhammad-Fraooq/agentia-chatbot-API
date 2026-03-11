# Agentia-World Backend API

FastAPI backend for Agentia-World, deployable on Hugging Face Spaces.

## Deployment on Hugging Face Spaces

1. Create a new Space on Hugging Face
2. Select **Docker** as the SDK
3. Upload these files:
   - `Dockerfile`
   - `requirements.txt`
   - `main.py` (and other application files)
   - `.env` (with your API keys, or use Spaces Secrets)

## Environment Variables

Set these in your Hugging Face Space settings:

- `PORT`: 7860 (default)
- `HOST`: 0.0.0.0
- Any additional API keys required by your application

## Local Development

```bash
# Build the Docker image
docker build -t agentia-world-backend .

# Run the container
docker run -p 7860:7860 agentia-world-backend
```

## API Endpoints

Once deployed, access the API at: `https://<your-space-id>.hf.space`

- `GET /` - Health check
- `GET /docs` - Interactive API documentation
