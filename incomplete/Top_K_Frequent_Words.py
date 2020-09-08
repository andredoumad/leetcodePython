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


s = Solution()

# print(s.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))
# print(s.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"],4))
print(s.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 3))




'''
from collections import defaultdict
from heapq import heappush, heappop

class WordFreq:
    def __init__(self, freq, word):
        self.freq = freq
        self.word = word
    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq.__lt__(other.freq)
        else:
            return self.word.__gt__(other.word)

class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        
        # word frequency
        word_frequency = defaultdict(int)
        for word in words:
            word_frequency[word] += 1
        
        # current k most frequent elements
        k_most_frequent = []
        for word, freq in word_frequency.items():
            heappush(k_most_frequent, WordFreq(freq, word))
            if len(k_most_frequent) == k + 1:
                heappop(k_most_frequent)
        
        res = []
        while len(k_most_frequent) != 0:
            res.insert(0, heappop(k_most_frequent).word)
        
        return res
'''
