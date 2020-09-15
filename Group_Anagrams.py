# Andre Doumad
# 200917
'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lower-case English letters.
'''
from typing import List
import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for str in strs:
            key = ''.join(sorted(str))
            if key in dic:
                dic[key].append(str)
            else:
                dic[key] = [str]
        return dic.values()





s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
