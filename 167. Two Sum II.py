"""
Given an array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.

Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.

The tests are generated such that there is exactly one solution. You may not use the same element twice.
"""

class Solution:
    def twoSum(numbers, target):
        original = numbers.copy()
        if len(numbers) == 2:
            return [1,2]
        else:
            if target > 0:
                while numbers[len(numbers)-1] > target:
                    numbers.pop(len(numbers)-1)
            elif target < 0:
                while numbers[0] < target:
                        numbers.pop(0)            
            ans = []
            for i in range(len(numbers)-1):
                for j in range(i+1,len(numbers)):
                    if numbers[i]+numbers[j] == target:
                        if original.count(numbers[i]) == 1:
                            ans.append((original.index(numbers[i]))+1)
                            ans.append((original.index(numbers[j]))+1)
                            break
                        else:
                            ans.append((original.index(numbers[i]))+1)
                            ans.append((original.index(numbers[i]))+2)
                            break
        return ans