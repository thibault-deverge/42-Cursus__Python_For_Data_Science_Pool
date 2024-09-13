from load_csv import load
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def main():
    data = load("population_total.csv")
    if data is None:
        exit(1)

    x_axis = data.columns[1:-50].astype(int)
    y_ticks = np.arange(0, 80, 20)

    france_population = extract_population(data, 'France')
    belgium_population = extract_population(data, 'Belgium')

    plt.plot(x_axis, france_population, 'g', label='France')
    plt.plot(x_axis, belgium_population, 'b', label='Belgium')

    plt.title('Population Projections')
    plt.xlabel('Year')
    plt.ylabel('Populations')
    plt.xticks(x_axis[::40])
    plt.yticks(y_ticks, ['', '20M', '40M', '60M'])

    plt.legend()
    plt.show()


def extract_population(data: pd.DataFrame, country: str) -> pd.Series:
    country_data = data[data.country == country]
    country_data = country_data.drop(columns=['country'])

    for year in country_data.columns:
        country_data[year] = country_data[year].apply(convert_population)

    return country_data.iloc[0, :-50]


def convert_population(obj):
    return float(obj.replace('M', ''))


if __name__ == "__main__":
    main()
