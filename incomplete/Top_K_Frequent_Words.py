# Andre Doumad
# 200821
'''
Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Input words contain only lowercase letters.
Follow up:
Try to solve it in O(n log k) time and O(n) extra space.
'''

class Solution:
    def topKFrequent(self, words, k):
        hashies = {}
        for w in words:
            if w not in hashies:
                hashies[w] = 1
            elif w in hashies:
                hashies[w]+=1
        res = []
        i = int(0)
        maxWords = int(k)
        while i <= maxWords:
            topW = []
            topCount = 0
            print('-------')
            for k,v in hashies.items():
                print('k ', k, ' v ', v)
                if v >= topCount:
                    topW.append(k)
                    topCount = v
            for w in topW:
                del hashies[w]
            topW.sort()
            if len(topW) > 0:
                for w in topW:
                    if i < maxWords:
                        print('appending1 ', w)
                        res.append(w)
                        i+=1
            else:
                print('appending2 ', topW)
                if topW != []:
                    res.append(topW)
                i+=1

        # res.sort()
        print('RESULT: ', res)
        return res

s = Solution()

# print(s.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))
# print(s.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"],4))
print(s.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 3))