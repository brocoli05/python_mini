## *args - Unlimited arguments
from typing import Any


def add(*args):
   # args is tuple
   print(args[0])
   """ Modify the add function to take an unlimited number of arguments. 
   Use a loop to sum all the arguments inside the function.
   Test it out by calling add() to calculate sum of some arguments. """
   sum = 0
   for n in args:
      sum += n

   return sum

# print(add(3, 5, 6, 1, 2))


## **kwargs - Unlimited keyword arguments
def calculate(n, **kwargs):
   print(type(kwargs))  # kwargs is dictionary
   print(kwargs)

   # for key, value in kwargs.items():
   #    print(key)
   #    print(value)
   n += kwargs["add"]
   n *= kwargs["multiply"]
   print(n)

# calculate(2, add=3, multiply=5)


class Car:
   def __init__(self, **kw):
      # self.make = kw["make"]
      # self.model = kw["model"]
      self.make = kw.get("make")
      self.model = kw.get("model")

# my_car = Car(make="Nissan", model="GT-R")
my_car = Car(make="Nissan")
print(my_car.model)  # None - get() avoids program crash 'Key error'