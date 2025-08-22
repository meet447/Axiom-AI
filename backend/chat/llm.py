import json
from typing import AsyncGenerator
from google import genai
from config import GEMINI_API_KEY, UNIO_API_KEY
import openai 

# async def chat_with_model(
#     message: str,
#     model: str = 'gemini-2.5-flash-lite',
# ) -> AsyncGenerator[str, None]:
    
    
#     client = genai.Client(api_key=GEMINI_API_KEY)
    
#     response = client.models.generate_content_stream(
#         model=model,
#         contents=message,
#     )
    
#     for chunk in response:
#         yield f'data: {json.dumps({"event": "text-chunk", "data": {"text": chunk.text}})}'
    
#     yield "data: DONE"
#     return


async def chat_with_model(
    message: str,
    model: str = 'google:gemini-2.0-flash-lite',
) -> AsyncGenerator[str, None]:
    
    
    unio = openai.Client(
        base_url="https://unio.onrender.com/v1/api",
        api_key=UNIO_API_KEY
    )
    
    messages = [
        {"role": "user", "content": message}
    ]
    
    response = unio.chat.completions.create(
        model="google:" + model,
        messages=messages,
        stream=True
    )
    
    for chunk in response:
        yield f'data: {json.dumps({"event": "text-chunk", "data": {"text": chunk.choices[0].delta.content or ""}})}'
    
    yield "data: DONE"
    return
    
