# Programmed by: Rebekah Joy E. Sevial
# Test drive for Fan class

# Import the class from the fan_class
from fan_class import Fan
# Define function for testing the fan, 2 times
def TestFan():
    first_try = Fan()
    second_try = Fan()
# Assigning the values of each attributes for first try and second try
    # first_try
    first_try.set_speed(3)
    first_try.set_fan_on()
    first_try.set_radius(10)
    first_try.set_color("Yellow")
# Print the output
    second_try.set_speed(2)
    second_try.set_fan_off()
    second_try.set_radius(5)
    second_try.set_color("Blue") 
# Call the main function