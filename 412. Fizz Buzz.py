"""
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i if non of the above conditions are true.
"""

class Solution:
    def fizzBuzz(self, n: int):
        op = []
        for i in range(n):
            if (i+1) % 3 == 0 and (i+1) % 5 == 0:
                op.append("FizzBuzz")
            elif (i+1) % 3 == 0:
                op.append("Fizz")
            elif (i+1) % 5 == 0:
                op.append("Buzz")
            else:
                op.append(str(i+1))
        return op