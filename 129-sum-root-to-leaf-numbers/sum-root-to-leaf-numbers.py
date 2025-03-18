# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def root_leaf(node, num):
            if not node:
                return 0
            if not node.left and not node.right:
                return num * 10 + node.val
            
            left = root_leaf(node.left, num * 10 + node.val)
            right = root_leaf(node.right, num * 10 + node.val)

            return left + right
      
        return root_leaf(root,0)