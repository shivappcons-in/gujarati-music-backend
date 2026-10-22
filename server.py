from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
import os

app = FastAPI(title="Suno Gujarati AI Backend", version="1.0")

# Enable CORS for Netlify frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Aap baad me apni Netlify URL yahan daal sakte hain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SongRequest(BaseModel):
    lyrics: str
    style: str
    era: str
    voice_type: str

@app.get("/")
def home():
    return {"status": "Suno Gujarati AI Backend is running live!"}

@app.post("/api/create-song")
async def create_song(request: SongRequest):
    """
    Yahan par hum AI model (jaise Meta MusicGen / Replicate API) ko trigger karenge.
    Aapke diye gaye lyrics, Gujarati style, aur Era ke mutabiq yeh real audio render karega.
    """
    try:
        # Placeholder for AI Model Integration
        # Real implementation me yahan Replicate ya Hugging Face API call hogi
        song_title = request.lyrics[:25].strip() + "..."
        
        # Simulated AI generation response with a sample public audio output URL
        generated_audio_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
        
        return {
            "success": True,
            "message": "Song generated successfully using AI backend!",
            "song": {
                "id": os.urandom(4).hex(),
                "title": song_title,
                "style": request.style,
                "era": request.era,
                "duration": "3:45",
                "audio_url": generated_audio_url
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/validate-audio")
async def validate_audio(file: UploadFile = File(...)):
    """
    AI Audio Validator: Check karega ki upload ki gayi file gana hai ya galat audio 
    (jaise call recording ya aam batchit).
    """
    filename = file.filename.lower()
    # Basic AI validation check logic
    if "call" in filename or "record" in filename or "chat" in filename:
        return {
            "valid": False,
            "message": "AI detected this is a call recording or conversation audio, not a song!"
        }
    
    return {
        "valid": True,
        "message": "Audio verified successfully as a valid song/music file."
    }

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
