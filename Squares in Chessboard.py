"""
Find total number of Squares in a N*N cheesboard.
"""
def squares(n):
    square = 0
    while n > 0:
        square += n*n
        n -= 1
        
    return square

print(squares(100000))