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

class Solution():
    def largestItemAssociation(self, itemAssociation):
        knownItems = []
        item_map = {}
        grid = []
        for i in range(0, len(itemAssociation)):
            if itemAssociation[i].first not in knownItems:
                knownItems.append(itemAssociation[i].first)
            if itemAssociation[i].second not in knownItems:
                knownItems.append(itemAssociation[i].second)
        print('known items ', knownItems)

        for i in range(0, len(itemAssociation)):
            grid.append([])
            for j in range(0, len(knownItems)):
                if knownItems[j] == itemAssociation[i].first:
                    grid[i].append('1')
                    item_map[i,j] = itemAssociation[i].first 
                elif knownItems[j] == itemAssociation[i].second:
                    grid[i].append('1')
                    item_map[i,j] = itemAssociation[i].second 
                else:
                    grid[i].append('0')

        for i in range(0, len(grid)):
            print(grid[i])

        numIslands = 0
        pairs = {}
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == '1':
                    pairs[numIslands] = []
                    self.dfs(grid, i, j, numIslands, pairs)
                    numIslands += 1
                    # pairs.append(p) 

        print('numIslands ', numIslands)
        biggestGroup = 0
        for k,v in pairs.items():
            print('group ', k, ' pairs ', v)
            if biggestGroup < len(v):
                biggestGroup = k
        print('biggest group is ', biggestGroup)
        res = []
        for coordinate in pairs[biggestGroup]:
            print(coordinate)
            print('item_map: ', item_map[coordinate[0],coordinate[1]])
            if item_map[coordinate[0],coordinate[1]] not in res:
                res.append(item_map[coordinate[0],coordinate[1]])
        print('RESULT: ', res)
        return res

    def dfs(self, grid, i, j,  numIslands, pairs):
        if i < 0 or j < 0 or i >=len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#'
        pairs[numIslands].append([i,j])
        self.dfs(grid, i+1, j, numIslands,  pairs) # down
        self.dfs(grid, i-1, j,  numIslands, pairs) # up
        self.dfs(grid, i, j-1,  numIslands, pairs) # left
        self.dfs(grid, i, j+1,  numIslands, pairs) # right



s = Solution()
print(s.largestItemAssociation([PairString('Item1', 'Item2'), PairString('Item3', 'Item4'), PairString('Item4', 'Item5')]) == ['Item3', 'Item4', 'Item5'])
print(s.largestItemAssociation([PairString('item1', 'item2')]) == ['item1','item2'])
'''
OUTPUT:
['1', '1', '0', '0', '0']
['0', '0', '1', '1', '0']
['0', '0', '0', '1', '1']
numIslands  2
group  0  pairs  [[0, 0], [0, 1]]
group  1  pairs  [[1, 2], [1, 3], [2, 3], [2, 4]]
biggest group is  1
[1, 2]
item_map:  Item3
[1, 3]
item_map:  Item4
[2, 3]
item_map:  Item4
[2, 4]
item_map:  Item5
RESULT:  ['Item3', 'Item4', 'Item5']
True
known items  ['item1', 'item2']
['1', '1']
numIslands  1
group  0  pairs  [[0, 0], [0, 1]]
biggest group is  0
[0, 0]
item_map:  item1
[0, 1]
item_map:  item2
RESULT:  ['item1', 'item2']
True
'''
















# print(s.largestItemAssociation([]) == [])
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

