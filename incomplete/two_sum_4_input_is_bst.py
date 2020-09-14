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
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        s = set()
        def helper(root, k):
            print(s)
            if not root: return False
            print('root.val ', root.val )
            print('k - root.val ', k - root.val)
            if k - root.val in s: return True
            s.add(root.val)
            return(helper(root.left, k) or helper(root.right, k))
        return helper(root, k)


s = Solution()

t = TreeNode(5,TreeNode(3, TreeNode(2), TreeNode(4)),TreeNode(6,None,TreeNode(7)))

print(s.findTarget(t, 9))

'''
output:
set()
root.val  5
k - root.val  4
{5}
root.val  3
k - root.val  6
{3, 5}
root.val  2
k - root.val  7
{2, 3, 5}
{2, 3, 5}
{2, 3, 5}
root.val  4
k - root.val  5
True
'''