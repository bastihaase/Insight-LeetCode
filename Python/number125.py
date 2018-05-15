# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Note: For the purpose of this problem, we define empty string as valid palindrome.

# Example 1:

# Input: "A man, a plan, a canal: Panama"
# Output: true

# Example 2:

# Input: "race a car"
# Output: false

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "":
            return True
        is_palindrome = self.only_alpha_num(s).lower()
        n = len(is_palindrome) // 2
        for i in range(n):
            if is_palindrome[i] != is_palindrome[-i-1]:
                return False
        return True



    def only_alpha_num(self, s):
        r = ""
        for x in s:
            if x.isalnum():
                r += x
        return r
