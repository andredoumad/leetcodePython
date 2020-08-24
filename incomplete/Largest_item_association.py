# Andre Doumad
# 200823
'''
This problem was asked by Amazon.

In order to improve customer experience, Amazon has developed a system to provide recommendations to the customers regarding the items they can purchase. Based on a historical customer purchase information, an item association can be defined as - if an item A is ordered by a customer, then item B is also likely to be ordered by the same customer. (e.g. Book1 is frequently ordered with Book2.). All items that are linked together by an item association can be considered to be in the same group. An item without any association to any other item can be considered to be its own item association with a group size of 1. 

given a list of item association relationships (i.e., group of items likely to be ordered together), write an algorithm that outputs the largest item association group. If the two groups have the same number of items then select the group which contains the item that appears first in lexicographic order.

Input:
The input to to the function/method consists of an argument- 
itemAssociation, a list containing pairs of strings representing the items that are ordered together.

Output:
Return a list of strings representing the largest item association group, sorted lexicographically.

EXAMPLE:
Input:
itemAssociation:
[[Item1, Item2],
 [Item3, Item4],
 [Item4, Item5]]

Output:
[Item3, Item4, Item5]

Explanation:
There are two item association groups:
group1: [Item1, Item2]
group2: [Item3, Item4, Item5]
In the available item associations, group2 has the largest association.
So, the output is [Item3, Item4, Item5].

Helper Description:
The following class is used to represent a pair of strings and is already implemented in the default code( no need to write this definition again in your code.)

class PairString():
    def __init__(self, first, second):
        self.first = first
        self.second = second

'''

class PairString():
    def __init__(self, first, second):
        self.first = first
        self.second = second

class Graph():
    def __init__(self):
        self.adj = {}

    def addEdge(self, v, e):
        if v not in self.adj:
            self.adj[v] = [e]
        else:
            self.adj[v].append(e)

    def printGraph(self):
        print('length of graph is ', len(self.adj))
        for k,v in self.adj.items():
            print('k ', k, ' v ', v)

    def dfs(self, start):
        self.doDfs(start, {start:True}, [start], self.adj)

    def doDfs(self, start, visited, queue, adj):
        print('dfs start: ', start)
        while len(queue) > 0:
            v = queue.pop()
            while len(adj[v]) > 0:
                e = adj[v].pop()
                if e not in visited:
                    visited[e] = True
                    print('node ', v, ' is connected to ', e)
                    # queue.append(e)
        if len(adj) > 0:
            adj.pop(start)
            start+=1
            print('length of graph is ', len(adj))
            self.doDfs(start, visited, [start], adj)


class Solution():
    def largestItemAssociation(self, itemAssociation):
        print('------------------')
        print('INPUT: ', itemAssociation)
        graph = Graph()
        for i in range(0, len(itemAssociation)):
            for j in range(0, len(itemAssociation[i])):
                graph.addEdge(i, itemAssociation[i][j])
        
        graph.printGraph()
        graph.dfs(0)

        res = True
        print('RESULT: ', res)
        print('------------------')
        return res



s = Solution()
# print(s.largestItemAssociation([]) == [])
print(s.largestItemAssociation([['Item1', 'Item2'], ['Item3', 'Item4'], ['Item4', 'Item5']]) == ['Item3', 'Item4', 'Item5'])
# print(s.largestItemAssociation([['item1','item2']]) == ['item1','item2'])
# print(s.largestItemAssociation([['item1','item2'],['item2','item3'],['item4','item5'],['item5','item6']]) == ['item1','item2','item3'])
# print(s.largestItemAssociation([['Item1','Item2'],['Item3','Item4'],['Item4','Item5']]) == ['Item3', 'Item4', 'Item5'])
# print(s.largestItemAssociation([['Item1','Item2'],['Item2','Item5'],['Item3']]) == ['Item1', 'Item2', 'Item5'])
# print(s.largestItemAssociation([['Item1','Item2'],['Item2','Item3'],['Item4','Item5'],['Item5','Item6']]) == ['Item1', 'Item2', 'Item3'])
# print(s.largestItemAssociation([["Item1","Item2"], ["Item1","Item3"], ["Item2","Item7"], ["Item3","Item7"], ["Item5","Item6"], ["Item3","Item7"]]) == ['Item1', 'Item2', 'Item3', 'Item7'])

# print(s.largestItemAssociation([['Item1','Item2'],['Item1','Item3'],['Item2','Item7'],['Item3','Item7'],['Item5','Item6'],['Item3','Item7']]) == ['Item1', 'Item2', 'Item3', 'Item7'])
# print(s.largestItemAssociation([['Item3','Item2','Item4'], ['Item1', 'Item2'],['Item3', 'Item5', 'Item7'],['Item6','Item8']]) == ['Item1', 'Item2', 'Item3', 'Item4', 'Item5', 'Item7'])



# this fails on the last 3 test cases. Doesnt create a graph.
# class Solution():
#     def largestItemAssociation(self, itemAssociation):
#         print('------------------')
#         print('INPUT: ', itemAssociation)
#         if itemAssociation == []:
#             return []
#         allItems = {}
#         for j in range(0, len(itemAssociation)):
#             for k in range(0, len(itemAssociation[j])):
#                 if itemAssociation[j][k] not in allItems:
#                     allItems[itemAssociation[j][k]] = [j]
#                 else:
#                     allItems[itemAssociation[j][k]].append(j)

#         print('--- all items ---')
#         mostFrequentItem = None
#         mostFrequentItemGroups = None
#         for k,v in allItems.items():
#             print('k ', k, ' v ', v)
#             if mostFrequentItem == None:
#                 mostFrequentItem = k
#                 mostFrequentItemGroups = v
#             elif len(mostFrequentItemGroups) < len(v):
#                 mostFrequentItem = k
#                 mostFrequentItemGroups = v
#         print('mostFrequentItem = ', mostFrequentItem)
#         print('mostFrequentItemGroups = ', mostFrequentItemGroups)
#         res = []
#         for i in range(0, len(mostFrequentItemGroups)):
#             # print('i ', i)
#             print('mostFrequentItemGroups[', i, '] ', mostFrequentItemGroups[i])
#             for j in range(0, len(itemAssociation[i])):
#                 print('contains items: ', itemAssociation[mostFrequentItemGroups[i]][j])
#                 if itemAssociation[mostFrequentItemGroups[i]][j] not in res:
#                     res.append(itemAssociation[mostFrequentItemGroups[i]][j])
#         print('RESULT: ', res)
#         print('------------------')
#         return res

