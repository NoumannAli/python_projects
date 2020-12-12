#Tickting Machine

riderHeight = input("What is your height in Cm: \n")
riderHeight = int(riderHeight)
bill = 0
if riderHeight > 120:
  
  riderAge = input("what is your age\n")
  riderAge = int(riderAge)
  if riderAge < 12:
    bill = 5
    print("your ticket is $5")
  elif riderAge < 18:
    bill = 7
    print("your ticket is $7")
  else:
    bill = 12
  photo = input("Do you want to take photo 'Y' or 'No'\n")
  if photo == "Y" or photo == "y":
    bill += 3
    

    
  print(f"Your Total is: ${bill}")
else: print("you are not allwed to ride")
