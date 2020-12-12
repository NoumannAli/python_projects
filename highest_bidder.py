from replit import clear
from art import logo
print(logo)

# empty dictionary
bidders = {}
keep_bidding = True

# function to check highest bidder
def bidding_track(bidders_track):

  # variables to store highest bid and bidder
  heighst_bid = 0
  height_bidder = ""
  
  # for loop to check highest bidder in dict
  for key in bidders:
    bid_amount = bidders[key]
    if bid_amount > heighst_bid:
      heighst_bid = bid_amount
      height_bidder = key
      
  # print out the winner
  print(f"{height_bidder} is the winner bid amount is: {heighst_bid}")

# while loop
while keep_bidding:
  bidder = input("What is your name ").lower()
  bid = int(input("Bid your amount: $"))
  bidders[bidder] = bid
  check = input("Is there Anymore bidder 'Yes' or 'No' ").lower()
  
  # checking if continue
  if check == "yes":
    keep_bidding = True
    clear()
  else:
    bidding_track(bidders)
    keep_bidding = False
       
