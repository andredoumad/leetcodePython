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
from itertools import permutations 
class Solution:
    def __init__(self):
        self.results = {}
        self.permutations_nums = []
    def test(self, lis, l, c, r):
        if lis[l] + lis[c] + lis[r] == 0:
            stringKey = ''
            stringKey += str(lis[l])
            stringKey += str(lis[c])
            stringKey += str(lis[r])
            if stringKey not in self.results:
                self.results[stringKey] = []
                self.results[stringKey].append(lis[l])
                self.results[stringKey].append(lis[c])
                self.results[stringKey].append(lis[r])

    def threeSum(self, nums):
        self.permutations_nums = permutations(nums)
        for vals in list(self.permutations_nums):
            print('testing: ', vals)
            for i in range(1, len(vals)-1):
                self.test(vals, i-1, i, i+1) # odds
        final = []
        for k,v in self.results.items():
            print('k ', k, ' v ', v)
            final.append(v)
        return final


solution = Solution()
results = solution.threeSum([-1, 0, 1, 2, -1, -4])
print(results)