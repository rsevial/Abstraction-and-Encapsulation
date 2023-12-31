# Programmed by: Rebekah Joy E. Sevial
# Test drive for Car class

# Import the class from car_class
from car_class import Car
# import module to edit the font and color
import fontstyle
# Create object for Car
car_object = Car(2020, "Inova", 0)
# Create For loop to get the speed of the car
# when accelerating
for i in range(5):
    car_object.accelerate()
    print("Accelerate:", car_object.get_speed())
# Print current speed when accelarating
print(fontstyle.apply("The current speed of the car is:", 'bold/purple/UNDERLINE'), car_object.get_speed(), '\n')
# when braking
for i in range(5):
    car_object.brake()
    print("Brake:", car_object.get_speed())
# Print current speed when braking
print(fontstyle.apply("The current speed of the car is:", 'bold/purple/UNDERLINE'), car_object.get_speed(), '\n')
