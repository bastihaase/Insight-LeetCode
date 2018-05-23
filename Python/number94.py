# Given a binary tree, return the inorder traversal of its nodes' values.

# Example:

# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3

# Output: [1,3,2]

# Follow up: Recursive solution is trivial, could you do it iteratively?

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        result = []
        if root.left:
            result += self.inorderTraversal(root.left)
        result += [root.val]
        if root.right:
            result += self.inorderTraversal(root.right)
        return result

# Now iteratively

class Solution2(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = [root]
        while root.left:
            stack.append(root.left)
            root = root.left

        result = []

        while stack:
            current = stack.pop()
            if current.right:
                right = current.right
                stack.append(right)
                while right.left:
                    stack.append(right.left)
                    right = right.left

            result.append(current.val)

        return result
