# Andre Doumad
# 200907
'''
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.

Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def dfs(n, t):
            if not n and not t: 
                return True
            if not n or not t: 
                return False
            return n.val == t.val and dfs(n.left, t.left) and dfs(n.right, t.right)

        stack = [s]
        while stack:
            n = stack.pop()
            if n.val == t.val and dfs(n, t): 
                return True
            if n.left: 
                stack.append(n.left)
            if n.right: 
                stack.append(n.right)
        return False