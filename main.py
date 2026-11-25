import os
import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv

# Chargement de la clé API
load_dotenv('API.env')
API_KEY = os.getenv("DEEPSEEK_API_KEY")
API_URL = "https://api.deepseek.com/chat/completions"

# Initialisation de l'API FastAPI
app = FastAPI(
    title="MatPro AI API",
    description="API de démonstration pour interagir avec un LLM (DeepSeek).",
    version="1.0.0"
)

# Le schéma de données (validation automatique)
class PromptRequest(BaseModel):
    message: str

@app.get("/")
def read_root():
    return {"status": "online", "message": "Bienvenue sur l'API de Mathis !"}

@app.post("/chat")
def chat_with_ai(request: PromptRequest):
    """
    Envoie un message à l'IA et retourne sa réponse.
    """
    if not API_KEY:
        raise HTTPException(status_code=500, detail="Clé API manquante côté serveur.")
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": "Tu es un assistant technique serviable et concis."},
            {"role": "user", "content": request.message}
        ],
        "temperature": 0.3
    }
    
    try:
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()
        resultat = response.json()['choices'][0]['message']['content']
        return {"reponse": resultat}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur de l'API LLM : {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)