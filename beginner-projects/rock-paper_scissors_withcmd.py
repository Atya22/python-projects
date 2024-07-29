#!/usr/bin/python3
import random
import cmd

class RockPaperScissors(cmd.Cmd):
    intro = "Welcome to Rock Paper Scissors! Type 'play' to start a game, or 'quit' to exit."
    prompt = "(RPS) "

    def __init__(self):
        super().__init__()
        self.rock = '''
            _______
        ---'   ____)
            (_____)
            (_____)
            (____)
        ---.__(___)
        '''

        self.paper = '''
            _______
        ---'   ____)____
                ______)
                _______)
                _______)
        ---.__________)
        '''

        self.scissors = '''
            _______
        ---'   ____)____
                ______)
            __________)
            (____)
        ---.__(___)
        '''
        self.signs = [self.rock, self.paper, self.scissors]

    def do_play(self, arg):
        """Play a game of Rock Paper Scissors"""
        while True:
            user_choice = self.get_user_choice()
            if user_choice is None:
                return

            computer_choice = random.randint(0, 2)
            
            print(self.signs[user_choice])
            print("Computer chose:")
            print(self.signs[computer_choice])

            result = self.determine_winner(user_choice, computer_choice)
            print(result)
            
            play_again = input("Do you want to play again? (yes/no): ").strip().lower()
            if play_again != 'yes':
                self.do_quit(None)
                break

    def get_user_choice(self):
        while True:
            try:
                choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
                if choice in [0, 1, 2]:
                    return choice
                else:
                    print("Invalid choice. Please enter 0, 1, or 2.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a draw!"
        elif (user_choice == 0 and computer_choice == 2) or \
             (user_choice == 1 and computer_choice == 0) or \
             (user_choice == 2 and computer_choice == 1):
            return "You win!"
        else:
            return "You lose!"

    def do_quit(self, arg):
        """Exit the game"""
        print("Thanks for playing!")
        return True

    def default(self, line):
        print(f"I don't understand '{line}'. Type 'help' for a list of commands.")

if __name__ == '__main__':
    RockPaperScissors().cmdloop()