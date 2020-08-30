# Andre Doumad
# 200824
'''
This problem was asked by Amazon.
Given a string s and an int k, return all unique substrings of s of size k with k distinct characters.

Example 1:
Input: s = "abcabc", k = 3
Output: ["abc", "bca", "cab"]
Example 2:

Input: s = "abacab", k = 3
Output: ["bac", "cab"]
Example 3:

Input: s = "awaglknagawunagwkwagl", k = 4
Output: ["wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", "nagw", "agwk", "kwag"]
Explanation: 
Substrings in order are: "wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", "nagw", "agwk", "kwag", "wagl" 
"wagl" is repeated twice, but is included in the output once.
Constraints:

The input string consists of only lowercase English letters [a-z]
0 ≤ k ≤ 26
'''

import unittest

class Solution():
    def solve(self, s, k):
        if not s or k == 0:
            return []
        


class UnitTest(unittest.TestCase):
    def test_a(self):
        s = Solution()
        result = s.solve('abcabc', 3)
        self.assertEqual(result, ["abc", "bca", "cab"])

if __name__ == '__main__':
    unittest.main()