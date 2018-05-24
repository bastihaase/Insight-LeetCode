#  Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

# Note: Do not modify the linked list.

# Follow up:
# Can you solve it without using extra space?

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return None

        if not head.next:
            return None

        if not head.next.next:
            if head.next == head:
                return head
            return None

        slow = head
        fast = head

        while slow.next and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                break

        if fast != slow:
            return None

        while head != slow:
            head = head.next
            slow = slow.next

        return slow
