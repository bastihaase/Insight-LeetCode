# Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

# Example 1:

# Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
# Output: 16
# Explanation: The two words can be "abcw", "xtfn".

# Example 2:

# Input: ["a","ab","abc","d","cd","bcd","abcd"]
# Output: 4
# Explanation: The two words can be "ab", "cd".

# Example 3:

# Input: ["a","aa","aaa","aaaa"]
# Output: 0
# Explanation: No such pair of words.


# Masking and using bitwise operation would be much faster!!!

class Solution:
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        best = 0

        swords = [set(word) for word in words]

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if swords[i] & swords[j] == set():
                    current = len(words[i]) * len(words[j])
                    best = max(current, best)

        return best


class Solution2:
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        d = {}
        for w in words:
            mask = 0
            for c in set(w):
                mask |= (1 << (ord(c) - 97))
            d[mask] = max(d.get(mask, 0), len(w))
        return max([d[x] * d[y] for x in d for y in d if not x & y] or [0])
