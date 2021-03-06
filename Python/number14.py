# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: ["flower","flow","flight"]
# Output: "fl"

# Example 2:

# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Note:

# All given inputs are in lowercase letters a-z.

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        current = strs[0]
        for i in range(1, len(strs)):
            current = self.commonPrefix(current, strs[i])
        return current


    def commonPrefix(self, stra, strb):
        m = min(len(stra), len(strb))
        for i in range(m):
            if stra[i] != strb[i]:
                return stra[:i]
        return stra[:m]


## second, more functional version

import functools

class Solution2:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        return functools.reduce(self.commonPrefix, strs)


    def commonPrefix(self, stra, strb):
        m = min(len(stra), len(strb))
        for i in range(m):
            if stra[i] != strb[i]:
                return stra[:i]
        return stra[:m]
