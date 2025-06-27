import random
# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''
#
# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''
#
# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
#
# Your_choice= int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))
#
# print("My Choice")
# if Your_choice == 0:
#     print(rock)
# elif Your_choice == 1:
#     print(paper)
# elif Your_choice == 2:
#     print(scissors)
# else:
#     print("Invalid choice! Please enter 0, 1, or 2.")
#     exit()
#
# Game = [rock,paper,scissors]
# computerturn = random.choice(Game)
# print("Computer chose:")
# print(computerturn)
#
# if Your_choice ==0 and computerturn == rock:
#     print("it's a Tie")
# elif Your_choice ==1 and computerturn == paper:
#     print("it's a Tie")
# elif Your_choice ==2 and computerturn == scissors:
#     print("it's a Tie")
# elif Your_choice ==0 and computerturn == scissors:
#     print("You Win")
# elif Your_choice ==2 and computerturn == paper:
#     print("You win")
# elif Your_choice ==1 and computerturn == rock:
#     print("You win")
# else:
#     print("You lose")


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

user_choice = int(input("Enter you input 0 - Rock , 1 - Paper & 2- scissors\n"))

Game_images = [rock,paper,scissors]

if user_choice >= 0 and user_choice <= 2:
    print("Your Choice:")
    print(Game_images[user_choice])
else:
    print("invalid input")
    exit()

computer_turn = random.randint(0,2)
print("Computer choice:")
print(Game_images[computer_turn])

if user_choice == computer_turn:
    print("It's a Tie")
elif(
        (user_choice==0 and computer_turn ==2) or
        (user_choice==1 and computer_turn ==0) or
        (user_choice ==2 and computer_turn==1)
):
# elif (user_choice == 0 and computer_turn ==2):
#     print("You win")
# elif (user_choice == 1 and computer_turn ==0):
#     print("You win")
# elif (user_choice ==2 and computer_turn==1):
    print("You win")
else:
    print("you lose")

#Another method using index value of computer turn

# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''
#
# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''
#
# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
#
# Game = [rock, paper, scissors]
#
# Your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
#
# if Your_choice < 0 or Your_choice > 2:
#     print("Invalid choice! Please enter 0, 1, or 2.")
#     exit()
#
# print("My Choice:")
# print(Game[Your_choice])
#
# computerturn = random.choice(Game)
# computer_choice_index = Game.index(computerturn)
#
# print("Computer chose:")
# print(computerturn)
#
# if Your_choice == computer_choice_index:
#     print("It's a Tie")
# elif (Your_choice == 0 and computer_choice_index == 2) or \
#      (Your_choice == 1 and computer_choice_index == 0) or \
#      (Your_choice == 2 and computer_choice_index == 1):
#     print("You Win")
# else:
#     print("You Lose")
