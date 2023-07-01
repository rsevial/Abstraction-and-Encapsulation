# Programmed by: Rebekah Joy E. Sevial
# Test drive for Pet class

# Import class from pet_class
from pet_class import Pet
# Create object for pet
# Ask user the name of their pet
pet_name = input("Enter the name of your pet: ")
# Ask user the animal type of their pet
pet_animal_type = input("Enter the animal type of your pet: ")
# Ask user the age of their pet
pet_age = input("Enter the age of your pet: ")
# Create object from the ans of the user
pet_object = Pet(pet_name, pet_animal_type, pet_age)
# Print the name, animal type and age of their pet