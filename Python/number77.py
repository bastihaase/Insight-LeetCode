# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

# Example:

# Input: n = 4, k = 2
# Output:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]

class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        stack = [([], 0)]

        while stack:
            current, last = stack.pop()
            if len(current) == k:
                res.append(current)
            elif last < n:
                stack.append((current + [last + 1], last + 1))
                stack.append((current, last + 1))

        return res
