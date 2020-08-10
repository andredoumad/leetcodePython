# Andre Doumad
'''
This Problem was asked by Amazon.

Given an integer array nums, find the contiguous subarray 
(containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, 
try coding another solution using the divide and conquer approach, which is more subtle.
'''

class Solution:
    def maxSubArray(self, nums):
        maxsum = nums[0]
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
            maxsum = max(nums[i], maxsum)
            print('nums[', i-1, '] ', nums[i-1], ' maxsum: ', maxsum)
        return maxsum

solution = Solution()
result = solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print('result is ', result)

'''
output:
nums[ 0 ]  -2  maxsum:  1
nums[ 1 ]  1  maxsum:  1
nums[ 2 ]  -2  maxsum:  4
nums[ 3 ]  4  maxsum:  4
nums[ 4 ]  3  maxsum:  5
nums[ 5 ]  5  maxsum:  6
nums[ 6 ]  6  maxsum:  6
nums[ 7 ]  1  maxsum:  6
result is  6
'''