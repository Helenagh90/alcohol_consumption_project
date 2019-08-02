def rename_column(df, old_column, new_column):
    return df.rename(columns={old_column: new_column})


def upper_column_values(df):
    return df.columns.str.upper()


def delete_nulls_columns(df):
    for column in df:
        if df[column].isnull().sum() > len(df.index)*50/100:
            return df.drop(column)


def delete_final_column_spaces(df):
    return df.columns.str.rstrip()


def delete_rows(df, column, row_text):
    return df.drop(df[df[column] == row_text].index)


def delete_columns(df, column):
    return df.drop(df[column])


def reset_index(df):
    return df.reset_index(df, axis=1) 


def export_final_csv(df):
    return df.to_csv('BBDD.csv')










