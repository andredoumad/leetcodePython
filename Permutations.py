# Andre Doumad
# 200908
'''
This question was asked by google.

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''
from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, end):
            if start == end:
                ans.append(nums[:])
            for i in range(start, end):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start+1, end)
                nums[start], nums[i] = nums[i], nums[start]
                
        ans = []
        backtrack(0, len(nums))
        return ans

s = Solution()
print(s.permute([1,2,3]))