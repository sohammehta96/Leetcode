"""
Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.

He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.
Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.
"""
def totalMoney(self, n: int) -> int:
    week = 0
    day = 1
    bank = 0

    while n > 0:
        if day == 8:
            week += 1
            day = 1
        bank += day + week
        day += 1
        n -= 1
    return bank