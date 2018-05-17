# Given a pattern and a string str, find if str follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

# Example 1:

# Input: pattern = "abba", str = "dog cat cat dog"
# Output: true

# Example 2:

# Input:pattern = "abba", str = "dog cat cat fish"
# Output: false

# Example 3:

# Input: pattern = "aaaa", str = "dog cat cat dog"
# Output: false

# Example 4:

# Input: pattern = "abba", str = "dog dog dog dog"
# Output: false

# Notes:
# You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split()
        if len(words) != len(pattern):
            return False
        save_assignments = {}
        for (p, word) in zip(pattern, words):
            if p in save_assignments:
                if save_assignments[p] != word:
                    return False
            else:
                save_assignments[p] = word
        return len(save_assignments.values()) == len(set(save_assignments.values()))
