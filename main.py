# Reading .CSV File Data with the help of Pandas Library

import pandas

data = pandas.read_csv("weather-data.csv")
# to print overall data or dataframe of a .csv file
print(data)

# to print specific column or series data of a .csv file
print(data["temp"])