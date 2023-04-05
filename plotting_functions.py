import matplotlib.pyplot as plt
from config import time_ranges
from pandas import DataFrame


def plot_correlation(data: DataFrame, countries: list, indicators: list, plotting_details: list) -> None:
    """
    Plots the scatter plot between different features to identify correlation

    Args:
        data (DataFrame): data to be plotted
        countries (list): list of countries to be plotted
        indicators (list): list of indicators to be plotted
        plotting_details (list): labels and titles for the plot
    """
    for country in countries:
        data_per_country = data.loc[country].T
        time_count = 0
        for year_data in [
            data_per_country.loc["1960":"1979"],
            data_per_country.loc["1980":"1999"],
            data_per_country.loc["2000":"2020"],
        ]:
            plt.scatter(
                year_data[indicators[0]].values,
                year_data[indicators[1]].values,
                color="r",
            )
            plt.title(
                f"{country} - {time_ranges[time_count]} - {plotting_details[0]}")
            plt.xlabel(plotting_details[1])
            plt.ylabel(plotting_details[2])
            time_count += 1
            plt.show()


def plot_scatter(data: DataFrame, indicators: list, countries: list, plotting_details: list) -> None:
    """Plotting satter plot for finding correlations

    Args:
        data (DataFrame): data to be plotted
        indicators (list): indicators to be correlated
        countries (list): countries for which data is too be populated
        plotting_details (list): labels and titles for the plot
    """   
    for country in countries:
        data_per_country = data.loc[country].T
        plt.scatter(data_per_country[indicators[0]], data_per_country[indicators[1]], color="magenta") 
        plt.title(f"{country} - {plotting_details[0]}")
        plt.xlabel(plotting_details[1])
        plt.ylabel(plotting_details[2])
        plt.show()
