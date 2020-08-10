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

class Graph(object):
    def __init__(self):
        self.adj = {}
        self.islands = 0

    def addEdge(self, v, e=None):
        if v in self.adj:
            self.adj[v].append(e)
        else:
            if e!=None:
                self.adj[v] = [e]
            else:
                self.adj[v] = []

    # DFS traversal
    def dfs(self, v):
        print('Depth first search')
        self.deep(v, {v:True}, [v], False)

    # BFS traversal
    def bfs(self, v):
        print('Breadth first search')
        self.deep(v, {v:True}, [v], True)

    def deep(self,start,b_visited,queue, bfs):
        if len(self.adj) == 0:
            return
        if len(self.adj) == 1:
            return
        while len(queue) > 0:
            v = queue.pop()
            print('length of self.adj ', len(self.adj))

            while len(self.adj[v]) > 0:
                e = self.adj[v].pop()
                if e not in b_visited:
                    b_visited[e] = True
                    print('node ' + str(v) +  ' is connected to ' + str(e))
                    queue.append(e)
                    if not bfs:
                        break
            if bfs:
                del self.adj[v]
        if not bfs:
            if self.adj[start]:
                self.deep(start,b_visited,[start], bfs)

    def printGraph(self):
        for k,v in self.adj.items():
            print('k ', k, ' v ', v)



class Solution(object):

    def numIslands(self, grid):
        graphA = Graph()
        for a in range(0, len(grid)):
            all_zero = True
            for b in range(0, len(grid[a])):
                if int(grid[a][b]) == 1:
                    all_zero = False
                    graphA.addEdge(int(a), b)
            if all_zero:
                graphA.addEdge(int(a), None)

        graphA.printGraph()
        graphA.dfs(0)
        graphA.printGraph()
        islands = 0
        for k,v in graphA.adj.items():
            islands += len(v)
        return islands

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