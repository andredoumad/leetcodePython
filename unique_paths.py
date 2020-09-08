# Andre Doumad
# 200907
'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot ('r') is trying to reach the bottom-right corner of the grid (marked 'f' in the diagram below).

r x x x x x x
x x x x x x x
x x x x x x f

How many possible unique paths are there?

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

7 x 3 grid. How many possible unique paths are there?
Input: m = 7, n = 3
Output: 28
'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1]*m for _ in range(n)]
        for i in range(1,n):
            for j in range(1,m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

s = Solution()
print(s.uniquePaths(7,3))

'''
class Solution(object):
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1]*m for _ in range(n)]
        for i in range(1,n):
            print(dp)
            for j in range(1,m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        print(dp)
        return dp[-1][-1]
'''

'''
output:
[[1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1]]
[[1, 1, 1, 1, 1, 1, 1], [1, 2, 3, 4, 5, 6, 7], [1, 1, 1, 1, 1, 1, 1]]
[[1, 1, 1, 1, 1, 1, 1], [1, 2, 3, 4, 5, 6, 7], [1, 3, 6, 10, 15, 21, 28]]
28
'''