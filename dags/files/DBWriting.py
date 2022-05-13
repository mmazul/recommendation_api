import pandas as pd
from files.aux_function import upload_pandas_to_s3


def DBWriting():
    df_ads_views = upload_pandas_to_s3('ads_views')