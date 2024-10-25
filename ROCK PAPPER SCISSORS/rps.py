import random
user_score = 0
comp_score = 0
ties = 0

name = input("enter your name:")
print(""" 
Winning Rules
1. Paper vs Rock --> Paper
2. Rock vs Scissors --> Rock
3.Scissors vs Papper --> Scissors""")

choice = int(input("enter your choice from 1-3:"))
print()
while choice > 3 or choice < 1:
    choice = int(input("enter valid input"))

if choice == 1:
    user_choice = "Rock"
elif choice == 2:
    user_choice = "paper"
else:
    user_choice = "Scissors"

print("The user's choice is",user_choice)
print("Now it is computer's turn")

computer = random.randint(1,3)

if computer == 1:
    comp_choice = "Rock"
elif computer == 2:
    comp_choice = "Paper"
else:
    comp_choice = "Scissors"

print("The computer's choice is", comp_choice)