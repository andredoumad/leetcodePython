'''
This Problem was asked by Amazon.

You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs.  
It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.  
The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  
The digit-logs should be put in their original order.

Return the final order of the logs.

Example 1:

Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]

Constraints:

0 <= logs.length <= 100
3 <= logs[i].length <= 100
logs[i] is guaranteed to have an identifier, and a word after the identifier.
'''

import unittest, typing, re
class Solution:
    def reorderLogFiles(self, logs):
        digit = []
        letter = []
        ans = []
        for w in logs:
            w = w.split()
            if w[1].isalpha():
                letter.append(" ".join(w[1:]) + " " + w[0])
            else:
                digit.append(w[0] + " " + " ".join(w[1:]))
        letter.sort()
        for l in letter: 
            l = l.split()
            ans.append(" ".join((l[-1:] + l[:-1])))
        return ans+digit


class unitTest(unittest.TestCase):
    def test_a(self):

        solution = Solution()
        result = solution.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"])
        print('RESULT IS: ', result)
        self.assertEqual(result,
        ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"], 
        'should equal ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]')

        # solution = Solution()
        # result = solution.reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"])
        # print('RESULT IS: ', result)
        # self.assertEqual(result,
        # ["a2 act car","g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"], 
        # 'should equal ["a2 act car","g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]')

        # solution = Solution()
        # result = solution.reorderLogFiles(["1 n u", "r 527", "j 893", "6 14", "6 82"])
        # print('RESULT IS: ', result)
        # self.assertEqual(result,
        # ["1 n u","r 527","j 893","6 14","6 82"], 
        # 'should equal ["1 n u","r 527","j 893","6 14","6 82"]')


if __name__ == '__main__':
    unittest.main()

'''
output:
RESULT IS:  ['let1 art can', 'let3 art zero', 'let2 own kit dig', 'dig1 8 1 5 1', 'dig2 3 6']
RESULT IS:  ['a2 act car', 'g1 act car', 'a8 act zoo', 'ab1 off key dog', 'a1 9 2 3 1', 'zo4 4 7']
RESULT IS:  ['1 n u', 'r 527', 'j 893', '6 14', '6 82']
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
'''