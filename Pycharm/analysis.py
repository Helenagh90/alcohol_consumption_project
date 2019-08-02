def month_values(df, column, column_value):
    return df[df[column] == column_value].iloc[:, 2:]


def pivot_table(df, values, columns, aggfunc):
    return df.pivot_table(values=values, columns=columns, aggfunc=aggfunc)


def concat_2_pivot_tables(pivot1, pivot2):
    return pd.concat([pivot1, pivot2], axis=1)


def interactive_graph(df, kind, x, y, x_title, y_title, title):
    return df.iplot(kind=kind, x=x, y=y, xTitle=x_title, yTitle=y_title, title=title)


