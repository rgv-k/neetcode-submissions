# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        q = deque()
        q.append(root)
        result = []

        while q:
            s = len(q)
            for i in range(s):
                h = q.popleft()
                if h.left:  q.append(h.left)
                if h.right: q.append(h.right)
            result.append(h.val)

        return result