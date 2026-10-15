# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head and not head.next: return None
        slow = head
        fast = head

        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        head2 = slow.next
        slow.next = None

        prev = None
        current = head2
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        head2 = prev

        while head and head2:
            temp1 = head.next
            temp2 = head2.next

            head.next = head2
            head2.next = temp1

            head = temp1
            head2 = temp2

