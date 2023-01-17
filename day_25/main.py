# with open("weather_data.csv") as data_files:
#    data = data_files.readlines()
#   print(data)

# import csv

# with open("weather_data.csv") as data_files:
#    data = csv.reader(data_files)
#   temperatures = []
#   for row in data:
#        print(row[1])
#       if row[1] != "temp":
#           temperatures.append(int(row[1])) # <- Convert to integer number
#   print(temperatures)
import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data["temp"]) # <- print the temperature column

# data_dict = data.to_dict()
# print(data_dict)

#temp_list = data["temp"].to_list()
# print(temp_list)

# average = sum(data["temp"]) / len(temp_list)
# or average = sum(temp_list) / len(temp_list)
# or print(data["temp"]).mean()
# print(average)

# print(data["temp"].max()) # <- To extract the max number of column

# print(data["condition"])
# or print(data.condition)

# Get Data in Row
# print(data[data.day == "Monday"])
#print(data[data.temp == data.temp.max()])

# Get condition of day
#monday = data[data.day == "Monday"]
#print(monday.condition)

#monday = data[data.day == "Monday"]
#monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

data_dict = {
    "animals": ["Turtle", "Dog", "Lion"],
    "age": [100, 15, 25]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")