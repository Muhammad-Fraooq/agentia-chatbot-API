import os
from openai import AsyncOpenAI
from dotenv import load_dotenv
from agents.run import RunConfig
from agents import OpenAIChatCompletionsModel

load_dotenv()

# ONLY FOR TRACING
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY", "")

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
BASE_URL = os.getenv("BASE_URL")

client = AsyncOpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url=BASE_URL
)

# Gemini model via Google AI Studio
MODEL = "qwen/qwen-2.5-72b-instruct"

model = OpenAIChatCompletionsModel(model=MODEL, openai_client=client)

config = RunConfig(
    model=model,
    model_provider=client,# type: ignore
    # tracing_disabled=True
)