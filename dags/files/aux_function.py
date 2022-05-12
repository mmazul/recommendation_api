""" Auxiliar functions """

import pandas as pd

def upload_pandas_to_s3(dataframe,
                        name: str,
                        bucket: str = 'recommendation-api-morales',
                        extension: str = 'csv'):

    dataframe.to_csv(f's3://{bucket}/{name}.{extension}', index=False)

def download_s3_to_pandas(name: str,
                          bucket: str = 'recommendation-api-morales',
                          extension: str = 'csv') -> pd.DataFrame:

    df = pd.read_csv(f's3://{bucket}/{name}.{extension}')
    return df
