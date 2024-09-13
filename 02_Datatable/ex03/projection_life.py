from load_csv import load
import matplotlib.pyplot as plt


def main():
    gdp_csv = load('income_per_person_gdppercapita_ppp_inflation_adjusted.csv')
    life_expectancy_csv = load('life_expectancy_years.csv')
    if gdp_csv is None or life_expectancy_csv is None:
        exit(1)

    x_axis = gdp_csv['1900']
    y_axis = life_expectancy_csv['1900']

    plt.figure(figsize=(10, 6))
    plt.scatter(x_axis, y_axis)

    plt.title('1900')
    plt.xlabel('Gross domestic product')
    plt.ylabel('Life Expectancy')

    plt.xlim(300, 11000)
    plt.xscale('log')

    xticks = [300, 1000, 10000]
    plt.xticks(xticks, labels=['300', '1k', '10k'])

    plt.show()


if __name__ == "__main__":
    main()
