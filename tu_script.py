import requests
import pandas as pd

API_KEY = "08e00792567d4861bef295d0dc72f6a5"

url = "https://api.football-data.org/v4/matches"
headers = {"X-Auth-Token": API_KEY}

response = requests.get(url, headers=headers)
data = response.json()

lista = []

for p in data["matches"]:
    try:
        lista.append({
            "local": p["homeTeam"]["name"],
            "visitante": p["awayTeam"]["name"]
        })
    except:
        pass

df = pd.DataFrame(lista)
df.to_csv("partidos.csv", index=False)

print("Datos guardados")
