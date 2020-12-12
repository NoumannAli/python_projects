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
choices = ["rock", "paper", "scissors"]

num = random.randint(0,2)

player = input("Type 'rock' 'paper' or 'scissors'\n")

computer = choices[num]


if computer == "paper":
  print(f"computer selected {computer}")
  print(paper)
if player == "paper":
  print(f"player selected {player}")
  print(paper)
if computer == "rock":
  print(f"computer selected {computer}")
  print(rock)
if player == "rock":
  print(f"player selected {player}")
  print(rock)
if computer == "scissors":
  print(f"computer selected {computer}")
  print(scissors)
if player == "scissors":
  print(f"player selected {player}")
  print(scissors)

if player == "rock" and computer == "paper":
  print("computer wins")
elif player == "rock" and computer == "rock":
  print("Its a Tie")
elif player == "paper" and computer == "rock":
  print("player wins")
elif player == "rock" and computer == "scissors":
  print("player wins")
elif player == "scissors" and computer == "rock":
  print("computer wins")
elif player == "scissors" and computer == "scissors":
  print("its a tie")
elif player == "paper" and computer == "scissors":
  print("computer wins")
elif player == "paper" and computer == "paper":
  print("its a tie")
elif player == "scissors" and computer == "paper":
  print("player wins")
elif player != "rock" or player != "paper" or player != "scissors":
  print("You Lose\nYou should enter 'rock, paper, or scissors'")
