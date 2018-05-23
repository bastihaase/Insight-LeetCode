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
