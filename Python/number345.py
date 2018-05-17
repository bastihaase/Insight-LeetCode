# Write a function that takes a string as input and reverse only the vowels of a string.

# Example 1:
# Given s = "hello", return "holle".

# Example 2:
# Given s = "leetcode", return "leotcede".

# Note:
# The vowels does not include the letter "y".


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == "":
            return ""
        mys = list(s)
        vowels = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])
        left = 0
        right = len(mys) - 1
        while left < right:
            while mys[left] not in vowels and left < right:
                left += 1
            while mys[right] not in vowels and right > left:
                right -= 1
            if right > left:
                temp = s[left]
                mys[left] = mys[right]
                mys[right] = temp
                left += 1
                right -= 1
        return "".join(mys)
