import pandas as pd
import random
import string
from files.aux_function import upload_pandas_to_s3, download_s3_to_pandas

def FiltrarDatos(**kwargs):
    date = kwargs['date']

    #Genero 20 advertiser_id activos y 5 inactivos por unica vez
    try:
        all_advertisers_df = download_s3_to_pandas('all_advertisers')
        advertisers_catalog_df = download_s3_to_pandas('advertisers_catalogs', index_col=0).to_dict('split')
        all_advertisers = all_advertisers_df.advertiser_id.tolist()
        advertisers_catalogs = {advertiser: advertisers_catalog_df['data'][n]
                                for n, advertiser in enumerate(advertisers_catalog_df['index'])}
        print(advertisers_catalogs)
    except:
        random.seed(4)
        active_advertisers = [''.join(random.choices(string.ascii_uppercase + string.digits, k = 20)) for _ in range(20)]
        inactive_advertisers = [''.join(random.choices(string.ascii_uppercase + string.digits, k = 20)) for _ in range(5)]
        all_advertisers = active_advertisers+inactive_advertisers

        all_advertisers_df = pd.DataFrame(all_advertisers, columns=['advertiser_id'])
        upload_pandas_to_s3(all_advertisers_df, 'all_advertisers')

        advertisers_catalogs = {}
        for advertiser in all_advertisers:
            advertisers_catalogs[advertiser] = [''.join(random.choices(string.ascii_lowercase + string.digits, k = 6)) for _ in range(100)]
        advertisers_catalogs_df = pd.DataFrame.from_dict(advertisers_catalogs, orient='index')
        upload_pandas_to_s3(advertisers_catalogs_df, 'advertisers_catalogs', index=True)

    #Genero lineas de vistas de producto

    product_views = []
    for _ in range(100_000):
        advertiser_i = random.choice(all_advertisers)
        product_views.append([advertiser_i, random.choice(advertisers_catalogs[advertiser_i]), date])

    df_product_views = pd.DataFrame(product_views, columns=['advertiser_id', 'product_id', 'date'])
    df_product_views = df_product_views.sort_values('date').reset_index(drop=True)

    upload_pandas_to_s3(df_product_views, f'product_views_{date}')

    #Genero lineas de vistas de ads

    ads_views = []
    for _ in range(100_000):
        advertiser_i = random.choice(all_advertisers)
        ads_views.append([advertiser_i, random.choice(advertisers_catalogs[advertiser_i]), random.choices(['impression', 'click'], weights=[99, 1])[0], date])
    df_ads_views = pd.DataFrame(ads_views, columns=['advertiser_id', 'product_id', 'type', 'date'])
    df_ads_views = df_ads_views.sort_values('date').reset_index(drop=True)

    upload_pandas_to_s3(df_ads_views, f'ads_views_{date}')



