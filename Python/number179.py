# Given a list of non negative integers, arrange them such that they form the largest number.

# Example 1:

# Input: [10,2]
# Output: "210"

# Example 2:

# Input: [3,30,34,5,9]
# Output: "9534330"

# Note: The result may be very large, so you need to return a string instead of an integer.

class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        def my_cmp(x, y):
            return cmp(int(str(x) + str(y)), int(str(y) + str(x)))
        nums.sort(cmp = my_cmp)
        return max("".join([str(x) for x in nums[::-1]]).lstrip("0"), "0")
