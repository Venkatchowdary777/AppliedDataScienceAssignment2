import pandas as pd


def load_dataframe(path, transform = False):
    df = pd.read_csv(path)
    if not transform:
        return df
    df = df.drop(['Country Code', 'Indicator Code'], axis =1)
    year_df = df.set_index(['Country Name', 'Indicator Name'])
    country_df = year_df.stack().unstack('Country Name')
    country_df.index.names = ['Indicator Name', 'years']
    return year_df, country_df