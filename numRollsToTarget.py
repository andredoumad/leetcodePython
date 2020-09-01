# Andre Doumad
# 200831
'''
You have d dice, and each die has f faces numbered 1, 2, ..., f.

Return the number of possible ways (out of fd total ways) modulo 10^9 + 7 to roll the dice so the sum of the face up numbers equals target.

Example 1:
Input: d = 1, f = 6, target = 3
Output: 1
Explanation: 
You throw one die with 6 faces.  There is only one way to get a sum of 3.

Example 2:
Input: d = 2, f = 6, target = 7
Output: 6
Explanation: 
You throw two dice, each with 6 faces.  There are 6 ways to get a sum of 7:
1+6, 2+5, 3+4, 4+3, 5+2, 6+1.

Example 3:
Input: d = 2, f = 5, target = 10
Output: 1
Explanation: 
You throw two dice, each with 5 faces.  There is only one way to get a sum of 10: 5+5.

Example 4:
Input: d = 1, f = 2, target = 3
Output: 0
Explanation: 
You throw one die with 2 faces.  There is no way to get a sum of 3.

Example 5:
Input: d = 30, f = 30, target = 500
Output: 222616187
Explanation: 
The answer must be returned modulo 10^9 + 7.
 

Constraints:

1 <= d, f <= 30
1 <= target <= 1000
'''

class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        memo = {}
        def dp(d, target):
            if d == 0:
                return 0 if target > 0 else 1
            if (d, target) in memo:
                return memo[(d, target)]
            to_return = 0
            for k in range(max(0, target-f), target):
                to_return += dp(d-1, k)
            memo[(d, target)] = to_return
            return to_return
        return dp(d, target) % (10**9 + 7)

s = Solution()
print(s.numRollsToTarget(1,6,3))
print(s.numRollsToTarget(2,6,7))
print(s.numRollsToTarget(2,5,10))
print(s.numRollsToTarget(1,2,3))
print(s.numRollsToTarget(30,30,500))


'''
Let dp(d, f, target) be the number of possible dice rolls for the given parameters.



As an initial example, pretend we have 5 dice with 6 faces each and we want to determine how many ways to make 18.
In other words, what is dp(5, 6, 18)?

At first glance, this is seems difficult and overwhelming. But if we make one simple observation, we can reduce this big problem into several smaller sub-problems. We have 5 dice, but let's first just look at ONE of these dice (say the last one). This die can take on f=6 different values (1 to 6), so we consider what happens when we fix its value to each possibility (6 cases):

Case 1: The last die is a 1. The remaining 4 dice must sum to 18-1=17. This can happen dp(4, 6, 17) ways.
Case 2: The last die is a 2. The remaining 4 dice must sum to 18-2=16. This can happen dp(4, 6, 16) ways.
Case 3: The last die is a 3. The remaining 4 dice must sum to 18-3=15. This can happen dp(4, 6, 15) ways.
Case 4: The last die is a 4. The remaining 4 dice must sum to 18-4=14. This can happen dp(4, 6, 14) ways.
Case 5: The last die is a 5. The remaining 4 dice must sum to 18-5=13. This can happen dp(4, 6, 13) ways.
Case 6: The last die is a 6. The remaining 4 dice must sum to 18-6=12. This can happen dp(4, 6, 12) ways.

dp(5, 6, 18) = dp(4, 6, 17) + dp(4, 6, 16) + dp(4, 6, 15) + dp(4, 6, 14) + dp(4, 6, 13) + dp(4, 6, 12)

We sum up the solutions these 6 cases to arrive at our result. Of course, each of these cases branches off into 6 cases of its own, and the recursion only resolves when d=0. The handling of this base case is explained below.



The general relation is:
dp(d, f, target) = dp(d-1, f, target-1) + dp(d-1, f, target-2) + ... + dp(d-1, f, target-f)

The base case occurs when d = 0. We can make target=0 with 0 dice, but nothing else.
So dp(0, f, t) = 0 iff t != 0, and dp(0, f, 0) = 1.

Use memoization to avoid repeated calculations and don't conisider negative targets.
'''