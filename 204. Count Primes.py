"""
Count the number of prime numbers less than a non-negative number, n.
"""
def countPrimes(n):
    if n <= 2:
        return 0
    
    arr = [True for i in range(n)]
    count = 0
    for i in range(2,len(arr)):
        if arr[i] == True:
            count += 1
            j = 2
            while i*j<n:
                arr[i*j] = False
                j += 1
    return count