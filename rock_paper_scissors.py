import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_set = [rock, paper, scissors]

user_guess = int(
    input("Type 0 for rock and 1 for paper and 2 for scissors : "))
pc_guess = random.randint(0, 2)

print(user_guess)

if user_guess > 2 or user_guess < 0:
    print("You typed an invalid number, You lose")

else:
    print(game_set[user_guess])
    print("Computer chose")
    print(game_set[pc_guess])

    if (user_guess == 0 and pc_guess == 2) or \
        (user_guess == 1 and pc_guess == 0) or \
            (user_guess == 2 and pc_guess == 1):
        print("you win")
    elif (user_guess == pc_guess):
        print("It's a draw")
    else:
        print("You lose")
