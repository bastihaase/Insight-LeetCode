# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

# Example 1:

# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.

# Example 2:

# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.
import math

class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        results = [0, 1, 2, 3, 1]

        for j in range(5, n + 1):
            best = j
            for i in range(1, j):
                tmp = i * i
                if tmp > j:
                    break
                current = 1 + results[j - tmp]
                if current < best:
                    best = current
            results.append(best)
        return results[n]
