import matplotlib.pyplot as plt
from config import time_ranges
from pandas import DataFrame


def plot_correlation(data: DataFrame, countries: list, indicators: list) -> None:
    """
    Plots the scatter plot between different features to identify correlation

    Args:
        data (DataFrame): data to be plotted
        countries (list): list of countries to be plotted
        indicators (list): list of indicators to be plotted
    """
    fig, ax = plt.subplots(len(countries), len(time_ranges), figsize=(15, 5))
    ax_row = 0
    for country in countries:
        data_per_country = data.loc[country].T
        ax_col = 0
        # fig, ax = plt.subplots(1, 3, figsize=(15, 5))
        for year_data in [
            data_per_country.loc["1960":"1979"],
            data_per_country.loc["1980":"1999"],
            data_per_country.loc["2000":"2020"],
        ]:
            ax[ax_row][ax_col].scatter(
                year_data[indicators[0]].values,
                year_data[indicators[1]].values,
                color="r",
            )
            ax[ax_row][ax_col].title.set_text(f"{country} - {time_ranges[ax_col]}")
            ax_col += 1
        ax_row += 1
    fig.tight_layout()
    plt.show()


