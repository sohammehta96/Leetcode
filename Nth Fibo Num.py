"""
Given a positive integer n, find the nth fibonacci number. 
Since the answer can be very large, return the answer modulo 1000000007.
"""
def nthfibo(n):
    arr = [0,1]
    
    i = 1    
    while len(arr) < n:
        arr.append(arr[i]+arr[i-1])
        i+=1
        
    return arr[n-1]

print(nthfibo(4))