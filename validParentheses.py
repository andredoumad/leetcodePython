# Andre Doumad
'''
This problem was asked by Amazon, Google, Facebook.

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

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
import unittest
class Solution:
    def isValid(self, s):
        brackMap= {'(':')','{':'}','[':']'}
        lefBracks = set(['(','{','['])
        stack = []
        for val in s:
            if val in lefBracks:
                stack.append(val)
            elif stack and val == brackMap[stack[-1]]:
                stack.pop()
            else:
                return False
        return stack == []


class UnitTest(unittest.TestCase):
    def test_a(self):
        solution = Solution()

        result = solution.isValid(r"()")
        print('result is ', result)
        self.assertEqual(result,True)

        result = solution.isValid(r"()[]{}")
        print('result is ', result)
        self.assertEqual(result,True)

        result = solution.isValid(r"(]")
        print('result is ', result)
        self.assertEqual(result,False)

        result = solution.isValid(r"([)]")
        print('result is ', result)
        self.assertEqual(result,False)

        result = solution.isValid(r"{[]}")
        print('result is ', result)
        self.assertEqual(result,True)

if __name__ == '__main__':
    unittest.main()

'''
result is  True
result is  True
result is  False
result is  False
result is  True
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
'''