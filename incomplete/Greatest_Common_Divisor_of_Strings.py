# Andre Doumad
# 200907
'''
For two strings s and t, we say "t divides s" if and only if s = t + ... + t  (t concatenated with itself 1 or more times)

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
Example 4:

Input: str1 = "ABCDEF", str2 = "ABC"
Output: ""
 

Constraints:

1 <= str1.length <= 1000
1 <= str2.length <= 1000
str1 and str2 consist of English uppercase letters.
'''
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        str1Length, str2Length = len(str1), len(str2)
        
        if str2Length > str1Length: # Ensures the longer string is str1 and shorter or equal string is str2
            return self.gcdOfStrings(str2, str1)
        
        if str1[:str2Length] == str2: # Check if shorter string (str2) is a prefix in longer string (str1)
		
            if str1Length == str2Length: # If str1 and str2 are of the same length then we have found the common divisor
                return str2
            
            return self.gcdOfStrings(str2, str1[str2Length:]) # return the gcd of the str2 and str1 minus the prefix

        return ""