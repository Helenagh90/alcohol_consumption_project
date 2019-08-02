import acquisition
import wrangling
import analysis
import reporting 


def read_file(file):
    my_file = acquisition.get_csv(file, 'UTF-8', '[,\t]', engine='python')
    return my_file


def clean_file(my_file):
    my_file = wrangling.delete_nulls_columns(my_file)
    my_file = wrangling.delete_final_column_spaces(my_file)
    my_file = wrangling.upper_column_values(my_file)
    my_file = wrangling.rename_column(my_file, 'FREQUENC', 'FREQUENCY')
    my_file = wrangling.delete_rows(my_file, 'FREQUENCY', 'LT1M').delete_rows(my_file, 'FREQUENCY', 'NM12').delete_rows(my_file, 'FREQUENCY', 'NVR').delete_rows(my_file, 'FREQUENCY', 'NVR_NM12')
    my_file = wrangling.delete_rows(my_file, 'AGE', 'TOTAL').delete_rows(my_file, 'AGE', 'Y15-29').delete_rows(my_file, 'AGE', 'Y15-64').delete_rows(my_file, 'AGE', 'Y18-24').delete_rows(my_file, 'AGE', 'Y18-44').delete_rows(my_file, 'AGE', 'Y18-64').delete_rows(my_file, 'AGE', 'Y25-64').delete_rows(my_file, 'AGE', 'Y45-54').delete_rows(my_file, 'AGE', 'Y55-64').delete_rows(my_file, 'AGE', 'Y_GE18').delete_rows(my_file, 'AGE', 'Y_GE65')
    my_file = wrangling.delete_rows(my_file, 'CITIZEN', 'EU28_FOR').delete_rows(my_file, 'CITIZEN', 'FOR').delete_rows(my_file, 'CITIZEN', 'EU28_FOR').delete_rows(my_file, 'CITIZEN', 'NEU28_FOR')
    my_file = wrangling.reset_index(my_file)
    return my_file


def analyze_file(my_file):
    my_file = analysis.month_values(my_file, 'FREQUENCY', 'MTH')
    my_file_age = analysis.pivot_table(my_file, values=['EU28', 'BE', 'BG', 'CZ', 'DK', 'DE', 'EE', 'IE', 'EL', 'ES',
                                                        'HR', 'IT', 'CY', 'LV', 'LT', 'LU', 'HU', 'MT', 'AT', 'PL',
                                                        'PT', 'RO', 'SI', 'SK', 'FI', 'SE', 'UK', 'IS', 'NO'],
                                       columns='SEX', aggfunc='mean')
    my_file_sex = analysis.pivot_table(my_file, values=['EU28', 'BE', 'BG', 'CZ', 'DK', 'DE', 'EE', 'IE', 'EL', 'ES',
                                                        'HR', 'IT', 'CY', 'LV', 'LT', 'LU', 'HU', 'MT', 'AT', 'PL',
                                                        'PT', 'RO', 'SI', 'SK', 'FI', 'SE', 'UK', 'IS', 'NO'],
                                       columns='AGE', aggfunc='mean')
    my_file = analysis.concat_2_pivot_tables(my_file_age, my_file_sex)
    plot1 = analysis.interactive_graph(my_file, 'bar', 'index', ['F', 'M', 'T'], 'Country', 'Avg. by sex',
                                       'Monthly avg. by sex and country')
    plot2 = analysis.interactive_graph('bar', 'index', ['Y75+', 'Y15-24', 'Y25-34', 'Y35-44', 'Y45-64', 'Y65-74'],
                                       'Country', 'Avg. by age', 'Monthly avg. by age and country')
    return my_file, plot1, plot2


def report_file(my_file, plot1, plot2):
    my_file = reporting.download_csv(my_file)
    plot1 = reporting.download_graph(plot1)
    plot2 = reporting.download_graph(plot2)
    return my_file, plot1, plot2


def main():
    read = read_file('../alcohol_consumption.tsv')
    clean = clean_file(read)
    analysis = analyze_file(clean)
    report_file(analysis)


if __name__ == '__main__':
    main()
