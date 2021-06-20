"""
Given a binary string, that is it contains only 0s and 1s. 
We need to make this string a sequence of alternate characters by flipping some of the bits, 
our goal is to minimize the number of bits to be flipped.
"""
def numberofflips(s):
    flips = 0
    a = len(num)
    element = ['1' if a % 2 == 1 else '0'][0] 
       
    for i in range(a):
        if i % 2 == 0 and s[i] != element:
            flips += 1
        if i % 2 == 1 and s[i] == element:
            flips += 1
    return flips


num = "001"
num = "0001010111"
print(numberofflips(num))