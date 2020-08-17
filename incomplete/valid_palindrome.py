# Andre Doumad
# 200816
'''
125. Valid Palindrome
Easy

1341

3073

Add to List

Share
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false

Constraints:

s consists only of printable ASCII characters.
'''
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True
        else:
            s = s.replace(' ', '')
            s = re.sub(r'\W+', '', s)
            s = s.lower()
            # s = filter(str.isalnum, s)
        print(s)
        # exit()
        i, j = 0, len(s)-1
        while i < j:
            if s[i] == s[j]:
                pass



solution= Solution()
result = solution.isPalindrome("A man, a plan, a canal: Panama")
print('result', result)
# assert(result, True)

result = solution.isPalindrome("race a car")
print('result', result)
# assert(result, False)
