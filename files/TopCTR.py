# Modelo TopTCR
# Cuantos clicks/impresion se hacen de cada producto
# df_ads_views.head(20)

import pandas as pd
import numpy as np

df_ads_views = pd.read_csv('ads_views.csv')
#print(df_ads_views.head(5))
#print(df_ads_views.head(10))



def TopCTR(adv):
    all_groups = df_ads_views.groupby(['advertiser_id', 'product_id', 'type'], as_index=False).count()
    # for adv in df_ads_views['advertiser_id'].unique():
    advertiser = all_groups.loc[all_groups['advertiser_id'] == adv]
    impress = []
    click = []
    ctr = {}
    for prod in advertiser['product_id'].unique():
        product = advertiser.loc[advertiser['product_id'] == prod]
        impress = (product.loc[product['type'] == 'impression']['date'])
        click = (product.loc[product['type'] == 'click']['date'])
        # print prod
        click = click.sum()
        # print('click',click)
        impress = impress.sum()
        # print ('impress',impress)
        suma = click + impress
        # print('suma' ,suma)
        rate = click/suma
        # print('rate', rate)
        ctr[prod] = rate

    return max(ctr)

print(TopCTR('KD9PHCBGYFBRI9ET1O9R'))
print(TopCTR('LW045DVYSGRD75TK6U54'))
print(TopCTR('IOBPI63RBJIHI5FB7U9O'))
print(TopCTR('LW045DVYSGRD75TK6U54'))

