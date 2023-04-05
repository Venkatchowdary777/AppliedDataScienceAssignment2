import pandas as pd
from stats import skew, kurtosis
from helper_functions import load_dataframe
from plotting_functions import plot_correlation, plot_scatter
from config import data_path, indicator_metadata_path, country_metadata_path

# Loading metadata related to indicators
indicators_metadata = load_dataframe(indicator_metadata_path)
indicators_metadata = indicators_metadata.drop(columns=["Unnamed: 4"])
print("============ Indicators List =============")
print(indicators_metadata.INDICATOR_NAME.head(5))

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
        ].head()
    )

# Loading main data with transformation
year_df, country_df = load_dataframe(data_path, transform=True)

# Picking few countries based on different income ranges
selected_countries = ["Australia", "Thailand", "India", "Yemen, Rep."]
indicators_codes = [
    "SP.URB.TOTL.IN.ZS",
    "EN.URB.MCTY.TL.ZS",
     "EN.POP.EL5M.UR.ZS"
]
indicators_of_interest = [
    list(
        indicators_metadata[
        indicators_metadata["INDICATOR_CODE"] == x]
        ["INDICATOR_NAME"].values
        )[0]
        for x in indicators_codes]

# Exploring statistical properties for indicators
for indicator in indicators_of_interest:
    print(f"=================Description of {indicator}===================")
    print(country_df[selected_countries + ["World"]].loc[indicator]
    .describe())

# Creating dataframes wrt skew and kurtosis for paired indicators
skew_df = pd.DataFrame(
    columns=indicators_of_interest,
    index=selected_countries)
     
kurtosis_df = pd.DataFrame(
    columns=indicators_of_interest,
    index=selected_countries)

for indicator in indicators_of_interest:
    for country in selected_countries + ["World"]:
        data = country_df[country].loc[indicator].values
        skew_df[indicator][country] = skew(data)
        kurtosis_df[indicator][country] = kurtosis(data)

print("======================== SKEW ======================", skew_df)
print("======================== Kurtosis ======================", kurtosis_df)

# Exploring correlations between indicators
countries = ["Japan", "Sudan"]
indicators = indicators_of_interest[:2]
print(indicators)
plot_correlation(
    year_df,
    countries,
    indicators,
    [
        "urban population vs agglomerations",
        "urban population",
        "urban agglomerations"
    ],
)


countries = ["China", "Bangladesh"]
indicators = [
    "Urban population (% of total population)",
    "CO2 emissions (kt)"
     ]
plot_scatter(
    year_df,
    indicators,
    countries,
    [
        "urban population vs CO2 emission",
        "urban population",
        "CO2 emissions"
    ],
)


countries = ["Malta", "Yemen, Rep."]
indicators = ["Population growth (annual %)", "Arable land (% of land area)"]
plot_correlation(
    year_df,
    countries,
    indicators,
    [
        "population vs arable land",
        "population growth",
        "arable land %"
    ],
)

countries = ["Korea, Dem. People's Rep.", "Indonesia", "China", "Korea, Rep."]
indicators = [
    "Urban population (% of total population)",
    "Electric power consumption (kWh per capita)",
]
plot_scatter(
    year_df,
    indicators,
    countries,
    [
        "urban population vs power consumption",
        "urban population",
        "electric power consumption",
    ],
)
