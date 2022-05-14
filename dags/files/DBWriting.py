from files.aux_function import download_s3_to_pandas, engine_ps
from sqlalchemy.types import String, Float, Integer


def DBWriting(**kwargs):
    date = kwargs['date']
    top_products_df = download_s3_to_pandas(f'top_products_{date}')
    top_products_df['date'] = date
    top_ctr_df = download_s3_to_pandas(f'top_ctr_{date}')
    top_ctr_df['date'] = date
    engine = engine_ps()

    with engine.connect() as con:
        con.execute(f"""BEGIN 
        DELETE FROM top_product WHERE date='{date}'; 
        EXCEPTION WHEN OTHERS THEN 
        NULL; 
        END;""")
        con.execute(f"""BEGIN 
        DELETE FROM top_ctr WHERE date='{date}'; 
        EXCEPTION WHEN OTHERS THEN 
        NULL; 
        END;""")

    top_products_df.to_sql('top_product', index=False, con=engine, if_exists='append',
                           dtype={"advertiser_id": String(),
                                  "product_id": String(),
                                  "count": Integer(),
                                  "date": String()
                                  })

    top_ctr_df.to_sql('top_ctr', index=False, con=engine, if_exists='append',
                           dtype={"advertiser_id": String(),
                                  "product_id": String(),
                                  "ctr": Float(),
                                  "date": String()
                                  })
