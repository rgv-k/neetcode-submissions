"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None

        copy = dict()
        original = head
        while original:
            copy[original] = Node(original.val)
            original = original.next

        original = head
        while original:
            copy[original].next = copy.get(original.next)
            copy[original].random = copy.get(original.random)
            original = original.next


        return copy[head]
