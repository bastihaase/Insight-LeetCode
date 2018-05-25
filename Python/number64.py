# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

# Example:

# Input:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.

# slow recursive solution, lots of overlap
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0

        stack = [((0, 0), 0)]
        n, m = len(grid), len(grid[0])
        best = float('inf')
        while stack:
            (i, j), value = stack.pop()
            if value < best:
                if i == n - 1 and j == m - 1:
                    best = min(best, value + grid[n - 1][m - 1])
                if i < n - 1:
                    stack.append(((i + 1, j), value + grid[i][j]))
                if j < m - 1:
                    stack.append(((i, j + 1), value + grid[i][j]))
        return best


class Solution2:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0

        n, m = len(grid), len(grid[0])

        dist = [[0] * m] * n

        dist[0][0] = grid[0][0]

        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    dist[i][j] = grid[i][j]
                elif i == 0:
                    dist[i][j] = grid[i][j] + dist[i][j - 1]
                elif j == 0:
                    dist[i][j] = grid[i][j] + dist[i - 1][j]
                else:
                    dist[i][j] = grid[i][j] + min(dist[i][j - 1], dist[i - 1][j])
        return dist[n - 1][m -1]
