# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

# For example, given the following triangle

# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]

# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

# Note:

# Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        for i, row in enumerate(triangle[: -1]):
            for j, entry in enumerate(row):
                if j == 0:
                    triangle[i + 1][j] += entry
                else:
                    triangle[i + 1][j] = min(triangle[i + 1][j], triangle[i + 1][j] - triangle[i][j - 1] + entry)
                triangle[i + 1][j + 1] += entry
        return min(triangle[-1])
