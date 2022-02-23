# Given a string s, find the length of the longest substring without repeating characters.
#
# Example 1:
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        result=[]
        for ch in s:
            if result.__contains__(ch):
                pass
            else:
                result.append(ch)
        # print(result)
        print(len(result))

sol=Solution()
sol.lengthOfLongestSubstring("abcabcbb")

