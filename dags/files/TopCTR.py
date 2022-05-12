import pandas as pd
from files.aux_function import download_s3_to_pandas


def TopCTR():
    df_ads_views = download_s3_to_pandas('ads_views')
    all_groups = df_ads_views.groupby(['advertiser_id', 'product_id', 'type'], as_index=False).count()
    final = []
    for adv in df_ads_views['advertiser_id'].unique():
        advertiser = all_groups.loc[all_groups['advertiser_id'] == adv]
        ctr = {}
        for prod in advertiser['product_id'].unique():
            product = advertiser.loc[advertiser['product_id'] == prod]
            impress = (product.loc[product['type'] == 'impression']['date'])
            click = (product.loc[product['type'] == 'click']['date'])
            click = click.sum()
            impress = impress.sum()
            suma = click + impress
            rate = click/suma
            ctr[prod] = rate
            lista = sorted(ctr.items(), key=lambda x: x[1], reverse=True)
            top_20 = lista[:20]
        for element in top_20:
            final.append([adv, element[0], element[1]])
    final = pd.DataFrame(final, columns=['advertiser_id','product_id','ctr'])
    return final