'''
TopProduct Model:
Por cada advertirser activo debe devolvuelve los 20 (o menos) productos más vistos en la web del cliente.
'''

#Librerias

import pandas as pd
import datetime
from files.aux_function import download_s3_to_pandas, upload_pandas_to_s3


def Top_products():
    #Leo los datos de las views
    df = download_s3_to_pandas('product_views')
    #Filtro por la fecha de hoyclea
    df_today = df =  df[df['date'] == datetime.datetime.now().date()]
    #Cuento las views por producto-advertiser
    df_today = pd.DataFrame({'count' : df.groupby(['advertiser_id', 'product_id'])['product_id'].count().sort_values(ascending=False)}).reset_index()
    #Devuelvo los 20 productos mas vistos por advertiser
    df_top20 = df_today.groupby('advertiser_id').apply(lambda x : x.sort_values(by = 'count', ascending = False).head(20).reset_index(drop = True)).droplevel(level=0)
    upload_pandas_to_s3(df_top20, 'top_products')




