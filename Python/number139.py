# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note:

#     The same word in the dictionary may be reused multiple times in the segmentation.
#     You may assume the dictionary does not contain duplicate words.

# Example 1:

# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".

# Example 2:

# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
#              Note that you are allowed to reuse a dictionary word.

# Example 3:

# Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: false


class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        stack = [s]
        words = set(wordDict)
        while stack:
            current = stack.pop()
            if current  in words:
                return True
            else:
                for x in words:
                    n = len(x)
                    if len(current) >= n and current[:n] == x:
                        stack.append(current[n:])
        return False


# dynamic - this one actually passes!

class Solution2:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        words = set(wordDict)
        results = [(s[:i + 1] in words) for i in range(len(s))]
        for i in range(len(s)):
            if not results[i]:
                for j in range(i):
                    if results[j] and s[j + 1 : i + 1] in words:
                        results[i] = True
                        break
        return results[-1]
