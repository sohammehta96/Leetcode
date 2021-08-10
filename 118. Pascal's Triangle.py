"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
"""
def generate(numRows):
    if numRows == 1:
        return [[1]]
    elif numRows == 2:
        return [[1],[1,1]]
    else:
        op = [[1],[1,1]]
        n = 2
        while n != numRows:
            arr = [1]
            for i in range(len(op[n-1])-1):
                arr.append(op[n-1][i]+op[n-1][i+1])
            arr.append(1)
            op.append(arr)
            n += 1
    return op