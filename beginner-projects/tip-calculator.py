#!/usr/bin/python3
# This is a simple tip calculator that calculates the total bill and the bill per person based on /
# the total bill, tip percentage and the number of people to split the bill.


print ("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give? (Please don't add any percentage signs)"))
split_between = float(input("How many people to split the bill?"))
total_bill = (bill + (bill * tip / 100))
bill_per_person = total_bill / split_between
print (f"Each person should pay: ${bill_per_person:.2f}")
