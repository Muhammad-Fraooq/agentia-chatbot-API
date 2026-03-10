import os
from openai import AsyncOpenAI
from dotenv import load_dotenv
from agents.run import RunConfig
from agents import OpenAIChatCompletionsModel

load_dotenv()

# ONLY FOR TRACING
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY", "")

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Use Google Gemini directly (more reliable than OpenRouter free tier)
BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"

client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url=BASE_URL
)

# Gemini model via Google AI Studio
MODEL = "gemini-2.0-flash"

model = OpenAIChatCompletionsModel(model=MODEL, openai_client=client)

config = RunConfig(
    model=model,
    model_provider=client,# type: ignore
    # tracing_disabled=True
)