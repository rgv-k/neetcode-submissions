# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def helper(self, root, max_value):
        if root is None:
            return 0

        if root.val >= max_value:
            max_value = max(root.val, max_value)
            return 1 + self.helper(root.left, max_value) + self.helper(root.right, max_value)

        else:
            return self.helper(root.left, max_value) + self.helper(root.right, max_value)

    def goodNodes(self, root: TreeNode) -> int:
        max_value = root.val
        return self.helper(root, max_value)
        