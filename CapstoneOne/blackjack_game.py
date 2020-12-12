############### Blackjack Project #####################

##################### Requirements #####################
#Requirment Create a deal_card() function that uses the List below to *return* a random card.

#Requirement: Create a function called calculate_score() that takes a List of cards as input
#and returns the score.

#Requirement: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Requirement: Deal the user and computer 2 cards each using deal_card() and append().

#Requirement: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Requirement: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Requirement: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#HRequirement: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Requirement: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#HRequirement: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Requirement: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Requirement: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

#Flow Chart Read this breakdown of program requirements:

import random
from replit import clear
from art import logo
print(logo)
#deal_card function

def deal_card():
  """this function will pick random cards from the deck"""""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card
  
#calculate function
def calculate_score(cards):
  """This function will calculate sum of all cards in hand"""
  if sum(cards) == 21 and len(cards) ==2:
    return 0
    if 11 in cards and sum(cards) > 21:
      cards.remove(11)
      cards.append(1)
  return sum(cards)

#compare function
def compare(user_score,computer_score):
  """This function will compare the final score of all cards in hand and pick a winner """
  if user_score == computer_score:
    return "Its Draw"
  elif computer_score > 21 and user_score > 21:
     return "Its Draw"
  elif computer_score == 0:
    return "Computer Wins😭"
  elif user_score == 0:
    return "You Win"
  elif user_score > 21:
    return "Computer win😭"
  elif computer_score > 21:
    return "You Win"
  elif user_score > computer_score:
    return "You Win"
  else:
    return "Computer Win😭"


game_end = False

def blackjack_game():
  """This is main function it will run the game"""
  game_end = False
  user_cards = []
  computer_cards = []
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not game_end:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"user cards  {user_cards} user score is: {user_score}")
    print(f"computer cards: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      game_end = True
    else:
      user_should_deal = input("Do you want to draw a card from deck type 'y' to play type 'n' to pass\n ").lower()
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        game_end = True
      
  while computer_score !=0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  result = compare(user_score,computer_score)
  print(f"\nUser Final Hand  {user_cards} user score is: {user_score}")
  print(f"Computer Final Hand: {computer_cards} computer score is: {computer_score}\n")
  print(result)

while input("\nDo want to start the game type 'y' or 'n' to exit ").lower()== "y":
  clear()
  print(logo)
  blackjack_game()




