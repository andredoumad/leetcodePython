# Andre Doumad
# 200914
'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
'''

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0]=='0':
            return 0

        dp = [0 for x in range(len(s) + 1)] 

        # base case initialization
        dp[0:2] = [1,1]

        for i in range(2, len(s) + 1): 
            # One step jump
            if 0 < int(s[i-1:i]):    #(2)
                dp[i] = dp[i - 1]
            # Two step jump
            if 10 <= int(s[i-2:i]) <= 26: #(3)
                dp[i] += dp[i - 2]
                
        return dp[-1]

        
s = Solution()
print(s.numDecodings("226"))