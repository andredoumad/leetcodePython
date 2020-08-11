# Andre Doumad
'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true

'''

class Solution:
    def isValid(self, s):
        print('--------------')
        print('testing: ', s)
        if len(s) % 2 != 0:
            print('s is odd, returning false!')
            return False
        
        brackets = []
        leftBrackets = 
        for i in range(0, len(s)):
            brackets.append(s[i])
        
        print(brackets)
        return s

solution = Solution()
result = solution.isValid(r"()")
print('result is ', result)

result = solution.isValid(r"()[]{}")
print('result is ', result)

result = solution.isValid(r"(]")
print('result is ', result)

result = solution.isValid(r"([)]")
print('result is ', result)

result = solution.isValid(r"{[]}")
print('result is ', result)
