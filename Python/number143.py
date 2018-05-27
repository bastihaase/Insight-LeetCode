# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

# You may not modify the values in the list's nodes, only nodes itself may be changed.

# Example 1:

# Given 1->2->3->4, reorder it to 1->4->2->3.

# Example 2:

# Given 1->2->3->4->5, reorder it to 1->5->2->4->3.

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

# iterative solution: put second half on stack and insert it!

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head and head.next and head.next.next:
            stack = []

            slow = head
            fast = head

            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next

            second_half = slow.next
            slow.next = None

            while second_half:
                stack.append(second_half)
                second_half = second_half.next

            current = head

            while stack:
                third = current.next
                middle = stack.pop()
                current.next = middle
                middle.next = third
                current = third










# Recursive solution, not efficient but easy on the eyes
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        self.reorder(head)

    def reorder(self, head):

        if not head or not head.next or not head.next.next:
            return head

        second_last = head

        while second_last.next.next:
            second_last = second_last.next
        last = second_last.next
        second_last.next = None

        third = head.next
        head.next = last
        last.next = self.reorder(third)
        return head

    # 1->2->3->4->5
    # second_last  1 2 3 4
    # last               5
    # third              2
    #  1->5 -> reorderList(2->3->4)
    # 2 -> 3 -> 4
    # second_last 2 3
    # last          4
    # third         3
    # 2 -> 4 -> reorderList(3)
