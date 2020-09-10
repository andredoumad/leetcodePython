# Andre Doumad
# 200908
'''
Find Words That Can Be Formed by Characters

You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

Example 1:
Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: 
The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

Example 2:
Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: 
The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.

Note:

1 <= words.length <= 1000
1 <= words[i].length, chars.length <= 100
All strings contain lowercase English letters only.
'''
from typing import List
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        counter = 0
        for w in words:
            print('--------')
            included = True
            charsList = []
            for c in chars:
                charsList.append(c)
            print(charsList)
            for c in w:
                if c in charsList:
                    charsList.remove(c)
                    print(charsList)
                else:
                    included = False
                    break
            if included:
                print('INCLUDED charsList: ', charsList)
                print('INCLUDED: w ', w)
                counter = counter+len(w)
        return counter

s = Solution()

print(s.countCharacters( ["cat","bt","hat","tree"], chars = "atach"))
'''
--------
['a', 't', 'a', 'c', 'h']
['a', 't', 'a', 'h']
['t', 'a', 'h']
['a', 'h']
INCLUDED charsList:  ['a', 'h']
INCLUDED: w  cat
--------
['a', 't', 'a', 'c', 'h']
--------
['a', 't', 'a', 'c', 'h']
['a', 't', 'a', 'c']
['t', 'a', 'c']
['a', 'c']
INCLUDED charsList:  ['a', 'c']
INCLUDED: w  hat
--------
['a', 't', 'a', 'c', 'h']
['a', 'a', 'c', 'h']
6
'''