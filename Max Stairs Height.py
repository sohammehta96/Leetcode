"""
Given N number of square blocks. The height of each square block is 1. 
The task is to create a  staircase of max height using these blocks.
Note: The first stair would require only one block, the second stair would require two blocks and so on.
"""
def maxheight(n):
    height = 0
    
    i = 1
    while n >= i:
        n = n - i
        height += 1
        i += 1
    
    return height

print(maxheight(10))