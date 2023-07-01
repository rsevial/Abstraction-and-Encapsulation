# Programmed by: Rebekah Joy E. Sevial
# Design a class named Fan to represent a fan

# Create a class named Fan
class Fan:
    # Define constructor of the Fan (speed, on, radius, color)
    def __init__(self, speed="slow",on = False, radius=5, color='blue'):
        # Create a private data named speed, on, radius, color
        self.__speed = speed
        self.__on = on
        self.__radius = radius
        self.__color = color
    # Define fan speed
    def speed(self, speed):
        if speed == 1:
            self.__speed = "slow"
        elif speed == 2:
            self.__speed = "medium"
        elif speed == 3:
            self.__speed = "fast"
        else:
            print("Speed, out-of-range. Set the speed again.")
# Create the getters for the four private data
    # Define method get_speed
    def get_speed(self):
        return self.__speed
    # Define method get_on
    def get_on(self):
        return self.__on
    # Define method get_radius
    def get_radius(self):
        return self.__radius
    # Define method get_color
    def get_color(self):
        return self.__color
# Create setters for the four private data
    # Define method set_speed
    def set_speed(self, speed):
        self.__speed = speed
    # Define method set_on
    def set_on(self, on):
        self.__on = on    
    # Define method set_radius
    def set_radius(self, radius):
        self.__radius = radius
    # Define method set_color
    def set_color(self, color):
        self.__color = color