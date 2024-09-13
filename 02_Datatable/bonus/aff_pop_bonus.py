from load_csv import load
from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys


def main():
    data = load("population_total.csv")
    if data is None:
        exit(1)

    try:
        if len(sys.argv) != 2:
            raise Exception("usage: python3 aff_pop.py <country>")
        country_name = sys.argv[1]
        country_population = extract_population(data, country_name.capitalize())
    except IndexError:
        print("error: country doesn't exists in the data file")
        exit(1)
    except Exception as error:
        print(f'error: {error}')
        exit(1)

    x_axis = data.columns[1:].astype(int)
    france_population = extract_population(data, 'France')

    max_population = max(france_population.max(), country_population.max())
    y_ticks_interval = max_population / 10
    y_ticks = np.arange(0, max_population, y_ticks_interval)

    plt.plot(x_axis, france_population, 'g', label='France')
    plt.plot(x_axis, country_population, 'b', label=country_name)

    plt.title('Population Projections')
    plt.xlabel('Year')
    plt.ylabel('Populations')

    plt.xticks(x_axis[::40])
    plt.yticks(y_ticks)

    plot = plt.gca()
    y_axis = plot.get_yaxis()
    formatter = FuncFormatter(format_y_ticks)
    y_axis.set_major_formatter(formatter)

    plt.legend()
    plt.show()


def extract_population(data: pd.DataFrame, country: str) -> pd.Series:
    country_data = data[data.country == country]
    country_data = country_data.drop(columns=['country'])

    if country_data.empty:
        raise ValueError("Country name is not correct.")

    for year in country_data.columns:
        country_data[year] = country_data[year].apply(convert_population)

    return country_data.squeeze()


def convert_population(obj):
    try:
        if 'M' in obj:
            return float(obj.replace('M', '')) * 1_000_000
        elif 'K' in obj:
            return float(obj.replace('K', '')) * 1_000
        elif 'B' in obj:
            return float(obj.replace('B', '')) * 1_000_000_000
        else:
            return float(obj)
    except ValueError:
        return 0.0


def format_y_ticks(value, osef):
    if value >= 1_000_000_000:
        return f'{value / 1_000_000_000:.1f}B'
    elif value >= 1_000_000:
        return f'{value / 1_000_000:.1f}M'
    elif value >= 1_000:
        return f'{value / 1_000:.1f}K'
    else:
        return str(value)


if __name__ == "__main__":
    main()
