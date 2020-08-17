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
        start = maxLength = 0
        usedChar = {}
        
        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength

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