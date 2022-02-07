from art import logo
print(logo)

import random

easy_level = 10
hard_level = 5

def difficulty():
  difficulty_level = input("Choose a difficulty level. Easy or hard? ")
  
  if difficulty_level == "easy":
    return easy_level
  else:
    return hard_level

def compare_choices(user_guess, computer_choice):
  if user_guess > computer_choice:
    print(f"You've guessed too high. ")
  elif user_guess < computer_choice:
      print(f"You've guessed too low. ")
  elif user_guess == computer_choice:
      print(f"The computer choice {computer_choice}.\nYou guessed {computer_choice}. You win!")

def game():
  print(f"Welcome to the Number Guessing Game!\nThe computer is thinking of a number between 1 and 100.")

  computer_choice = random.randint(1, 100)

  turns = difficulty()

  user_guess = 0

  while user_guess != computer_choice:
    print(f"You have {turns} turns remaining.")
    user_guess = int(input("What number do you think it is? "))
    turns -= 1
    
    compare_choices(user_guess, computer_choice)
    
    if turns == 0:
      print("You've run out of guesses. You lose.")
      return 

game()