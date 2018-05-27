# Reverse a linked list from position m to n. Do it in one-pass.

# Note: 1 ≤ m ≤ n ≤ length of list.

# Example:

# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):


    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if n <= m:
            return head

        if not head or not head.next:
            return head

        current = head
        dummy = ListNode(0)
        dummy.next = head
        previous = dummy


        while m > 1 and current.next:
            previous = current
            current = current.next
            m -= 1
            n -= 1

        if not current.next:
            return head

        one = current
        two = one.next
        three = two.next


        while n > 1:
            two.next = one
            one = two
            two = three
            if not three:
                break
            three = three.next
            n -= 1

        previous.next = one
        current.next = two

        return dummy.next
