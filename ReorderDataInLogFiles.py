'''
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


# passes 60 of 63 cases only >.< -- needs refactoring....
import unittest, typing, re
class Solution:

    def sortIt(self, logsInput):
        sorted_logs = logsInput
        sorted_logs_dict = {}
        for a in range(0, len(sorted_logs)):
            logs = sorted_logs[a].split()
            k = logs[0]
            v = ''
            tag = ''
            print('k is ', k)
            print('length of k is ', len(k))
            for i in range(0, len(k)):
                if not re.search(r'\d', k[i]):
                    tag += k[i]
            if tag == '':
                tag = logs[1]

            print('tag ', tag)
            for b in range(1, len(logs)):
                v += ' '
                v += logs[b]
                if b == len(logs)-1:
                    v += ' '
                    v += tag
            sorted_logs[a] = v
            sorted_logs_dict[k] = v
        print('pre sort logs ', sorted_logs)
        sorted_logs = sorted(sorted_logs)
        print('sorted logs ', sorted_logs)
        keys = []
        for k, v in sorted_logs_dict.items():
            print('k, ', k, ' v, ', v)
        # exit()
        for k,v in sorted_logs_dict.items():
            for a in range(0, len(sorted_logs)):
                if sorted_logs[a] == v:
                    string = str(k)
                    #print('k is ', str(k))
                    #print('v is ', v)
                    # for c in range(0, len(v)):
                    #     string+= v[c]
                    splits = v.split()
                    string += ' '
                    for c in range(0, len(splits)-1):
                        string += splits[c]
                        if c < len(splits)-2:
                            string += ' '
                    sorted_logs[a] = str(string)
        print('final logs ', sorted_logs)

        return sorted_logs

    def reorderLogFiles(self, logs):
        #print('input: ' + str(logs))
        letLogs = []
        digLogs = []
        for i in range(0, len(logs)):
            #print('logs[i] ', logs[i])
            first_word = ''
            for b in range(0, len(logs[i])):
                if logs[i][b] == ' ':
                    break
                else:
                    first_word += logs[i][b]
            #print('first_word ', first_word)
            v = logs[i][len(first_word):]
            #print('v = ', v)
            if not re.search(r'\d', v):
                letLogs.append(logs[i])
            else:
                digLogs.append(logs[i])
        #print('letLogs ', letLogs)
        #print('digLogs ', digLogs)
        sorted_letLogs = self.sortIt(letLogs)
        compiled_logs = sorted_letLogs
        for i in range(0, len(digLogs)):
            compiled_logs.append(digLogs[i])
        # print('compiled logs: ', compiled_logs)
        return compiled_logs


class unitTest(unittest.TestCase):
    def test_a(self):

        # solution = Solution()
        # result = solution.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"])
        # print('RESULT IS: ', result)
        # self.assertEqual(result,
        # ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"], 
        # 'should equal ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]')

        # solution = Solution()
        # result = solution.reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"])
        # print('RESULT IS: ', result)
        # self.assertEqual(result,
        # ["a2 act car","g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"], 
        # 'should equal ["a2 act car","g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]')

        solution = Solution()
        result = solution.reorderLogFiles(["1 n u", "r 527", "j 893", "6 14", "6 82"])
        print('RESULT IS: ', result)
        self.assertEqual(result,
        ["1 n u","r 527","j 893","6 14","6 82"], 
        'should equal ["1 n u","r 527","j 893","6 14","6 82"]')


if __name__ == '__main__':
    unittest.main()