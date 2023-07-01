# Programmed by: Rebekah Joy E. Sevial
# Design a class named Pet

# Create class named Pet
class Pet:
# Define constructor of the Pet (name, animal_type, age)
    def __init__(self, name, animal_type, age):
# Create a private data for the name, animal_type, age
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age
# Create setters for the three private data
    # Define method set_name
    def set_name(self, name):
        self.__name = name
    # Define method set_animal_type
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type
    # Define method set_age
    def set_age(self, age):
        self.__age = age
# Create the getters for the three private data
    # Define method get_name
    def get_name(self):
        return self.__name
    # Define method get_animal_type
    def get_animal_type(self):
        return self.__animal_type
# Define method get_age