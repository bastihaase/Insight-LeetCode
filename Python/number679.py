#  Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

#     Any left parenthesis '(' must have a corresponding right parenthesis ')'.
#     Any right parenthesis ')' must have a corresponding left parenthesis '('.
#     Left parenthesis '(' must go before the corresponding right parenthesis ')'.
#     '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
#     An empty string is also valid.

# Example 1:

# Input: "()"
# Output: True

# Example 2:

# Input: "(*)"
# Output: True

# Example 3:

# Input: "(*))"
# Output: True

# Note:

#     The string size will be in the range [1, 100].


class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        minimum_left = 0
        maximum_left = 0
        for x in s:
            if x == "(":
                minimum_left += 1
                maximum_left += 1
            elif x == ")":
                maximum_left -= 1
                minimum_left -= 1
            elif x == "*":
                minimum_left -= 1
                maximum_left += 1
            if maximum_left < 0:
                return False
            minimum_left = max(0, minimum_left)
        return minimum_left <= 0
