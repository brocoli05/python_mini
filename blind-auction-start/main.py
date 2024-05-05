from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo

print(logo)

bids = {}
bidding_finished = False


## Loop through the dictionary and find the highest bidder
def find_highest_bidder(bidding_record):
  # bidding_record = {"Angela": 123, "James": 321}
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bidder_price = bidding_record[bidder]
    if bidder_price > highest_bid:
      highest_bid = bidder_price
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes' or 'no'.")

  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clear()
