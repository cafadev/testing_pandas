import csv
import pandas as pd


def get_dataframe():
    data = []

    with open('./raw_data/raw_data.dat', newline='') as f_input:
        file = csv.reader(f_input, quotechar='\x01')
        for row in file:
            data.append([v.strip('"') for v in row])

    columns = data[1]

    df = pd.DataFrame(data[4:], columns=columns)
    df["TIMESTAMP"] = df["TIMESTAMP"].apply(pd.Timestamp, tz="America/Tegucigalpa")
    return df
