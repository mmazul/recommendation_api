""" SQL tempplates"""

recommendation_day_adv_model = """
SELECT 
    product_id 
FROM 
    {{ table }}
WHERE 
    advertiser_id = {{ adv }}
    AND date = {{ today }}
"""

recommendation_last_n_day_adv = """
SELECT 
    product_id 
FROM 
    top_product
WHERE 
    advertiser_id={{ adv }}
    AND date<={{ end_date }}
    AND date>{{ start_date }}
UNION ALL
SELECT 
    product_id 
FROM 
    top_ctr
WHERE 
    advertiser_id={adv}
    AND date<={{ end_date }}
    AND date>{{ start_date }}
"""