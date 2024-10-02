from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
from groq import Groq

app = FastAPI()

GROQ_API_KEY = "gsk_api_key"  # Replace with actual API key
client = Groq(api_key=GROQ_API_KEY)

class PromptRequest(BaseModel):
    prompt: str

@app.post("/complete-text")
async def complete_text(request: PromptRequest):
    if not request.prompt:
        raise HTTPException(status_code=400, detail="Prompt is required")

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": request.prompt,
                }
            ],
            model="llama3-8b-8192",  
        )

        completion = chat_completion.choices[0].message.content

        return {"completion": completion}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
