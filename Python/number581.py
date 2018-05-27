# Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

# You need to find the shortest such subarray and output its length.

# Example 1:

# Input: [2, 6, 4, 8, 10, 9, 15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

# Note:

#     Then length of the input array is in range [1, 10,000].
#     The input array may contain duplicates, so ascending order here means <=.


class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        while left < right and nums[left] <= nums[left + 1]:
            left += 1

        if left >= right:
            return 0

        while nums[right] >= nums[right - 1]:
            right -= 1

        biggest, smallest = max(nums[left: right + 1]), min(nums[left: right + 1])

        while left > 0 and nums[left - 1] > smallest:
            left -= 1

        while right + 1 < len(nums) and nums[right + 1] < biggest:
            right += 1

        return right - left + 1
