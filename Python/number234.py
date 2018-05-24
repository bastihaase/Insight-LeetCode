# Given a singly linked list, determine if it is a palindrome.

# Example 1:

# Input: 1->2
# Output: false

# Example 2:

# Input: 1->2->2->1
# Output: true

# Follow up:
# Could you do it in O(n) time and O(1) space?


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True

        #find the middle
        slow = head
        fast = head

        previous_elements = []

        while fast.next and fast.next.next:
            previous_elements.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        if fast.next:
            previous_elements.append(slow.val)
        # go to the end with slow and check if values agree
        slow = slow.next

        while slow:
            current = previous_elements.pop()
            if current != slow.val:
                return False
            slow = slow.next

        return True
