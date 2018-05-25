# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example 1:

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

# Example 2:

# Input: "cbbd"
# Output: "bb"



class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        pali = [[False for y in range(len(s))] for x in range(len(s))]

        if not s:
            return ""

        best = ""
        longest = -1
        if len(set(s)) == 1:
            return s
        for l in range(len(s)):
            for i in range(len(s) - l):
                j = i + l

                if l == 0:
                    pali[i][j] = True
                elif l == 1:
                    pali[i][j] = s[i] == s[j]
                else:
                    pali[i][j] = pali[i + 1][j - 1] and s[i] == s[j]

                if l > longest and pali[i][j]:
                    best = s[i:j + 1]
                    longest = l

        return best
