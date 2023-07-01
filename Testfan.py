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
    # second try
    second_try.set_speed(2)
    second_try.set_fan_off()
    second_try.set_radius(5)
    second_try.set_color("Blue") 
    # import module to edit the font and color
    import fontstyle
    # Print the output
    print(fontstyle.apply('First Object', 'bold/UNDERLINE/yellow'))
    print('Speed: ', fontstyle.apply(first_try.get_speed(), 'Italic'), '\nRadius: ', fontstyle.apply(first_try.get_radius(), 'Italic'), '\nColor: ', fontstyle.apply(first_try.get_color(), 'Italic'), '\nOn/Off: ', fontstyle.apply(first_try.get_on(), 'Italic'),'\n')
    print(fontstyle.apply('Second Object', 'bold/UNDERLINE/blue'))
    print('Speed: ', fontstyle.apply(second_try.get_speed(), 'Italic'), '\nRadius: ', fontstyle.apply(second_try.get_radius(), 'Italic'), '\nColor: ', fontstyle.apply(second_try.get_color(), 'Italic'), '\nOn/Off: ', fontstyle.apply(second_try.get_on(), 'Italic'))
# Call the main function
TestFan()
