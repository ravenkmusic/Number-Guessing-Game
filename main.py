#Number Guessing Game Objectives:

# Include an ASCII art logo.

from art import logo
print(logo)

# Allow the player to submit a guess for a number between 1 and 100.

import random
computer_choice = random.randint(0, 101)

user_guess = int(input("The computer is thinking of a number between 1 and 100.\n What do you think it is?"))

# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
turns = 5

if user_guess > computer_choice:
  print("Too high.")
elif user_guess < computer_choice:
  print("Too low.")
# If they got the answer correct, show the actual answer to the player.
elif user_guess == computer_choice:
  print(f"The computer choice {computer_choice}.\nYou guessed {computer_choice}. You win!")
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

