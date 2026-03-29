import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ta configuration RapidAPI
API_KEY = "5d8a8c7318538c931d8b071fa9f63be5"
HOST = "api-football-v1.p.rapidapi.com"

@app.get("/api/pronos")
async def get_live_data():
    # On récupère les 10 prochains matchs mondiaux (Plus simple pour tester)
    url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"
    querystring = {"next": "10"} 
    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": HOST
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)
        data = response.json()
        
        final_pronos = []
        for item in data.get('response', []):
            home = item['teams']['home']['name']
            away = item['teams']['away']['name']
            league = item['league']['name']
            # Extraction de l'heure (format HH:mm)
            time_str = item['fixture']['date'][11:16]

            # LOGIQUE OMNIBET : Génération de prono auto
            # On simule un prono basé sur la ligue
            final_pronos.append({
                "sport": league,
                "match": f"{home} vs {away}",
                "prono": "Plus de 1,5 buts (Auto-Bot)",
                "cote": 1.48,
                "conf": 91,
                "color": "blue",
                "time": time_str
            })
        return final_pronos
    except:
        return [{"match": "Initialisation...", "prono": "Serveur en cours de réveil", "cote": 0, "conf": 0}]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
