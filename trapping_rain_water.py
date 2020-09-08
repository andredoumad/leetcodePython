# Andre Doumad
# 200906
'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


Represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water are being trapped.

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3: return 0 
        left, right = 0, len(height) -1
        l_max, r_max = height[left], height[right]
        volume = 0
        while left < right:
            l_max, r_max = max(height[left], l_max), max(height[right], r_max)
            if l_max < r_max:
                volume += l_max - height[left]
                left += 1
            else:
                volume += r_max -height[right]
                right -= 1
        return volume



s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))




























'''
def trap(self, bars):
    if not bars or len(bars) < 3:
        return 0
    volume = 0
    left, right = 0, len(bars) - 1
    l_max, r_max = bars[left], bars[right]
    while left < right:
        l_max, r_max = max(bars[left], l_max), max(bars[right], r_max)
        if l_max <= r_max:
            volume += l_max - bars[left]
            left += 1
        else:
            volume += r_max - bars[right]
            right -= 1
    return volume
'''