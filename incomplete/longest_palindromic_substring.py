# Andre Doumad
'''
Given a string s, find the longest palindromic substring in s. 
You may assume that the maximum length of s is 1000.

Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: "cbbd"
Output: "bb"
'''

class Solution:
    # starting at l,r expand outwards and find the palindrome
    def test(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]

    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            odd  = self.test(s, i, i)
            even = self.test(s, i, i+1)
            res = max(res, odd, even, key=len)
        return res

solution = Solution()
result = solution.longestPalindrome('babad')
print('result ', result)

result = solution.longestPalindrome('cbbd')
print('result ', result)

result = solution.longestPalindrome('bb')
print('result ', result)


result = solution.longestPalindrome('abb')
print('result ', result)

result = solution.longestPalindrome('ccd')
print('result ', result)