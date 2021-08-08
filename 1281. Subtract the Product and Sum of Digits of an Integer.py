"""
Given an integer number n, return the difference between the product of its digits and the sum of its digits.
"""
def subtractProductAndSum(self, n: int) -> int:
    prod = 1
    add = 0
    
    while n > 0:
        prod,add = prod*(n%10),add+(n%10)
        n = n//10
    return prod - add