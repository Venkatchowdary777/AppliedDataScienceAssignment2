import pandas as pd
from stats import skew, kurtosis
from helper_functions import load_dataframe
from config import data_path, indicator_metadata_path, country_metadata_path

# from plotting functions import pie_chart, line_chart, bar_chart

# Loading metadata related to indicators
indicators_metadata = load_dataframe(indicator_metadata_path)
indicators_metadata = indicators_metadata.drop(columns=["Unnamed: 4"])

# Loading metadata related to indicators
country_metadata = load_dataframe(country_metadata_path)
country_metadata = country_metadata.drop(columns=["Unnamed: 5"]).dropna()

# Printing the countries based on income group filter
distinct_regions = country_metadata.IncomeGroup.unique()
print(f"Distinct income groups: {distinct_regions}")

for region in distinct_regions:
    print(f"============{region}====================")
    print(
        country_metadata[country_metadata["IncomeGroup"] == region][
            ["TableName", "Region"]
        ]
    )

# Loading main data with transformation
year_df, country_df = load_dataframe(data_path, transform=True)

# Picking few countries based on different income ranges
selected_countries = ["Australia", "Thailand", "India", "Yemen, Rep."]
indicators_of_interest = [
    "Urban population (% of total population)",
    "Population in urban agglomerations of more than 1 million (% of total population)",
    "Population living in areas where elevation is below 5 meters (% of total population)",
]

# Exploring statistical properties for indicators
for indicator in indicators_of_interest:
    print(f"================={indicator}===================")
    print(country_df[selected_countries + ["World"]].loc[indicator].describe())

# Creating dataframes wrt skew and kurtosis for paired indicators
skew_df = pd.DataFrame(columns = indicators_of_interest, index=selected_countries)
kurtosis_df = pd.DataFrame(columns = indicators_of_interest, index = selected_countries)
for indicator in indicators_of_interest:
    for country in selected_countries+["World"]:   
        skew_df[indicator][country] = skew(country_df[country].loc[indicator].values)
        kurtosis_df[indicator][country] = kurtosis(country_df[country].loc[indicator].values)

print("SKEW", skew_df)
print("Kurtosis", kurtosis_df)