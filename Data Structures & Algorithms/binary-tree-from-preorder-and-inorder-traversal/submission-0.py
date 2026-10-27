# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index = {value:index for index, value in enumerate(inorder)}
        pre_index = 0
        def builder(left, right):
            nonlocal pre_index
            if left > right:
                return None
            root_val = preorder[pre_index]

            node = TreeNode(root_val)
            pre_index += 1
            mid = inorder_index[root_val]

            node.left = builder(left, mid - 1)
            node.right = builder(mid + 1, right)
            return node

        return builder(0, len(inorder) - 1)