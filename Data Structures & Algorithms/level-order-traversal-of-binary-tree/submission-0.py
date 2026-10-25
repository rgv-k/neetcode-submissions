# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        queue = deque()
        queue.append(root)

        result = []

        while queue:
            s = len(queue)
            level = []
            for i in range(s):
                n = queue.popleft()
                if n.left: queue.append(n.left)
                if n.right:queue.append(n.right)
                level.append(n.val)

            result.append(level)

        return result


        