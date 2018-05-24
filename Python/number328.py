# Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

# You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

# Example:

# Input: 1->2->3->4->5->NULL
# Output: 1->3->5->2->4->NULL

# Note:

#     The relative order inside both the even and odd groups should remain as it was in the input.
#     The first node is considered odd, the second node even and so on ...


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        even_head = head.next
        odd = head
        even = head.next
        while odd.next and odd.next.next and even.next and even.next.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next

        if odd.next.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = None

        odd.next = even_head
        return head
