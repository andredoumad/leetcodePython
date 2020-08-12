# Andre Doumad
'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''

class Solution:
    def reverse(self, x):
        minI = -2**31
        maxI = 2**31

        q = str(x)
        print('q ', q)
        neg = False
        if q[0] == '-':
            neg = True
        result = ''
        if not neg:
            for i in reversed(range(0, len(q))):
                result+=q[i]
        else:
            for i in reversed(range(1, len(q))):
                result+=q[i]
            
        result = int(result)
        if neg == True:
            result *= -1
        if result > minI and result < maxI:
            return result
        else:
            return 0

solution = Solution()
print(solution.reverse(123))
print(solution.reverse(int(123*-1)))

'''
output:
q  123
321
q  -123
-321
'''