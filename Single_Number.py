# Andre Doumad
# 200919
'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:
Input: [2,2,1]
Output: 1

Example 2:
Input: [4,1,2,1,2]
Output: 4
'''
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        print('solving for, ', nums)
        nums_dic = {}
        for i in range(len(nums)):
            if nums[i] not in nums_dic:
                nums_dic[nums[i]] = 1
            else:
                nums_dic[nums[i]] += 1
        for k,v in nums_dic.items():
            if v == 1:
                return k

s = Solution()
print(s.singleNumber([2,2,1]))
print(s.singleNumber([4,1,2,1,2]))