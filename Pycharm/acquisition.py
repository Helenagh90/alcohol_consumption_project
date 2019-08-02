import pandas as pd


def get_csv(csv_file, encoding_value, separation):
    df = pd.read_csv(csv_file, encoding=encoding_value, sep=separation)
    return df 
