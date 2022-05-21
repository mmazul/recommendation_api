from fastapi import FastAPI
from app.aux_function import engine_ps
from datetime import date, timedelta
from app.sql_templates import (
    recommendation_day_adv_model,
    recommendation_last_n_day_adv,
    advertisers_count_last_n_days
)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "recommendatApi"}

@app.get("/recommendations/{adv}/{modelo}")
async def advertiser(adv: str, model: str):
    try:
        engine = engine_ps()
        if model == "TopProduct":
            table = 'top_product'
        elif model == "TopCTR":
            table = 'top_ctr'
        else:
            table = None

        params = {
            'table': table,
            'adv': adv,
            'today': str(date.today() - timedelta(days=1))
        }

        with engine.connect() as con:
            recommendations_exe = con.execute(recommendation_day_adv_model.format(**params))
            recommendations_raw = recommendations_exe.fetchall()
            recommendations_list = [i[0] for i in recommendations_raw]

        return {"Advertiser": adv,
                "modelo": model,
                "recommendations": recommendations_list
                }
    except ValueError:
        print(ValueError)


@app.get("/stats")
async def stats():
    try:
        engine = engine_ps()
        with engine.connect() as con:
            params = {
                'start_date': str(date.today() - timedelta(days=8)),
                'end_date': str(date.today() - timedelta(days=1)),
            }
            adv_exe = con.execute(advertisers_count_last_n_days.format(**params))
            advertisers = adv_exe.fetchone()[0]

        return {"Cantidad de advertisers": advertisers}

    except ValueError:
        print(ValueError)


@app.get("/history/{adv}")
async def history(adv: int):
    try:
        engine = engine_ps()
        with engine.connect() as con:
            params = {
                'adv': adv,
                'start_date': str(date.today() - timedelta(days=8)),
                'end_date': str(date.today() - timedelta(days=1)),
            }
            recommendations_exe = con.execute(recommendation_last_n_day_adv.format(**params))
            recommendations_raw = recommendations_exe.fetchall()
            recommendations_list = list(set([i[0] for i in recommendations_raw]))

        return {"Advertiser": adv,
                "recommendations_last_7_days": recommendations_list
                }
    except ValueError:
        print(ValueError)
