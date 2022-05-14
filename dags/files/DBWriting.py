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
        top_product_exist = con.execute(f"""SELECT EXISTS (SELECT * FROM top_product)""")
        print(top_product_exist)
        if top_product_exist[0].items()[1]:
            con.execute(f"""BEGIN; 
            DELETE FROM top_product WHERE date='{date}'; 
            COMMIT;""")

        top_ctr_exist = con.execute(f"""SELECT EXISTS (SELECT * FROM top_ctr)""")
        print(top_ctr_exist)
        if top_ctr_exist[0].items()[1]:
            con.execute(f"""BEGIN; 
                    DELETE FROM top_ctr WHERE date='{date}'; 
                    COMMIT;""")

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
