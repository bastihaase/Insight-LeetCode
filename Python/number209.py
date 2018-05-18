# Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

# Example:

# Input: [2,3,1,2,4,3], s = 7
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem constraint.

# Follow up:
# If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).


# first brute force solution
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        current_sum = 0
        best_length = 0
        i = 0

        while i < len(nums):
            current_sum = nums[i]
            j = i
            while current_sum < s and j < len(nums) - 1:
                j += 1
                current_sum += nums[j]
            while i < j and current_sum - nums[i] >= s:
                current_sum -= nums[i]
                i += 1
            if current_sum >= s:
                if best_length == 0:
                    best_length = j - i + 1
                else:
                    best_length = min(best_length, j - i + 1)
            i += 1
        return best_length



class Solution2(object):
    def minSubArrayLen(self, s, nums):
        n = len(nums)
        curr_sum = 0
        min_len = n + 1

        start = 0
        end = 0
        while end < n:


            while curr_sum < s and end < n:
                curr_sum += nums[end]
                end+= 1

            while curr_sum >= s and start < n:

                if end - start < min_len:
                    min_len = end - start

                curr_sum -= nums[start]
                start+= 1

        if min_len == n + 1:
            return 0
        return min_len
