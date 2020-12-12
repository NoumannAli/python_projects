import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
namesAsCSV = input("Give me everybody's names, seperated by a comma. ").upper()
names = namesAsCSV.split(", ")


#Write your code below this line 👇
print(names)
# random_num = random.randint(len(names))
random_num = random.randint(0,len(names) -1)
who_will_pay_bill = names[random_num]

print(f"'{who_will_pay_bill}' will pay bill today")
