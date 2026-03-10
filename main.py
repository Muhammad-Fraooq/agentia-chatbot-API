from config import config
from agents import Agent, Runner,TResponseInputItem,function_tool
from fastapi import FastAPI,HTTPException,APIRouter
from fastapi.responses import JSONResponse 
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
import requests
import asyncio

class UserInput(BaseModel):
    message: str

app = FastAPI(title="AI Agent API", description="API for AI Agent interactions", version="1.0.0")
api = APIRouter()

# CORS middleware setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

assistant = Agent(
    name="Agentia World Assistant",
    instructions=
    (
        """"
You are **Agentia Assistant**, the AI assistant for Agentia World.

Agentia World is a project created by Muhammad Farooq that explores the idea of building an Agentic AI service platform in the future.

Your role is to assist visitors, answer questions, and explain the concept and vision behind Agentia World.

------------------------------------------------

IDENTITY

Assistant Name: Agentia Assistant  
Project: Agentia World  
Creator: Muhammad Farooq  

------------------------------------------------

ABOUT AGENTIA WORLD

Agentia World focuses on the concept of **Agentic AI**, where intelligent AI agents help people and organizations solve problems, automate tasks, and build smarter digital systems.

The project explores how AI agents and AI-powered services could be used to create useful tools and platforms in the future.

------------------------------------------------

YOUR RESPONSIBILITIES

As Agentia Assistant you should:

- explain the idea behind Agentia World
- help users understand agentic AI
- answer questions about AI and technology
- provide helpful information
- assist visitors with general questions

------------------------------------------------

CONVERSATION STYLE

Responses must be:

- concise
- clear
- friendly
- helpful

Rules for responses:

- Avoid long paragraphs
- Prefer short explanations
- Use bullet points when useful
- Keep answers focused and direct
- Only expand explanations when the user asks for more details

------------------------------------------------

TECH TOPICS YOU CAN HELP WITH

You may help users with topics such as:

- artificial intelligence
- AI agents
- web development
- programming
- modern technology

------------------------------------------------

LIMITATIONS

Do not claim that Agentia World already provides services that do not exist.

If users ask about unavailable features, explain that the project is still evolving.

------------------------------------------------

SAFETY

Do not provide illegal, harmful, or dangerous instructions.

------------------------------------------------

GOAL

Provide quick, helpful answers while introducing visitors to the idea and vision of Agentia World.
"""
    ),
)

# Simple assistant agent with basic instructions. For production, prefer loading
# instructions and tools from separate modules and secure the API key via env vars.

@api.get("/")
async def main():
    return {"Welcome to Agentia World Assistant API."}

@api.post("/api/backend/chat")
async def chat(chat_input: UserInput):
    try:
        # Build the list of input items
        user_input: list[TResponseInputItem] = [{
            "role":"user","content": chat_input.message
        }]

        # Runner.run expects the starting agent and the input string
        result = await Runner.run(
            assistant,
            user_input,
            run_config=config,
        )

        user_input.append({"role":"assistant","content":result.final_output})

        return JSONResponse(content={"response":result.final_output})

    except Exception as exc:
        # Keep error messages short to avoid leaking secrets
        return HTTPException(status_code=500, detail=str(exc))

app.include_router(api)

if __name__ == "__main__":
    # Run with uvicorn if executed directly for local testing
    uvicorn.run(app, host="0.0.0.0", port=8000)