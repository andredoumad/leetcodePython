# Andre Doumad
# 200824
'''
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

class BST():

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





    # delete

    # find

    # rotate left

    # rotate right


bst = BST()
bst.insert(2)
bst.insert(1)
bst.insert(3)
bst.printtree()




























# #Distance between Nodes in BST
# nums = [5, 3, 1, 4, 2, 7, 6, 8]
# node1 = 2
# node2 = 6

# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None

# class Solution:
#     def atob(self, nums, node1, node2):
#         root = Node(nums[0])
#         for num in nums:
#             if num != nums[0]:
#                  self.build_tree(root, num)
                    
#         mid = self.lca(root, node1, node2)
#         print("mid:", mid.val, "root", root.val)
        
#         return self.getdis(root, node1) + self.getdis(root, node2)
        
    
#     def lca(self, root, node1, node2):
#         if not root:
#             return None
        
#         if root.val == node1 or root.val == node2:
#             return root
#         left = self.lca(root.left, node1, node2)
#         right = self.lca(root.right, node1, node2)
#         if left and right:
#             return root
#         elif left:
#             return left
#         elif right:
#             return right
#         return None
    
#     def getdis(self, root, val):
#         if val > root.val:
#             return self.getdis(root.right, val)+1
#         elif val < root.val:
#             return self.getdis(root.left, val)+1
#         else:
#             return 0

#     def build_tree(self, root, num):
#         if num < root.val:
#             if root.left:
#                 self.build_tree(root.left, num)
#             else:
#                 root.left = Node(num)
#                 return 
#         else:
#             if root.right:
#                 self.build_tree(root.right, num)
#             else:
#                 root.right = Node(num)
#                 return

# Dis = Solution()
# print("dis_is:", Dis.atob(nums, node1, node2))