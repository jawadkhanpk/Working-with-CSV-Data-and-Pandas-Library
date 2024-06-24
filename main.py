import pandas

data = pandas.read_csv("weather-data.csv")
# to print overall data of a .csv file
print(data)

# to print specific column of a .csv file
print(data["temp"])
