# A message containing letters from A-Z is being encoded to numbers using the following mapping:

# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26

# Given a non-empty string containing only digits, determine the total number of ways to decode it.

# Example 1:

# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).

# Example 2:

# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0':
            return 0
        array = [0] * (len(s) + 1)
        array[0] = 1
        array[1] = 0
        for i, x in enumerate(s):
            ix = int(x)
            if ix != 0:
                array[i + 1] += array[i]
            if i > 0 and s[i-1] != '0' and 0 < 10 * int(s[i - 1]) + ix < 27:
                array[i + 1] += array[i - 1]
        return array[-1]
