# Andre Doumad
# 200904
'''
Given an array of strings products and a string searchWord. We want to design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with the searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return list of lists of the suggested products after each character of searchWord is typed. 

 

Example 1:

Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]
Example 2:

Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
Example 3:

Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]
Example 4:

Input: products = ["havana"], searchWord = "tatiana"
Output: [[],[],[],[],[],[],[]]
 

Constraints:

1 <= products.length <= 1000
There are no repeated elements in products.
1 <= Σ products[i].length <= 2 * 10^4
All characters of products[i] are lower-case English letters.
1 <= searchWord.length <= 1000
All characters of searchWord are lower-case English letters.

'''
from typing import List
import unittest

## SOLUTION IS A TRIE 
'''
Complexity depends on the sorting, the process of building Trie and the length of searchWord. Sorting cost time O(m * n), due to involving comparing String, which cost time O(m) for each comparison, building Trie cost O(m * n). Therefore,
Time: O(m * n + L), space: O(m * n + L * m) - including return list ans, where m = average length of products, n = products.length, L = searchWord.length().
'''
class Trie():
    def __init__(self):
        self.sub = {}
        self.suggestions = []

class Solution():
    def insert(self, word, root):
        for ch in word:
            if ch not in root.sub:
                root.sub[ch] = Trie()
            root = root.sub[ch]
            root.suggestions.append(word)
            root.suggestions.sort()
            if len(root.suggestions) > 3:
                root.suggestions.pop()
    def search(self, word, root):
        ans = []
        for ch in word:
            if root:
                root = root.sub.get(ch)
            if root and root.suggestions:
                ans.append(root.suggestions)
            else:
                ans.append([])
        return ans
    def suggestedProducts(self, products, searchWord):
        root = Trie()
        for word in products:
            self.insert(word, root)
        return self.search(searchWord, root)

class UnitTest(unittest.TestCase):
    def test_a(self):
        s = Solution()
        result = s.suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "m")
        print('result for m = ', result)
        result = s.suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mou")
        print('result for mou = ', result)
        result = s.suggestedProducts(["havanna"], searchWord = "tatiana")
        print('result for mou = ', result)

if __name__ == '__main__':
    unittest.main()

'''
class Trie:
    def __init__(self):
        self.sub = {}
        self.suggestion = []

class Solution:
    def insert(self, product, root):
        trie = root
        for char in product:
            if char not in  trie.sub:
                trie.sub[char] = Trie()
            trie = trie.sub[char]
            trie.suggestion.append(product)
            trie.suggestion.sort()
            if len(trie.suggestion) > 3:
                trie.suggestion.pop()

    def search(self, searchWord, root):
        ans = []
        for char in searchWord:
            if root:
                root = root.sub.get(char)
            if root.suggestion:
                print('root.suggestion ', root.suggestion)
                ans.append(root.suggestion)

            # ans.append(root.suggestion if root else [])
            # print('ans')
        return ans

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = Trie()
        for product in sorted(products):
            self.insert(product, root)
        
        return self.search(searchWord, root)

'''