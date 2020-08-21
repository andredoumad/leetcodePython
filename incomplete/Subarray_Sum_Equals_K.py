# Andre Doumad
# 200820
'''
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2
 
Constraints:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
'''
class Solution:
    def subarraySum(self, nums, k):
        sums = {0:1}
        t=s=0
        for num in nums:
            s += num
            t += sums.get(s-k,0)
            sums[s] = sums.get(s,0)+1
        return t
solution = Solution()
print(solution.subarraySum([1,1,1], 2))
print(solution.subarraySum([1,2,3], 3))
print(solution.subarraySum([1,2,1,2,1], 3))
print(solution.subarraySum([-1,-1,1], 0))

'''
output:
2
2
4
1
'''