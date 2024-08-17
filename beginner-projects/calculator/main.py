#!/usr/bin/python3
from art import logo

#operations 
def add(n1, n2):
    """This function returns addition of the given arguments

    Args:
        n1 (float): The first number
        n2 (float): The second number

    Returns:
        float: The sum of the two numbers
    """
    return n1 + n2

def substract(n1, n2):
    """This function returns substraction of the given arguments

    Args:
        n1 (float): The first number
        n2 (float): The second number

    Returns:
        float: The difference of the two numbers
    """
    return n1 - n2

def multiply(n1, n2):
    """This function returns multiplication of the given arguments

    Args:
        n1 (float): The first number
        n2 (float): The second number

    Returns:
        float: The product of the two numbers
    """
    return n1 * n2

def divide(n1, n2):
    """This function returns division of the given arguments

    Args:
        n1 (float): The first number
        n2 (float): The second number

    Returns:
        float: The quotient of n1 divided by n2.
    """
    return n1 / n2

operations = {
    "+" : add,
    "-": substract,
    "*": multiply,
    "/": divide
}

#calulating:
def calculator():
    """This function is a simple calculator that takes two numbers and an operation and returns the result
    
    It continuously prompts the user for an operation and a number, performs the calculation, and displays the result.
    The user can choose to continue calculating with the result or start a new calculation.
    """
    print(logo)
    should_accumulate = True
    num1 = float(input("What is the first number?\n"))
    
    while should_accumulate:
        operation = input("+\n-\n*\n*\nPick an operation\n")
        num2 = float(input("What's the next number\n"))
        result = operations[operation](num1, num2)
        print(f"{num1} {operation} {num2} = {result}")
        continue_or_restart = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation\n").lower()
        if  continue_or_restart == "y":
            num1 = result
        else:
            should_accumulate = False
            print("\n" * 25)
            calculator()

calculator()