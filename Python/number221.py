# Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

# Example:

# Input:

# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0

# Output: 4

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        n, m = len(matrix), len(matrix[0])
        dp = [[int(x) for x in y] for y in matrix]
        best = 0
        for i in range(n):
            for j in range(m):
                if i != 0 and j != 0:
                    if dp[i][j]:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                best = max(best, dp[i][j])
        return best ** 2
