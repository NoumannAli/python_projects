#Step 1
import random
from hangman_art import stages
from hangman_words import word_list
from hangman_art import logo
from replit import clear

print(logo)
chosen_word = random.choice(word_list)
print(f"These 2 letters are in the word {chosen_word[1],chosen_word[4]}")
display = []
for _ in range(0,len(chosen_word)):
  display += "_"

print(display)
end_of_game = False
lives = 6

while not end_of_game:
  guess = input("Guess the word?").lower()
  clear()
  for letter in range(0,len(chosen_word)):
    if guess == chosen_word[letter]:
      display[letter] = guess
      print("YaY! 'Correct Guess'\n")
      if "_" not in display:
        print("You Win")
        end_of_game = True
  
  if guess not in chosen_word :
    lives -= 1
    print("OoOoPs! 'Wrong guess'\n")

    
    if lives == 0:
      print("You Lose\n")
      end_of_game = True
  print(display)
  print(stages[lives])
