# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head: return None
        l = 1
        r = left

        prev = None
        current = head
        
        while current != None and l + 1<= left:
            bleft_node = current
            current = current.next
            l += 1

        left_node = current

        while current != None and r <= right:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
            r += 1

        left_node.next = current
        if left == 1:
            head = prev
        else:
            bleft_node.next = prev

        return head

        