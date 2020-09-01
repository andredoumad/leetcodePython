# Andre Doumad
# 200831
'''
You are given an undirected connected graph. An articulation point (or cut vertex) is defined as a vertex which, when removed along with associated edges, makes the graph disconnected (or more precisely, increases the number of connected components in the graph). The task is to find all articulation points in the given graph.

Input:
The input to the function/method consists of three arguments:

numNodes, an integer representing the number of nodes in the graph.
numEdges, an integer representing the number of edges in the graph.
edges, the list of pair of integers - A, B representing an edge between the nodes A and B.
Output:
Return a list of integers representing the critical nodes.

Example:

Input: numNodes = 7, numEdges = 7, edges = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]

Output: [2, 3, 5]
'''
import collections

class Solution:
    def __init__(self):
        pass

    def adjacencyGraph(self,edges, node, numEdges):
        self.graph = collections.defaultdict(list)
        articulation_point = []
        for each in edges:
            self.graph[each[0]].append(each[1])
            self.graph[each[1]].append(each[0])

        for k,v in self.graph.items():
            temp = v
            self.graph[k] = []

            self.visited = set()
            self.visited.add(k)
            # this is a hack but it works
            if k == numEdges-1:
                each = 0
            else:
                each = k+1

            que =[each]
            while que:
                item = que.pop()
                if item not in self.visited:
                    que.extend(self.graph[item])
                    self.visited.add(item)
            if len(self.visited) < node:
                articulation_point.append(k)
            self.graph[k].extend(temp)

        return articulation_point

s = Solution()
print(s.adjacencyGraph(node = 7, numEdges = 7, edges = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]))