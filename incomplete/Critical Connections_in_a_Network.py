# Andre Doumad
# 200908
'''
There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network where connections[i] = [a, b] represents a connection between servers a and b. Any server can reach any other server directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some server unable to reach some other server.

Return all critical connections in the network in any order.
Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.
 

Constraints:

1 <= n <= 10^5
n-1 <= connections.length <= 10^5
connections[i][0] != connections[i][1]
There are no repeated connections.
'''

'''

https://leetcode.com/problems/critical-connections-in-a-network/discuss/601695/Cleanest-and-Easiest-Understand-Python-Solution-99-Time-100-Mem
'''



class Solution(object):
    def criticalConnections(self, n, connections):
        # graph construction
        graph = [[] for i in range(n)]
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        
        # depth initialization
        depths = [-1] * n
        results = []
        
        """
        visit every node exactly once, the starting point does not matter
        (as long as graph is connected)
        """
        def dfs(prev_node, cur_node, cur_depth):
            depths[cur_node] = cur_depth
            min_depth = cur_depth
            for neighbor in graph[cur_node]:
                if neighbor == prev_node: continue
                """
                find the temporary depth reached by a neighbor
                """
                temp_depth = depths[neighbor]
                """
                if the node is unexplored,  assign it's depth to current depth + 1
                """
                if temp_depth == -1:
                    temp_depth = dfs(cur_node, neighbor, cur_depth+1)
                """
                if the returned depth is deeper than the "current depth", then it is a critical connection
                else, update the min_depth
                NOTE: we are comparing the "returned depth from neighbor (temp_dpeth)" to the "current depth reached by DFS" rather than the "min_depth" that is going to be returned.
                    because once the temp_depth is returned by a neighbor, it is the minimum depth of it. 
                """
                if temp_depth > cur_depth:
                    results.append([cur_node, neighbor])
                else:
                    min_depth = min(min_depth, temp_depth)
            """
            return the minimum depth reached by a node
            """
            depths[cur_node] = min_depth
            return min_depth
        
        # start at node-0
        dfs(None, 0, 0)
        
        return results