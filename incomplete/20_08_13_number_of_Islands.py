# Andre Doumad
#TODO This needs refactoring and further tests. It passes all but a few corner cases.
'''
This Problem was asked by Amazon.

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
'''
import unittest, typing

class Solution:
    def numIslands(self, grid):
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    print(i,j)
                    self.dfs(grid,i,j)
                    count  += 1
        #print(grid)
        return count
    # use a helper function to flip connected '1's to 0
    def dfs(self,grid,i,j):
        grid[i][j] = 0
        for dr,dc in (1,0), (-1,0), (0,-1), (0,1):
            r = i + dr
            c = j + dc
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c]=='1':
                self.dfs(grid,r,c)


class unitTest(unittest.TestCase):
    def test_a(self):
        solution = Solution()
        result = solution.numIslands(grid=[
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
            ])
        print('NUMBER OF ISLANDS: ', result)

        solution = Solution()
        result = solution.numIslands(grid=[
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
            ])
        print('NUMBER OF ISLANDS: ', result)

        solution = Solution()
        result = solution.numIslands(grid=[
            ])
        print('NUMBER OF ISLANDS: ', result)

        solution = Solution()
        result = solution.numIslands(grid=[["1"]])
        print('NUMBER OF ISLANDS: ', result)

        solution = Solution()
        result = solution.numIslands(grid=[["1","1"]])
        print('NUMBER OF ISLANDS: ', result)
if __name__=='__main__':
    unittest.main()

'''
0 0
NUMBER OF ISLANDS:  1
0 0
2 2
3 3
NUMBER OF ISLANDS:  3
NUMBER OF ISLANDS:  0
0 0
NUMBER OF ISLANDS:  1
0 0
NUMBER OF ISLANDS:  1
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
'''