import pandas as pd


<<<<<<< Updated upstream
def get_csv(csv_file, encoding_value, separation):
    df = pd.read_csv(csv_file, encoding=encoding_value, sep=separation)
    return df 
=======
def get_csv(csv_file, encoding_value, separation, engine):
    df = pd.read_csv(csv_file, encoding=encoding_value, sep=separation, engine=engine)
    return df
>>>>>>> Stashed changes
