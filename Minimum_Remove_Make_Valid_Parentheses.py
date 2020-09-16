# Andre Doumad
# 200820
'''
Given a string s of '(' , ')' and lowercase English characters. 

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
Example 4:

Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"
 

Constraints:

1 <= s.length <= 10^5
s[i] is one of  '(' , ')' and lowercase English letters.
'''
import unittest
class Solution:
    def minRemoveToMakeValid(self, s):
        print('-----------\nsolve for ', s)
        stack = []
        for idx, char in enumerate(s):
            print('idx ', idx, ' char ', char, ' stack ', stack)
            if char == "(":
                stack.append(("(", idx))
            elif char == ")":
                if stack and stack[-1][0] == "(":
                    stack.pop()
                else:
                    stack.append((")", idx))
        while stack:
            char, idx = stack.pop()
            print('s[:idx] ', s[:idx])
            print('s[idx+1:] ', s[idx+1:])
            s = s[:idx] + s[idx+1:]
        return s


class UnitTest(unittest.TestCase):
    def test_a(self):
        solution = Solution()
        result = solution.minRemoveToMakeValid("lee(t(c)o)de)")
        self.assertEqual(result, "lee(t(c)o)de")
        result = solution.minRemoveToMakeValid("a)b(c)d")
        self.assertEqual(result, "ab(c)d")
        result = solution.minRemoveToMakeValid("))((")
        self.assertEqual(result, "")
        result = solution.minRemoveToMakeValid("(a(b(c)d)")
        self.assertEqual(result, "a(b(c)d)")
        result = solution.minRemoveToMakeValid("())()(((")
        self.assertEqual(result, "()()")

if __name__=="__main__":
    unittest.main()