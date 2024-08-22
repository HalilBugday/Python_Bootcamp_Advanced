import random

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
game_img = [rock, paper, scissors]

user_choice = int(input("What do you chose?\n 0 for Rock. \n 1 for Paper. \n 2 for Scissors. \n"))
# 0 -> Rock
# 1 -> Paper
# 2 -> Scissors
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number! You lose!")
    exit()

print(game_img[user_choice])
print(f"You chose {user_choice}")

comp_choice = random.randint(0,2)
print(game_img[comp_choice])

print(f"Computer chose {comp_choice}")

if user_choice == 0 and comp_choice == 2:
    print("You win!")
elif comp_choice == 0 and user_choice == 2:
    print("You lose!")
# 2-1, 1-2
elif comp_choice > user_choice:
    print("You lose!")
elif user_choice > comp_choice:
    print("You win!")

elif user_choice == comp_choice:
    print("It's draw!")

