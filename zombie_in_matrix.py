# Andre Doumad
# 200827
'''
This problem was asked by Amazon.

Given a 2D grid, each cell is either a zombie 1 or a human 0. 
Zombies can turn adjacent (up/down/left/right) human beings into zombies every hour. 
Find out how many hours does it take to infect all humans?

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

'''

class Solution():
    def minHours(self, grid):
        if not grid: return 0
        nrow, ncol = len(grid), len(grid[0])
        hours = 0
        directions = [[0,1],[0,-1],[-1,0],[1,0]]
        zombies = [] # hour, row, col
        for row in range(nrow):
            for col in range(ncol):
                if grid[row][col] == 1:
                    zombies.append([0, row, col])  
        while zombies:
            print('zombies: ', zombies)
            hours, x, y = zombies.pop(0)
            print('zombies: ', zombies)
            for direction in directions:
                X = x+direction[0]
                Y = y+direction[1]
                if 0<=X<nrow and 0<=Y<ncol and grid[X][Y] == 0:
                    grid[X][Y] = 1
                    zombies.append([hours+1, X, Y])
        return hours

s = Solution()
print(s.minHours([
            [0, 1, 1, 0, 1],
            [0, 1, 0, 1, 0],
            [0, 0, 0, 0, 1],
            [0, 1, 0, 0, 0]
            ]))

