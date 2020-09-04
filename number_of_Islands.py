# Andre Doumad
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
        if not grid:
            return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#'
        self.dfs(grid, i+1, j) # check down
        self.dfs(grid, i-1, j) # check up
        self.dfs(grid, i, j+1) # check right
        self.dfs(grid, i, j-1) # check left


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
        self.assertEqual(result, 1)

        solution = Solution()
        result = solution.numIslands(grid=[
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
            ])
        print('NUMBER OF ISLANDS: ', result)
        self.assertEqual(result, 3)

        solution = Solution()
        result = solution.numIslands(grid=[])
        print('NUMBER OF ISLANDS: ', result)
        self.assertEqual(result, 0)

        solution = Solution()
        result = solution.numIslands(grid=[["1"]])
        print('NUMBER OF ISLANDS: ', result)
        self.assertEqual(result, 1)

        solution = Solution()
        result = solution.numIslands(grid=[["1","1"]])
        print('NUMBER OF ISLANDS: ', result)
        self.assertEqual(result, 1)


if __name__=='__main__':
    unittest.main()

'''
==========
Finding number of islands given:
['1', '1', '1', '1', '0']
['1', '1', '0', '1', '0']
['1', '1', '0', '0', '0']
['0', '0', '0', '0', '0']
---before---
['1', '1', '1', '1', '0']
['1', '1', '0', '1', '0']
['1', '1', '0', '0', '0']
['0', '0', '0', '0', '0']
---after---
['#', '#', '#', '#', '0']
['#', '#', '0', '#', '0']
['#', '#', '0', '0', '0']
['0', '0', '0', '0', '0']
islands:  1
NUMBER OF ISLANDS:  1
==========
Finding number of islands given:
['1', '1', '0', '0', '0']
['1', '1', '0', '0', '0']
['0', '0', '1', '0', '0']
['0', '0', '0', '1', '1']
---before---
['1', '1', '0', '0', '0']
['1', '1', '0', '0', '0']
['0', '0', '1', '0', '0']
['0', '0', '0', '1', '1']
---after---
['#', '#', '0', '0', '0']
['#', '#', '0', '0', '0']
['0', '0', '1', '0', '0']
['0', '0', '0', '1', '1']
islands:  1
---before---
['#', '#', '0', '0', '0']
['#', '#', '0', '0', '0']
['0', '0', '1', '0', '0']
['0', '0', '0', '1', '1']
---after---
['#', '#', '0', '0', '0']
['#', '#', '0', '0', '0']
['0', '0', '#', '0', '0']
['0', '0', '0', '1', '1']
islands:  2
---before---
['#', '#', '0', '0', '0']
['#', '#', '0', '0', '0']
['0', '0', '#', '0', '0']
['0', '0', '0', '1', '1']
---after---
['#', '#', '0', '0', '0']
['#', '#', '0', '0', '0']
['0', '0', '#', '0', '0']
['0', '0', '0', '#', '#']
islands:  3
NUMBER OF ISLANDS:  3
==========
Finding number of islands given:
NUMBER OF ISLANDS:  0
==========
Finding number of islands given:
['1']
---before---
['1']
---after---
['#']
islands:  1
NUMBER OF ISLANDS:  1
==========
Finding number of islands given:
['1', '1']
---before---
['1', '1']
---after---
['#', '#']
islands:  1
NUMBER OF ISLANDS:  1
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
'''