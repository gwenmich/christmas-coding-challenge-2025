# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")

temp_list = data["temp"].to_list()
avg_temp = sum(temp_list) / len(temp_list)

print(avg_temp)
# print(data["temp"])