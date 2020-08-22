# Andre Doumad
# 200821
'''
This problem was asked by FAANG companies...

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''
from typing import List
class Solution:
    def dfs(self, leftRemain, rightRemain, path, res):
        if leftRemain > rightRemain or leftRemain < 0 or rightRemain < 0:
            return
        if leftRemain == 0 and rightRemain == 0:
            res.append(path)
        self.dfs(leftRemain-1, rightRemain, path+"(", res)
        self.dfs(leftRemain, rightRemain-1, path+")", res)

    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.dfs(n,n,"",res)
        return res

s = Solution()
print(s.generateParenthesis(3))
'''
['((()))', '(()())', '(())()', '()(())', '()()()']
'''