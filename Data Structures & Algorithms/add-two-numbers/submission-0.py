# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def addNumbers(head1, head2, carry) -> Optional[ListNode]:
            if (not head1) and (not head2) and (carry == 0): return None

            digit1 = head1.val if head1 else 0
            digit2 = head2.val if head2 else 0

            total = digit1 + digit2 + carry
            new = ListNode(total%10)
            new.next = addNumbers(head1.next if head1 else None, head2.next if head2 else None, total//10)
            return new

        return addNumbers(l1, l2, 0)