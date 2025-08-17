import json
from typing import AsyncGenerator
from google import genai
from config import GEMINI_API_KEY
     
async def chat_with_model(
    message: str,
    model: str = 'gemini-2.5-flash-lite',
) -> AsyncGenerator[str, None]:
    
    
    client = genai.Client(api_key=GEMINI_API_KEY)
    
    response = client.models.generate_content_stream(
        model=model,
        contents=message,
    )
    
    for chunk in response:
        yield f'data: {json.dumps({"event": "text-chunk", "data": {"text": chunk.text}})}'
    
    yield "data: DONE"
    return

    