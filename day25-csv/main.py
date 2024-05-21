####################################### Read csv file ####################################
## METHOD 1 - open file
""" Open the weather_data.csv. 
Use .readlines() to create a list named data that contains the values from the .csv file. """

# with open("weather_data.csv") as data_file:
#    data = data_file.readlines()
#    print(data)

## METHOD 2 - import csv
# import csv

# with open("weather_data.csv") as data_file:
#    data = csv.reader(data_file)
#    temperatures = []
#    for row in data:
#       if row[1] != "temp":
#          temperature = int(row[1])
#          temperatures.append(temperature)
      
#    print(temperatures)


## METHOD 3 - import pandas
import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])

# print(type(data))  # DataFrame
# print(type(data["temp"]))  # Series

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)
# print(len(temp_list))

# Calculate the average temperature
# average_temp = sum(temp_list) / len(temp_list)
# print(average_temp)

# print(data["temp"].mean())
# print(data["temp"].max())

# Get Data in Columns
# print(data["condition"]) 
# print(data.condition)  # same result

# Get Data in Row
# print(data[data.day == "Monday"])

# Print the row of data which has the highest temperature
# print(data[data.temp == max(data.temp)])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)

# # Convert Monday's temperature to Fahrenheit
# monday_temp = monday.temp[0]
# monday_temp_f = (monday_temp * 9 / 5) + 32
# print(monday_temp_f)

# Create a dataframe from scratch
# data_dict = {
#    "students": ["Amy", "James", "Angela"],
#    "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
color = data["Primary Fur Color"]

# count the number of each squirrel
gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrel_count)
print(red_squirrel_count)
print(black_squirrel_count)

# define the keys
data_dict = {
   "Fur Color": ["Gray", "Cinnamon", "Black"],
   "Count": [gray_squirrel_count, red_squirrel_count, black_squirrel_count],
}

# make the data frame and convert it to a csv file
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")