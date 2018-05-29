#  Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

# Example 1:

# Input: [1,2,1]
# Output: [2,-1,2]
# Explanation: The first 1's next greater number is 2;
# The number 2 can't find next greater number;
# The second 1's next greater number needs to search circularly, which is also 2.

# Note: The length of given array won't exceed 10000.
 # brute force tle
class Solution:
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) < 2:
            return [-1] * len(nums)
        n = len(nums)
        res = []
        for i in range(n):
            c = nums[i]
            j = (i + 1) % n
            while j != i and nums[j] <= c:
                j = (j + 1) % n
            if j != i:
                res.append(nums[j])
            else:
                res.append(-1)
        return res
