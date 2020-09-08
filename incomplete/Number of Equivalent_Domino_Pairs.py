# Andre Doumad
# 200908
'''
Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a==c and b==d), or (a==d and b==c) - that is, one domino can be rotated to be equal to another domino.

Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

 

Example 1:

Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
Output: 1
 

Constraints:

1 <= dominoes.length <= 40000
1 <= dominoes[i][j] <= 9
'''
'''
Solution:
Use a dictionary to count how many times a domino appeared. By sort the list, we can easily identify the same domino, order doesn't matter here.
Then calculate how many pairs are there:
For each domino, number of pairs = n*(n-1)//2 , where n is the frequency that a domino appeared.
At first choice, we have n choices, then (n - 1) choices. Since the order of the pair doesn't matter, we need to divide by 2 to deduct the duplicate.
'''
from typing import List
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        # step 1: count the dominoes
        d = {}
        for domi in dominoes:
            p = tuple(sorted(domi))
            print('p ', p)
            if p in d:
                d[p] += 1
            else:
                d[p] = 1
        # step 2: caculate the pairs. for each pair, number of pairs = n*(n-1)//2
        c = 0
        for n in d.values():
            s = n*(n-1)//2
            c += s
        return c

s = Solution()
print(s.numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6]]))
'''
Complexity Analysis

Time complexity: O(n)
Dictionary takes O(1) to store.
To generate the dictionary takes n*O(1) and calculate pairs takes O(n), the total time complexity is O(n), where n is the length of the input list.
Space complexity: O(n)
At worst case (every item in the input list appeared once), the algorithm needs a dictionary which it's size equals the length of the list, where n is the length of the input list.
'''