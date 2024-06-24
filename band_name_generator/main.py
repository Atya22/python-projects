#!/usr/bin/python3
"""This is a simple band name generator."""

def get_input(prompt):
    """ This function is going to take the prompt as an argument and return the user input."""
    while True:
        user_input = input(prompt).strip() # Remove leading and trailing spaces
        if user_input.replace(" ", "").isalpha():
            return user_input
        else:
            print("Input must contain only letters and spaces. Please try again.")

print("Welcome to the Band Name Generator.")
city_name = get_input("What's the name of the city you grew up in?\n")
pet_name = get_input("What's the name of your pet?\n")
print("Your band name could be " + city_name + " " + pet_name)