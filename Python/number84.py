# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


# Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].




# The largest rectangle is shown in the shaded area, which has area = 10 unit.


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        results = {}
        best = 0

        for i, x in enumerate(heights):
            results[x] = {}
            for j in range(1, x + 1):
                if i > 0:
                    results[x][j] = j + results[heights[i - 1]].get(j, 0)
                else:
                    results[x][j] = j
                best = max(best, results[x][j])
        return best
