# Andre Doumad
# 200817
'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
class Solution:
    def twoSum(self, i, res, nums):
        lo, hi = i+1, len(nums)-1
        while lo<hi:
            sum = nums[i] + nums[lo] + nums[hi]
            if sum < 0:
                lo +=1
            elif sum > 0:
                hi -=1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo +=1
                hi -=1
                while lo<hi and nums[lo] ==nums[lo-1]:
                    lo+=1
        return res

    def threeSum(self, nums):
        res = []
        nums.sort()
        print(nums)
        for i in range(0, len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i-1] != nums[i]:
                self.twoSum(i, res, nums)
        return res

solution = Solution()
results = solution.threeSum([-1, 0, 1, 2, -1, -4])
print(results)