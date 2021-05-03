import pandas as pd
from google.cloud import bigquery

def send_df_to_bigquery(df):
    PROJECT = '{PROJECT-ID}'
    DATASET = '{DATASET-NAME}'
    TABLE = '{TABLE-NAME}'


    bigquery_client = bigquery.Client()

    table_name = f"{PROJECT}.{DATASET}.{TABLE}"

    job_config = bigquery.LoadJobConfig(
    schema=[
        bigquery.SchemaField("column1", bigquery.enums.SqlTypeNames.STRING),
        bigquery.SchemaField("column2", bigquery.enums.SqlTypeNames.INTEGER),
        bigquery.SchemaField("column3", bigquery.enums.SqlTypeNames.STRING),
        bigquery.SchemaField("column4", bigquery.enums.SqlTypeNames.STRING),
    ],
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
    )
    query_job = bigquery_client.load_table_from_dataframe(
        df
        , table_name
        , job_config=job_config
    )
    query_job.result()
