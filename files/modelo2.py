'''
TopProduct Model:
Por cada advertirser activo debe devolvuelve los 20 (o menos) productos más vistos en la web del cliente.
'''

#Librerias

import pandas as pd
import datetime
import numpy as np


def Top_products (df_views, advertiser_id):
    df = pd.read_csv()
    df_today = df =  df[df['date'] == datetime.datetime.now().date()]
    df_today = pd.DataFrame({'count' : df.groupby(['advertiser_id', 'product_id'])['product_id'].count().sort_values(ascending=False)}).reset_index()



