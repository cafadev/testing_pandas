from datetime import datetime
from dataframe import get_dataframe

import pytz

def split_data():
    df = get_dataframe()

    for date in df['TIMESTAMP'].dt.date.unique():
        df_filtered = df[df['TIMESTAMP'].dt.date == date]
        date_str = datetime.strftime(date, '%Y%m%d')
        file_name = f'./data/{date_str}.csv'
        df_filtered.to_csv(file_name, index=False)


def split_by_date(since_date, until_date):
    df = get_dataframe()

    timezone = pytz.timezone("America/Tegucigalpa")

    try:
        parsed_since_date = datetime.strptime(since_date, '%Y-%m-%d')
        parsed_until_date = datetime.strptime(until_date, '%Y-%m-%d')
    except:
        raise Exception("Date should follow the next format: yyyy-mm-dd")

    since_date_aware = timezone.localize(parsed_since_date)
    until_date_aware = timezone.localize(parsed_until_date)

    filtered_df = df.loc[
        (df['TIMESTAMP'] >= since_date_aware) & (df['TIMESTAMP'] <= until_date_aware)
    ]

    file_name = f'./filtered_data/{since_date}__{until_date}.csv'
    filtered_df.to_csv(file_name, index=False)


def reset():
    df = get_dataframe()
    filtered_df = df.tail(1)

    file_name = f'./filtered_data/reset.csv'
    filtered_df.to_csv(file_name, index=False)
