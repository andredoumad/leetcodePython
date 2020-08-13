# Andre Doumad
'''
This problem is asked by Amazon

Given two non-negative integers num1 and num2 represented as string, 
return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''
class Solution:
    def addStrings(self, num1, num2):
        s = map(str,num1)
        s = ''.join(s)
        num1_digit = int(s)
        
        s = map(str, num2)
        s = ''.join(s)
        num2_digit = int(s)
        return str(num1_digit + num2_digit)

import unittest
class UnitTest(unittest.TestCase):
    def test_a(self):
        solution = Solution()
        result = solution.addStrings('3237', '1374')
        print('result: ', result)
        self.assertEqual(result, "4611")

if __name__ == '__main__':
    unittest.main()

'''
result:  4611
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
'''