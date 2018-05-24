# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

# Example 1:

# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]

# Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.

# Example 2:

# [[0,0,0,0,0,0,0,0]]

# Given the above grid, return 0.

# Note: The length of each dimension in the given grid does not exceed 50.


class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n, m = len(grid), len(grid[0])

        def compute_area(i, j):
            if not grid:
                return 0
            if j < 0 or j >= m or i < 0 or i >= n or not grid[i][j]:
                return 0
            grid[i][j] = 0

            return 1 + compute_area(i - 1, j) + compute_area(i + 1, j) + compute_area(i, j + 1) + compute_area(i, j - 1)

        ans = 0
        for i in range(n):
            for j in range(m):
                ans = max(ans, compute_area(i, j))

        return ans
