# Andre Doumad
# 200827
'''
Given a 2D grid, each cell is either a zombie 1 or a human 0. Zombies can turn adjacent (up/down/left/right) human beings into zombies every hour. Find out how many hours does it take to infect all humans?

Example:

Input:
[[0, 1, 1, 0, 1],
 [0, 1, 0, 1, 0],
 [0, 0, 0, 0, 1],
 [0, 1, 0, 0, 0]]

Output: 2

Explanation:
At the end of the 1st hour, the status of the grid:
[[1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [0, 1, 0, 1, 1],
 [1, 1, 1, 0, 1]]

At the end of the 2nd hour, the status of the grid:
[[1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1]]


}
'''

class Solution():
    def minHours(self, grid):
        hours = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 1:
                    # print('before')
                    # self.printGrid(grid)
                    self.dfs(grid, i, j)
                    hours += 1
                    print('after')
                    self.printGrid(grid)
        print('final')
        self.printGrid(grid)
        return hours

    def printGrid(self, grid):
        print('--- zambies ---')
        for i in range(0, len(grid)):
            print(grid[i])

    def dfs(self, grid,i,j):
        if i+1 < len(grid) and j >= 0 and j < len(grid[0]): # down
            if grid[i+1][j] == 0:
                grid[i+1][j] = 'z'
        if i-1 >= 0 and j >= 0 and j < len(grid[0]): # up
            if grid[i-1][j] == 0:
                grid[i-1][j] = 'z'
        if j+1 < len(grid[0]) and i >= 0 and i < len(grid): # right
            if grid[i][j+1] == 0:
                grid[i][j+1] = 'z'
        if j-1 >= 0 and i >= 0 and i < len(grid): # left
            if grid[i][j-1] == 0:
                grid[i][j-1] = 'z'

        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != 1:
            return
        grid[i][j] = 'z'

        self.dfs(grid, i+1, j) # down
        self.dfs(grid, i-1, j) # up
        self.dfs(grid, i, j-1) # left
        self.dfs(grid, i, j+1) # right


s = Solution()
print('hours: ', s.minHours([
            [0, 1, 1, 0, 1],
            [0, 1, 0, 1, 0],
            [0, 0, 0, 0, 1],
            [0, 1, 0, 0, 0]
            ]))
