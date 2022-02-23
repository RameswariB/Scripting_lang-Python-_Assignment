# 5. Longest Palindromic Substring
# Given a string s, return the longest palindromic substring in s.
#
# Example 1:
#
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

class Solution(object):
    def longestPalindrome(self, s):
        n=len(s)
        maxLenghth=1
        start=0
        for i in range(n):
            for j in range(i,n):
                flag=1
                for k in range(0, ((j - i) // 2) + 1):
                    if (str[i + k] != str[j - k]):
                        flag = 0
                if (flag != 0 and (j - i + 1) > maxLength):
                    start = i
                    maxLength = j - i + 1

        print("Longest palindrome subString is: ", end = "")
        printSubStr(str, start, start + maxLength - 1)
        return maxLength

def printSubStr(str, low, high):
    for i in range(low, high + 1):
        print(str[i], end = "")


sol=Solution()
sol.longestPalindrome("greek")