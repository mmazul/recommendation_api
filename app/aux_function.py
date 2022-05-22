""" Auxiliar functions """

import pandas as pd
from decouple import config
from sqlalchemy import create_engine
import os

def engine_ps():
    username = config('PS_USER')
    password = config('PS_PASSWORD')
    host = config('PS_HOST')
    port = config('PS_PORT', default='5432')
    database = config('PS_DATABASE', default="postgres")
    engine = create_engine(F'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}',
                           echo=False)

    return engine

