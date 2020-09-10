# Andre Doumad
# 200908
'''
Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Restrictions:
The string consists of lower English letters only.
Length of the given string and k will in the range [1, 10000]
'''
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        i = 0
        length = len(s) // k
        str = ''
 
        while i < length:
            if i % 2 == 0:
                str += ''.join(reversed(s[k*i: k*i + k]))
            else:
                str += s[k*i: k*i + k]
            i += 1
            
        if i % 2 == 0:   
            str += ''.join(reversed(s[i*k:]))
        else:
            str+= s[i*k:]
        return str