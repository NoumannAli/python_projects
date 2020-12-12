#Requirements

# You are going to write a program that tests the compatibility between two people. We're going to use the super scientific method recommended by BuzzFeed.

# To work out the love score between two people:

# Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number.

# This video gives you more details on this:


# For Love Scores less than 10 or greater than 90, the message should be:

# "Your score is **x**, you go together like coke and mentos."

# For Love Scores between 40 and 50, the message should be:

# "Your score is **y**, you are alright together."

# Otherwise, the message will just be their score. e.g.:

# "Your score is **z**."

#User Inputs
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combinedString = name1+name2

combinedString = combinedString.lower()

#matching alphabets
t = combinedString.count("t")
r = combinedString.count("r")
u = combinedString.count("u")
e = combinedString.count("e")

l = combinedString.count("l")
o = combinedString.count("o")
v = combinedString.count("v")
e = combinedString.count("e")

#adding scores
true= t+r+u+e
love = l+o+v+e

love_score = int(str(true) + str(love))

#matching scores
if love_score <=10 or love_score >=90:
  print(f"Your love score is {love_score} you go together like coke and mentos")
elif love_score >=40 and love_score <=50:
  print(f"Your love score is {love_score} you are alright together.")
else:
  print(f"Your love score is {love_score}")
