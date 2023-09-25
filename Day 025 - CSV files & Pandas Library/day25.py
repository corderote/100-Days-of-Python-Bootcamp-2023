# -----------------------------------------------------------------------------
# CSV Files.
# CSV stands for Comma Separated Values.
import csv
import pandas

# Using what we know to read the CSV file:
# weather_file = open("weather_data.csv", "r")
# weather_data = weather_file.read()
# weather_file.close()
# weather_data_list = weather_data.split("\n")
# print(weather_data_list)

# Using the csv library from python.

with open("weather_data.csv") as weather_file:
    weather_data = csv.reader(weather_file)
    for row in weather_data:
        print(row)

# -----------------------------------------------------------------------------
# Exercise 1 - Extract a list with only the temperatures from the file.
with open("weather_data.csv") as weather_file:
    weather_data = csv.reader(weather_file)
    weather_temperatures = []
    for row in weather_data:
        if row[1] != "temp":
            weather_temperatures.append(int(row[1]))
print(weather_temperatures)

# -----------------------------------------------------------------------------
# Pandas Library.
weather_data = pandas.read_csv("weather_data.csv")
print(weather_data)
print(weather_data["temp"])

# -----------------------------------------------------------------------------
# Data Frames & Series
# Series inside the pandas library works as a list in python.
# Data frames takes multiple Series and works as the tables that we see in our
# csv files.
# Both are Data Types from panda.
# More info at Panda's documentation: https://pandas.pydata.org/docs/
# https://pandas.pydata.org/docs/reference/index.html

weather_dict = weather_data.to_dict()
print(weather_dict)
temperature_list = weather_data["temp"].to_list()
print(temperature_list)
# -----------------------------------------------------------------------------
# Exercise 2 - Get Average Temperature from the weather_data.csv
total_temperature = sum(temperature_list)
# for i in temperature_list:
#     total_temperature += i
average_temperature = round(total_temperature/len(temperature_list))
print(f"Average Temperature: {average_temperature}")
# Easier way with pandas:
print(weather_data["temp"].mean())

# TIP: If you want to avoid using the quote to access the Series in panda, you
# can just use the column as an attribute.
print(weather_data.temp)

# Get data from rows:
monday = weather_data[weather_data.day == "Monday"]
print(monday.condition)
# -----------------------------------------------------------------------------
# Exercise 3 - Get row where the temperature was its maximum.
print(weather_data[weather_data.temp == weather_data.temp.max()])

# -----------------------------------------------------------------------------
# Create a DataFrame and documents.
my_dict = {
    "column_1": ["name_1", "name_2", "name_3", "name_4", "name_5"],
    "column_2": ["value_1", "value_2", "value_3", "value_4", "value_5"],
}
my_data_frame = pandas.DataFrame(my_dict)
print(my_data_frame)
# my_data_frame.to_csv("data_frame.csv")
