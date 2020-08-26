# Andre Doumad
# 200824
'''
This problem was asked by FAANG companies.

Given a list of unique integers nums, construct a BST from it (you need to insert nodes one-by-one with the given order to get the BST) and find the distance between two nodes node1 and node2. Distance is the number of edges between two nodes. If any of the given nodes does not appear in the BST, return -1.

Example 1:

Input: nums = [2, 1, 3], node1 = 1, node2 = 3
Output: 2
Explanation:
     2
   /   \
  1     3
'''

import sys
class Node():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def min(self):
        if self.left:
            return self.left.min()
        else:
            return self

class Solution():

    def __init__(self):
        self.root = None

    # insert
    def insert(self, val):
        if self.root == None:
            self.root = Node(val)
            return
        self.doInsert(self.root, val)

    def doInsert(self, node, val):
        if node.val > val:
            if node.left:
                return self.doInsert(node.left, val)
            else:
                node.left = Node(val)
        elif node.val < val:
            if node.right:
                return self.doInsert(node.right, val)
            else:
                node.right = Node(val)
        else:
            node.val = val

    def printtree(self):
        print('-------------')
        print('TREE: ')
        self.doPrettyPrint(self.root, '', True)
        print('-------------')

    def doPrettyPrint(self, node, indent, last):
        if node:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write('R-----')
                indent += '     '
            else:
                sys.stdout.write('L-----')
                indent += '|----'
            print(str(node.val))
            self.doPrettyPrint(node.left, indent, False)
            self.doPrettyPrint(node.right, indent, True)

    def lca(self, root, node1, node2):
        if not root:
            return None
        
        if root.val == node1 or root.val == node2:
            return root
        left = self.lca(root.left, node1, node2)
        right = self.lca(root.right, node1, node2)
        if left and right:
            return root
        elif left:
            return left
        elif right:
            return right
        return None


    def getdis(self, root, val):
        if val > root.val:
            return self.getdis(root.right, val)+1
        elif val < root.val:
            return self.getdis(root.left, val)+1
        else:
            return 0

    def solve(self, nums, node1, node2):
        for num in nums:
            self.insert(num)
        self.printtree()

        mid = self.lca(self.root, node1, node2)
        print(mid.val)
        return self.getdis(self.root, node1) + self.getdis(self.root, node2)



nums = [2,1,3]
node1 = 1
node2 = 3
s = Solution()
print(s.solve(nums, node1, node2))


'''
------------
TREE: 
R-----2
     L-----1
     R-----3
-------------
2
2
'''