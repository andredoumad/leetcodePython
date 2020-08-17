# Andre Doumad
# 200816
'''
This problem was asked by Amazon.

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
            s = re.sub(r'_', '', s)
            s = s.lower()
        print(s)
        i, j = 0, len(s)-1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True



solution= Solution()
result = solution.isPalindrome("A man, a plan, a canal: Panama")
print('result', result)

result = solution.isPalindrome("race a car")
print('result', result)