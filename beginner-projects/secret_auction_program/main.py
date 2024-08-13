#!/usr/bin/python3
from art import logo
print(logo)
all_bidders = {}
should_continue = True

#we should declare the function first
def find_highest_bidder(bidding_dictionary):
    winner = ""
    max_bid = 0
    for bidder in bidding_dictionary:
        bit_amount = bidding_dictionary[bidder]
        if bit_amount > max_bid:
            max_bid = bit_amount
            winner = bidder
    print("\n" * 20)
    print (f"The winner is {winner} with a bid of ${max_bid}")

while should_continue == True:
    name = input("What is your name?\n")
    bid = int(input("What is your bid?\n"))
    all_bidders[name] = bid
  
    add_player = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if add_player == "no":
        should_continue = False
        find_highest_bidder(all_bidders)
    elif add_player == "yes":
        print ("\n" * 20)