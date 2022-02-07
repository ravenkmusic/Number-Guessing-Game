#Number Guessing Game Objectives:

# Include an ASCII art logo.

from art import logo
print(logo)

# Allow the player to submit a guess for a number between 1 and 100.

import random

easy_level = 10
hard_level = 5

print("Welcome to the Number Guessing Game!\nThe computer is thinking of a number between 1 and 100.")

computer_choice = random.randint(1, 100)

def difficulty():
  difficulty_level = input("Choose a difficulty level. Easy or hard? ")
  
  if difficulty_level == "easy":
    return easy_level
  else:
    return hard_level

def compare_choices(user_guess, computer_choice):
  if user_guess > computer_choice:
    print(f"Too high. You have {turns} remaining. Enter another guess. ")
  elif user_guess < computer_choice:
      print(f"Too low. You have {turns} remaining. Enter another guess. ")
    # If they got the answer correct, show the actual answer to the player.
  elif user_guess == computer_choice:
      print(f"The computer choice {computer_choice}.\nYou guessed {computer_choice}. You win!")

turns = difficulty()

while user_guess != computer_guess:
  user_guess = int(input("What number do you think it is? "))


compare_choices(user_guess, computer_choice)


# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.

 
# Track the number of turns remaining.

# If they run out of turns, provide feedback to the player.

# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

