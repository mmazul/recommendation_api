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

avg_distinct_product_last_n_days = """
SELECT avg(product_ids) as n
FROM (SELECT advertiser_id, count(distinct product_id) as product_ids
FROM (
    SELECT 
       advertiser_id,
       product_id
    FROM 
        top_product
    WHERE 
        to_date(date, 'YYYY-MM-DD')<=to_date('{end_date}', 'YYYY-MM-DD')
        AND to_date(date, 'YYYY-MM-DD')>to_date('{start_date}', 'YYYY-MM-DD')
    UNION ALL
    SELECT 
        advertiser_id,
        product_id
    FROM 
        top_ctr
    WHERE 
        to_date(date, 'YYYY-MM-DD')<=to_date('{end_date}', 'YYYY-MM-DD')
        AND to_date(date, 'YYYY-MM-DD')>to_date('{start_date}', 'YYYY-MM-DD')
) AS a
GROUP BY 1
) AS b
"""


stats_coincidences_last_n_days = """
SELECT avg((coincidences::float)/(product_ids_total::float)) as coincidences_ratio
FROM (
SELECT 
    coalesce(top_product.advertiser_id, top_ctr.advertiser_id) as advertiser_id,
    count(distinct coalesce(top_product.product_id,top_ctr.product_id)) as product_ids_total,
    count(distinct case when top_product.product_id is not null and top_ctr.product_id is not null then
    top_product.product_id end) as coincidences
FROM top_product
FULL OUTER JOIN top_ctr ON (top_product.advertiser_id=top_ctr.advertiser_id AND
top_product.product_id=top_ctr.product_id )
WHERE 
    (to_date(top_product.date, 'YYYY-MM-DD')<=to_date('{end_date}', 'YYYY-MM-DD')
    AND to_date(top_product.date, 'YYYY-MM-DD')>to_date('{start_date}', 'YYYY-MM-DD'))
    OR (to_date(top_ctr.date, 'YYYY-MM-DD')<=to_date('{end_date}', 'YYYY-MM-DD')
    AND to_date(top_ctr.date, 'YYYY-MM-DD')>to_date('{start_date}', 'YYYY-MM-DD'))
GROUP BY 1
) AS A
"""
