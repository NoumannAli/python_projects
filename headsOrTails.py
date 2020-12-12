
import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)


#Write your code below this line 👇

random_side = random.randint(0,1)

if random_side == 0:
  print("Tails")
else:
  print("Heads")
