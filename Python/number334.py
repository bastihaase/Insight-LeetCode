#  Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

# Formally the function should:

#     Return true if there exists i, j, k
#     such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.

# Your algorithm should run in O(n) time complexity and O(1) space complexity.

# Examples:
# Given [1, 2, 3, 4, 5],
# return true.

# Given [5, 4, 3, 2, 1],
# return false.

class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        run, one, two = None, None, None
        for x in nums:
            if x != 0: print(x)
            if not run:
                run, one = 1, x
                run = True
            else:
                if two != None:
                    if x > two:
                        return True
                    else:
                        if one < x < two:
                            two = x
                        elif x < one:
                            one = x
                elif one != None:
                    if x > one:
                        two = x
                    else:
                        one  = x
        return False
