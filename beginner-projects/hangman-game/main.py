#!/usr/bin/python3
import random
from hangman_art import logo, stages
from hangman_words import word_list

chosen_word = random.choice(word_list)
lives = 6

print (logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#If the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = []

for letter in chosen_word:
    display += "_"
for element in display:
    print(element, end = " ")
print()

while "_" in display and lives > 0:
    guess = input("Guess a letter: ").lower()
    
    #check if letter is already gussed
    if guess in display:
      print(f"You already guessed {guess}")
      print(stages[lives])

    #Check guessed letter
    #If the letter at that position matches 'guess' then reveal that letter in the display at that position.
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
    # If guess is not in the chosen_word, then reduce 'lives' by 1.
    if guess not in chosen_word:
            lives -= 1
            print(f"You guessed {letter} that's not in the word. You lose a life")
            print(stages[lives])
            if lives == 0:
                print("You lose")

    #print display 
    print(f"{' '.join(display)}")

if "_" not in display:
    print("You win")
