"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
"""
def getRow(rowIndex):
    if rowIndex == 0:
        return [1]
    elif rowIndex == 1:
        return [1,1]
    else:
        op = [[1],[1,1]]
        n = 2
        while n != rowIndex+1:
            arr = [1]
            for i in range(len(op[n-1])-1):
                arr.append(op[n-1][i]+op[n-1][i+1])
            arr.append(1)
            op.append(arr)
            n += 1
    return op[rowIndex]