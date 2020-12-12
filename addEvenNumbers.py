#Write your code below this row 👇
total = 0
#First method
for i in range(1,101):
  if i % 2 == 0:
    total +=i
print(total)


#second method
total_second = 0
for i in range(0,101,2):
  total_second += i
print(total_second)
