#!/usr/bin/python3
import random
#input from user
    
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
signs = [rock, paper, scissors]
computer_choice = random.randint(0, 2)

if user_choice > 2 or user_choice < 0:
    print(" You typed an invalid number. You lose!")
else:
    print(signs[user_choice])

print("Computer chose:")
print(signs[computer_choice])

if user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice == 1 and computer_choice == 0:
    print("You win!")
elif user_choice == 2 and computer_choice == 1:
    print("You win!")
elif user_choice == computer_choice:
    print("It's a draw!")
else:
    print("You lose!")