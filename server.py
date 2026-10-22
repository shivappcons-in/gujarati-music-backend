from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
    return {
        "status": "success",
        "message": f"Successfully generated Gujarati song for prompt: {prompt}",
        "audio_url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
    }
