# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sm = 0
        def find(node):
            nonlocal sm
            if  not node:
                return

            if low <= node.val <= high:
                sm += node.val

            find(node.left)
            find(node.right)

        find(root)

        return sm