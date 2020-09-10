# Andre Doumad
# 200909
'''
The Maze II
There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, find the shortest distance for the ball to stop at the destination. The distance is defined by the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included). If the ball cannot stop at the destination, return -1.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.

Example 1:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (4, 4)

Output: 12

Explanation: One shortest way is : left -> down -> left -> down -> right -> down -> right.
             The total distance is 1 + 1 + 3 + 1 + 2 + 2 + 2 = 12.

Example 2:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (3, 2)

Output: -1

Explanation: There is no way for the ball to stop at the destination.

Note:

There is only one ball and one destination in the maze.
Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.
'''
from typing import List
import heapq

# solution: https://leetcode.com/problems/the-maze-ii/discuss/98398/Python-Solution-with-explanation-(Dijkstra's-algorithm)

class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        dest=tuple(destination)
        m=len(maze)
        n=len(maze[0])
        res=None 
        def go(start, direction):
            # return the stop position and length
            i, j = start
            ii, jj = direction
            l=0
            while 0<=i+ii<m and 0<=j+jj<n and maze[i+ii][j+jj]!=1:
                i+=ii
                j+=jj
                l+=1
            return l, (i,j)
        # bfs (dijkstra: https://en.wikipedia.org/wiki/Dijkstra's_algorithm)
        visited={}
        q=[]
        heapq.heappush(q, (0, tuple(start)))
        while q:
            length, cur = heapq.heappop(q)
            if cur in visited and visited[cur]<=length:
                continue # if cur is visited and with a shorter length, skip it.
            visited[cur]=length
            if cur == dest:
                return length
            for direction in [(-1, 0), (1, 0), (0,-1), (0,1)]:
                l, np = go(cur, direction)
                heapq.heappush(q, (length+l, np))
        return -1

#Example 1:
s = Solution()
maze = [
    [0,0,1,0,0],
    [0,0,0,0,0],
    [0,0,0,1,0],
    [1,1,0,1,1],
    [0,0,0,0,0]
]
print(s.shortestDistance(maze, [0,4],[4,4]))


'''
output:
12
'''
