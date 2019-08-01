def rename_column(df, old_column, new_column):
    return df.rename(columns={old_column: new_column}, inplace=True)


def upper_column_values(df):#
    return df.columns.str.upper(inplace=True)


def delete_nulls_columns(df):#
    for column in df:
        if df[column].isnull().sum() > len(df.index)*50/100:
            return df.dop(column)


def delete_final_column_spaces(df):
    return df.columns.str.strip(inplace=True)


def delete_rows(df, column, row_text):
    return df.drop(df[df[column] == row_text].index, inplace=True)


def delete_columns(df, column):
    return df.drop(df[column], inplace=True)


def reset_index(df):
    return df.reset_index(df, axis=1)













