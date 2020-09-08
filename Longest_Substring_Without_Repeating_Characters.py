# Andre Doumad
'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

import unittest

class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        dic, res, start = {}, 0, 0
        for i, ch in enumerate(s):
            if ch in dic:
                res = max(res, i-start)
                start = max(start, dic[ch]+1)
            dic[ch] = i
        return max(res, len(s)-start)
class UnitTest(unittest.TestCase):
    def test_a(self):

        solution = Solution()

        result = solution.lengthOfLongestSubstring('abcabcbb')
        print('result ', result)
        self.assertEqual(result,3)

        result = solution.lengthOfLongestSubstring('bbbbb')
        print('result ', result)
        self.assertEqual(result,1)

        result = solution.lengthOfLongestSubstring('pwwkew')
        print('result ', result)
        self.assertEqual(result,3)

        result = solution.lengthOfLongestSubstring('bwf')
        print('result ', result)
        self.assertEqual(result,3)

        result = solution.lengthOfLongestSubstring('au')
        print('result ', result)
        self.assertEqual(result,2)
if __name__ == '__main__':
    unittest.main()




'''
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic, res, start, = {}, 0, 0
        for i, ch in enumerate(s):
            # when char already in dictionary
            if ch in dic:
                # check length from start of string to index
                res = max(res, i-start)
                # update start of string index to the next index
                start = max(start, dic[ch]+1)
            # add/update char to/of dictionary 
            print('i ', i)
            dic[ch] = i
        # answer is either in the begining/middle OR some mid to the end of string
        
        for k,v in dic.items():
            print('k ', k, ' v ', v)

        print('res ', res)
        print('len(s)-start ', len(s)-start)
        return max(res, len(s)-start)
'''



'''
new string =  ab
new string =  bca
new string =  bca
new string =  bca
new string =  bca
new string =  bca
new string =  bca
new string =  bca
result  3
new string =  b
new string =  b
new string =  b
new string =  b
new string =  b
result  1
new string =  pw
new string =  pw
new string =  pw
new string =  kew
new string =  kew
new string =  kew
result  3
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
'''

