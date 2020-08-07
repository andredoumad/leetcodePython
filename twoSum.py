# Andre Doumad
'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        answer = []
        print(nums)
        for i in range(len(nums)):
            # if you subtract the target from the current nums value 
            # just search for that in the dictionary, this way as soon as
            # a solution is found you can return it
            findThis = target-nums[i]
            print('findThis ', findThis)
            print('dictionary ', dictionary)
            if findThis in dictionary:
                findThisIndex = nums.index(findThis)
                print('findThisIndex ' + str(findThisIndex))
                if i != findThisIndex:
                    return sorted([i, findThisIndex])
            dictionary[nums[i]] = i


solution = Solution()
print(solution.twoSum(nums=[3, 5, 8, 2, 7, 11, 15], target=9))

'''
OUTPUT:
[3, 5, 8, 2, 7, 11, 15]
findThis  6
dictionary  {}
findThis  4
dictionary  {3: 0}
findThis  1
dictionary  {3: 0, 5: 1}
findThis  7
dictionary  {3: 0, 5: 1, 8: 2}
findThis  2
dictionary  {3: 0, 5: 1, 8: 2, 2: 3}
findThisIndex 3
[3, 4]
'''