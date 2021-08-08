"""
At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you, and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

Note that you don't have any change in hand at first.

Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with correct change, or false otherwise.
"""
def lemonadeChange(bills):
    five = 0
    ten = 0
    for each in bills:
        if each == 5:
            five += 1
        elif each == 10 and five >= 1:
            five -= 1
            ten += 1
        elif each == 20 and ten >= 1 and five >=1 :
            ten -= 1
            five -= 1
        elif each == 20 and ten == 0 and five >= 3:
            five -= 3
        else:
            return False
    if five >= 0 and ten >= 0:
        return True
    return False