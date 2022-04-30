""" Auxiliar functions """

import boto3

def upload_pandas_to_s3(dataframe, name: str):
    dataframe.to_csv(name)
    s3 = boto3.client("s3")
    s3.upload_file(
        Filename=name,
        Bucket="recommendation-api-morales",
        Key=name,
    )
