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


# divide and conquer style, divide  at the min of bar

class Solution2(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0
        if len(heights) == 1:
            return heights[0]



        minimum = float('inf')
        min_index = -1

        for i, x in enumerate(heights):
            print(min_index)
            if x < minimum:
                minimum = x
                min_index = i

        op1 = self.largestRectangleArea(heights[:min_index])
        op2 = self.largestRectangleArea(heights[min_index + 1:])
        op3 = minimum * len(heights)

        return max(op1, op2, op3)




# O(n) using stack

class Solution3(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        temp = []
        stack = []
        # append -infinity to evaluate the whole stack!
        heights.append(float('-inf'))
        for i,h in enumerate(heights):
            cpos = i
            while stack and h < stack[-1][0]:
                ch, cpos = stack.pop()
                temp.append(ch*(i - cpos ))
            stack.append([h, cpos])

        return max(temp) if temp else 0
