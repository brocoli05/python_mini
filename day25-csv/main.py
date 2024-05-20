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

data = pandas.read_csv("weather_data.csv")
print(data)
print(data["temp"])
