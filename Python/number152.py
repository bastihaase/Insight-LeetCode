# Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

# Example 1:

# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

# Example 2:

# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        e = [nums[0]]
        d = [nums[0]]
        for x in nums[1:]:
            d.append(max(x, x * d[-1], x * e[-1]))
            e.append(min(x, x * d[-2], x * e[-1]))
        return max(d)
