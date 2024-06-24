import pandas

data_dictionary = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dictionary)
print(data)

data.to_csv("new_data.csv")  # this line will create a .csv file and save DataFrame data