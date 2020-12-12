#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: You might need to do some research in Google to figure out how to do this.

print("Welcome to bill calculator")
bill_Total = input("please enter your bill total\n")
tip_Pay = input("What % tip would you like to give (12 , 20 , 30)\n")
people_Count = input("please enter how many people to split the bill\n")


bill_Total = float(bill_Total)
people_Count = int(people_Count)
tip_Pay = int(tip_Pay)
bill_With_Tip = tip_Pay / 100 * bill_Total + bill_Total


total_Bill = (bill_With_Tip / people_Count) 
final_Payout = (round(total_Bill , 2))

print(f"Each person should pay ${final_Payout}")
