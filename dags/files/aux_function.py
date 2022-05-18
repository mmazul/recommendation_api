""" Auxiliar functions """

import pandas as pd
from decouple import config
from sqlalchemy import create_engine

def engine_ps():
    username = config('PS_USER')
    password = config('PS_PASSWORD')
    host = config('PS_HOST')
    port = config('PS_PORT', default='5432')
    database = config('PS_DATABASE', default="postgres")
    engine = create_engine(F'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}',
                           echo=False)

    return engine

def upload_pandas_to_s3(dataframe,
                        name: str,
                        bucket: str = 'tp-udesa-dai',
                        extension: str = 'csv',
                        index: bool = False,
                        ):
    print(f'Upload ---> s3://{bucket}/{name}.{extension}')
    dataframe.to_csv(f's3://{bucket}/{name}.{extension}', index=index)
    print(f'Upload ---> {len(dataframe)}')

def download_s3_to_pandas(name: str,
                          bucket: str = 'tp-udesa-dai',
                          extension: str = 'csv',
                          index_col=None) -> pd.DataFrame:
    print(f'Download --->s3://{bucket}/{name}.{extension}')
    df = pd.read_csv(f's3://{bucket}/{name}.{extension}', index_col=index_col)
    print(f'Download ---> {len(df)}')
    return df
