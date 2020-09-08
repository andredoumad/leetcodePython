# Andre Doumad
# 200907
'''
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:

Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
 

Example 2:

Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return False
        return self._findTarget(root, set(), k)
        
    def _findTarget(self, node, nodes, k):
        if not node:
            return False
        
        complement = k-node.val
        
        if complement in nodes:
            return True
        nodes.add(node.val)
        return self._findTarget(node.left, nodes, k) or self._findTarget(node.right, nodes, k)