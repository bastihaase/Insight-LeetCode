# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

# Example 1:

# Input: 1->2->3->3->4->4->5
# Output: 1->2->5

# Example 2:

# Input: 1->1->1->2->3
# Output: 2->3

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        dummy = ListNode(0)
        dummy.next = head
        previous = dummy
        left = head
        right = head

        found_duplicate = False

        while right.next:
            right = right.next

            if found_duplicate:
                if right.val != left.val:
                    previous.next = right
                    left = right
                    found_duplicate = False
            else:
                if right.val != left.val:
                    previous = left
                    left = right
                else:
                    found_duplicate = True
        if found_duplicate:
            previous.next = None

        return dummy.next