# Programmed by: Rebekah Joy E. Sevial
# Design a class named Car

# Create a class named Car
class Car:
# Define constructor of the Car (year_model, make, speed)
    # Create a private data for the year_model, make, speed
    def __init__(self, year_model, make, speed = 0):
        self.__year_model = year_model
        self.__make = make
        self.__speed = speed
# Define methods for acceleration
    def accelerate(self):
        self.__speed += 5
        return self.__speed
# Define methods for brake
# Define methods for get_speed