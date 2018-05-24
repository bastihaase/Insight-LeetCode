# Given an unsorted integer array, find the smallest missing positive integer.

# Example 1:

# Input: [1,2,0]
# Output: 3

# Example 2:

# Input: [3,4,-1,1]
# Output: 2

# Example 3:

# Input: [7,8,9,11,12]
# Output: 1

# Note:

# Your algorithm should run in O(n) time and uses constant extra space.

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        n = len(nums)
        m = min(min(nums), -1)

        for x in nums:
            y = x
            if x < m:
                y = -y + 2 * m - 1

            if 1 <= y <= n and nums[y-1] >= m:
                nums[y - 1] = 2 * m - nums[y - 1] - 1
        print(nums)
        for i in range(n):
            if nums[i] >= m:
                return i + 1
        return n + 1
