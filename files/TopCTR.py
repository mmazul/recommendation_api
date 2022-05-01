# Modelo TopTCR
# Cuantos clicks/impresion se hacen de cada producto
# df_ads_views.head(20)

import pandas as pd
import numpy as np

df_ads_views = pd.read_csv('ads_views.csv')
#print(df_ads_views.head(5))
#print(df_ads_views.head(10))



def TopCTR():
    all_groups = df_ads_views.groupby(['advertiser_id', 'product_id', 'type'], as_index=False).count()
    final = []
    for adv in df_ads_views['advertiser_id'].unique():
        advertiser = all_groups.loc[all_groups['advertiser_id'] == adv]
        ctr = {}
        lista = {}
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
            lista = sorted(ctr.items(), key=lambda x: x[1], reverse=True)
            top_20 = lista[:20]
        for element in top_20:
            final.append([adv, element[0], element[1]])
    final = pd.DataFrame(final,columns=['advertiser_id','product_id','ctr'])
#    resultado = pd.DataFrame(columns=['advertiser_id','CTR'])
#    for key in final:
#        resultado = resultado.append([key,final[key]])
    return final
    # return pd.DataFrame(list(final),columns=['advertiser_id','prod','ctr'])

print (TopCTR())