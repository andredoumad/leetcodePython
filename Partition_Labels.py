# Andre Doumad
# 200820
'''
This problem was asked by Amazon.

A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

Note:

S will have length in range [1, 500].
S will consist of lowercase English letters ('a' to 'z') only.
'''

class Solution:
    def partitionLabels(self, S):
        result, last_seen, max_last_seen, count = [], {}, 0, 0
        for i, char in enumerate(S):
            last_seen[char] = i
        for i, char in enumerate(S):
            max_last_seen = max(max_last_seen, last_seen[char])
            count += 1
            if i == max_last_seen:
                result.append(count)
                count = 0
        return result


solution = Solution()
print(solution.partitionLabels('ababcbacadefegdehijhklij'))






# solution = Solution()
# solution.partitionLabels('ababcbacadefegdehijhklij')