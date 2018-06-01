# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.

# The encoded string should be as compact as possible.

# Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = ""
        if not root:
            return res
        queue = [root]
        while queue:
            current = queue.pop(0)
            res = res + str(current.val) + " "
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return res



    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def add(head, value):
            if value < head.val:
                if head.left:
                    add(head.left, value)
                else:
                    head.left = TreeNode(value)
            else:
                if head.right:
                    add(head.right, value)
                else:
                    head.right = TreeNode(value)

        values = [int(x) for x in data.split()]
        if not values:
            return None
        head = TreeNode(values[0])

        i = 1

        while i < len(values):
            add(head, values[i])
            i += 1
        return head


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
