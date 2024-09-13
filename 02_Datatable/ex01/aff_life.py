from load_csv import load
import matplotlib.pyplot as plt


def main():
    """Load csv data, and make a plot of France life expectancy"""
    data = load("life_expectancy_years.csv")
    if data is None:
        exit(1)

    france_data = data[data.country == 'France']
    x_axis = data.columns[1:].astype(int)
    y_axis = france_data.iloc[0, 1:]

    plt.plot(x_axis, y_axis, linewidth=2)

    plt.title('France Life expectancy Projections', fontdict={"fontsize": 16})
    plt.xlabel('Year', fontdict={"fontsize": 16})
    plt.ylabel('Life expectancy', fontdict={"fontsize": 16})
    plt.xticks(x_axis[::40])
    plt.yticks(range(30, 100, 10))

    plt.show()


if __name__ == "__main__":
    main()
