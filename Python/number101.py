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
        return self.isMirror(root.left, root.right)

    def isMirror(self, r1, r2):
        if not r1 or not r2:
            if not r1 and not r2:
                return True
            else:
                return False

        if r1.val != r2.val:
            return False

        return self.isMirror(r1.left, r2.right) and self.isMirror(r1.right, r2.left)

# not completed yet
class Solution2:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        dfs = []
        stack = []

        def peek(stack):
            if len(stack) > 0:
                return stack[-1]
            return None

        current = (root, "m")
        while True:
            while root:
                if root.right:
                    stack.append((root.right, "r"))
                stack.append(current)
                root = root.left
                current = (root, "l")

            root, orientation = stack.pop()

            if root is not None:
                if root.right is not None:#  and peek(stack) == root.right:
                    if peek(stack) == root.right:
                        stack.pop()
                    stack.append((root, orientation))
                    tmp = root.right
                    root.right = None
                    root = tmp
                    orientation = "r"
                else:
                    dfs.append(str(root.val) + orientation)
                    root = None

            if len(stack) <= 0:
                break

        return dfs
