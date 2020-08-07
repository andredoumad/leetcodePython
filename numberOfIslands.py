# Andre Doumad
'''
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
    def __init__(self, v):
        self.v = v
        self.adj = {}
        # for i in range(0, v):
        #     self.adj[i] = [i]
        # self.printGraph()
        self.islands = 0

    def addEdge(self, v, e):
        print('add edge')
        if v in self.adj:
            self.adj[v].append(e)
        else:
            self.adj[v] = [e]
        # self.printGraph()

    # DFS traversal
    def dfs(self, v):
        print('Depth first search')
        self.deep(v, {v:True}, [v], False)

    def deep(self,start,b_visited,queue, bfs):
        print(self.adj)
        while len(queue) > 0:
            v = queue.pop()
            while len(self.adj[v]) > 0:
                e = self.adj[v].pop()
                # print('e ', e)
                # print(self.adj[v])
                
                if e not in b_visited:
                    b_visited[e] = True
                    print('node ' + str(v) +  ' is connected to ' + str(e))
                    queue.append(e)
                    # self.islands +=1
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
        print('grid height ', len(grid))
        graphA = Graph(len(grid))
        for a in range(0, len(grid)):
            print('grid[' + str(a) + '] ' + str(grid[a]))
            for b in range(0, len(grid[a])):
                print('grid[' + str(a) + '] ' + str(grid[a]))
                print('vector ', a, ' edge, ', b, ' is : ', grid[a][b])
                if int(grid[a][b]) == 1:
                    print('adding vector: ', a, ' edge ',b)
                    graphA.addEdge(int(a), b)
        graphA.printGraph()
        path = graphA.dfs(0)
        print(path)
        print('islands ', graphA.islands)



class unitTest(unittest.TestCase):
    def test_a(self):
        # solution = Solution()
        # solution.numIslands(grid=[
        #     ["1","1","1","1","0"],
        #     ["1","1","0","1","0"],
        #     ["1","1","0","0","0"],
        #     ["0","0","0","0","0"]
        #     ])
        solution = Solution()
        solution.numIslands(grid=[
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
            ])

if __name__=='__main__':
    unittest.main()