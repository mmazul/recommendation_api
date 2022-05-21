""" SQL tempplates"""

recommendation_day_adv_model = """
SELECT 
    product_id 
FROM 
    {table}
WHERE 
    advertiser_id = '{adv}'
    AND  to_date(date, 'YYYY-MM-DD') = to_date('{today}', 'YYYY-MM-DD')
"""

recommendation_last_n_day_adv = """
SELECT 
    product_id 
FROM 
    top_product
WHERE 
    advertiser_id='{adv}'
    AND to_date(date, 'YYYY-MM-DD')<=to_date('{end_date}', 'YYYY-MM-DD')
    AND to_date(date, 'YYYY-MM-DD')>to_date('{start_date}', 'YYYY-MM-DD')
UNION ALL
SELECT 
    product_id 
FROM 
    top_ctr
WHERE 
    advertiser_id='{adv}'
    AND to_date(date, 'YYYY-MM-DD')<=to_date('{end_date}', 'YYYY-MM-DD')
    AND to_date(date, 'YYYY-MM-DD')>to_date('{start_date}', 'YYYY-MM-DD')
"""

advertisers_count_last_n_days = """
SELECT count(distinct advertiser_id)  as n
FROM (
    SELECT 
       advertiser_id
    FROM 
        top_product
    WHERE 
        to_date(date, 'YYYY-MM-DD')<=to_date('{end_date}', 'YYYY-MM-DD')
        AND to_date(date, 'YYYY-MM-DD')>to_date('{start_date}', 'YYYY-MM-DD')
    UNION ALL
    SELECT 
        advertiser_id
    FROM 
        top_ctr
    WHERE 
        to_date(date, 'YYYY-MM-DD')<=to_date('{end_date}', 'YYYY-MM-DD')
        AND to_date(date, 'YYYY-MM-DD')>to_date('{start_date}', 'YYYY-MM-DD')
) AS a
"""
