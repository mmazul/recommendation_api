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
        top_product_exist = con.execute(f"""SELECT EXISTS (
        SELECT FROM pg_tables WHERE schemaname = 'public' AND tablename  = 'top_product');""")
        top_product_exist_bool = top_product_exist.fetchone()[0]
        print(f"top_product_exist {str(top_product_exist_bool)}")
        if top_product_exist_bool:
            con.execute(f"""BEGIN; 
            DELETE FROM top_product WHERE date='{date}'; 
            COMMIT;""")

        top_ctr_exist = con.execute(f"""SELECT EXISTS (
        SELECT FROM pg_tables WHERE schemaname = 'public' AND tablename  = 'top_ctr');""")
        top_ctr_exist_bool = top_ctr_exist.fetchone()[0]
        print(f"top_ctr_exist {str(top_ctr_exist_bool)}")
        if top_ctr_exist_bool:
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
