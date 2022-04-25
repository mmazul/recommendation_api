import pandas as pd
import random
import string
#import boto3

#Genero 20 advertiser_id activos y 5 inactivos

random.seed(4)
active_advertisers = [''.join(random.choices(string.ascii_uppercase + string.digits, k = 20)) for _ in range(20)]
inactive_advertisers = [''.join(random.choices(string.ascii_uppercase + string.digits, k = 20)) for _ in range(5)]
all_advertisers = active_advertisers+inactive_advertisers

pd.DataFrame(active_advertisers, columns=['advertiser_id']).to_csv('advertiser_ids', index=False)

advertisers_catalogs = {}
for advertiser in all_advertisers:
    advertisers_catalogs[advertiser] = [''.join(random.choices(string.ascii_lowercase + string.digits, k = 6)) for _ in range(100)]

possible_dates = [f'2022-04-{day:02d}' for day in range(5,15)]

#Genero lineas de vistas de producto

product_views = [[advertiser := random.choice(all_advertisers), random.choice(advertisers_catalogs[advertiser]), random.choice(possible_dates)] for _ in range(100_000)]
df_product_views = pd.DataFrame(product_views, columns=['advertiser_id', 'product_id', 'date'])
df_product_views = df_product_views.sort_values('date').reset_index(drop=True)

df_product_views.to_csv('product_views.csv', index=False)

#Genero lineas de vistas de ads

ads_views = [[advertiser := random.choice(all_advertisers), random.choice(advertisers_catalogs[advertiser]), random.choices(['impression', 'click'], weights=[99, 1])[0], random.choice(possible_dates)] for _ in range(100_000)]
df_ads_views = pd.DataFrame(ads_views, columns=['advertiser_id', 'product_id', 'type', 'date'])
df_ads_views = df_ads_views.sort_values('date').reset_index(drop=True)
print(df_ads_views.head())

df_ads_views.to_csv('ads_views.csv', index=False)




