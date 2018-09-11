# Author: John Asare
# Date: Sep 11 2018
# Description: Savings


""" A short code to assume how much an account will grown with a fixed APR interest """

money_to_start = float(input("How much money do you want to start with?: "))

APR = float(input("(i.e 40% will be .04 or 0.04) What is the APR?: "))

amount = float(input("What amount do you want to get?: "))

year = 0

while money_to_start < amount:
    money_to_start = money_to_start * (1 + APR)
    year = year + 1
    print("after year", year, "the amount is at", round(money_to_start))



