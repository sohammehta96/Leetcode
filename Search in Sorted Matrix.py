"""
Given a matrix of size n x m, where every row and column is sorted in increasing order, and a number x. 
Find whether element x is present in the matrix or not.
"""
def findnuminmatrix(mat,x):
    rows, cols = len(mat), len(mat[0])
    for i in range(rows):
        if mat[i][0] > x :
            row = i
            break
    for j in range(cols):
        if mat[row-1][j] == x:
            return True
            break
    
    return False
        
        
matrix = [[1,2,3],[7,8,9],[10,11,12],[23,24,25],[45,47,49],[67,89,90]]
num = 49

print(findnuminmatrix(matrix,num))