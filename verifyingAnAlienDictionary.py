# Andre Doumad
'''
This question was asked by Amazon.

Written in an alien language, surprisingly they also use english lowercase letters, 
but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the 
alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) 
According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as 
the blank character which is less than any other character (More info).

Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.
'''

import unittest

class Solution:
    '''
    Runtime: 36 ms, faster than 80.31% of Python3 online submissions for Verifying an Alien Dictionary.
    Memory Usage: 13.8 MB, less than 67.75% of Python3 online submissions for Verifying an Alien Dictionary.
    '''
    def isAlienSorted(self, words, order):
        for a in range(0, len(words)-1):
            word_a = words[a]
            for b in range(1, len(words)):
                word_b = words[b]
                i = 0
                while i < len(word_a) and i < len(word_b):
                    letter_score_a = len(order) - order.index(word_a[i])
                    letter_score_b = len(order) - order.index(word_b[i])
                    if letter_score_a < letter_score_b:
                        return False
                    elif letter_score_a > letter_score_b:
                        break
                    i+=1
                if i >= len(word_b):
                    return False                    
        return True

class UnitTest(unittest.TestCase):
    def test_a(self):
        solution = Solution()

        result = solution.isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz")
        self.assertTrue(result)

        result = solution.isAlienSorted(["word","world","row"], "worldabcefghijkmnpqstuvxyz")
        self.assertFalse(result)

        result = solution.isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz")
        self.assertFalse(result)

if __name__=='__main__':
    unittest.main()