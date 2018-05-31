# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.

# Example:

# Input: head = 1->4->3->2->5->2, x = 3
# Output: 1->2->2->4->3->5


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return head

        new_head = None
        small = new_head
        big_head = None
        big = big_head
        while head:
            if head.val >= x:
                if big:
                    big.next = head
                    big = head
                else:
                    big_head = head
                    big = big_head
            else:
                if small:
                    small.next = head
                    small = head
                else:
                    new_head = head
                    small = new_head
            head = head.next
        if small:
            small.next = big_head
        if new_head:
            return new_head
        return big_head
