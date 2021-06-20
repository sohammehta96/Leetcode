"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
"""
class Solution:
    def trap(self, height):
        total_water = 0

        for i in range(1,len(height)):
            wat = min(max(height[0:i]),max(height[i:len(height)]))
            wi = wat - height[i]
            if wi >= 0:
                total_water = total_water + wi
                
        return total_water