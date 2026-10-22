from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Gujarati Music Creator AI Backend is Live!"}

@app.post("/generate-song")
def generate_song(data: dict):
    prompt = data.get("prompt", "")
    style = data.get("style", "")
    
    # Yahan aap Suno AI ya Hugging Face ka real audio generation API model integration dal sakte hain
    # Jaise ki external AI service se audio URL fetch karna
    
    generated_audio_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" # Ise apne AI model ke output URL se replace karein
    
    return {
        "status": "success",
        "message": f"Successfully generated Gujarati song for style: {style}",
        "audio_url": generated_audio_url
    }
