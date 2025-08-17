from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware  
from chat.llm import chat_with_model
from chat.basic.generate import generate_response
from chat.expert.generate import generate_response_expert
from typing import List
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    thread_id: int | None = None
    query: str
    history: List
    model: str
    pro_search: bool = False

@app.get('/')
async def read_root():
    return [{"status": "all routes and services working"},{'message': 'Welcome to the Axiom API'}]

@app.post('/chat')
async def chat_endpoint(payload: ChatRequest):
    model_map = {
        'fast': 'gemini-2.5-flash',
        'powerful': 'gemini-2.5-pro',
        'hyper': 'gemini-2.5-flash-lite'
    }

    model = model_map.get(payload.model)
    if not model:
        raise HTTPException(status_code=400, detail="Unsupported model")

    if payload.pro_search:
        return StreamingResponse(
            generate_response_expert(query=payload.query, history=payload.history),
            media_type='text/event-stream'
        )
    else:
        return StreamingResponse(
            generate_response(query=payload.query, history=payload.history, model=model),
            media_type="text/event-stream"
        )