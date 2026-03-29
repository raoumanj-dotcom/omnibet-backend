from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import random

app = FastAPI()

# Autorise ton interface iPhone à lire les données du serveur
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "OmniBet System Online", "version": "2.7.1"}

@app.get("/api/pronos")
async def get_pronos():
    # Simulation d'extraction Winamax/Unibet
    # Dans une version V3, on intègre ici le scraper Selenium/BeautifulSoup
    pronos_db = [
        {
            "id": 1,
            "sport": "Football",
            "match": "PSG vs Marseille",
            "prono": "1N & +1,5 buts",
            "cote": 1.45,
            "conf": 94,
            "color": "blue",
            "time": "20:45"
        },
        {
            "id": 2,
            "sport": "Tennis",
            "match": "Alcaraz vs Sinner",
            "prono": "Plus de 21.5 Jeux",
            "cote": 1.68,
            "conf": 89,
            "color": "purple",
            "time": "18:30"
        },
        {
            "id": 3,
            "sport": "NBA",
            "match": "Bucks vs Celtics",
            "prono": "Giannis Over 26.5 Pts",
            "cote": 1.62,
            "conf": 92,
            "color": "orange",
            "time": "02:00"
        }
    ]
    return pronos_db

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
