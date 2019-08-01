import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


import acquisition
import wrangling
import analysis
import reporting


def read_file(file):
    my_file = acquisition.get_csv(file, "UTF-8", "[,\t]")
    return my_file


def clean_file(my_file):
    my_file = wrangling.delete_nulls_columns(my_file)
    my_file = wrangling.delete_final_column_spaces(my_file)
    my_file = wrangling.upper_column_values(my_file)
    my_file = wrangling.rename_column(my_file, "FREQUENC", "FREQUENCY")
    my_file = wrangling.delete_rows(my_file, "FREQUENCY", "LT1M").delete_rows(my_file, "FREQUENCY", "NM12").delete_rows(my_file, "FREQUENCY", "NVR").delete_rows(my_file, "FREQUENCY", "NVR_NM12")
    my_file = wrangling.delete_rows(my_file, "AGE", "TOTAL").delete_rows(my_file, "AGE", "Y15-29").delete_rows(my_file, "AGE", "Y15-64").delete_rows(my_file, "AGE", "Y18-24").delete_rows(my_file, "AGE", "Y18-44").delete_rows(my_file, "AGE", "Y18-64").delete_rows(my_file, "AGE", "Y25-64").delete_rows(my_file, "AGE", "Y45-54").delete_rows(my_file, "AGE", "Y55-64").delete_rows(my_file, "AGE", "Y_GE18").delete_rows(my_file, "AGE", "Y_GE65")
    my_file = wrangling.delete_rows(my_file, "CITIZEN", "EU28_FOR").delete_rows(my_file, "CITIZEN", "FOR").delete_rows(my_file, "CITIZEN", "EU28_FOR").delete_rows(my_file, "CITIZEN", "NEU28_FOR")
    my_file = wrangling.reset_index(my_file)
    return my_file


def analyze_file(df):
    my_data = analysis.percent(df, 'Fatalities', 'Aboard')
    my_data = analysis.filter_col(my_data, 'Country')
    my_data = analysis.filter_data(my_data, 'Country')
    plot = analysis.draw_plot('Country', my_data)
    # my_data = reporting.change_null(df)
    return my_data, plot


def report(df, plot):
    my_data = reporting.download_csv(df)
    plot = reporting.download_plot(plot)
    return my_data, plot


def main():
    read = read_file("alcohol_consumption_project.csv")
    clean = clean_file(read)
    analysis, figure = analyze_file(clean)
    report(analysis, figure)


if __name__ == "__main__":
    main()
