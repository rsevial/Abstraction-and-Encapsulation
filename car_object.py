# Programmed by: Rebekah Joy E. Sevial
# Test drive for Car class

# Import the class from car_class
from car_class import Car
# Create object for Car
car_object = Car(2020, "Inova", 0)
# Create For loop to get the speed of the car
# when accelerating
for i in range(5):
    car_object.__accelerate()
    print("Accelerate:", car_object.get_speed())
# Print current speed when accelarating
# when braking
# Print current speed when braking
