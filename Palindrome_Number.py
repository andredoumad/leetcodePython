# Andre Doumad
# 200919
'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true

Example 2:
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Follow up:
Coud you solve it without converting the integer to a string?
'''
import unittest
class Solution:
    def isPalindrome(self, x: int) -> bool:
        print('solving for ', x)
        if 0 <= x < 10: return True
        if x < 0: return False
        p, res = x, 0
        while p:
            res = res * 10 + p % 10
            print(res)
            p= int(p/10)
        return res == x

class UnitTest(unittest.TestCase):
    def test_a(self):
        s = Solution()
        result = s.isPalindrome(121)
        self.assertTrue(result)
        result = s.isPalindrome(-121)
        self.assertFalse(result)
        result = s.isPalindrome(10)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()

'''
solving for  121
1
12
121
solving for  -121
solving for  10
0
1
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
'''