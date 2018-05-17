# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

# Example:

# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        if len(height) <= 1:
            return 0

        left = 0
        while left < len(height) and height[left] == 0:
            left += 1
        right = left + 1
        volume = 0

        while right < len(height):
            lh = height[left]
            rm = right
            while height[right] < lh and right < len(height):
                if height[rm] <= height[right]:
                    rm = right
                right += 1
            if right >= len(height):
                volume += self.water(left, rm, height)
                left = rm
                right = left + 1
            else:
                volume += self.water(left, right, height)
                left = right
                right += 1
        return volume

    def water(self, left, right, height):
        level = min(height[left], height[right])
        volume = 0
        for i in range(left + 1, right):
            volume += level - height[i]
