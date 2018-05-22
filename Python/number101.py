# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3

# But the following [1,2,2,null,3,null,3] is not:

#     1
#    / \
#   2   2
#    \   \
#    3    3


class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if not (root.left and root.right):
            return not(root.left or root.right)
        return self.isEqual(root.left, root.right)

    def isEqual(self, r1, r2):
        if not r1 or not r2:
            if not r1 and not r2:
                return True
            else:
                return False

        if r1.val != r2.val:
            return False

        return self.isEqual(r1.left, r2.right) and self.isEqual(r1.right, r2.left)


class Solution2:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        dfs = []
        stack = [root]

        while stack != []:
            # make dfs but also return whether you are left or right child
            # then, the output will reveal if it is symmetric
