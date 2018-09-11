# Author: John Asare
# Date: Sep 11 2018
# Description: Savings


""" A short code to assume how much an account will grown with a fixed APR interest """

Money_to_start = int(input("How much money do you want to start with?: "))

APR = float(input("(i.e 40% will be .04 or 0.04 What is the APR?:  )"))

Amount = int(input("What amount do you want to get?: "))

Next_year = Amount * (1 + APR)

