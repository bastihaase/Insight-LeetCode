#  The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

# Determine the maximum amount of money the thief can rob tonight without alerting the police.

# Example 1:

#      3
#     / \
#    2   3
#     \   \
#      3   1

# Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

# Example 2:

#      3
#     / \
#    4   5
#   / \   \
#  1   3   1

# Maximum amount of money the thief can rob = 4 + 5 = 9.

# Credits:
# Special thanks to @dietpepsi for adding this problem and creating all test cases.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.help_rob(root))

    def help_rob(self, root):
        if root is None:
            return (0, 0)
        left = self.help_rob(root.left)
        right = self.help_rob(root.right)
        return (left[1] + right[1] + root.val, max(right) +  max(left))
