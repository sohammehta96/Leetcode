"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""
def climbStairs(self, n: int) -> int:
    if n <= 2:
        return n
    arr = [1,1]
    while len(arr) != n+1:
        arr.append(arr[len(arr)-1] + arr[len(arr)-2])
    return arr[len(arr)-1]