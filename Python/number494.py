#  You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

# Find out how many ways to assign symbols to make sum of integers equal to target S.

# Example 1:

# Input: nums is [1, 1, 1, 1, 1], S is 3.
# Output: 5
# Explanation:

# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3

# There are 5 ways to assign symbols to make the sum of nums be target 3.

# Note:

#     The length of the given array is positive and will not exceed 20.
#     The sum of elements in the given array will not exceed 1000.
#     Your output answer is guaranteed to be fitted in a 32-bit integer.


class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        results = {0: 1}

        for x in nums:
            new_results = {}
            for value, possibilities in results.items():
                new_results[value + x] = new_results.get(value + x, 0) + possibilities
                new_results[value - x] = new_results.get(value - x, 0) + possibilities
                results = new_results
        return results.get(S, 0)
