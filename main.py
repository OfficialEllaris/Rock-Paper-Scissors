import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
          _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)__
         __________)
        (____)
---.__(___)
"""

# Computer's Choice
computer_choice = random.randint(0, 2)

# User's Choice (already set to Rock, Paper or Scissors)
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# Game Logic
game_choices = str(user_choice) + str(computer_choice)

# Possible outcomes
draws = ["00", "11", "22"]
wins = ["02", "10", "21"]
losses = ["01", "12", "20"]

# Printing User and Computer Choices
print(rock if user_choice == 0 else paper if user_choice == 1 else scissors)

print(f"Computer chose: \n {rock if computer_choice == 0 else paper if computer_choice == 1 else scissors}")

# Determining Outcome
if game_choices in draws:
    result = "It's a draw."
elif game_choices in wins:
    result = "You Win!"
elif game_choices in losses:
    result = "You Lose!"
else:
    result = "Invalid Input. You Lose!"

# Printing the outcome
print(result)
