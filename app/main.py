from fastapi import FastAPI
import numpy as np

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "recomendatApi"}

@app.get("/recomendations/{adv}/{modelo}")
async def advertiser(adv: int, modelo: str):
    return {"Advertiser": adv,
            "modelo": modelo}

@app.get("/stats")
async def stats():
    return {"Estadisticas: ",
            "Cantidad de advertisers",
            "Advertisers que más varían sus recomendaciones por día",
            "Estadísticas de coincidencia entre ambos modelos para los diferentes advs"}

@app.get("/history/{adv}")
async def history(adv: int):
    return {"Recomendaciones para": adv, "en los ultimos 7 dias": adv}