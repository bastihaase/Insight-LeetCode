# Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

# Example 1:

# Input: [2,2,3,4]
# Output: 3
# Explanation:
# Valid combinations are:
# 2,3,4 (using the first 2)
# 2,3,4 (using the second 2)
# 2,2,3

# Note:

#     The length of the given array won't exceed 1000.
#     The integers in the given array are in the range of [0, 1000].

class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i = 0
        while i < len(nums) and nums[i] == 0:
            i += 1
        nums = nums[i:]

        pos = 0

        if len(nums) < 3:
            return 0

        for i, a in enumerate(nums):
            last = i + 2
            for j, b in enumerate(nums[i + 1: len(nums) - 1]):
                while last < len(nums) and a + b > nums[last]:
                    last += 1
                pos += last - (j + i + 1) - 1

        return pos
