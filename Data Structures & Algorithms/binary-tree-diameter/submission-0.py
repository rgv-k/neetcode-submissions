# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.diameter = 0
    def heightTree(self, root: Optional[treeNode]):
        if root is None:
            return 0

        left = self.heightTree(root.left)
        right = self.heightTree(root.right)

        self.diameter = max(self.diameter, left+right)
        return 1 + max(left, right)
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        h = self.heightTree(root)
        return self.diameter